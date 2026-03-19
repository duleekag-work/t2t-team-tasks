FROM mcr.microsoft.com/devcontainers/python:3.12


# ---- System dependencies (keep minimal but safe) ----
RUN apt-get update && apt-get install -y \
    sudo \
    ca-certificates \
    curl \
    gnupg \
    build-essential \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# ---- Upgrade Python packaging tooling (CRITICAL for pyproject.toml) ----
RUN python -m pip install --upgrade \
    pip \
    setuptools \
    wheel

# ---- Install Docker CLI (Docker-in-Docker / Docker-from-Docker) ----
RUN install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    && chmod a+r /etc/apt/keyrings/docker.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
        https://download.docker.com/linux/debian \
        $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
        > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y \
        docker-ce-cli \
        docker-compose-plugin \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
