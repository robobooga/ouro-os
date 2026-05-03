@entity ADR-001
@brief The ouro/ directory is a clean distributable skeleton and must not contain project-specific documentation.

## Context

Ourobor OS is installed into target projects via `npx skills add robobooga/ourobor-os`. The `ouro/` directory is zipped by `package.py` and shipped directly to users — whatever is in it lands in their project root.

During early development, `ouro/wiki/` was the natural location for Ourobor OS's own documentation. The wiki infrastructure is already there, the schema is defined, and using it would demonstrate the system eating its own dog food.

## Decision

The `ouro/wiki/` subdirectories (`entities/`, `decisions/`, `patterns/`, `maps/`) must remain empty (`.gitkeep` only) in the repository. No project-specific documentation is written there.

## Alternatives Considered

- **Write docs in `ouro/wiki/`**: Rejected. Any content written there ships to every user's project at install time, polluting their workspace with Ourobor OS's internal notes from day one.
- **Strip docs during packaging**: Rejected. The packager would need to distinguish "internal" files from template files — fragile, error-prone, and creates a permanent discrepancy between what the repo contains and what gets shipped.

## Trade-offs

- **Lost**: The project cannot self-document using its own primary infrastructure without special casing.
- **Gained**: The distributed package stays purposefully empty. Users get a blank slate with no noise to remove, which is the correct first-run experience.

## Rationale

A clean install experience is non-negotiable for a tool whose first impression is the emptiness of its directories. See [ADR-002](ADR-002-wiki-as-dual-purpose.md) for the alternative location chosen for project documentation.
