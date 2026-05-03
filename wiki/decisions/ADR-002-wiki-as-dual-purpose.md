@entity ADR-002
@brief A root-level wiki/ directory serves as both internal project documentation and a reference example for users.

## Context

With `ouro/wiki/` reserved as a clean skeleton (see [ADR-001](ADR-001-ouro-as-distributable-skeleton.md)), the project needed an alternative location for two things:

1. **Internal documentation** — entities, decisions, and patterns for Ourobor OS's own codebase.
2. **A reference example** — a populated wiki that users can examine to understand what the system looks like in practice. New users who install the skill get empty directories and no model to follow.

## Decision

A root-level `wiki/` directory mirrors the `ouro/wiki/` structure exactly: same schema, same Doxygen conventions, same subdirectories (`entities/`, `decisions/`, `patterns/`, `maps/`). It is excluded from the distributed package.

It serves both purposes simultaneously — maintaining internal docs automatically keeps the reference example up to date.

`AGENT.md` references `wiki/` as the project's brain so all sessions default to maintaining it.

`SKILL.md` is intentionally omitted from `wiki/` — it is packaging metadata for `npx skills`, not documentation.

## Alternatives Considered

- **`docs/wiki/`**: Adds an extra nesting level and distances the wiki from the root where LLMs naturally look first.
- **Separate `example/` directory**: Splits the two purposes into two locations, requiring double maintenance to keep them aligned.
- **A demo branch**: Hard to keep in sync with main, and invisible to users browsing the default branch on GitHub.
- **Write example docs in a README section**: Flat text doesn't demonstrate the directory structure or file conventions that users need to replicate.

## Trade-offs

- **Lost**: A clear visual separation between "this is internal" and "this is an example."
- **Gained**: Single source of truth. One directory, two jobs. Less maintenance surface, more coherent.

## Rationale

The dual purpose works because the two needs are identical: both want a realistic, well-maintained wiki that follows the schema. Splitting them would mean maintaining two wikis that should always look the same.
