# Cloud Run Deployment Guide

This site (and related subdomains) are hosted on Google Cloud Run with a Global Load Balancer fronted by Cloudflare DNS.

## Architecture Overview

```text
User Request (HTTPS)
    ↓
Cloudflare (DNS + SSL termination)
    ↓
GCP Global Load Balancer (static IP + Google-managed SSL cert)
    ↓
Cloud Run Services (us-central1)
    ├── ggbsite (port 80 - Jekyll/nginx)
    └── culinaryotter.garygigabytes.com (port 3000 - Node.js/Express, requires DB)
```

## Current Deployment Status

- **ggbsite**: Deployed and active at `https://garygigabytes.com`
  - Cloud Run Service: `ggbsite` (us-central1)
  - Image: `gcr.io/<PROJECT_ID>/ggbsite:latest`
  - Ports: 80
  
- **culinaryotter**: Not yet active (requires MySQL database setup)
  - Cloud Run Service: `culinaryotter` (us-central1)
  - Image: `gcr.io/<PROJECT_ID>/culinaryotter:latest`
  - Ports: 3000
  - Status: Deployment requires `MYSQL_*` environment variables and database connectivity

## DNS Configuration

All DNS records live in a single Cloudflare zone: `garygigabytes.com`

### Current DNS Records

- `garygigabytes.com` → `<STATIC_IP>` (proxied)
- `*.garygigabytes.com` → `<STATIC_IP>` (proxied - covers all subdomains)
- `culinaryotter.garygigabytes.com` → `<STATIC_IP>` (proxied)
- `hexmaster.garygigabytes.com` → `<STATIC_IP>` (proxied)

### Updating DNS

A template zone file is available in `cloudflare-dns.txt`. To update Cloudflare:

1. Edit the IP placeholder if needed
2. Cloudflare Dashboard → `garygigabytes.com` → DNS → **Import DNS records**
3. Upload the `cloudflare-dns.txt` file
4. Verify SSL/TLS mode is set to **Full** (not Full Strict)

## Deploying New Versions

### Manual Deploy (ggbsite)

Build and push to Cloud Run:

```bash
# Build locally using Cloud Build
gcloud builds submit . --tag gcr.io/<PROJECT_ID>/ggbsite:latest

# Deploy to Cloud Run
gcloud run deploy ggbsite \
  --image gcr.io/<PROJECT_ID>/ggbsite:latest \
  --region us-central1 \
  --platform managed
```

### CI/CD Deploy (GitHub Actions - Future)

Planned: GitHub Actions workflow will automatically:

1. Build on push to `publish` branch
2. Push to GHCR (GitHub Container Registry)
3. Deploy to Cloud Run

See `.github/workflows/deploy.yml` for setup details.

## SSL Certificate Status

Google-managed SSL certificate: `garygigabytes-cert`

Check provisioning status:

```bash
gcloud compute ssl-certificates describe garygigabytes-cert --global
```

Expected statuses:

- `PROVISIONING` - Certificate is being validated (wait up to 15 minutes)
- `ACTIVE` - Certificate is ready and in use

## Load Balancer Components

### Global Load Balancer Resources

- **Static IP**: `gary-gigabytes-ip` (34.36.126.59)
- **URL Map**: `gary-gigabytes-urlmap` (routes based on hostname)
- **HTTPS Proxy**: `gary-gigabytes-proxy`
- **HTTP Proxy**: `gary-gigabytes-http-proxy` (redirects to HTTPS)
- **Forwarding Rules**:
  - `gary-gigabytes-https` (port 443)
  - `gary-gigabytes-http` (port 80)

### Backend Services

- **ggbsite-backend**: Global backend service
  - NEG: `ggbsite-neg` (serverless, Cloud Run)
  - Region: us-central1

## Monitoring & Troubleshooting

### View Cloud Run Logs

```bash
gcloud run services describe ggbsite --region us-central1
gcloud logging read "resource.type=cloud_run_revision" --limit=50
```

### Check Load Balancer Health

```bash
gcloud compute backend-services get-health ggbsite-backend --global
```

### Test Connectivity

```bash
curl -v https://garygigabytes.com
curl -v https://culinaryotter.garygigabytes.com
```

## Adding New Subdomains or Services

1. Create Cloud Run service
2. Create serverless NEG
3. Add backend service (or reuse existing)
4. Update URL map with new hostname → backend mapping
5. Update Cloudflare DNS with new A record
6. (Optional) Create additional SSL certificate if needed

## Cost Considerations

- **Cloud Run**: Pay per request + compute time. Scales to zero when idle.
- **Load Balancer**: Hourly charge for IP + forwarding rules + backend service
- **Google-managed SSL**: No additional cost
- **Cloudflare**: Managed separately, not charged by GCP

## Related Documentation

- [CLOUD_RUN_SETUP.md](CLOUD_RUN_SETUP.md) - One-time GCP project setup
- [README.md](README.md) - Project overview
- `.github/workflows/deploy.yml` - CI/CD configuration
