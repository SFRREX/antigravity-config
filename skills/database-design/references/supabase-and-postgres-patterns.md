# Supabase & Modern PostgreSQL Development Patterns

## 1. Row-Level Security (RLS) Policy Architecture
Always enable RLS on user-facing tables:
```sql
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;

-- Tenants can only see their own organization data
CREATE POLICY "Tenant isolation for user_profiles"
ON user_profiles
FOR ALL
USING (org_id = (SELECT current_setting('app.current_org_id')::uuid));
```

## 2. Generated Columns & Computed Values
Store precomputed expressions for fast indexing without trigger overhead:
```sql
ALTER TABLE products 
ADD COLUMN search_vector tsvector 
GENERATED ALWAYS AS (to_tsvector('english', coalesce(name, '') || ' ' || coalesce(description, ''))) STORED;

CREATE INDEX idx_products_search ON products USING gin(search_vector);
```

## 3. Atomic Upserts (ON CONFLICT)
```sql
INSERT INTO user_stats (user_id, login_count, last_login)
VALUES ($1, 1, clock_timestamp())
ON CONFLICT (user_id) DO UPDATE SET
    login_count = user_stats.login_count + 1,
    last_login = EXCLUDED.last_login;
```

