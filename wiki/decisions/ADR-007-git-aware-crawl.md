@entity ADR-007
@brief `--crawl --git` limits staging to git-changed files, replacing full-directory crawls for ongoing sessions to keep the capture queue small and synthesis cost low.

## Context

`capture.py --crawl` walks every file in the project and stages all of them. This is appropriate for the very first wiki population, but wasteful afterwards: unchanged files are re-queued, the LLM must re-synthesize docs it already wrote, and the queue grows beyond what the `capture-synthesize-loop` pattern warns against ("long queues lose context fidelity and become expensive").

The wiki is designed to compound incrementally — only new knowledge should enter the queue. The delta between sessions is precisely what git tracks.

## Decision

A `--git [N]` modifier was added to `--crawl`:

```bash
python capture.py --crawl --git        # working tree changes + last 1 commit
python capture.py --crawl --git 3     # working tree changes + last 3 commits
```

Internally, `get_git_changed_files(depth)` runs four git commands and unions the results:
1. `git diff --name-only` — unstaged tracked changes
2. `git diff --name-only --cached` — staged changes
3. `git ls-files --others --exclude-standard` — untracked new files
4. `git diff --name-only HEAD~{depth} HEAD` — files changed in the last `depth` commits

`crawl_git()` applies the same sensitivity, binary, and ignore-list filters as `crawl()`, restricted to files within the target directory. All git commands fail silently so the script degrades gracefully in non-git environments.

## Alternatives Considered

- **Full crawl always**: Simple but expensive; re-synthesizes unchanged code every session.
- **Manual per-file capture**: `capture.py path/to/file.py` is exact but requires the developer to know which files changed — defeats the automation purpose.
- **File-watch daemon**: Would require a persistent process and OS-specific APIs; out of scope for a stdlib-only portable skill.

## Trade-offs

| Factor | Impact |
|--------|--------|
| Queue size | Significantly reduced for ongoing sessions |
| Token cost | Proportional to actual changes, not codebase size |
| Git required | Graceful fallback (empty result + helpful message); full `--crawl` still available |
| Depth default | `1` covers the most recent commit; users who work in multi-commit batches should pass a larger N |
| Non-git changes | Files edited outside git (e.g. untracked, never-committed) are caught by the `git ls-files --others` command |

## Rationale

Git is already assumed present (`.git` is in `IGNORED_DIRS`). Scoping crawl to changed files is the most direct way to honour the "compounding" principle: the wiki should grow with new knowledge, not recycle old knowledge on every session start.

The `AGENT_PROTOCOL.md` was updated to make `--crawl --git` the recommended session-start command when the wiki already exists, with bare `--crawl` reserved for initial population.
