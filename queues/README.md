# Work queue index

Two kinds of queue files:

- `01-11`: Validity review of each `TODO.md` unchecked item and each `DESIGN_TODO.md` defect.

- `A-F`: Concrete document lists — the actual files and cards that need checking.
  Each item is a checkbox.

## Document queues (files to check)

| File | Checkboxes | What |
| --- | ---: | --- |
| `A-title-question-marks.md` | 0 | Wiki files with `:::{.proof title="?"}` at HEAD. All resolved — zero instances remain. |
| `B-naked-urls.md` | 0 | Wiki files with bare `<https://...>` link text. All 161 converted and committed. |
| `C-unsolved-cards.md` | 6195 | Every unsolved problem/exercise card. 2055 exercises, 4140 problems. Issue #2 target. **Generated** — `just unsolved`, and by the commit gate when a commit touches the corpus. Do not hand-edit: a card leaves by gaining a solution. |
| `D-duplicate-bodies.md` | 2 | Duplicate-body pair, dispositioned (keep both). Done. |
| `E-pdf-attachments.md` | 358 | Every PDF not in any collection provenance. 45 exam candidates, 83 solutions, 8 homework, 15 notes, 212 other. Each fully listed. |
| `F-wiki-doctor.md` | 59 (STALE) | All items reference old wiki paths (`wiki/Algebra/` etc.) that no longer exist. Needs regeneration from `just doctor`. |

## Validity review queues (TODO.md items)

| File | Open | Done | Owner | Notes |
| --- | ---: | ---: | --- | --- |
| `01-corpus-defects.md` | 2 | 2 | #2 (OPEN) | 1.3/1.4 done, 1.1/1.2 open (source review) |
| `02-publish-authored-pages.md` | 0 | 4 | #5, #23 (COMPLETED) | All verified via Queue 06 |
| `03-publish-subject-branches.md` | 0 | 8 | #24–#29 (COMPLETED) | All verified via Queue 06 |
| `04-reader-exam-generator.md` | 0 | 7 | #10 (COMPLETED) | All done |
| `05-repair-rendered-residue.md` | 0 | 3 | #41 (COMPLETED) | All defects resolved (Queue 11) |
| `06-prove-deployed-site.md` | 0 | 7 | #30 (COMPLETED) | All verified against local build |
| `07-source-preservation-closeout.md` | 2 | 4 | #11 (COMPLETED) | M4/M6 record-keeping |
| `08-owner-decisions.md` | 0 | 3 | none | All done |
| `09-author-solutions.md` | 6 | 0 | #2 (OPEN) | Repeating loop |
| `10-close-roadmap.md` | 0 | 5 | #1 (CLOSED) | All obligations hold |
| `11-design-issues.md` | 0 | 25 | #41 surface | 25/25 resolved (17 fixed, 8 design-accepted) |

## How to use

Read a document queue (A-F). Check each file/card against its criterion.
Commit each completed check.
When a queue is empty, the work is done.
