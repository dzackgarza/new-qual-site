# Statement-layer repair spec — slice 5: §4.D ex. 1–10, §4.F ex. 1–3

Authority: `tmp/hat/AT.txt` = `pdftotext -layout` of `tmp/hat/AT.pdf`; §4.D exercises occupy
lines 22149–22189, §4.F exercises lines 22600–22615. The PDF glyph layer was additionally
checked (book pages 447, 455, 456) to settle the asterisk question — see Coverage.

Nothing under `corpus/` was modified. Every `OLD` block below is a verbatim copy of a
contiguous run of the named card file and occurs **exactly once** in it (verified
mechanically), so the patches apply without disambiguation.

## Defects

### 1. §4.D Exercise 5 — lost bracketed pointer ("Hence …")

CARD: corpus/collections/SRC-TEXT-HAT02/4-d/E-HAT-4.D-5.md
BOOK: AT.txt:22163-22164  "Then use the Thom isomorphism to show that the Hopf invariant of p must be ±1 . [Hence n = 1, 2, 4, 8 by Adams’ theorem.]"
OLD: |
```
Then use the Thom isomorphism to show that the Hopf invariant of $p$ must be $\pm 1$.
```
NEW: |
```
Then use the Thom isomorphism to show that the Hopf invariant of $p$ must be $\pm 1$. [Hence $n = 1, 2, 4, 8$ by Adams’ theorem.]
```
WHY: The printed bracketed pointer "[Hence n = 1, 2, 4, 8 by Adams’ theorem.]" was dropped.

### 2. §4.D Exercise 6 — lost bracketed remark ("When n > 1 …")

CARD: corpus/collections/SRC-TEXT-HAT02/4-d/E-HAT-4.D-6.md
BOOK: AT.txt:22167-22169  "Conversely, if M is simply-connected and H ∗ (M; Z) ≈ H ∗ (CPn ; Z) as rings, show there is a bundle S 1 →E →M where E ≃ S 2n+1 . [When n > 1 there are examples where M is not homeomorphic to CPn .]"
OLD: |
```
Conversely, if $M$ is simply-connected and $H^*(M; \ZZ) \approx H^*(\CP^n; \ZZ)$ as rings, show there is a bundle $S^1 \to E \to M$ where $E \simeq S^{2n+1}$.
```
NEW: |
```
Conversely, if $M$ is simply-connected and $H^*(M; \ZZ) \approx H^*(\CP^n; \ZZ)$ as rings, show there is a bundle $S^1 \to E \to M$ where $E \simeq S^{2n+1}$. [When $n > 1$ there are examples where $M$ is not homeomorphic to $\CP^n$.]
```
WHY: The printed bracketed remark "[When n > 1 there are examples where M is not homeomorphic to CPn .]" was dropped.

### 3. §4.D Exercise 9 — lost `[Hint: …]`

CARD: corpus/collections/SRC-TEXT-HAT02/4-d/E-HAT-4.D-9.md
BOOK: AT.txt:22181-22182  "[Hint: Diagonal matrices in U(n) are compositions of scalar multiplication in n lines in Cn , and CPn−1 is connected.]"
OLD: |
```
Do the same for the diagonal subgroup of $Sp(n)$.
```
NEW: |
```
Do the same for the diagonal subgroup of $Sp(n)$. [Hint: Diagonal matrices in $U(n)$ are compositions of scalar multiplication in $n$ lines in $\CC^n$, and $\CP^{n-1}$ is connected.]
```
WHY: The printed hint "[Hint: Diagonal matrices in U(n) are compositions of scalar multiplication in n lines in Cn , and CPn−1 is connected.]" was dropped.

### 4. §4.D Exercise 10 — lost printed parenthetical on the quaternionic determinant

CARD: corpus/collections/SRC-TEXT-HAT02/4-d/E-HAT-4.D-10.md
BOOK: AT.txt:22183-22186  "Fill in the details of the following argument to show that every n× n matrix A with entries in H has an eigenvalue in H . (The usual argument over C involving roots of the characteristic polynomial does not work due to the lack of a good quaternionic determinant function.)"
OLD: |
```
Fill in the details of the following argument to show that every $n \times n$ matrix $A$ with entries in $\quaternions$ has an eigenvalue in $\quaternions$.
```
NEW: |
```
Fill in the details of the following argument to show that every $n \times n$ matrix $A$ with entries in $\quaternions$ has an eigenvalue in $\quaternions$. (The usual argument over $\CC$ involving roots of the characteristic polynomial does not work due to the lack of a good quaternionic determinant function.)
```
WHY: The printed parenthetical "(The usual argument over C involving roots of the characteristic polynomial does not work due to the lack of a good quaternionic determinant function.)" was dropped.

### 5. §4.F Exercise 2 — lost `[Use …]`

CARD: corpus/collections/SRC-TEXT-HAT02/4-f/E-HAT-4.F-2.md
BOOK: AT.txt:22610-22611  "Show that if X is a finite complex, these maps eventually become isomorphisms. [Use induction on the number of cells of X and the five-lemma.]"
OLD: |
```
Show that if $X$ is a finite complex, these maps eventually become isomorphisms.
```
NEW: |
```
Show that if $X$ is a finite complex, these maps eventually become isomorphisms. [Use induction on the number of cells of $X$ and the five-lemma.]
```
WHY: The printed bracketed pointer "[Use induction on the number of cells of X and the five-lemma.]" was dropped.

## No change (statement checked word by word against the printed item; no printed content lost)

- `4-d/E-HAT-4.D-1.md` — AT.txt:22150-22154, complete (bundle S²→CP³→S⁴, the pullback by a degree k map, k > 1, the Leray–Hirsch conclusion). No bracket, parenthetical or asterisk in the printed item.
- `4-d/E-HAT-4.D-2.md` — AT.txt:22155-22156, complete.
- `4-d/E-HAT-4.D-3.md` — AT.txt:22157-22158, complete, including "as in Corollary 4D.3" and the generator list.
- `4-d/E-HAT-4.D-4.md` — AT.txt:22159-22160, complete.
- `4-d/E-HAT-4.D-7.md` — AT.txt:22170-22171, complete.
- `4-d/E-HAT-4.D-8.md` — AT.txt:22172-22176, complete, including "B₊ is the union of B with a disjoint basepoint", the reduced suspension Σⁿ(B₊) and "in §3.2".
- `4-f/E-HAT-4.F-1.md` — AT.txt:22601-22603, complete (both halves of the exercise; the printed item is not an "iff", it is "implies" plus "the converse also holds for countable CW complexes").
- `4-f/E-HAT-4.F-3.md` — AT.txt:22612-22615, complete. Considered and rejected as a defect: the card writes `hocolim` where the book prints "lim" with a subscript arrow ("the direct limits mean mapping telescopes" is retained in the card, and a mapping telescope *is* the homotopy colimit), so no printed content is lost. Not patched.

## Coverage

Slice 5 is 13 cards and all 13 were compared: §4.D exercises 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
and §4.F exercises 1, 2, 3. Five are defective (the four lost bracketed/parenthetical items and one
lost hint above); eight already match and are listed under "No change". No card in this slice was
left unread.

Checks performed beyond the word diff:

- **Asterisks.** `AT.txt` contains no text-mode asterisk anywhere (the only `∗` occurrences are the
  superscript of `H ∗`). To rule out an asterisk that the text extraction dropped, the PDF glyph
  positions were inspected: on book pages 447, 455, 456 every exercise number ("1." … "10.",
  "1." … "3.") begins flush at the left text margin x = 72.0 with no preceding glyph, and no star
  glyph occurs on those pages. These exercises are therefore unstarred in print, and none of them
  has lettered sub-parts, so there was no starred sub-part to restore.
- **Half-iff.** Each printed item was read for "if and only if": §4.D 1–10 and §4.F 1–3 contain none
  (4.D ex. 6 has a genuine "Conversely, …" second sentence, which the card keeps in full), so no
  card in this slice halves an iff.
- **Deliberately not "fixed".** Typographic paraphrase that preserves the mathematics was left
  alone: hyphen vs. en dash in "Leray–Hirsch", `\ldots` for "···", "n-tuple"/"n×n" hyphenation,
  and `\xrightarrow{p}` for the book's labelled arrow in §4.D ex. 5.
