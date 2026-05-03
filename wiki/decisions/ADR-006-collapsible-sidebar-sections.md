@entity ADR-006
@brief Sidebar sections with more than 20 links collapse via HTML details/summary to keep the sidebar manageable as the wiki grows.

## Context

As the wiki grows, sections like Decisions or Entities can accumulate many pages, making the sidebar unwieldy and requiring excessive scrolling.

## Decision

In `base.html`, any nav section whose page count exceeds 20 renders as a `<details class="nav-section">` element with a `<summary>` header instead of a plain `<h4>`. Smaller sections remain unchanged. A small inline DOMContentLoaded script reopens the `<details>` block that contains the currently active page, so navigation context is never lost.

## Consequences

- Sidebar stays compact by default for large sections.
- The active section always opens automatically — no manual hunting.
- Zero build-time cost; purely a template + CSS change.
- The threshold (20) is a constant in the Jinja2 template. If it needs to be configurable, it could be passed as a template variable from `builder.py`.

## Alternatives Rejected

- **JavaScript-only toggle**: adds complexity without benefit since `<details>` is native HTML with no dependencies.
- **Always collapsed**: bad UX — users would always need an extra click even for small sections.
