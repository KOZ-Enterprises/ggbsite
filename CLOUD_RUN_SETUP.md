# GCP Cloud Run Setup Guide

One-time bootstrap guide for setting up the Gary Gigabytes infrastructure on Google Cloud Run.

## Prerequisites

- `gcloud` CLI installed and authenticated
- GCP billing account active
- Cloudflare account with `garygigabytes.com` domain

## 1. Create GCP Project & Enable APIs

```bash
# Create a new project
gcloud projects create <PROJECT_ID> --name="Gary Gigabytes"

# Set it as active
gcloud config set project <PROJECT_ID>

# Link billing account
gcloud billing accounts list  # Get account ID
gcloud billing projects link <PROJECT_ID> --billing-account=<ACCOUNT_ID>

# Enable required APIs
gcloud services enable \
  run.googleapis.com \
  compute.googleapis.com \
  certificatemanager.googleapis.com \
  cloudbuild.googleapis.com \
  artifactregistry.googleapis.com
```

## 2. Build and Deploy ggbsite

```bash
# Build using Cloud Build (pulls from repo, builds Dockerfile, pushes to GCR)
gcloud builds submit /path/to/ggbsite --tag gcr.io/<PROJECT_ID>/ggbsite:latest

# Deploy to Cloud Run
gcloud run deploy ggbsite \
  --image gcr.io/<PROJECT_ID>/ggbsite:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 80
```

Note: Replace `<PROJECT_ID>` with your actual GCP project ID (e.g., `gary-gigabytes`).

## 3. Reserve Static IP & Create Load Balancer

### 3a. Reserve Static IP

```bash
gcloud compute addresses create gary-gigabytes-ip --global
gcloud compute addresses describe gary-gigabytes-ip --global --format='value(address)'
# Note this IP — you'll need it for Cloudflare DNS
```

### 3b. Create Serverless NEG (Network Endpoint Group)

```bash
gcloud compute network-endpoint-groups create ggbsite-neg \
  --region us-central1 \
  --network-endpoint-type serverless \
  --cloud-run-service ggbsite
```

### 3c. Create Backend Service

```bash
gcloud compute backend-services create ggbsite-backend --global
gcloud compute backend-services add-backend ggbsite-backend \
  --global \
  --network-endpoint-group ggbsite-neg \
  --network-endpoint-group-region us-central1
```

### 3d. Create Google-Managed SSL Certificate

```bash
gcloud compute ssl-certificates create garygigabytes-cert \
  --domains garygigabytes.com \
  --global
```

**Important**: This certificate will stay in PROVISIONING state until DNS is updated in step 4.

### 3e. Create URL Map & HTTPS Proxy

```bash
# Create URL map (routes to ggbsite-backend by default)
gcloud compute url-maps create gary-gigabytes-urlmap \
  --default-service ggbsite-backend

# Create HTTPS proxy
gcloud compute target-https-proxies create gary-gigabytes-proxy \
  --url-map gary-gigabytes-urlmap \
  --ssl-certificates garygigabytes-cert
```

### 3f. Create Forwarding Rules

```bash
# HTTPS (port 443)
gcloud compute forwarding-rules create gary-gigabytes-https \
  --global \
  --target-https-proxy gary-gigabytes-proxy \
  --address gary-gigabytes-ip \
  --ports 443

# HTTP → HTTPS redirect setup
# First, create URL map for HTTP redirect
cat > http-redirect-urlmap.yaml <<EOF
name: gary-gigabytes-http-redirect
defaultUrlRedirect:
  httpsRedirect: true
  redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
EOF

gcloud compute url-maps import gary-gigabytes-http-redirect \
  --source http-redirect-urlmap.yaml \
  --global \
  --quiet

# Create HTTP proxy
gcloud compute target-http-proxies create gary-gigabytes-http-proxy \
  --url-map gary-gigabytes-http-redirect

# HTTP forwarding rule (port 80)
gcloud compute forwarding-rules create gary-gigabytes-http \
  --global \
  --target-http-proxy gary-gigabytes-http-proxy \
  --address gary-gigabytes-ip \
  --ports 80
```

## 4. Update Cloudflare DNS

1. Get the static IP from step 3a
2. In the `cloudflare-dns.txt` file, replace `<STATIC_IP>` with your GCP static IP
3. Cloudflare Dashboard → `garygigabytes.com` → DNS → **Import DNS records**
4. Upload the updated `cloudflare-dns.txt` file
5. Verify DNS propagation (can take 5-15 minutes)
6. Check SSL certificate provisioning status:

```bash
gcloud compute ssl-certificates describe garygigabytes-cert --global
```

Wait until status shows `ACTIVE` (typically 5-15 minutes after DNS update).

1. Set Cloudflare SSL/TLS mode to **Full** (not Full Strict):
   - Cloudflare Dashboard → SSL/TLS → Overview → Full

## 5. Verify Deployment

```bash
# Test HTTP → HTTPS redirect
curl -v http://garygigabytes.com

# Test HTTPS access
curl -v https://garygigabytes.com

# Check load balancer health
gcloud compute backend-services get-health ggbsite-backend --global
```

## 6. (Optional) Set Up CI/CD

See `.github/workflows/deploy.yml` and [DEPLOYMENT.md](DEPLOYMENT.md) for GitHub Actions setup.

This requires:

- GCP service account with Cloud Run permissions
- GitHub secrets: `WIF_PROVIDER`, `WIF_SERVICE_ACCOUNT`, `GCP_PROJECT_ID`

## Troubleshooting

### SSL Certificate Stuck in PROVISIONING

- Ensure Cloudflare DNS records are pointing to the GCP static IP
- Verify DNS propagation: `dig garygigabytes.com`
- Give it 15 minutes after DNS update
- Check logs: `gcloud compute ssl-certificates describe garygigabytes-cert --global`

### Cloud Run Service Not Responding

```bash
# Check service status
gcloud run services describe ggbsite --region us-central1

# View recent logs
gcloud logging read "resource.type=cloud_run_revision" --limit=20

# Check load balancer backend health
gcloud compute backend-services get-health ggbsite-backend --global
```

### Load Balancer Not Routing Traffic

- Verify backend service has at least one healthy endpoint
- Check URL map is correctly configured: `gcloud compute url-maps describe gary-gigabytes-urlmap`
- Verify forwarding rules exist: `gcloud compute forwarding-rules list --global`

## Cleanup (if needed)

```bash
# Delete forwarding rules
gcloud compute forwarding-rules delete gary-gigabytes-https --global --quiet
gcloud compute forwarding-rules delete gary-gigabytes-http --global --quiet

# Delete proxies
gcloud compute target-https-proxies delete gary-gigabytes-proxy --global --quiet
gcloud compute target-http-proxies delete gary-gigabytes-http-proxy --global --quiet

# Delete URL maps
gcloud compute url-maps delete gary-gigabytes-urlmap --global --quiet
gcloud compute url-maps delete gary-gigabytes-http-redirect --global --quiet

# Delete SSL cert
gcloud compute ssl-certificates delete garygigabytes-cert --global --quiet

# Delete backend service
gcloud compute backend-services delete ggbsite-backend --global --quiet

# Delete NEG
gcloud compute network-endpoint-groups delete ggbsite-neg --region us-central1 --quiet

# Delete static IP
gcloud compute addresses delete gary-gigabytes-ip --global --quiet

# Delete Cloud Run service
gcloud run services delete ggbsite --region us-central1 --quiet
```
