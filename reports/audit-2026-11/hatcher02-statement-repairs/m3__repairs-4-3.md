# Repairs — `SRC-TEXT-HAT02`, section `4-3` (immediate exercises 1–24)

Authority: `tmp/hat/AT.txt`, §4.3 "Exercises", lines 20755–20830. Line numbers are
counted the way `awk 'NR'` and `sed -n` count them (records separated by `\n`), NOT
the way Python's `str.splitlines()` counts them: AT.txt contains form-feed characters
and `splitlines()` would inflate every number. Text was cross-checked against
`tmp/hat/AT.pdf` pages 428–429 (`pdftotext -layout`), which reads identically; no
asterisk appears on any of exercises 1–24, so there is no starred-exercise marker to
restore in this section.

Convention in the blocks below: the characters between the two `|` on the `OLD:` and
`NEW:` lines are the exact file text and are not Markdown; the pipes are the fence.
Every `OLD` below was checked to occur exactly once in its card file.

## Defects (6 of 24)

### E-HAT-4.3-5 — bracketed hint dropped

CARD: corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-5.md
BOOK: AT.txt:20768-20769  "Show that [X, S n ] ≈ H n (X; Z) if X is an n dimensional CW complex. [Build a K(Z, n) from S n by attaching cells of dimension ≥ n + 2 .]"
OLD: |Show that $[X, S^n] \approx H^n(X; \ZZ)$ if $X$ is an $n$-dimensional CW complex.|
NEW: |Show that $[X, S^n] \approx H^n(X; \ZZ)$ if $X$ is an $n$-dimensional CW complex. [Build a $K(\ZZ, n)$ from $S^n$ by attaching cells of dimension $\geq n + 2$.]|
WHY: The printed bracketed hint was dropped entirely.

### E-HAT-4.3-9 — bracketed pointer dropped

CARD: corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-9.md
BOOK: AT.txt:20779-20780  "Show that a linear projection of a 2 simplex onto one of its edges is a fibration but not a fiber bundle. [Use the preceding problem.]"
OLD: |Show that a linear projection of a 2-simplex onto one of its edges is a fibration but not a fiber bundle.|
NEW: |Show that a linear projection of a 2-simplex onto one of its edges is a fibration but not a fiber bundle. [Use the preceding problem.]|
WHY: The printed bracketed pointer to the preceding exercise was dropped entirely.

### E-HAT-4.3-13 — bracketed hint dropped

CARD: corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-13.md
BOOK: AT.txt:20795-20797  "Given a map f : A→B and a homotopy equivalence g : C →A , show that the fibrations Ef →B and Ef g →B are fiber homotopy equivalent. [One approach is to use Corollary 0.21 to reduce to the case of deformation retractions.]"
OLD: |Given a map $f: A \to B$ and a homotopy equivalence $g: C \to A$, show that the fibrations $E_f \to B$ and $E_{fg} \to B$ are fiber homotopy equivalent.|
NEW: |Given a map $f: A \to B$ and a homotopy equivalence $g: C \to A$, show that the fibrations $E_f \to B$ and $E_{fg} \to B$ are fiber homotopy equivalent. [One approach is to use Corollary 0.21 to reduce to the case of deformation retractions.]|
WHY: The printed bracketed hint was dropped entirely.

### E-HAT-4.3-14 — bracketed pointer dropped

CARD: corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-14.md
BOOK: AT.txt:20798-20801  "For a space B , let M(B) denote the set of equivalence classes of maps f : A→B where f1 : A1 →B is equivalent to f2 : A2 →B if there exists a homotopy equivalence g : A1 →A2 such that f1 ≃ f2 g . Show the natural map F(B)→M(B) is a bijection. [See Exercises 11 and 13.]"
OLD: |Show the natural map $\mathcal{F}(B) \to \mathcal{M}(B)$ is a bijection.|
NEW: |Show the natural map $\mathcal{F}(B) \to \mathcal{M}(B)$ is a bijection. [See Exercises 11 and 13.]|
WHY: The printed bracketed cross-reference to Exercises 11 and 13 was dropped entirely.

### E-HAT-4.3-22 — "iff" halved to "if"

CARD: corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-22.md
BOOK: AT.txt:20822-20823  "Show that a principal fibration ΩC -→ E --→ B is fiber homotopy equivalent to the product ΩC × B iff it has a section, a map s : B →E with ps = 11."
OLD: |Show that a principal fibration $\Omega C \to E \xrightarrow{p} B$ is fiber homotopy equivalent to the product $\Omega C \times B$ if it has a section, a map $s: B \to E$ with $ps = \id$.|
NEW: |Show that a principal fibration $\Omega C \to E \xrightarrow{p} B$ is fiber homotopy equivalent to the product $\Omega C \times B$ if and only if it has a section, a map $s: B \to E$ with $ps = \id$.|
WHY: The printed "iff" was recorded as the one-way implication "if", losing the converse.

### E-HAT-4.3-23 — bracketed hint dropped

CARD: corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-23.md
BOOK: AT.txt:20825-20827  "if there is an abelian CW complex Y and a map X →Y inducing an isomorphism H∗ (X; Z) ≈ H∗ (Y ; Z) , then such a Y is unique up to homotopy equivalence. [Use Corollary 4.73 with W the mapping cylinder of X →Y .]"
OLD: |Prove the following uniqueness result for the Quillen plus construction: Given a connected CW complex $X$, if there is an abelian CW complex $Y$ and a map $X \to Y$ inducing an isomorphism $H_*(X; \ZZ) \approx H_*(Y; \ZZ)$, then such a $Y$ is unique up to homotopy equivalence.|
NEW: |Prove the following uniqueness result for the Quillen plus construction: Given a connected CW complex $X$, if there is an abelian CW complex $Y$ and a map $X \to Y$ inducing an isomorphism $H_*(X; \ZZ) \approx H_*(Y; \ZZ)$, then such a $Y$ is unique up to homotopy equivalence. [Use Corollary 4.73 with $W$ the mapping cylinder of $X \to Y$.]|
WHY: The printed bracketed hint was dropped entirely.

## No change (18 of 24)

Statements compared word by word against the printed items and found to preserve all
printed content; the only differences are typographic (`H–space` vs `H-space`,
`2 simplex` vs `2-simplex`, `1_1` vs `\id`, `loopspace` vs `loop space`) or a
fuller rendering of a printed abbreviation (`iff` → "if and only if" in 4.3-8, which
is a strengthening of the visible text, not a loss).

- `E-HAT-4.3-1` (AT.txt:20755–20758) — matches, including both halves of the
  homology/cohomology contrast and the closing question.
- `E-HAT-4.3-2` (AT.txt:20759–20761) — matches.
- `E-HAT-4.3-3` (AT.txt:20762–20764) — matches.
- `E-HAT-4.3-4` (AT.txt:20765–20767) — matches.
- `E-HAT-4.3-6` (AT.txt:20770–20773) — matches, including the second printed
  sentence "Show also that … unique up to homotopy."
- `E-HAT-4.3-7` (AT.txt:20774–20776) — matches.
- `E-HAT-4.3-8` (AT.txt:20777–20778) — matches; printed "iff" already rendered
  as "if and only if".
- `E-HAT-4.3-10` (AT.txt:20781–20786) — matches, including the "Deduce that …"
  clause.
- `E-HAT-4.3-11` (AT.txt:20790–20792) — matches.
- `E-HAT-4.3-12` (AT.txt:20793–20794) — matches.
- `E-HAT-4.3-15` (AT.txt:20802–20803) — matches.
- `E-HAT-4.3-16` (AT.txt:20804–20806) — matches.
- `E-HAT-4.3-17` (AT.txt:20807) — matches.
- `E-HAT-4.3-18` (AT.txt:20808–20810) — matches, including both counts
  ("last three terms", "last six terms").
- `E-HAT-4.3-19` (AT.txt:20812–20816) — matches, including the printed "iff".
- `E-HAT-4.3-20` (AT.txt:20817–20818) — matches.
- `E-HAT-4.3-21` (AT.txt:20819–20820) — matches.
- `E-HAT-4.3-24` (AT.txt:20828–20830) — matches.

## Coverage

I compared all 24 cards of `corpus/collections/SRC-TEXT-HAT02/4-3/`
(`E-HAT-4.3-1` … `E-HAT-4.3-24`) against `tmp/hat/AT.txt` lines 20755–20830, the
complete §4.3 exercise list, and cross-checked the printed items against pages
428–429 of `tmp/hat/AT.pdf`. None of the 24 was left unexamined. Method: a
word-by-word diff of each card's `::: {.problem}` block against the extracted
printed item (normalising LaTeX to the extractor's plain text), plus a targeted
sweep for every `[...]` bracket group and every `iff` in the printed range. The
printed range contains exactly five bracketed hints/pointers (exercises 5, 9, 13,
14, 23) and exactly three `iff`s (exercises 8, 19, 22); the cards had lost all five
hints and one of the three `iff`s, which are the six defects above. No printed
parenthetical, starred marker or other matter was found missing from the remaining
eighteen cards. I did not inspect, and make no claim about, any card outside
`4-3`.
