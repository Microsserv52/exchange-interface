---
icon: lucide/route
---

# Contract

## Endpoint

`GET /exchanges/{from}/{to}`

| Component | Rule |
| --- | --- |
| Authentication | Bearer HS256 JWT; `sub` must be the account UUID. |
| `from`, `to` | ISO 4217 alphabetic codes, three letters, case-insensitive. |
| Success | `200` with `ExchangeRate`. |
| Invalid code | `422 INVALID_CURRENCY`. |
| ISO-valid but provider-unsupported | `422 UNSUPPORTED_CURRENCY`. |
| Provider timeout, 5xx or malformed payload | `502 PROVIDER_UNAVAILABLE` or `PROVIDER_INVALID_RESPONSE`. |
| Provider rate limit | `429 RATE_LIMITED` with `Retry-After`. |
| Missing provider configuration | `503 PROVIDER_NOT_CONFIGURED`. |
| Instance concurrency saturated | `503 PROVIDER_BUSY`. |

## ExchangeRate

```json
{
  "sell": 0.8202,
  "buy": 0.8150,
  "date": "2021-09-01 14:23:42",
  "id-account": "0195ae95-5be7-7dd3-b35d-7a7d87c404fb"
}
```

| Field | Type | Rules |
| --- | --- | --- |
| `sell` | number > 0 | Provider sell rate after the configured spread. |
| `buy` | number > 0 | Provider buy rate after the configured spread. |
| `date` | string | UTC `YYYY-MM-DD HH:MM:SS`. |
| `id-account` | UUID string | Token subject. |

!!! warning "Timestamp timezone"

    The platform contract requires the space-separated `date` format without an
    offset. The value is always UTC; the service converts the provider timestamp
    to UTC before formatting it.

## Error envelope

```json
{
  "code": "PROVIDER_UNAVAILABLE",
  "message": "Exchange provider is unavailable"
}
```

Error messages never include provider API keys, authorization headers or raw
provider payloads.

## Machine-readable files

- [OpenAPI](openapi/exchange.yaml)
- [Rate schema](schemas/exchange-rate.schema.json)
- [Error schema](schemas/error.schema.json)
