@entity ADR-005
@brief `capture.py --crawl` now skips credential directories and sensitive files to prevent secrets from entering the capture queue.

## Context

`capture.py --crawl` stages every readable text file it finds. With only a basic `ignored_dirs` set (`.git`, `node_modules`, etc.), a crawl of a real project would routinely pick up `.env` files, PEM keys, SSH private keys, AWS credentials, and Terraform state — writing them verbatim into the plaintext `capture-queue.md`.

This is a silent data-leak risk: the queue is committed to version control in some workflows, and is read by LLM agents that may log or cache context.

## Decision

Three module-level constants and one guard function were added to `capture.py`:

- **`IGNORED_DIRS`** — expanded from 9 to ~50 entries, now including credential directories (`.aws`, `.ssh`, `.gnupg`, `secrets`, `certs`, `vault`, etc.) and infrastructure state directories (`.terraform`, `.vagrant`).
- **`SENSITIVE_NAMES`** — exact filenames skipped unconditionally (`.env` variants, SSH key files, `credentials.json`, `service-account.json`, `.netrc`, etc.).
- **`SENSITIVE_SUFFIXES`** — extensions skipped unconditionally (`.pem`, `.key`, `.p12`, `.pfx`, `.crt`, `.der`, `.secret`, `.token`, `.asc`, etc.).
- **`is_sensitive(file_path)`** — combines the above with heuristic substring matching on the filename (`secret`, `credential`, `password`, `token`, `api_key`, etc.).

The crawl loop calls `is_sensitive()` before `is_binary()` and before `stage()`. Skipped sensitive files are counted and reported in the crawl summary.

The `ouro/README.md` was updated with a callout directing users to review and adjust these constants for their project.

## Alternatives Considered

- **`.crawlignore` config file**: Flexible but adds a new file format, a parser, and documentation burden. Deferred — the constants approach is sufficient for now and easier to read at a glance.
- **CLI flags (`--exclude`, `--ignore`)**: Would allow per-invocation overrides but complicates the interface. The primary use case is a one-time crawl at project setup, not repeated ad-hoc use.
- **Warn instead of skip**: Would surface the sensitive file in the queue with a warning marker. Rejected — putting secret content in the queue even with a warning is worse than omitting it.

## Trade-offs

- **Lost**: A crawl will silently omit files the user might actually want to document (e.g. a `certs/` directory containing only public CA bundles). Users must adjust `IGNORED_DIRS` to opt back in.
- **Gained**: Secrets do not enter the capture queue by default. The skip count in the summary makes the omissions visible so users know to investigate.

## Rationale

Secure-by-default is the right posture for a tool that reads arbitrary project files into a plaintext log. The constants are clearly labeled and easy to edit; the README callout directs users to do so. The risk of silently excluding a non-sensitive file is far lower than the risk of silently capturing a secret.

@note The keyword list in `is_sensitive()` (`secret`, `credential`, `password`, `passwd`, `apikey`, `api_key`, `token`, `private_key`) is the most likely source of false positives. Projects that use these words in non-secret filenames (e.g. `token_counter.py`) should remove the relevant keywords from the list.
