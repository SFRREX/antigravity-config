# Docker Compose Multi-Container Patterns

## Full-Stack Architecture with PostgreSQL, Redis & App

```yaml
version: '3.8'

services:
  db:
    image: postgres:17-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: app_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d app_db"]
      interval: 5s
      timeout: 5s
      retries: 5
    networks:
      - internal

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    command: ["redis-server", "--appendonly", "yes"]
    volumes:
      - redisdata:/data
    networks:
      - internal

  api:
    build:
      context: .
      target: runner
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgres://postgres:${DB_PASSWORD}@db:5432/app_db
      REDIS_URL: redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
    networks:
      - internal
      - public

volumes:
  pgdata:
  redisdata:

secrets:
  db_password:
    file: ./secrets/db_password.txt

networks:
  internal:
    internal: true
  public:
```

