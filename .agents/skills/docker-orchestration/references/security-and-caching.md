# Container Security & Rootless Hardening

## 1. Never Run as Root
Default containers execute as root (`uid 0`). An escaped container process inherits host root privileges:
```dockerfile
# Create dedicated unprivileged group and user
RUN addgroup -S appgroup -g 10001 && \
    adduser -S -G appgroup -u 10001 -h /home/appuser appuser

# Set working directory ownership
WORKDIR /app
RUN chown -R appuser:appgroup /app

# Switch to non-root
USER appuser
```

## 2. Read-Only Root Filesystem
Make the container filesystem immutable, mounting writeable `/tmp` in tmpfs:
```yaml
services:
  app:
    read_only: true
    tmpfs:
      - /tmp
```

## 3. Drop Unneeded Linux Capabilities
```yaml
services:
  app:
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
```

## 4. Scan Images for CVEs
In PowerShell:
```powershell
docker scout cves my-app:latest
docker scout quickview my-app:latest
```
