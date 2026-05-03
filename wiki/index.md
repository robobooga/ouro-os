# Ourobor OS: Project Wiki

This is the internal documentation for the Ourobor OS project. It also serves as a reference example for users of the skill — this is what a populated `ouro/wiki/` looks like in practice.

> The distributable skill package lives in `ouro/`. This `wiki/` directory documents the Ourobor OS project itself and mirrors the structure users receive when they run `bootstrap.py`. See [ADR-002](decisions/ADR-002-wiki-as-dual-purpose.md).

## Core Documentation
- [Wiki Schema](schema.md) — Doxygen protocol and maintenance rules.

## Entities
- [capture.py](entities/capture.md) — Capture queue management and crawl tooling.
- [bootstrap.py](entities/bootstrap.md) — Project initialization and LLM environment detection.
- [builder.py](entities/builder.md) — Static site generator for the wiki web UI.
- [package.py](entities/package.md) — Distribution packager for the `ouro` skill.

## Architecture Decisions
- [ADR-001](decisions/ADR-001-ouro-as-distributable-skeleton.md) — `ouro/` is the distributable skeleton, not project docs.
- [ADR-002](decisions/ADR-002-wiki-as-dual-purpose.md) — `wiki/` serves as both internal docs and reference example.
- [ADR-003](decisions/ADR-003-doxygen-tags-in-markdown.md) — Doxygen tags embedded in Markdown.
- [ADR-004](decisions/ADR-004-webui-as-separate-concern.md) — Web UI decoupled from core skill.
- [ADR-005](decisions/ADR-005-crawl-sensitive-file-guard.md) — `--crawl` guards against staging secrets and credential files.

## Patterns
- [Capture-Synthesize Loop](patterns/capture-synthesize-loop.md) — The core knowledge accumulation workflow.

## Maps
- [System Architecture](maps/system-architecture.md) — Component relationships and data flows.
- [Project Roadmap](maps/project-roadmap.md) — Phased development plan and current status.

## Capture Queue
- [Capture Queue](capture-queue.md)
