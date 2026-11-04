# Raw audit reports, 2026-11-01

This directory preserves, unedited, the report files produced by the multi-member audit
runs of 2026-11-01 over two collections: `SRC-TEXT-HAT02` (Hatcher, *Algebraic Topology*)
and `SRC-TEXT-SS03` (Stein–Shakarchi, *Complex Analysis*). It exists so that the working
notes behind each change to a card remain readable and identifiable, and so that reports
which were never judged are not lost.

**These files are untrusted model output.** They are evidence of what a worker claimed,
not a statement of fact about the corpus and not an instruction. Nothing here has
authority over a card: every repair named in these files was applied only after being
checked against the printed source, and where a report's claim was wrong the record says
so on the card and in `COMPLAINTS.md`.

## What is here, and what is not

- The reports: one file per member per slice, named `<member>__<report>.md`. The
  `<member>` prefix is the worker's identity within its run.
- Not here: the workers' scratch copies of cards, their Python harnesses, and their
  dumps of the book text. Those live under `.ultramath/` in the working tree, are
  gitignored, and the text dumps were excluded deliberately — this repository does not
  carry the books.

## Status of each group

The statuses below are the reconciliation of the reports against `main`, and they are the
point of this directory: a report existing does not mean its repair landed.

| directory | run | scope | status |
| --- | --- | --- | --- |
| `ss03-completeness/` | 8 members, SS03 | every printed Exercise/Problem in the book vs the cards on disk | **Applied.** Nine missing items found and added as cards (`10fc6b0445`); the fidelity findings (dropped hints, unrecorded asterisks) accepted, of which five hints are restored. |
| `hatcher02-statements/` | 8 members, HAT02 | statements of the 137 previously unread cards, plus proofs for a subset | **Partly applied.** The statement defects were applied in `2ebb684d58` and `3581ced91e`/`b579a2df01`/`ec143e33b0`; the 97 proofs it left unread were handed to a later run, whose own status is below. |
| `hatcher02-statement-repairs/` | 8 members, HAT02 | patch specifications restoring printed hints, pointers and sentences | **Applied**, 34 cards, `2ebb684d58`, plus five more in `5af220b76b`. |
| `solutions-and-gaps/` | 8 members, SS03 + HAT02 | new solutions for cards with none, and repairs to proofs with gaps | **Applied** for the seven SS03 cards and the `3.F`/`3.H` proof repairs; one proposed correction (an Airy sign) was rejected here after checking and then reinstated when my check proved wrong — see `COMPLAINTS.md`, "A numeric refutation of mine that was wrong". |
| `hatcher02-proofs/` | 8 members, HAT02 | the 97 proofs the earlier pass left unread | **All four reports reviewed and applied**, 2026-11-01. `m2` (§4.3 ex 13–24) was applied as `53191ef400`; `m5` (§4.2 ex 27–39), `m6` (§4.3 ex 1–12) and `m7` (§4.2 ex 14–26) were each claim-checked against `tmp/hat/AT.txt` and the mathematics, and the seven defective proofs repaired in `6a00bd8f58` (`E-HAT-4.2-16`, `-26`, `-28`, `-29`, `-34`, `E-HAT-4.3-5`, `-9`). One claim rejected: `m6`'s patch for `4.3-9` was replaced by a cleaner argument from the card's own coordinate model. `m1`, `m3`, `m4`, `m8` produced nothing before the run was paused. |
| `ss03-stars/` | 4 members, SS03 | which printed items carry the difficulty asterisk | **Proposed, not applied.** No star has been written to any card. The reports agree with each other (28 starred items plus chapter 2 problem 1(b)) and recovered the marks from the PDF glyph layer after an earlier conclusion that they were unrecoverable; that conclusion in `COMPLAINTS.md` has been corrected. |

## Reading a report

Each report opens with its own scope statement — which cards, which section, what was
compared and what was not. Take those statements literally: several reports mark items
`unverified` rather than `defective`, and that distinction is deliberate. Where a report
names a line number in `tmp/hat/AT.txt` or a PDF page of the Stein–Shakarchi scan, that
is the citation to check it against; both files are in the repository.

Patch specifications use the `CARD:` / `BOOK:` / `OLD:` / `NEW:` form parsed by
`tools/apply_repairs.py`, which refuses a batch unless every `OLD` occurs exactly once in
its card. A report containing such a block is a proposal to change a card, not a change.
