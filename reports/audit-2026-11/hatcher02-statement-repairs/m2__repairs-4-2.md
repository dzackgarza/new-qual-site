# repairs-4-2 — statement-layer patch specification for §4.2 immediate exercises 1–20

Slice 1 of the disjoint slices: `corpus/collections/SRC-TEXT-HAT02/4-2/E-HAT-4.2-1.md` … `E-HAT-4.2-20.md`.
Authority: `tmp/hat/AT.txt`, §4.2 *Exercises* (line 19319 onwards; book pp. 389–390).
Patch specification only — nothing under `corpus/` was modified. Each `OLD` block is a verbatim, single-line run of the named card file and occurs there exactly once, so it can be applied mechanically with a plain string replacement.

## Repairs

### E-HAT-4.2-5

CARD: corpus/collections/SRC-TEXT-HAT02/4-2/E-HAT-4.2-5.md
BOOK: AT.txt:19331-19332  "Let X be the mapping torus of f , the quotient space of (Sα2 ∨ Sβ2 )× I under the identifications (x, 0) ∼ (f (x), 1) ."

OLD:
```
Let $X$ be the mapping torus of $f$.
```
NEW:
```
Let $X$ be the mapping torus of $f$, the quotient space of $(S_\alpha^2 \vee S_\beta^2) \times I$ under the identifications $(x, 0) \sim (f(x), 1)$.
```
WHY: Printed appositive dropped: the book defines the mapping torus as the quotient of (Sα2 ∨ Sβ2 )× I by (x, 0) ∼ (f (x), 1), which fixes the gluing convention.

### E-HAT-4.2-12

CARD: corpus/collections/SRC-TEXT-HAT02/4-2/E-HAT-4.2-12.md
BOOK: AT.txt:19359-19364  "[The latter condition can be restated in terms of homology with local coefficients as saying that f∗ : H∗ (X; Z[π1 X])→H∗ (Y ; Z[π1 Y ]) is an isomorphism; see §3.H.]"

OLD:
```
Show that a map $f: X \to Y$ of connected CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_1$ and if a lift $\tilde{f}: \tilde{X} \to \tilde{Y}$ to the universal covers induces an isomorphism on homology.
```
NEW:
```
Show that a map $f: X \to Y$ of connected CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_1$ and if a lift $\tilde{f}: \tilde{X} \to \tilde{Y}$ to the universal covers induces an isomorphism on homology. [The latter condition can be restated in terms of homology with local coefficients as saying that $f_*: H_*(X; \ZZ[\pi_1 X]) \to H_*(Y; \ZZ[\pi_1 Y])$ is an isomorphism; see §3.H.]
```
WHY: Printed bracketed hint dropped: the restatement in homology with local coefficients (with the pointer to §3.H) is missing.

### E-HAT-4.2-13

CARD: corpus/collections/SRC-TEXT-HAT02/4-2/E-HAT-4.2-13.md
BOOK: AT.txt:19366-19367  "[Pass to universal covers and use homology.]"

OLD:
```
Show that a map between connected $n$-dimensional CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_i$ for $i \leq n$.
```
NEW:
```
Show that a map between connected $n$-dimensional CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_i$ for $i \leq n$. [Pass to universal covers and use homology.]
```
WHY: Printed bracketed hint [Pass to universal covers and use homology.] dropped.

### E-HAT-4.2-14

CARD: corpus/collections/SRC-TEXT-HAT02/4-2/E-HAT-4.2-14.md
BOOK: AT.txt:19369-19370  "[Use the Hurewicz homomorphism.]"

OLD:
```
If an $n$-dimensional CW complex $X$ contains a subcomplex $Y$ homotopy equivalent to $S^n$, show that the map $\pi_n(Y) \to \pi_n(X)$ induced by inclusion is injective.
```
NEW:
```
If an $n$-dimensional CW complex $X$ contains a subcomplex $Y$ homotopy equivalent to $S^n$, show that the map $\pi_n(Y) \to \pi_n(X)$ induced by inclusion is injective. [Use the Hurewicz homomorphism.]
```
WHY: Printed bracketed hint [Use the Hurewicz homomorphism.] dropped.

### E-HAT-4.2-15

CARD: corpus/collections/SRC-TEXT-HAT02/4-2/E-HAT-4.2-15.md
BOOK: AT.txt:19372-19377  "[Use Poincaré duality, and also the fact that closed manifolds are homotopy equiva- lent to CW complexes, from Corollary A.12 in the Appendix. The stronger statement that a closed simply-connected 3 manifold is homeomorphic to S 3 is the Poincaré conjecture, finally proved by Perelman. The higher-dimensional analog, that a closed n manifold homotopy equivalent to S n is homeomorphic to S n , had been proved earlier for all n ≥ 4 .]"

OLD:
```
Show that a closed simply-connected 3-manifold is homotopy equivalent to $S^3$.
```
NEW:
```
Show that a closed simply-connected 3-manifold is homotopy equivalent to $S^3$. [Use Poincaré duality, and also the fact that closed manifolds are homotopy equivalent to CW complexes, from Corollary A.12 in the Appendix. The stronger statement that a closed simply-connected 3-manifold is homeomorphic to $S^3$ is the Poincaré conjecture, finally proved by Perelman. The higher-dimensional analog, that a closed $n$-manifold homotopy equivalent to $S^n$ is homeomorphic to $S^n$, had been proved earlier for all $n \geq 4$.]
```
WHY: Printed five-sentence bracketed hint (Poincaré duality, Corollary A.12, the Poincaré conjecture/Perelman, and the n ≥ 4 analogue) dropped entirely.

### E-HAT-4.2-18

CARD: corpus/collections/SRC-TEXT-HAT02/4-2/E-HAT-4.2-18.md
BOOK: AT.txt:19389-19390  "[Use the Künneth formula.]"

OLD:
```
If $X$ and $Y$ are simply-connected CW complexes such that $\tilde{H}_i(X)$ and $\tilde{H}_j(Y)$ are finite and of relatively prime orders for all pairs $(i, j)$, show that the inclusion $X \vee Y \hookrightarrow X \times Y$ is a homotopy equivalence and $X \wedge Y$ is contractible.
```
NEW:
```
If $X$ and $Y$ are simply-connected CW complexes such that $\tilde{H}_i(X)$ and $\tilde{H}_j(Y)$ are finite and of relatively prime orders for all pairs $(i, j)$, show that the inclusion $X \vee Y \hookrightarrow X \times Y$ is a homotopy equivalence and $X \wedge Y$ is contractible. [Use the Künneth formula.]
```
WHY: Printed bracketed hint [Use the Künneth formula.] dropped.

## No change

- `E-HAT-4.2-1.md` — printed item is one sentence with no bracketed matter; card is word-for-word identical.
- `E-HAT-4.2-2.md` — identical, including "for n odd and nontrivial for n even"; no printed hint.
- `E-HAT-4.2-3.md` — identical (lens space of dimension 2n + 1; module over Z[π1 (X)]); no printed hint.
- `E-HAT-4.2-4.md` — identical, including the product over k of πn (Skn ) (card renders it as `\prod_k`); no printed hint.
- `E-HAT-4.2-6.md` — identical (pair (CX, X) with CX the cone on X); no printed hint.
- `E-HAT-4.2-7.md` — identical ("prescribed homotopy groups πi (X) and prescribed actions of π1 (X) on the πi (X) 's"); no printed hint.
- `E-HAT-4.2-8.md` — identical one-sentence exercise; no printed hint.
- `E-HAT-4.2-9.md` — identical, including the second printed sentence "Use the preceding exercise to give an example where this fails in the nonsimply-connected case."
- `E-HAT-4.2-10.md` — identical, including both printed sentences about πn (X) finitely generated or not and πn′ (X) finite or infinite; no printed hint. (The card writes the cyclic quotient with `\bigl(p(t)\bigr)`, the print with angle brackets; same mathematics, not a defect.)
- `E-HAT-4.2-11.md` — identical, including "a free group" and the RP2 clause; "1 skeleton" vs the card's "1-skeleton" is a typographic hyphen only.
- `E-HAT-4.2-16.md` — identical, including the printed pointer "via the Hurewicz theorem and results of §3.3."
- `E-HAT-4.2-17.md` — identical, including "Deduce that CW complex K(G, n) 's are uniquely determined, up to homotopy type, by G and n"; the card's plural "CW complexes" is a paraphrase that preserves the mathematics.
- `E-HAT-4.2-19.md` — identical; no printed hint.
- `E-HAT-4.2-20.md` — identical, including "the action of π1 on πn is trivial for all n > 1"; no printed hint.

## Coverage

compared word-for-word against AT.txt: all twenty cards of this slice, exercises 1–20 (lines 19320–19393). Nothing in this slice was left unreviewed, so no card is reported as unexamined. No `if and only if` was halved anywhere in exercises 1–20: the only conditional wording is exercise 12's "if it induces an isomorphism on π1 and if a lift … induces an isomorphism on homology", and the card keeps both "if"s. No asterisk needed restoring in this slice either: §4.2 exercises 1–20 are not starred in the printed text. Checked two ways — AT.txt contains no `*` at all and, in lines 19319–19393, only the mathematical `∗` of f∗ / H∗; and in the PDF text layer of pages 398–399 (book pp. 389–390) every exercise number 1–23 begins its block at the same left edge (x = 72, LucidaBright-Demi) with no star glyph before or after it, those pages containing no asterisk character other than the mathematical `∗`. Defects found: 6 of 20 (exercises 5, 12, 13, 14, 15, 18); 14 cards already match.

Transcription note: the `BOOK` quote for E-HAT-4.2-12 is one printed item that straddles the page break, so AT.txt lines 19360–19362 (running head of p. 390 and blank space) lie inside the quoted range but are not part of the item. Every other quote is contiguous in AT.txt.

Judgment call, flagged for the assembler: the E-HAT-4.2-5 block is not a bracketed hint but the printed definition of the mapping torus, in apposition after "the mapping torus of $f$". It drops fourteen printed words and the gluing convention, so I count it as lost printed matter; if the repair is restricted to bracketed material only, that is the one block to drop from this file. The other five blocks are bracketed hints, verbatim.
