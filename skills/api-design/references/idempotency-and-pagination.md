# Idempotent Operations & Cursor Pagination Patterns

## 1. Idempotency Key Handling
When an API client sends `Idempotency-Key: <UUID>`:
1. Check Redis/Database cache for the key.
2. If key exists and status is `completed`, return the cached response immediately without re-executing logic.
3. If key exists and status is `in_progress`, return `409 Conflict` (request currently processing).
4. If key does not exist:
   - Insert key with `status: in_progress` (TTL: 24 hours).
   - Execute the transaction.
   - Cache final response code and body.
   - Update key with `status: completed`.

## 2. Keyset (Cursor-Based) Pagination
Never use `OFFSET` on large datasets ($O(N)$ scan overhead and page drift on inserts). Use keyset pagination:

```sql
-- Fetch next page after cursor
SELECT id, title, created_at
FROM articles
WHERE (created_at, id) < ($last_created_at, $last_id)
ORDER BY created_at DESC, id DESC
LIMIT 50;
```

API Response:
```json
{
  "data": [...],
  "pagination": {
    "has_more": true,
    "next_cursor": "eyJjcmVhdGVkX2F0IjoxNzEzNTQxMiwiaWQiOiJvYmpfOTkxIn0="
  }
}
```

