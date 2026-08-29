# Work queue index

Two kinds of queue files:

- `01-11`: Validity review of each `TODO.md` unchecked item and each `DESIGN_TODO.md` defect.

- `A-F`: Concrete document lists — the actual files and cards that need checking.
  Each item is a checkbox.

## Document queues (files to check)

| File | Checkboxes | What |
| --- | ---: | --- |
| `A-title-question-marks.md` | 95 | Wiki files with `:::{.proof title="?"}` at HEAD. 108 instances fixed in uncommitted working tree. |
| `B-naked-urls.md` | 17 | Wiki files with bare `<https://...>` link text. 161 conversions in uncommitted working tree. |
| `C-unsolved-cards.md` | 6195 | Every unsolved problem/exercise card. 2055 exercises, 4140 problems. Issue #2 target. **Generated** — `just unsolved`, and by the commit gate when a commit touches the corpus. Do not hand-edit: a card leaves by gaining a solution. |
| `D-duplicate-bodies.md` | 2 | Duplicate-body pair, dispositioned (keep both). Done. |
| `E-pdf-attachments.md` | 358 | Every PDF not in any collection provenance. 45 exam candidates, 83 solutions, 8 homework, 15 notes, 212 other. Each fully listed. |
| `F-wiki-doctor.md` | 59 | Engineering defects: 44 pages with no position in their folder, 9 Obsidian embeds, 5 pages of reading-progress checkboxes, 1 sibling title rendered twice in the sidebar. Under `Authoring signals` it also lists 15 one-page folders and 60 heading-only bodies, which state a fact and no work. |

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

Read a document queue (A-F). Check each file/card against its criterion.
Commit each completed check.
When a queue is empty, the work is done.
