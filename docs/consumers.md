---
icon: lucide/users
---

# Consumers

## Generate a client

```bash
git clone --branch v0.1.0 https://github.com/Microsserv52/exchange-interface.git
npx @openapitools/openapi-generator-cli generate \
  -i exchange-interface/openapi/exchange.yaml \
  -g typescript-fetch \
  -o generated/exchange-client
```

## Validate captured payloads

```bash
uvx --from check-jsonschema check-jsonschema \
  --schemafile schemas/exchange-rate.schema.json exchange.json
```

## Contract tests in a service

1. Copy the pinned `schemas/` and `openapi/` artifacts into your test
   resources, or check out this repository in CI.
2. Validate every success payload against `exchange-rate.schema.json`.
3. Validate every error payload against `error.schema.json`.
4. Assert status codes, authentication and `Retry-After` behavior.

The Exchange service validates its responses against a vendored contract
snapshot. Update that snapshot from the pinned interface revision when changing
the contract.
