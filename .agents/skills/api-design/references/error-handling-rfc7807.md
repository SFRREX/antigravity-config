# RFC 7807 Problem Details & Error Handling Standard

## HTTP Status Code Hierarchy
Always map errors to appropriate HTTP status codes:

- `400 Bad Request`: Malformed JSON or syntax errors.
- `401 Unauthorized`: Missing or invalid authentication token.
- `403 Forbidden`: Authenticated user lacks permission for this specific resource.
- `404 Not Found`: Resource does not exist (or concealed for security).
- `409 Conflict`: Unique constraint violation or state transition conflict.
- `422 Unprocessable Entity`: Syntactically valid JSON, but violates business validation rules.
- `429 Too Many Requests`: Rate limit exceeded (include `Retry-After` header).
- `500 Internal Server Error`: Unhandled application exception.

## Field-Level Error Details
Always return structured array of parameter errors:
```json
{
  "type": "https://api.example.com/errors/invalid-payload",
  "title": "Invalid Payload",
  "status": 422,
  "invalid_params": [
    { "name": "email", "reason": "Invalid email address format" },
    { "name": "age", "reason": "Must be 18 or older" }
  ]
}
```
