@entity ADR-004
@brief The web UI (ouro-webui/) is decoupled from the core ouro/ skill and is not part of the distributed package.

## Context

Ourobor OS's primary interface is plain Markdown files — readable in any editor, any LLM context window, and any terminal. A web UI for browsing the wiki was prototyped in `ouro-webui/` using `mistune` and `jinja2`.

The question arose whether `builder.py` and its templates should be bundled into the distributed `ouro/` skill package so users get a dashboard out of the box.

## Decision

The web UI lives in `ouro-webui/` and is excluded from the distributed package. Users who want a rendered dashboard use the web UI separately. The core skill has no dependency on `mistune`, `jinja2`, or the templates.

## Alternatives Considered

- **Bundle web UI in `ouro/`**: Adds `mistune`, `jinja2`, and template files to every install. Most users running the skill in an LLM coding session don't need a browser dashboard — this adds weight with no benefit for the majority use case.
- **Make web UI a separate pip package**: Premature. The web UI has known bugs (template inheritance broken, no navigation sidebar) and is not ready for independent distribution.
- **Build web UI with JavaScript (client-side)**: Would eliminate Python dependencies for rendering, but adds a JS build step and larger file footprint. Over-engineered for the current stage.

## Trade-offs

- **Lost**: Out-of-the-box visual dashboard for new users. The install experience is text-only.
- **Gained**: Core skill stays lightweight — pure Python stdlib plus Markdown files. The web UI can evolve (and be fixed) independently without affecting skill compatibility or version constraints.

## Rationale

The wiki's primary consumer is an LLM agent reading files in a coding session, not a human browsing in a browser. The web UI is a nice-to-have for human navigation and is not on the critical path for the skill's core value proposition.

@note The web UI is stable. All previously documented issues have been resolved. See [builder.py entity](../entities/builder.md) for current status.
