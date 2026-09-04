# Work queue index

Two kinds of queue files:

- `01-11`: Validity review of each `TODO.md` unchecked item and each `DESIGN_TODO.md` defect.

- `A-G`: Concrete document lists — the actual files and cards that need checking.
  Each item is a checkbox.

## Document queues (files to check)

| File | State | What |
| --- | --- | --- |
| `A-title-question-marks.md` | done | Wiki files with `:::{.proof title="?"}` at HEAD. All resolved — zero instances remain. |
| `B-naked-urls.md` | done | Wiki files with bare `<https://...>` link text. All 161 converted and committed. |
| `C-unsolved-cards.md` | active, generated | Every unsolved problem card. Issue #2 target. **Generated** — `just unsolved`, and by the commit gate when a commit touches the corpus. Do not hand-edit or mirror its changing count here: a card leaves by gaining a solution. |
| `D-duplicate-bodies.md` | done | Duplicate-body pair, dispositioned (keep both). |
| `E-pdf-attachments.md` | active | Every PDF not in any collection provenance, classified by document content. The authored work is creating collection cards and extracting problems, one document at a time. |
| `F-wiki-doctor.md` | done | `just doctor` findings; the 5 structural one-child directories are recorded non-defects with real content. |
| `G-math-error-scan.md` | done | All 66 candidate mathematical errors found by the reading pass have been independently re-derived and dispositioned. |

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

Read a document queue (A-G). Check each file/card against its criterion.
Commit each completed check.
When a queue is empty, the work is done.
