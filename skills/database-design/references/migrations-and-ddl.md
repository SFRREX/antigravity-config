# Zero-Downtime SQL Migrations & DDL Patterns

## 1. Adding Columns with Defaults
In PostgreSQL 11+, adding a column with a constant default does NOT rewrite the table:
```sql
-- Safe and fast in PG 11+
ALTER TABLE users ADD COLUMN is_verified BOOLEAN NOT NULL DEFAULT false;
```

## 2. Creating Indexes Without Table Locks
Never run raw `CREATE INDEX` on production tables (it acquires `SHARE` lock, blocking writes):
```sql
-- Safe concurrent indexing
CREATE INDEX CONCURRENTLY idx_users_phone ON users(phone);
```

## 3. Renaming Columns Safely (Expand / Contract Pattern)
1. **Phase 1 (Expand)**: Add the new column: `ALTER TABLE users ADD COLUMN full_name TEXT;`
2. **Phase 2 (Dual Write)**: Write to both old and new columns via trigger or app code.
3. **Phase 3 (Backfill)**: Backfill historical data in bounded batches:
   ```sql
   UPDATE users SET full_name = name WHERE full_name IS NULL AND id IN (SELECT id FROM users WHERE full_name IS NULL LIMIT 1000);
   ```
4. **Phase 4 (Contract)**: Switch reads to `full_name`, deprecate and drop old column `name`.

