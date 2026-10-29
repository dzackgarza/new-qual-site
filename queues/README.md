# Work queue index

Two kinds of queue files:

- `01`–`12`: Validity review of `TODO.md` items and of the wiki design defects once recorded in `DESIGN_TODO.md` (removed in `9334a7e02`). All are closed.

- `A`–`H`: Concrete document lists — the actual files and cards that need checking or migration.

The order of remaining work is the [TODO.md milestone](../TODO.md#milestone-publish-with-every-remedial-obligation-cleared), not this index.

## Document queues (files to check)

| File | State | What |
| --- | --- | --- |
| `C-unsolved-cards.md` | active, generated | Every unsolved problem card. Issue #2 target. **Generated** — `just unsolved`, and by the commit gate when a commit touches the corpus. Do not hand-edit or mirror its changing count here: a card leaves by gaining a solution. |

## Validity review queues (TODO.md items)

| File | Open | Done | Owner | Notes |
| --- | ---: | ---: | --- | --- |
| `01-corpus-defects.md` | 0 | 4 | #2 (OPEN) | All done |
| `02-publish-authored-pages.md` | 0 | 4 | #5, #23 (COMPLETED) | All verified via Queue 06 |
| `03-publish-subject-branches.md` | 0 | 8 | #24–#29 (COMPLETED) | All verified via Queue 06 |
| `04-reader-exam-generator.md` | 0 | 7 | #10 (COMPLETED) | All done |
| `05-repair-rendered-residue.md` | 0 | 3 | #41 (COMPLETED) | All defects resolved (Queue 11) |
| `06-prove-deployed-site.md` | 0 | 7 | #30 (COMPLETED) | All verified against local build |
| `07-source-preservation-closeout.md` | 0 | 6 | #11 (COMPLETED) | All done |
| `08-owner-decisions.md` | 0 | 3 | none | All done |
| ~~`09-author-solutions.md`~~ | — | — | — | Removed: redundant with Queue C |
| `10-close-roadmap.md` | 0 | 5 | #1 (CLOSED) | All obligations hold |
| `11-design-issues.md` | 0 | 25 | #41 surface | 25/25 resolved (17 fixed, 8 design-accepted) |

## How to use

Read a document queue (A-H). Check each file/card against its criterion.
Commit each completed check.
When a queue is empty, the work is done.
