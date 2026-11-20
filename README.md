# Exchange interface

Canonical HTTP contract for the [Microsserv52 Exchange service](https://github.com/Microsserv52/exchange).
The contract is published independently so Gateway, Order and contract tests can
consume the exact version without cloning the service or the
[platform repository](https://github.com/Microsserv52/platform).

[![Contract validation](https://github.com/Microsserv52/exchange-interface/actions/workflows/ci.yml/badge.svg)](https://github.com/Microsserv52/exchange-interface/actions/workflows/ci.yml)
[![Documentation](https://github.com/Microsserv52/exchange-interface/actions/workflows/docs.yml/badge.svg)](https://microsserv52.github.io/exchange-interface/)

> [!IMPORTANT]
> This repository contains contract artifacts only. It has no provider
> credentials, HTTP client implementation or deployment infrastructure. The
> runnable service lives in [`Microsserv52/exchange`](https://github.com/Microsserv52/exchange).

## Quick start

```bash
git clone https://github.com/Microsserv52/exchange-interface.git
cd exchange-interface
./scripts/bootstrap.sh
```

`bootstrap.sh` validates the OpenAPI document, every JSON Schema and every
example. It prefers Docker and falls back to local `uv` only when Docker is not
available. No runtime container is required for consumers: the published
artifacts are plain YAML and JSON files.

## Artifacts

| Artifact | Purpose |
| --- | --- |
| [`openapi/exchange.yaml`](openapi/exchange.yaml) | Canonical OpenAPI 3.1 document. |
| [`schemas/exchange-rate.schema.json`](schemas/exchange-rate.schema.json) | Exchange response schema. |
| [`schemas/error.schema.json`](schemas/error.schema.json) | Stable error envelope. |
| [`examples/`](examples/) | Valid, unsupported-currency and provider-failure examples. |

## Endpoint

`GET /exchanges/{from}/{to}` requires a bearer JWT whose `sub` is the account
UUID.

```json
{
  "sell": 0.8202,
  "buy": 0.8150,
  "date": "2021-09-01 14:23:42",
  "id-account": "0195ae95-5be7-7dd3-b35d-7a7d87c404fb"
}
```

`date` is UTC. Unsupported or invalid ISO 4217 codes return `422`. Provider
failures return `502`. Provider rate limiting returns `429`; missing provider
configuration or instance saturation returns `503`.

The platform Gateway routes `/exchanges/**` to the Exchange service.

## Consuming the contract

1. Pin a release tag or commit SHA from this repository.
2. Read `openapi/exchange.yaml` into your client generator or contract test.
3. Keep generated client versions aligned with the service release notes.
4. Treat unknown error fields as forward compatible; required fields and status
   codes are stable.

## Versioning

Semantic versioning applies: MAJOR for removed fields or changed status codes,
MINOR for additive optional fields or errors, PATCH for documentation. See
[Versioning](docs/versioning.md).

## Validation commands

```bash
make bootstrap   # container-first contract validation
make validate    # force Docker validation
make lint        # Ruff formatting and lint checks
make test        # validator regression tests
```

## Links

- [Microsserv52 organization](https://github.com/Microsserv52)
- [Platform repository](https://github.com/Microsserv52/platform)
- [Published platform documentation](https://microsserv52.github.io/platform/)
- [Exchange service repository](https://github.com/Microsserv52/exchange)
- [Exchange interface documentation](https://microsserv52.github.io/exchange-interface/)
