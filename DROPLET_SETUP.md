# Droplet Setup Guide: From Zero to Orchestration

Replacing a corrupted droplet is a hassle, but it's the perfect time to build back better. This guide will take you from a fresh Ubuntu install to a production-ready server.

## 1. Initial Access & Security

Once your droplet is created on DigitalOcean:

### SSH Login

From your local machine, use the private part of the key you uploaded to DigitalOcean:

```powershell
# IMPORTANT: On a fresh droplet, you MUST log in as 'root' first.
# DigitalOcean adds your key to the root user by default.
ssh -i G:\Keys\digitalocean\id_rsa root@129.212.166.222
```

> [!CAUTION]
> If you try to log in as `flynn` or any other user before creating them, you will get a `Permission denied (publickey)` error. The `root` user is the only one authorized out of the box.

### System Updates

Keep the foundation solid:

```bash
apt update && apt upgrade -y
```

### Create a New User

Running as root is risky. Create your `flynn` user with sudo privileges and add them to the `docker` group:

```bash
# 1. Create the user
adduser flynn

# 2. ADD TO SUDO GROUP (CRITICAL: Must run this while logged in as root!)
usermod -aG sudo flynn

# 3. Copy SSH keys from root to flynn
rsync --archive --chown=flynn:flynn ~/.ssh /home/flynn

# 4. Verify flynn is in the sudo group
groups flynn
# Expected output: flynn : flynn sudo

# 5. Switch to the new user
su - flynn
```

### Basic Firewall (UFW)

Only allow the essentials (SSH, HTTP, HTTPS):

```bash
ufw allow OpenSSH
ufw allow 80
ufw allow 443
ufw enable
```

---

## 2. Install Docker Engine

Since everything runs in containers, this is the most critical step.

### Install Prerequisites

```bash
apt install ca-certificates curl gnupg lsb-release -y
```

### Add Docker Repository

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Install Docker & Compose V2

```bash
apt update
apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y

# Allow your user to run docker without sudo
sudo usermod -aG docker $USER
# Log out and back in for this to take effect
```

---

## 3. Prepare the Orchestration Workspace

We’re moving away from scattered folders to a unified `~/server` directory.

### Create the Structure

```bash
mkdir -p ~/server/nginx/conf.d
mkdir -p ~/server/nginx/certs
```

### Verify Docker

```bash
docker --version
docker compose version
```

*(You should see Docker Compose V2.x.x)*

---

## 4. Next Steps: Deploying the Services

Now that the OS is ready and Docker is installed, follow the [**`DEPLOYMENT.md`**](file:///c:/Users/gkuep/RubymineProjects/ggbsite/DEPLOYMENT.md) guide to:

1. Generate your Cloudflare SSL certs.
2. Copy your `docker-compose.yml` and `default.conf` files.
3. Launch the unified proxy.

### Site Ready

*System is configured and ready for deployment.*
