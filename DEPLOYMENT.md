# Deployment & Setup

This document outlines the technical configuration and deployment workflow for the `ggbsite` project.

## Workflow Overview

The site follows a registry-based deployment strategy. Images are built and pushed to GitHub Container Registry (GHCR) automatically, then pulled to the production server.

1. **Local Dev**: Build/test the container.
2. **Push**: Commit and push to the `publish` branch.
3. **CI/CD**: GitHub Actions builds the image and pushes to `ghcr.io/koz-enterprises/ggbsite:latest`.
4. **Deploy**: Production server pulls the new image and restarts the container.

---

## Prerequisites

- **Docker & Docker Compose** (V2 recommended)
- **GitHub Container Registry Access**
- **Production Server with Nginx Proxy Network**

## Local Development

If you're testing locally, you can use the internal Docker setup to simulate the production environment.

1. **Configure Networking**: If not running behind a proxy locally, uncomment the `ports` mapping in `docker-compose.yml`:

    ```yaml
    ports:
      - "8080:80"
    ```

2. **Build and Run**:

    ```bash
    docker compose up --build
    ```

3. **Access**: Visit `http://localhost:8080`.

## Production Deployment

### 1. GitHub Actions Setup

The workflow is defined in `.github/workflows/deploy.yml`. It triggers specifically on pushes to the `publish` branch. It uses `GITHUB_TOKEN` for permissions, so no extra secrets are required for GHCR authentication.

### 2. Server-Side Setup

On your DigitalOcean server, ensure the shared network exists:

```bash
docker network create proxy_network
```

Ensure your `docker-compose.yml` points to the GHCR image:

```yaml
services:
  web:
    image: ghcr.io/koz-enterprises/ggbsite:latest
```

### 3. Execution

To update the live site after the GitHub Action completes:

```bash
docker compose pull
docker compose up -d
```

## Reverse Proxy Configuration

The main Nginx container on the server must be on the `proxy_network`. Use the following server block to route traffic to the `ggbsite` container:

```nginx
server {
    server_name garygigabytes.com;

    location / {
        proxy_pass http://ggsite:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
