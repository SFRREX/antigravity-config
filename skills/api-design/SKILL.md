---
name: api-design
description: Production RESTful API contract design and OpenAPI specification engine. Designs type-safe HTTP APIs, OpenAPI 3.1 documents, idempotent mutation keys (Idempotency-Key), standardized RFC 7807 error envelopes, cursor-based pagination, and backwards-compatible versioning. Use when designing API endpoints, writing OpenAPI/Swagger specs, standardizing error codes, implementing webhook payloads, or reviewing API architecture.
---

# RESTful API Contract & Architecture Master Skill

Production standards, schema design patterns, and operational protocols for modern HTTP and RESTful APIs.

## Core Capabilities
- **OpenAPI 3.1 Specification**: Single source of truth for request schemas, response codes, security schemes (Bearer JWT, API Keys), and component models.
- **RFC 7807 Problem Details**: Standardized machine-readable error responses (`application/problem+json`) with error types, titles, statuses, and field-level validation violations.
- **Idempotency Standards**: Using `Idempotency-Key` headers on mutating requests (`POST /v1/payments`) to prevent double-charging or duplicate record creation on network retries.
- **Cursor-Based Pagination**: Safe, monotonic keyset pagination (`?limit=50&starting_after=obj_123`) over unstable offset pagination.
- **Consistent URI & Verb Conventions**: Plural nouns (`/api/v1/customers`), explicit sub-resources (`/api/v1/customers/{id}/invoices`), proper HTTP verbs (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).

---

## When to Invoke This Skill
Activate this skill when:
- Designing new backend endpoints, route handlers, or microservices.
- Authoring or auditing OpenAPI 3.0 / 3.1 YAML/JSON specifications.
- Defining error response formats across an engineering team.
- Implementing webhook dispatchers or webhook ingestion handlers.
- Resolving breaking API changes with backwards-compatible versioning.

---

## Standardized RFC 7807 Error Response (`application/problem+json`)

```json
{
  "type": "https://api.example.com/errors/validation-failed",
  "title": "Validation Failed",
  "status": 422,
  "detail": "The request payload failed validation against the schema.",
  "instance": "/api/v1/users/usr_981/orders",
  "code": "VALIDATION_ERROR",
  "invalid_params": [
    {
      "name": "amount",
      "reason": "Must be greater than 0"
    },
    {
      "name": "currency",
      "reason": "Must be an ISO 4217 code (e.g. USD, EUR)"
    }
  ]
}
```

---

## Reference Guides
- [OpenAPI 3.1 Specification Blueprint](./references/openapi-specification.md)
- [RFC 7807 Problem Details & Error Handling Standard](./references/error-handling-rfc7807.md)
- [Idempotent Operations & Cursor Pagination Patterns](./references/idempotency-and-pagination.md)
