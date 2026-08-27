# Work queue index

Two kinds of queue files:

- `01-11`: Validity review of each `TODO.md` unchecked item and each `DESIGN_TODO.md` defect. Per-item status (open/done/decision-unmade) with evidence.
- `A-E`: Concrete document lists — the actual files and cards that need checking. These are the long lists.

## Document queues (files to check)

| File | Count | What |
| --- | ---: | --- |
| `A-title-question-marks.md` | 95 | Wiki files with `:::{.proof title="?"}` at HEAD. 108 instances fixed in uncommitted working tree. |
| `B-naked-urls.md` | 17 | Wiki files with bare `<https://...>` link text. 161 conversions in uncommitted working tree. |
| `C-unsolved-cards.md` | 6195 | Problem/exercise cards with no solution and no incoming `solves` relation. Issue #2 target. |
| `D-duplicate-bodies.md` | 1 pair | Duplicate-body pair, dispositioned (keep both). Done. |
| `E-pdf-attachments.md` | 358 | PDFs on disk not in any collection provenance. 45 exam candidates, 83 solutions, 8 homework, 15 notes, 212 other. |

## Validity review queues (TODO.md items)

| File | Open | Done | Owner | Notes |
| --- | ---: | ---: | --- | --- |
| `01-corpus-defects.md` | 2 | 2 | #2 (OPEN) | 1.3 done, 1.4 partial |
| `02-publish-authored-pages.md` | 4 | 0 | #5, #23 (COMPLETED) | Needs rebuild |
| `03-publish-subject-branches.md` | 2 | 6 | #24–#29 (COMPLETED) | Publication done; proof not |
| `04-reader-exam-generator.md` | 3 | 4 | #10 (COMPLETED) | 4.6/4.7 decisions unmade |
| `05-repair-rendered-residue.md` | 3 | 0 | #41 (COMPLETED) | 22 defects untouched |
| `06-prove-deployed-site.md` | 7 | 0 | #30 (COMPLETED) | Needs rebuild |
| `07-source-preservation-closeout.md` | 2 | 4 | #11 (COMPLETED) | M4/M6 record-keeping |
| `08-owner-decisions.md` | 2 | 0 | none | Needs rebuild + decision |
| `09-author-solutions.md` | 6 | 0 | #2 (OPEN) | Repeating loop |
| `10-close-roadmap.md` | 1 | 4 | #1 (CLOSED) | 10.3 contested |
| `11-design-issues.md` | 22 | 3 | #41 surface | 3 being fixed in working tree |

## How to use

Read a document queue (A-E). Check each file/card against its criterion.
Commit each completed check. When a queue is empty, the work is done.

Validity review queues (01-11) record whether each TODO.md item is real open work.
They do not themselves need checking — they are the assessment.