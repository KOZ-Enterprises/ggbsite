# Fresh Droplet Deployment Guide

Since you're starting fresh, we're using a **Unified Proxy** setup. This means one master orchestration file manages your main Nginx entry point and all your sites.

## 1. Initial Server Setup

SSH into your fresh droplet and prepare the directory structure:

```bash
mkdir -p ~/server/nginx/conf.d
mkdir -p ~/server/nginx/certs
```

## 2. SSL Certificates (Cloudflare Origin Certs)

Since you're using Cloudflare, you can use their free **Origin Certificates**. These are valid for 15 years and encrypt traffic between Cloudflare and your server.

1. **Generate Certificates**:
    - In Cloudflare, go to **SSL/TLS** -> **Origin Server**.
    - Click **Create Certificate**.
    - Keep default settings (List your domains: `garygigabytes.com`, `*.garygigabytes.com`, etc.).
    - Cloudflare will show you a **Private Key** and an **Origin Certificate**.
2. **Save Locally**:
    - Save the **Origin Certificate** as `server/nginx/certs/garygigabytes.pem`.
    - Save the **Private Key** as `server/nginx/certs/garygigabytes.key`.
    - (Repeat for `culinaryotter` or use one cert that covers both if they are on the same Cloudflare account).

## 3. Copy Configuration and Certs

Navigate to your server directory and start the orchestration:

```bash
cd ~/server
docker compose up -d
```

## 4. Site Updates (CI/CD)

Your workflow for updating the sites remains automated:

1. **Develop Locally**: Make changes to `ggbsite` or `culinaryotter`.
2. **Push to Publish**: Push the `publish` branch to trigger the GitHub Action.
3. **Redeploy**: Once the Action finishes, run this on your server:

    ```bash
    cd ~/server
    docker compose pull
    docker compose up -d
    ```

## 5. Cloudflare Settings

In your Cloudflare Dashboard:

1. **DNS**: Ensure both domains point to your new Droplet IP (with the Orange Cloud "Proxied" enabled).
2. **SSL/TLS**: Set the mode to **"Full"** or **"Full (Strict)"**. Cloudflare handles the visitor-facing certificates, and Nginx handles the internal routing.

---

### Master Server Configuration Snippet

**`server/docker-compose.yml`**:

```yaml
services:
  nginx-proxy:
    image: nginx:alpine
    container_name: main-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
    networks:
      - web-network
    restart: always

  ggbsite:
    image: ghcr.io/koz-enterprises/ggbsite:latest
    container_name: ggbsite
    networks:
      - web-network
    restart: always

  culinaryotter:
    image: ghcr.io/koz-enterprises/culinaryotter:latest 
    container_name: culinaryotter
    networks:
      - web-network
    restart: always

networks:
  web-network:
    driver: bridge
```
