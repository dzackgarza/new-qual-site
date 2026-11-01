# repairs-4-a — slice 4 (4-a, 4-b, 4-i), section 4.A

Hatcher, *Algebraic Topology*, §4.A exercises 1–5, AT.txt:21092-21129. Patch specification only; nothing under `corpus/` was modified.

Quotes of AT.txt are verbatim in wording; its lossy glyph linearisation is normalised (`hX, Y i` → `⟨X, Y⟩`, a raised `W` → `∨`, `֏` → `↦`), and superscripts and subscripts are written spaced as AT.txt prints them. Line ranges are exact.

CARD: corpus/collections/SRC-TEXT-HAT02/4-a/E-HAT-4.A-2.md
BOOK: AT.txt:21097-21101  "2. Show that under the map ⟨X, Y⟩→Homπn (X, x0 ), πn (Y , y0 ) , [f ] ↦ f∗ , the action of π1 (Y , y0 ) on ⟨X, Y⟩ corresponds to composing with the action on πn (Y , y0 ) , that is, (γf )∗ = βγ f∗ . Deduce a bijection of [X, K(π , 1)] with the set of orbits of Hom(π1 (X), π ) under composition with inner automorphisms of π . In particular, if π is abelian then [X, K(π , 1)] = ⟨X, K(π , 1)⟩ = Hom(π1 (X), π ) ."
OLD: |
Deduce a bijection of $[X, K(\pi, 1)]$ with the set of orbits of $\operatorname{Hom}(\pi_1(X), \pi)$ under composition with inner automorphisms of $\pi$.
|
NEW: |
Deduce a bijection of $[X, K(\pi, 1)]$ with the set of orbits of $\operatorname{Hom}(\pi_1(X), \pi)$ under composition with inner automorphisms of $\pi$.
In particular, if $\pi$ is abelian then $[X, K(\pi, 1)] = \langle X, K(\pi, 1) \rangle = \operatorname{Hom}(\pi_1(X), \pi)$.
|
WHY: The printed exercise ends with a further sentence, "In particular, if π is abelian then [X, K(π, 1)] = ⟨X, K(π, 1)⟩ = Hom(π1(X), π)", which the card dropped whole.

CARD: corpus/collections/SRC-TEXT-HAT02/4-a/E-HAT-4.A-4.md
BOOK: AT.txt:21108-21113  "4. With the notation of the preceding problem, show that Aut( ∨n S k ) ≈ GLn (Z) for k > 1 , where ∨n S k denotes the wedge sum of n copies of S k and GLn (Z) is the group of n×n matrices with entries in Z having an inverse matrix of the same form. [ GLn (Z) is the automorphism group of Zn ≈ πk ( ∨n S k ) ≈ Hk ( ∨n S k ) .]"
OLD: |
With the notation of the preceding problem, show that $\operatorname{Aut}(\bigvee_n S^k) \approx \operatorname{GL}_n(\ZZ)$ for $k > 1$, where $\bigvee_n S^k$ denotes the wedge sum of $n$ copies of $S^k$ and $\operatorname{GL}_n(\ZZ)$ is the group of $n \times n$ matrices with entries in $\ZZ$ having an inverse matrix of the same form.
|
NEW: |
With the notation of the preceding problem, show that $\operatorname{Aut}(\bigvee_n S^k) \approx \operatorname{GL}_n(\ZZ)$ for $k > 1$, where $\bigvee_n S^k$ denotes the wedge sum of $n$ copies of $S^k$ and $\operatorname{GL}_n(\ZZ)$ is the group of $n \times n$ matrices with entries in $\ZZ$ having an inverse matrix of the same form.
[$\operatorname{GL}_n(\ZZ)$ is the automorphism group of $\ZZ^n \approx \pi_k(\bigvee_n S^k) \approx H_k(\bigvee_n S^k)$.]
|
WHY: The printed bracketed hint stating that GLn (Z) is the automorphism group of Zn ≈ πk (∨n S k ) ≈ Hk (∨n S k ) was missing.

## no change

- `corpus/collections/SRC-TEXT-HAT02/4-a/E-HAT-4.A-1.md` — compared with AT.txt:21093-21095. The printed exercise has no bracketed hint, no asterisk and no parenthetical, and the card statement reproduces it word for word. No change.
- `corpus/collections/SRC-TEXT-HAT02/4-a/E-HAT-4.A-3.md` — compared with AT.txt:21102-21106. The card keeps the printed trailing clause "that is, automorphisms modulo inner automorphisms"; nothing printed is missing. No change.
- `corpus/collections/SRC-TEXT-HAT02/4-a/E-HAT-4.A-5.md` — compared with AT.txt:21114-21129. Parts (a), (b), (c) are all present, with both printed sentences of (b) and both sentences of (c); no part is starred in the print. No change.

## comparison summary

Compared card by card against the printed §4.A exercises, AT.txt:21092-21129: `E-HAT-4.A-1`, `E-HAT-4.A-2`, `E-HAT-4.A-3`, `E-HAT-4.A-4`, `E-HAT-4.A-5` — all five cards that exist in `4-a`. Defective: 4.A-2 (dropped final printed sentence) and 4.A-4 (dropped bracketed hint). Sound as stored: 4.A-1, 4.A-3, 4.A-5.

Not compared: every other card of SRC-TEXT-HAT02. The other two sections of this slice are reported in `repairs-4-b.md` and `repairs-4-i.md`; all remaining sections belong to other members' slices and were not read against the book. The printed §4.A exercises carry no asterisks and no sub-part stars, so no asterisk needed restoring here.
