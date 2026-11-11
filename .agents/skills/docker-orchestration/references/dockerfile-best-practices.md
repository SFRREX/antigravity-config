# Dockerfile Best Practices & Layer Caching

## 1. Instruction Ordering for Cache Maximization
Docker caches each layer until an instruction changes. Subsequent instructions must re-execute:

```dockerfile
# 1. Base OS (Changes rarely)
FROM node:20-alpine

# 2. Working directory
WORKDIR /app

# 3. System packages (Changes rarely)
RUN apk add --no-cache curl

# 4. Dependency manifests ONLY (Changes on new packages)
COPY package*.json ./

# 5. Dependency install (Cached until package.json changes)
RUN npm ci

# 6. Application source code (Changes frequently)
COPY . .

# 7. Build step
RUN npm run build
```

## 2. Dockerignore Requirements
Always create a `.dockerignore` file alongside the `Dockerfile`:
```text
node_modules
.git
.github
*.log
.env*
.DS_Store
dist
coverage
```

## 3. Windows PowerShell Invocation Patterns
In PowerShell on Windows:
```powershell
# Build with BuildKit enabled
$env:DOCKER_BUILDKIT=1
docker build -t my-app:latest .

# Inspect image layers and size
docker history my-app:latest

# Run with port mapping and env file
docker run --rm -p 8080:8000 --env-file .env.production my-app:latest
```
