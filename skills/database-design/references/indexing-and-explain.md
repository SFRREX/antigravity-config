# PostgreSQL Indexing & EXPLAIN ANALYZE Guide

## 1. Index Selection Matrix

| Data / Query Pattern | Optimal Index | Example Syntax |
| :--- | :--- | :--- |
| Exact equality (`id = $1`) | **B-tree** (Default) | `CREATE INDEX idx_users_email ON users(email);` |
| Composite search (`tenant_id = $1 AND status = $2`) | **Multi-Column B-tree** | `CREATE INDEX idx_orders_tenant_status ON orders(tenant_id, status);` |
| JSONB containment (`data @> '{"role": "admin"}'`) | **GIN** (`jsonb_path_ops`) | `CREATE INDEX idx_data_gin ON users USING gin(data jsonb_path_ops);` |
| Array containment (`tags @> ARRAY['ai']`) | **GIN** | `CREATE INDEX idx_posts_tags ON posts USING gin(tags);` |
| Monotonic time series (`created_at > NOW() - '7 days'`) | **BRIN** (Block Range) | `CREATE INDEX idx_logs_created_brin ON logs USING brin(created_at);` |
| Soft deletes (`deleted_at IS NULL`) | **Partial Index** | `CREATE INDEX idx_active_users ON users(email) WHERE deleted_at IS NULL;` |

## 2. Reading EXPLAIN (ANALYZE, BUFFERS)
Always run:
```sql
EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
SELECT * FROM orders WHERE tenant_id = '123' AND created_at > NOW() - INTERVAL '30 days';
```

### Critical Signals to Identify:
1. **Seq Scan on Large Tables**: If table has >1,000 rows and query does `Seq Scan`, an index is missing.
2. **Buffers: shared hit vs shared read**:
   - `shared hit`: Page found in RAM cache (PostgreSQL shared buffers).
   - `shared read`: Page had to be fetched from physical disk.
3. **Rows Removed by Filter**: High number of removed rows indicates the index is not selective enough.
4. **Sort Method: external merge Disk**: Sort spilled to disk. Increase `work_mem` or create an index that provides pre-sorted order (`CREATE INDEX ... ON orders (created_at DESC)`).
