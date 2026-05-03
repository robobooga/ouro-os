@entity ProjectRoadmap
@brief Phased development plan for Ourobor OS, synthesized from docs/PLAN.md.

## Objective

Establish a compounding, product-agnostic LLM Wiki system (`ouro/wiki/`) supported by an offline-first dashboard (`ouro-webui/`). The wiki serves as the persistent knowledge base maintained by the LLM and curated by the developer.

## Phase 1: Ouro Core — COMPLETED

1. Created `ouro/wiki/schema.md` — philosophy, taxonomy, and maintenance protocols.
2. Created `ouro/wiki/index.md` — initialized the hub with links to categories.
3. Updated `CLAUDE.md` / `GEMINI.md` — LLM agent maintenance protocol appended.
4. Initialized logging and cleanup of project documentation.

@note PLAN.md references populating `ouro/wiki/entities/Parser.md` and foundational ADRs as part of Phase 1. These were not kept — the `ouro/` wiki directories must stay empty (skeleton only). See [ADR-001](../decisions/ADR-001-ouro-as-distributable-skeleton.md). The project's own documentation now lives in `wiki/` instead. See [ADR-002](../decisions/ADR-002-wiki-as-dual-purpose.md).

## Phase 2: Ouro-WebUI — IN PROGRESS

1. ✅ Scaffold `ouro-webui/` directory and basic structure.
2. ✅ Develop `builder.py` using `mistune` (Markdown + Doxygen tag processing) and `jinja2` (templating).
3. ⬜ Create responsive, portable dashboard templates.
4. ⬜ Integrate custom Mistune renderer for Ourobor protocol tags (`@entity`, `@brief`, `@note`, `@warning`).
5. ⬜ Verify generation and portability of the dashboard.

@warning Phase 2 is blocked by bugs in the current implementation. See [builder.py entity](../entities/builder.md) for the specific issues: broken Jinja2 template inheritance, dead code in `build()`, and no inter-page navigation. These must be resolved before the Phase 2 verification criteria can be met.

## Verification Criteria

These define what "done" looks like for the current phase:

| Criterion | Status |
|-----------|--------|
| LLM can look up a decision or entity in the wiki | ✅ Met — `wiki/` is now populated |
| `python ouro-webui/builder.py` generates a functional, linked dashboard | ❌ Blocked — template bug |
| Wiki structure is portable and drop-in ready | ✅ Met — `ouro/` skeleton is clean |

## Source

Synthesized from `docs/PLAN.md`. That file can be considered superseded by this entry and the broader `wiki/` documentation. It is retained in `docs/` as a historical artifact.
