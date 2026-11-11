---
name: docker-orchestration
description: Production containerization and Docker orchestration engine. Generates and audits secure multi-stage Dockerfiles, optimized docker-compose architectures, build layer caching, and rootless container environments. Use when containerizing applications, writing Dockerfiles, configuring docker-compose, optimizing container image sizes, or troubleshooting container build failures.
---

# Docker & Container Orchestration Master Skill

Production guidelines, security standards, and operational patterns for Docker and Docker Compose environments on Windows and Linux hosts.

## Core Capabilities
- **Multi-Stage Builds**: Minimalist final runtime images (distroless / alpine / slim) separating build dependencies from deployment artifacts.
- **Layer Caching Optimization**: Ordering instructions by change frequency (`COPY package*.json` $\rightarrow$ `RUN install` $\rightarrow$ `COPY src`).
- **Security & Hardening**: Rootless execution (`USER nonroot`), read-only root filesystems, dropping unused Linux capabilities, minimal exposed attack surface.
- **Compose Multi-Container Patterns**: Health checks, persistent volume mounting, private network segmentation, dependency ordering (`condition: service_healthy`).
- **Windows PowerShell First**: Native PowerShell container CLI commands, volume path formatting, and Docker Desktop integration.

---

## When to Invoke This Skill
Activate this skill when:
- Creating a new `Dockerfile` or `docker-compose.yml`.
- Optimizing an existing image that is too large or slow to build.
- Resolving build failures, cache invalidation issues, or container networking problems.
- Auditing container security (checking for root users, exposed secrets, or vulnerable base images).
- Setting up local development stacks with persistent database containers (PostgreSQL, Redis).

---

## Dockerfile Standard Architecture (Multi-Stage Node/Python/Go)

### Node.js (Vite / Next.js / Express)
```dockerfile
# Stage 1: Dependencies & Build
FROM node:20-alpine AS builder
WORKDIR /app
RUN apk add --no-cache libc6-compat
COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts
COPY . .
RUN npm run build && npm prune --production

# Stage 2: Minimal Production Runtime
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 appuser
COPY --from=builder --chown=appuser:nodejs /app/dist ./dist
COPY --from=builder --chown=appuser:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=appuser:nodejs /app/package.json ./package.json
USER appuser
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Python (FastAPI / Flask)
```dockerfile
# Stage 1: Build virtual environment
FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim AS runner
WORKDIR /app
RUN useradd -u 1001 -m nonroot
COPY --from=builder /opt/venv /opt/venv
COPY --chown=nonroot:nonroot . .
ENV PATH="/opt/venv/bin:$PATH"
USER nonroot
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Reference Guides
- [Dockerfile Best Practices & Layer Caching](./references/dockerfile-best-practices.md)
- [Docker Compose Multi-Container Patterns](./references/compose-patterns.md)
- [Container Security & Rootless Hardening](./references/security-and-caching.md)
