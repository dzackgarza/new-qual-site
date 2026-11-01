# Evidence audit and card census for SRC-TEXT-HAT02

Auditor: m5. Direction: test the premise on which the other seven directions and the brief rest —
that the 16 "already read" sections really carry the stated completion evidence — and audit in full
any card that fails the test and that no other direction holds.

Method: for every card I parsed the YAML frontmatter `audit:` list and recorded each event with its
`by`/`date`/`note` (`audit_events.py`, output `audit_events.json`, both in this directory). A card
counts as *established read* only if it carries a `solution-reviewed` event **by `claude`** with a
non-empty note, which is the brief's own criterion.

## 1. Card census (the brief asks for the count per section)

`corpus/collections/SRC-TEXT-HAT02/` has 31 section directories and **437 cards**:

| section | cards | cards with a `solution-reviewed` event | of those, by `claude` | cards with **no** `solution-reviewed` at all |
|---|---|---|---|---|
| 1-1 | 20 | 16 | **0** | E-HAT-1.1-1, -11, -12, -17 |
| 1-2 | 22 | 22 | 22 | — |
| 1-3 | 33 | 33 | 33 | — |
| 1-a | 14 | 14 | 14 | — |
| 1-b | 9 | 9 | 9 | — |
| 2-1 | 31 | 31 | 31 | — |
| 2-2 | 42 | 42 | 42 | — |
| 2-3 | 4 | 4 | 4 | — |
| 2-b | 11 | 9 | **0** | E-HAT-2.B-5, -9 |
| 2-c | 9 | 8 | **0** | E-HAT-2.C-2 |
| 3-1 | 13 | 13 | 13 | — |
| 3-2 | 17 | 17 | 17 | — |
| 3-3 | 35 | 35 | 35 | — |
| 3-a | 6 | 6 | 6 | — |
| 3-b | 5 | 5 | 5 | — |
| 3-c | 16 | 16 | 16 | — |
| 3-d | 3 | 2 | 0 | E-HAT-3.D-3 |
| 3-e | 4 | 4 | 4 | — |
| 3-f | 9 | 7 | 0 | E-HAT-3.F-3, -8 |
| 3-h | 6 | 5 | 0 | E-HAT-3.H-2 |
| 4-1 | 23 | 21 | 9 | E-HAT-4.1-13, -18 |
| 4-2 | 39 | 34 | 0 | E-HAT-4.2-5, -8, -24, -26, -32 |
| 4-3 | 24 | 21 | 0 | E-HAT-4.3-19, -22, -24 |
| 4-a | 5 | 2 | 0 | E-HAT-4.A-1, -2, -4 |
| 4-b | 2 | 1 | 0 | E-HAT-4.B-1 |
| 4-d | 10 | 7 | 0 | E-HAT-4.D-3, -5, -6 |
| 4-f | 3 | 3 | 0 | — |
| 4-g | 4 | 2 | 0 | E-HAT-4.G-2, -4 |
| 4-h | 4 | 2 | 0 | E-HAT-4.H-2, -4 |
| 4-i | 3 | 2 | 0 | E-HAT-4.I-2 |
| 4-k | 6 | 5 | 0 | E-HAT-4.K-2 |
| 4-l | 5 | 5 | 0 | — |

34 cards of the collection carry no `solution-reviewed` event of any kind.

## 2. Result of the evidence test

**The brief's completion claim holds for fifteen of the sixteen sections it lists**, and the data
corroborate it in an unexpected place: in §4.1 exactly the nine cards `E-HAT-4.1-1 … -9` carry
`claude` reviews, which is precisely the "§4.1 exercises 1–9" the brief declares done. So the
`claude`-reviewed subset really is the done slice there.

**It fails for §1.1.** No card of §1.1 carries a `solution-reviewed` event by `claude`; 16 carry one
by `gpt-5.6-sol`, and four carry none at all (`1.1-1`, `1.1-11`, `1.1-12`, `1.1-17`). By the
brief's own criterion, §1.1 cannot be reported as read on that evidence. Since the criterion fails
for the whole section, I audited **all 20 §1.1 cards** instead of assuming the other 16; full
verdicts in `findings-1-1-evidence.md`. Result: 19 statements match the printed exercises exactly and
all 20 proofs are correct, with two exceptions — `E-HAT-1.1-16(c)` prints a verbal description
("winds twice around the core circle … through a clasp") where the book prints only "A the circle
shown in the figure" (2051), which `AT.txt` cannot corroborate, and its proof depends on that
description; and `E-HAT-1.1-17` cites Proposition 1.5 (1479) for a track formula the proposition does
not state.

**A whole coverage hole:** §2.B (11 cards) and §2.C (9 cards) are in *neither* list. They are not
among the sections the brief declares read, and they are not among the sections it hands out —
"§4.2 onward" starts after them, and `3.D, 3.F, 3.H, 4.1#10–23` do not include them. None of the
seven other directions (d1 §3.D, d2 §4.3, d3 §3.F, d4 §3.H+§4.1, d5 §4.2, d6 §4.A–4.L, d7
book-side index) covers them, and no card of either section carries a `claude` review. Together
with the 20 §1.1 cards above, these 40 cards are the remaining unread cards that nobody else took;
I read all 40:

* §2.B: 11 cards, 11 printed exercises — statements all match, defects in `findings-2-B.md`
  (2.B-1 wrong for k=0 or ℓ=0; Alexander duality's nonempty/proper hypotheses unchecked in 2.B-1,
  2.B-2, 2.B-5; 2.B-5's duality/intersection step unjustified; 2.B-7 rests on a figure absent from
  the witness; 2.B-6 has two unchecked assertions).
* §2.C: 9 cards, 9 printed exercises — statements all match, no false proof; one card
  (`E-HAT-2.C-2`) has mis-nested `pf-step`/`pf-proof` divs and a `kind: exercise` mismatch; see
  `findings-2-C.md`.
* §1.1: 4 cards as described, statements match, proofs correct, one misattributed citation
  (`1.1-17` cites Proposition 1.5 for a formula it does not state); see `findings-1-1-evidence.md`.

## 3. Notes for the other directions (not my slice; not audited)

* Cards in the unread sections that have **no** `solution-reviewed` event, i.e. the ones with the
  weakest provenance, are listed in the table above: `3.D-3`, `3.F-3`, `3.F-8`, `3.H-2`,
  `4.1-13`, `4.1-18`, `4.2-5/-8/-24/-26/-32`, `4.3-19/-22/-24`, `4.A-1/-2/-4`, `4.B-1`,
  `4.D-3/-5/-6`, `4.G-2/-4`, `4.H-2/-4`, `4.I-2`, `4.K-2`.
* Extraction hazard: the printed exercises of §2.B are **split** in `tmp/hat/AT.txt`. Exercises
  1–6 are at 8816–8842 and exercises 7–11 at 8846–8860, with the `Section 2.C 177` running head
  interleaved at 8843. Anyone counting §2.B's exercises from 8815 forward and stopping at the next
  running head will conclude there are six and that five cards are spurious. There are eleven.
* Overlines and composition dots are dropped by the extraction. `AT.txt` 9197 prints
  `f (z1 , ··· , z2k ) = (z2 , −z1 , ...)` with no bars, yet the book's map is conjugate-linear
  (it says so at 9002–9003, "This map is only 'conjugate-linear' over C"), and 1991 prints
  `f0 g0 ≃ f1 g1` where the printed text has `f_0 · g_0`. A statement that "differs" from the
  extraction only by bars or dots is not a defect.
* Sections of the book that have no directory in the collection are consistent with the witness for
  the two I checked: §2.A runs 8346–8437 with no `Exercises` block before §2.B's at 8815, and §3.G
  runs 16016–16309 with no `Exercises` block before §3.H's at 16310. No card is missing there.

## 4. What I did not do

* I audited only `§1.1`, `§2.B` and `§2.C` (40 cards). I did not audit any section held by another
  direction (`3.D`, `3.F`, `3.H`, `4.1#10–23`, `4.2`, `4.3`, `4.A`–`4.L`).
* I did not edit anything under `corpus/`.
* The per-card verdicts above are only as good as my reading of the printed text in `AT.txt`; where
  a figure is essential (2.B-7) the witness cannot settle the question and I say so.
