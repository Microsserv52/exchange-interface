---
icon: lucide/git-branch
---

# Versioning

The contract uses semantic versioning and is identified by the repository tag.

| Change | Version |
| --- | --- |
| Remove or rename a required field, change a status code or auth rule | MAJOR |
| Add an optional field, endpoint or error code | MINOR |
| Documentation, examples, schema metadata | PATCH |

## Compatibility rules

- Clients must ignore unknown optional fields.
- `sell`, `buy`, `date` and `id-account` remain required within a major version.
- Rates remain JSON numbers and identifiers remain UUID strings.
- The canonical path remains `/exchanges/{from}/{to}` inside a major version.
- The `date` value remains UTC and keeps the documented format.

## Service alignment

The Exchange service records the interface tag it implements in its changelog
and README. A service release must not publish before its contract checks pass
against this repository.
