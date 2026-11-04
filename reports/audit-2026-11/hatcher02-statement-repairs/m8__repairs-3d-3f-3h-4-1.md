# repairs-3d-3f-3h-4-1 — slice 8 (`3-d`, `3-f`, `3-h`, `4-1` exercises 10–23)

Hatcher, *Algebraic Topology*. Patch specification only; nothing under `corpus/` was modified.

Method: a harness (`harness.py`, in this directory) segmented the printed exercise runs of
AT.txt into numbered exercises (§3.D:15094-15099, §3.F:15974-16023, §3.H:16835-16863,
§4.1:17818-17915), paired each card with its printed exercise, and diffed them as prose-token
and bracket/parenthesis-span streams; every flagged gap was then adjudicated against the printed
page. Quotes of AT.txt are verbatim in wording; its glyph linearisation is normalised in the same
way the cards already normalise it (`֏` → `\mapsto`, `π1` → `\pi_1`, `Z2` → `\ZZ_2`). Line ranges
are exact.

CARD: corpus/collections/SRC-TEXT-HAT02/4-1/E-HAT-4.1-15.md
BOOK: AT.txt:17884-17886  "(c) Finish the argument by showing that an invertible n× n matrix can be joined by a path of such matrices to either the identity matrix or the matrix of a reflection. (Use Gaussian elimination, for example.)"
OLD: |
(c) Finish the argument by showing that an invertible $n \times n$ matrix can be joined by a path of such matrices to either the identity matrix or the matrix of a reflection.
|
NEW: |
(c) Finish the argument by showing that an invertible $n \times n$ matrix can be joined by a path of such matrices to either the identity matrix or the matrix of a reflection. (Use Gaussian elimination, for example.)
|
WHY: The printed parenthetical "(Use Gaussian elimination, for example.)", which closes part (c), was dropped.

CARD: corpus/collections/SRC-TEXT-HAT02/4-1/E-HAT-4.1-22.md
BOOK: AT.txt:17907-17909  "22. Show that a path-connected space X has a CW approximation with countably many cells iff πn (X) is countable for all n . [Use the results on simplicial approximations to maps and spaces in §2.C.]"
OLD: |
Show that a path-connected space $X$ has a CW approximation with countably many cells if and only if $\pi_n(X)$ is countable for all $n$.
|
NEW: |
Show that a path-connected space $X$ has a CW approximation with countably many cells if and only if $\pi_n(X)$ is countable for all $n$.
[Use the results on simplicial approximations to maps and spaces in §2.C.]
|
WHY: The printed bracketed pointer "[Use the results on simplicial approximations to maps and spaces in §2.C.]" was missing (the earlier "if and only if" for the printed "iff" is faithful and is left alone).

## no change

All thirty other cards of the slice were compared word by word with the printed page and keep
their statements. Points that a token diff raises but that are not losses of printed content:

- `3-d/E-HAT-3.D-1`, `3-d/E-HAT-3.D-2`, `3-d/E-HAT-3.D-3` (AT.txt:15094-15099) — exact, including
  the bracketed "[Consider the homeomorphisms …]" of 3.D-1.
- `3-f/E-HAT-3.F-1` (AT.txt:15974-15979) — complete; "gluing" for the printed "glueing" is a
  paraphrase, and the card's double quotes carry the printed single quotes' emphasis.
- `3-f/E-HAT-3.F-2` (AT.txt:15982-15984) — complete; the printed line is dislocated by the
  extraction (`lim1← Gi = 0` cut off from its display), and the card restores the full display.
- `3-f/E-HAT-3.F-3`, `3-f/E-HAT-3.F-5`, `3-f/E-HAT-3.F-6`, `3-f/E-HAT-3.F-7`, `3-f/E-HAT-3.F-8`
  (AT.txt:15985-16010) — complete, bracketed hint of F-3 included.
- `3-f/E-HAT-3.F-4` (AT.txt:15988-15991) — complete; printed "iff" is spelled "if and only if",
  which preserves the biconditional.
- `3-f/E-HAT-3.F-9` (AT.txt:16011-16023) — complete; the card replaces the printed pointer "across
  the top of the following diagram" by the top row itself (the diagram is an image in AT.pdf and
  has no text in AT.txt), and its first three terms `Hom(pA, Z) → Ext(Ap , Z) → Ext(A, Z)` are the
  sequence printed in the proof of Proposition 3F.12 at AT.txt:15929-15931. Both printed sub-parts
  (a), (b) are present.
- `3-h/E-HAT-3.H-1` … `3-h/E-HAT-3.H-6` (AT.txt:16835-16863) — complete, including the bracketed
  hint of 3.H-5 ("[Use Proposition 3H.5 and compute …]") and 3.H-3's `[X, BAut(G)]` (written
  `B\operatorname{Aut}(G)`); `\mathcal{B}(X;G)` for the printed `B(X; G)` is house style, not a
  loss.
- `4-1/E-HAT-4.1-10`, `-11`, `-12`, `-14`, `-16`, `-17`, `-18`, `-20`, `-21`, `-23`
  (AT.txt:17861-17915) — complete; "skeleta" for the printed "skeletons" (4.1-14) and the rendered
  `X_m^n` of 4.1-21 are paraphrases that keep the mathematics. (4.1-15(a) likewise keeps the
  printed parenthetical "(or simplicial approximation, Theorem 2C.1)"; only its part (c) is
  defective, see the patch above.)
- `4-1/E-HAT-4.1-19` (AT.txt:17894-17897) — printed "iff" spelled "if and only if"; complete.

## one structural defect, outside the content-loss categories

`4-1/E-HAT-4.1-13` (AT.txt:17872-17873) keeps the printed wording — "Use the extension lemma to
show that a CW complex retracts onto any contractible subcomplex" — and loses no printed matter,
but its statement sits in a `::: {.exercise}` block while all 31 other cards of the slice use
`::: {.problem}`; a statement-layer applier that reads only `.problem` blocks will see no
statement at all. It is not listed above because its wording needs no repair, but the block name
alone could be changed (`::: {.exercise}` → `::: {.problem}`, one occurrence in that file).

## comparison summary

Compared: all 32 cards of this slice — `E-HAT-3.D-1`, `-2`, `-3`; `E-HAT-3.F-1` … `-9`;
`E-HAT-3.H-1` … `-6`; `E-HAT-4.1-10` … `-23`. Defective: `E-HAT-4.1-15` (dropped printed
parenthetical) and `E-HAT-4.1-22` (dropped bracketed pointer). Sound as stored: the other thirty.
Not compared: the rest of SRC-TEXT-HAT02 — §4.1 exercises 1–9 and every other section belong to
other members' slices.

Asterisks: the printed runs of this slice carry no starred exercises and no starred sub-parts in
the authority. In AT.txt:15093-15100, 15973-16023, 16834-16863 and 17817-17915 there is no `*`
and no `∗` next to any exercise number or sub-part label; every `∗` in those ranges is the dual
of a map or of a cohomology group (`H∗`, `f ∗`, `i∗`). The text layer of AT.pdf gives the same
`∗` count, so there is no star in this slice to restore.
