# Repair specification — SRC-TEXT-HAT02, Hatcher §4.G and §4.H (slice 6)

**Scope.** The 8 cards of `corpus/collections/SRC-TEXT-HAT02/4-g/` (E-HAT-4.G-1 … 4) and
`corpus/collections/SRC-TEXT-HAT02/4-h/` (E-HAT-4.H-1 … 4).
**Authority.** `tmp/hat/AT.txt`: the §4.G "Exercises" heading at AT.txt:22813 and the §4.H
"Exercises" heading at AT.txt:23110. Each section prints exactly four exercises and all four
are carded in each, so the slice is complete. **Nothing under `corpus/` was touched.**

**Result.** 4 of the 8 cards lose printed matter. All four losses are a dropped *bracketed*
printed item at the end of the exercise. In this slice there is no starred exercise, no printed
parenthetical inside a sentence, no halved "if and only if", and no missing sub-part.

## Repairs (4)

### E-HAT-4.G-3 — printed pointer dropped

CARD: corpus/collections/SRC-TEXT-HAT02/4-g/E-HAT-4.G-3.md
BOOK: AT.txt:22820-22821  "3. What is the nerve of the cover of a simplicial complex by the open stars of its vertices? [See Lemma 2C.2.]"

OLD:
```
What is the nerve of the cover of a simplicial complex by the open stars of its vertices?
```
NEW:
```
What is the nerve of the cover of a simplicial complex by the open stars of its vertices?
[See Lemma 2C.2.]
```
WHY: The printed bracketed pointer "[See Lemma 2C.2.]" was dropped, so the card loses the cross-reference the book prints with this question.

### E-HAT-4.G-4 — printed bracketed remark dropped

CARD: corpus/collections/SRC-TEXT-HAT02/4-g/E-HAT-4.G-4.md
BOOK: AT.txt:22822-22823  "4. Show that Proposition 4G.2 and its corollary hold also for CW complexes and covers by families of subcomplexes. [CW complexes are paracompact; see [VBKT].]"

OLD:
```
Show that Proposition 4G.2 and its corollary hold also for CW complexes and covers by families of subcomplexes.
```
NEW:
```
Show that Proposition 4G.2 and its corollary hold also for CW complexes and covers by families of subcomplexes.
[CW complexes are paracompact; see [VBKT].]
```
WHY: The printed bracketed remark "[CW complexes are paracompact; see [VBKT].]" was dropped, so the card loses both the justification the book supplies for the extension to CW complexes and its pointer to [VBKT].

### E-HAT-4.H-1 — printed bracketed hint dropped

CARD: corpus/collections/SRC-TEXT-HAT02/4-h/E-HAT-4.H-1.md
BOOK: AT.txt:23111-23113  "1. Show that if A ֓ X is a cofibration of compact Hausdorff spaces, then for any space Y , the map Y X →Y A obtained by restriction of functions is a fibration. [If A ֓ X is a cofibration, so is A× Y ֓ X × Y for any space Y .]"

OLD:
```
Show that if $A \hookrightarrow X$ is a cofibration of compact Hausdorff spaces, then for any space $Y$, the map $Y^X \to Y^A$ obtained by restriction of functions is a fibration.
```
NEW:
```
Show that if $A \hookrightarrow X$ is a cofibration of compact Hausdorff spaces, then for any space $Y$, the map $Y^X \to Y^A$ obtained by restriction of functions is a fibration.
[If $A \hookrightarrow X$ is a cofibration, so is $A \times Y \hookrightarrow X \times Y$ for any space $Y$.]
```
WHY: The printed bracketed hint "[If A ↪ X is a cofibration, so is A × Y ↪ X × Y for any space Y.]" was dropped, so the card loses the step the book tells the reader to use.

### E-HAT-4.H-3 — printed bracketed pointer dropped

CARD: corpus/collections/SRC-TEXT-HAT02/4-h/E-HAT-4.H-3.md
BOOK: AT.txt:23117-23119  "3. For fibrations E1 →B and E2 →B , show that a fiber-preserving map E1 →E2 that is a homotopy equivalence is in fact a fiber homotopy equivalence. [This is dual to Proposition 0.19.]"

OLD:
```
For fibrations $E_1 \to B$ and $E_2 \to B$, show that a fiber-preserving map $E_1 \to E_2$ that is a homotopy equivalence is in fact a fiber homotopy equivalence.
```
NEW:
```
For fibrations $E_1 \to B$ and $E_2 \to B$, show that a fiber-preserving map $E_1 \to E_2$ that is a homotopy equivalence is in fact a fiber homotopy equivalence.
[This is dual to Proposition 0.19.]
```
WHY: The printed bracketed pointer "[This is dual to Proposition 0.19.]" was dropped, so the card loses the reference the book prints for this exercise.

## No change (4)

- `corpus/collections/SRC-TEXT-HAT02/4-g/E-HAT-4.G-1.md` — statement matches AT.txt:22815-22817 word for word
  ("Show that for a sequence of maps X0 →f1 X1 →f2 ···, the infinite iterated mapping cylinder
  M(f1 , f2 , ···), which is the union of the finite iterated mapping cylinders M(f1 , ··· , fn ),
  deformation retracts onto the mapping telescope."); only the arrow labels are set in LaTeX.
- `corpus/collections/SRC-TEXT-HAT02/4-g/E-HAT-4.G-2.md` — matches AT.txt:22818-22819
  ("Show that if X is a complex of spaces in which all the maps are homeomorphisms, then the
  projection ∆X →Γ is a fiber bundle.").
- `corpus/collections/SRC-TEXT-HAT02/4-h/E-HAT-4.H-4.md` — matches AT.txt:23120-23121
  ("Define the dual of an iterated mapping cylinder precisely, in terms of maps from ∆n , and use
  this to give a definition of ∇X , the dual of ∆X , for X a complex of spaces."); the printed item
  has no bracketed matter.
- `corpus/collections/SRC-TEXT-HAT02/4-h/E-HAT-4.H-2.md` — the mathematics matches AT.txt:23114-23116
  ("Consider a pushout diagram as at the right, where B ⊔f X is B with X attached along A via f .
  Show that if A ֓ X is a cofibration, so is B ֓ B ⊔f X ."). The card writes "Consider a pushout
  diagram where …" (dropping the words "as at the right", which point at a figure printed beside
  the exercise) and writes ⊔f as ∪f . I do not treat either as a repair: the figure is not part of
  the card, so the pointer has nothing to point at, and no mathematics is lost. Flagged here so a
  reviewer can override the judgement; the block, if wanted, is
  `Consider a pushout diagram where` → `Consider a pushout diagram as at the right, where`.

## Notes

- **Asterisks.** AT.txt carries no exercise star anywhere in the book: the character `∗` (U+2217)
  occurs 2085 times in the file, but always as the join / dual-group symbol (`X ∗ Y`, `D4m∗`), never
  as an exercise mark, and it does not occur in AT.txt:22813-22824 or AT.txt:23110-23121. Neither
  exercise list in this slice therefore supports an asterisk restoration, and none is invented here.
- **"iff".** No exercise in §4.G or §4.H contains an "if and only if"; nothing is halved in these
  eight cards.
- **AT.txt's hookarrow glyph.** AT.txt renders the printed ↪ of these exercises as U+0593
  (HEBREW ACCENT SHALSHELET), a font-mapping artifact of the PDF text extraction. The BOOK quotes
  above reproduce AT.txt verbatim, including that glyph; the NEW blocks render it in the cards'
  existing `\hookrightarrow` style.
- **Audit trail.** Cards E-HAT-4.G-3, E-HAT-4.H-1 and E-HAT-4.H-3 carry `source-checked` notes of
  2026-09-09 asserting that "the stored statement matches". For all three that assertion is false:
  the printed bracketed item is absent from the card as it stands. (The same note on E-HAT-4.G-1 is
  accurate.)
- **Verification.** Each OLD block above was checked mechanically to occur exactly once in its card
  file, and each NEW block equals that OLD run with the restored matter appended on the following
  line, which is the form the other repaired cards in this collection already use.

## Coverage

Compared: all 8 cards of the slice — E-HAT-4.G-1, E-HAT-4.G-2, E-HAT-4.G-3, E-HAT-4.G-4 against
AT.txt:22813-22823, and E-HAT-4.H-1, E-HAT-4.H-2, E-HAT-4.H-3, E-HAT-4.H-4 against
AT.txt:23110-23121. That is every exercise printed in §4.G and in §4.H. Not compared, because they
belong to other members' slices: §3.D, §3.F, §3.H, §4.1, §4.2, §4.3, §4.A, §4.B, §4.D, §4.F, §4.I,
§4.K, §4.L.
