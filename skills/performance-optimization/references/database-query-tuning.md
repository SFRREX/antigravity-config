# Database Query Tuning & N+1 Elimination

## 1. N+1 Query Detection & Batching
When fetching related records across parent rows:
```typescript
// ❌ N+1 Query Anti-Pattern: 1 query for users + N queries for posts
const users = await db.query('SELECT * FROM users LIMIT 50');
for (const user of users) {
  user.posts = await db.query('SELECT * FROM posts WHERE user_id = $1', [user.id]);
}

// ✅ Batched / Dataloader Pattern: Exactly 2 queries
const users = await db.query('SELECT * FROM users LIMIT 50');
const userIds = users.map(u => u.id);
const posts = await db.query('SELECT * FROM posts WHERE user_id = ANY($1)', [userIds]);
```

## 2. Connection Pool Sizing Formula
Optimal pool size according to PostgreSQL core maintainers:
$$\text{pool\_size} = (2 \times \text{CPU\_cores}) + \text{effective\_spindle\_count}$$

Never configure 500 connections on an 8-core database server (causes severe CPU context switching). Use PgBouncer or Supabase transaction pooler for high concurrency.

