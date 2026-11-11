---
name: database-design
description: Master relational database architecture and PostgreSQL engineering engine. Designs normalized schemas, type-safe migrations, high-performance indexing strategies (B-tree, GIN, BRIN), constraint verification, and EXPLAIN (ANALYZE, BUFFERS) query optimization. Use when designing schemas, writing SQL migrations, diagnosing slow database queries, setting up foreign keys, or working with PostgreSQL, Supabase, SQLite, or Prisma/Drizzle ORMs.
---

# Relational Database Architecture & PostgreSQL Master Skill

Production guidelines for relational database schema modeling, SQL migrations, index selection, constraint enforcement, and query performance tuning.

## Core Capabilities
- **Schema Normalization & Modeling**: Third Normal Form (3NF), UUIDv7/ULID primary keys, explicit foreign key cascading (`ON DELETE RESTRICT/CASCADE`), timestamp standards (`timestamptz`).
- **High-Performance Indexing**:
  - **B-tree**: Default for equality, range queries, and sorting.
  - **GIN (Generalized Inverted Index)**: Full-text search, JSONB attributes (`jsonb_path_ops`), array containment (`@>`).
  - **BRIN (Block Range Index)**: Append-only time-series data and log tables.
  - **Partial Indexes**: Indexing only active records (`WHERE deleted_at IS NULL`).
- **Query Plan Interpretation**: Profiling queries with `EXPLAIN (ANALYZE, BUFFERS, VERBOSE)` to identify sequential scans, hash joins, and memory spills.
- **Migration Discipline**: Safe zero-downtime DDL changes (adding columns with defaults, concurrent index creation `CREATE INDEX CONCURRENTLY`).

---

## When to Invoke This Skill
Activate this skill when:
- Designing new tables or database schemas for web applications.
- Writing migration files (raw SQL, Prisma, Drizzle, Knex, Alembic).
- Troubleshooting slow SQL queries or database CPU spikes.
- Choosing the right index type for complex JSONB or array columns.
- Enforcing database-level business constraints (unique composite keys, check constraints).

---

## Production PostgreSQL Table Schema Template

```sql
-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Standardized production table pattern
CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug VARCHAR(64) NOT NULL,
    name VARCHAR(255) NOT NULL,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    deleted_at TIMESTAMPTZ,

    -- Constraints
    CONSTRAINT uq_organizations_slug UNIQUE (slug),
    CONSTRAINT chk_organizations_slug_format CHECK (slug ~* '^[a-z0-9-]+$')
);

-- Fast lookup for non-deleted records
CREATE UNIQUE INDEX idx_organizations_active_slug 
    ON organizations (slug) 
    WHERE deleted_at IS NULL;

-- Fast JSONB containment search
CREATE INDEX idx_organizations_metadata_gin 
    ON organizations USING gin (metadata jsonb_path_ops);
```

---

## Reference Guides
- [PostgreSQL Indexing & EXPLAIN ANALYZE Guide](./references/indexing-and-explain.md)
- [Zero-Downtime SQL Migrations & DDL Patterns](./references/migrations-and-ddl.md)
- [Supabase & Modern PostgreSQL Development Patterns](./references/supabase-and-postgres-patterns.md)
