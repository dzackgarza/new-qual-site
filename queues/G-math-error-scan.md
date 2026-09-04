# Document queue G: Mathematical error scan — corpus cards

66 candidate findings from a reading pass over the solution/proof bodies of a
sample of problem and theory cards across all five areas (2026-08-31).
Per AGENTS.md, incorrect data is the most urgent class of data issue.

Each finding below states what the reader found wrong and, where known, the
correct mathematics. Findings are candidates to read and disposition, not
verdicts: for each one, open the card, re-derive the point independently, and
either fix the card (one card, one commit) or record why the finding is wrong.
Disposition order follows the finding numbers.

## Disposition checklist

- [x] 1. E-6AOD7 — Centralizer/center confusion in the class equation
  Disposition 2026-09-01: confirmed by re-derivation and fixed on the card.
  Lines 30 and 32 now read $Z(G)$; line 28 and the $[G:Z(g)]$ factors keep the
  centralizer reading.
- [x] 2. T-BRWA7 — Five-lemma proof is garbled
  Investigation 2026-09-01: finding confirmed, and deeper than reported.
  (a) The proof body is ill-typed ($p \circ n$ with $n(x) \in B'$, an
  undefined $n'$, $p$ applied to $B'$-elements).
  (b) The committed statement reverses the outer hypotheses: the five lemma
  needs $q$ surjective and $l$ injective, not $q$ injective and $l$
  surjective. Verified against Wikipedia "Five lemma" (proof citing Massey
  1991 p. 184), fetched 2026-09-01.
  (c) The diagram needs verticals at $A$ and $D$ as well as $B, C, E$; the
  chases use all three squares.
  Repair method: restate the card in the source's own labeling (top row
  $A \to B \to C \to D \to E$ with maps $k, l, m, n$; bottom row primed;
  verticals $f, g, h, i, j$; hypotheses $k$ epi, $l, m$ iso, $n$ mono,
  conclusion $g$ iso) and copy the source's two chases verbatim. Do not
  translate to the card's old letters: the source's $l, m, n, q$ name
  different arrows than the card's, and the notation dictionary is the
  failure mode that corrupted four drafting attempts.
  Disposition 2026-09-04: repaired with a complete typed diagram and direct
  injectivity/surjectivity chases under the standard hypotheses: left outer
  vertical epi, adjacent verticals isomorphisms, right outer vertical mono.
- [x] 3. FR-EDJWQ — Difference quotient set equal to the derivative
  Disposition 2026-09-04: confirmed and fixed. The proof now keeps the
  difference quotient as a factor that converges to $f'(x_0)$ instead of
  asserting that it equals the derivative for nearby $x$.
- [x] 4. E-J3QMJ — Constancy on a closed subdisk: wrong/inadequate justification
  Disposition 2026-09-04: confirmed and fixed. The card now assumes
  $f\in\Hol(\DD)$ and $0<r<1$ explicitly and applies the identity theorem to
  $f-c$, which vanishes on the open disk $r\DD$.
- [x] 5. E-BXDQY — Bounded comparison mis-written
  Disposition 2026-09-04: confirmed and fixed. The statement now records that
  $f,g$ are entire, and the solution correctly bounds $h=f/g$, removes its
  singularities at zeros of $g$, and concludes $f=cg$ with $|c|\leq1$.
- [x] 6. P-H2AG2 — Kronecker-sequence index typo in statement
  Disposition 2026-09-04: confirmed and fixed. The statement now defines
  $u_k(j)=\delta_{kj}$, matching the title and the solution, and the stray
  conjunction in the sentence was removed.
- [x] 7. E-YAMX6 — Broken intermediate algebra in the keyhole-contour residue step
  Disposition 2026-09-04: confirmed, with additional live errors. The original
  range $0<\alpha<2$ was false for the displayed integral: the large keyhole
  arc is $O(R^{\alpha-1})$, and the integral diverges for $\alpha\geq1$.
  The card now states $0<\alpha<1$ and gives a coherent branch choice, keyhole
  jump, residue, arc estimates, and final value
  $\pi\alpha\csc(\pi\alpha)$.
- [x] 8. E-AMD-TSJ7AKE5 — Statement conflates the conjugate union with the conjugate count
  Disposition 2026-09-04: confirmed and fixed. The statement now uses the set
  $\mathcal C(H)=\{gHg^{-1}:g\in G\}$ of conjugate subgroups; its cardinality,
  not the cardinality of their union as subsets of $G$, is $[G:N_G(H)]$.
- [x] 9. E-OUBBQ — Wrong difference-quotient factorization for `x^n`
  Disposition 2026-09-04: confirmed and fixed. The difference-of-powers
  factorization now uses
  $\sum_{k=0}^{n-1}x^{n-1-k}y^k$, yielding the stated Lipschitz bound
  $nM^{n-1}|x-y|$ and an explicit uniform-continuity $\delta$.
- [x] 10. E-ZXKDY — Degree not defined for the factorization maps
  Disposition 2026-09-04: confirmed and fixed. The proof now factors the
  induced map on $H_n$ through $H_n(S^n\setminus\{p\})=0$ and concludes
  directly from the definition of degree, without assigning a degree to maps
  whose source and target are not both $S^n$.
- [x] 11. T-77SHB — Cayley transform direction is backwards
  Disposition 2026-09-04: confirmed and fixed. The card now states that
  $G(w)=i(1-w)/(1+w)$ maps $\DD\to\HH$, while its inverse
  $F(z)=(i-z)/(i+z)$ maps $\HH\to\DD$.
- [x] 12. E-ZCPKK — Cross-multiplication step is mis-written
  Disposition 2026-09-04: confirmed and fixed. The statement now excludes the
  pole $z=-1$, and the solution correctly conjugates the denominator before
  cross-multiplying, giving $2|z|^2-2=0$.
- [x] 13. E-AIQEU — Final answer `sec`/`csc` slip; pole-location formula wrong
  Disposition 2026-09-04: confirmed, with additional corrupted contour algebra.
  The card now uses the rectangle of height $\pi$, the correct poles
  $(k+1/2)\pi i$, rigorous vertical-side estimates for $|\Re a|<1$, and the
  residue at $i\pi/2$ to obtain $\pi\sec(\pi a/2)$.
- [x] 14. E-WNTXK — Wrong function composition in the Cayley argument
  Disposition 2026-09-04: confirmed and fixed. The bounded entire function is
  $T\circ f:\CC\to\DD$, where $T:\HH\to\DD$ is the Cayley transform; the old
  text wrote the ill-typed composition $f\circ T$.
- [x] 15. E-P7SIB — `sin(4θ)` formula missing the factor 4 and a sign
  Disposition 2026-09-04: confirmed and fixed. The imaginary part of
  $(\cos\theta+i\sin\theta)^4$ is now copied correctly as
  $4\cos^3\theta\sin\theta-4\cos\theta\sin^3\theta$.
- [x] 16. E-WAYFS — Residue of `csc(πz)` wrong
  Disposition 2026-09-04: confirmed and fixed. Since the zeros of
  $\sin(\pi z)$ are simple,
  $\Res_{z=k}\csc(\pi z)=1/(\pi\cos(\pi k))=(-1)^k/\pi$.
- [x] 17. E-P3RLK — Solution proves the converse theorem, not the stated exercise
  Disposition 2026-09-04: confirmed and fixed. The solution now extends an
  arbitrary subspace-open cover of the closed set $A$ to a cover of $X$ by
  adjoining $X\setminus A$, takes a finite subcover of compact $X$, and then
  restricts back to $A$.
- [x] 18. E-ASWCD — flawed subtraction step in the proof of continuity from below for outer measure
  Disposition 2026-09-04: confirmed, with a deeper defect: the asserted theorem
  is false for arbitrary outer measures. The card now states and proves
  continuity on the Carathéodory-measurable $\sigma$-algebra, where the outer
  measure restricts to a measure, and gives an explicit outer measure on
  $\NN$ showing that both continuity statements can fail on arbitrary sets.
- [x] 19. E-2HIKG — spurious factor of 2 and inconsistent simplification in the semicircular-cont...
  Disposition 2026-09-04: confirmed, with multiple additional phase errors in
  both old contour derivations. The card now gives one coherent upper-half-plane
  contour proof: the negative axis contributes $e^{i\pi/3}I$, the only enclosed
  pole is $i$ with residue $e^{i\pi/6}/(2i)$, and the result is
  $I=\pi/\sqrt3$.
- [x] 20. E-AKNDW — wrong numerical value (`π/4` for `π/2`) in the main derivation of `∫ 1/(1+x²)...
  Disposition 2026-09-04: confirmed and fixed. The duplicate derivations were
  replaced by one residue proof: $\Res_{z=i}(1+z^2)^{-2}=1/(4i)$, hence
  $2\pi i\Res=\pi/2$, and the upper-semicircle contribution is
  $O(R^{-3})$.
- [x] 21. E-3B2YA — wrong value and wrong identity for the cube root of unity in the annotation
  Disposition 2026-09-04: confirmed and fixed. The annotation now records
  $\zeta_3=-1/2+i\sqrt3/2$, with sum of the conjugate roots $-1$ and product
  $1$, which is exactly the factorization data for $z^2+z+1$.
- [x] 22. E-3OJLH — circular Schwarz-lemma application; `F(0)=0` is false
  Disposition 2026-09-04: confirmed and rewritten. The proof now factors
  $f(z)=zg(z)$ by Schwarz, applies Schwarz to the odd part
  $h=(g(z)-g(-z))/2$, and handles the equality case using the even part and
  the parallelogram identity. The statement also now excludes $z=0$ from the
  rigidity hypothesis, since equality at $0$ is automatic for every $f$.
- [x] 23. E-CLSFF — false claim that the remaining entire function $Q$ is constant
  Disposition 2026-09-04: confirmed and fixed. After subtracting the principal
  parts at the finite poles, the remainder is entire on $\CC$ and meromorphic
  at $\infty$, hence polynomial. The old proof incorrectly forced this
  polynomial part to be constant, which would exclude rational functions such
  as $f(z)=z$.
- [x] 24. E-CFTRQ — two slips in the proof that $\mathrm{Aut}(\mathbb{CP}^1)$ is the set of fract...
  Disposition 2026-09-04: confirmed and rewritten. Instead of patching the
  corrupted affine/inversion calculation, the card now proves both inclusions
  projectively: $A\in\GL_2(\CC)$ induces a Möbius automorphism, and a
  rational automorphism $p/q$ has generic fiber cardinality
  $d=\max(\deg p,\deg q)$ counted with multiplicity; injectivity and the
  holomorphic inverse force $d=1$.
- [x] 25. E-EOMTI — the semicircular-reduction solution computes the wrong auxiliary integral
  Disposition 2026-09-04: confirmed and rewritten. The auxiliary integral is
  $A=\int_0^\infty(1+x^2)^{-2}dx=\pi/4$, not the unsquared Cauchy
  integral. A single indented-semicycle proof now gives
  $2I+i\pi A=-\pi/2+i\pi^2/4$, hence $I=-\pi/4$.
- [x] 26. E-FS7GZ — wrong distance-to-branch-cut for the second center
  Disposition 2026-09-04: confirmed and fixed. For the principal square root,
  the Taylor radius is the distance to $\RR_{\leq0}$. The radii are $5$ at
  $4+3i$ and $3$ at $-4+3i$; the old value $4$ was not the distance to the
  cut.
- [x] 27. E-FUIDU — Schwarz–Pick bound computed as $7/2$ instead of $7/12$
  Disposition 2026-09-04: confirmed and fixed. Schwarz–Pick gives
  $(1-(3/4)^2)/(1-(1/2)^2)=7/12<2/3$, so the requested map cannot exist.
- [x] 28. E-FVXIT — wrong chain-rule formula in the computation of the sharp bound on $|f'(0)|$
  Disposition 2026-09-04: confirmed, with a deeper statement defect. In this
  corpus $\HH$ is the upper half-plane, so $f(0)=2$ is impossible. The intended
  target is the right half-plane $\HH_R$; after that correction, conjugating by
  $w\mapsto iw/2$ and the Cayley map gives
  $|F'(0)|=|f'(0)|/4\le1$, with equality for
  $f(z)=2(1+\lambda z)/(1-\lambda z)$.
- [ ] 29. E-GAGCW — wrong right-hand side in the Schwarz–Pick rearrangement
- [ ] 30. E-GFNDF — non-equicontinuity argued at the wrong point
- [ ] 31. E-GPCW2 — sign of the stated value of $\int_{-1}^1 dx/((x-a)\sqrt{1-x^2})$
- [ ] 32. E-GPFKM — wrong inverse Cayley map in applying Schwarz
- [ ] 33. E-4H3JY — "why the image is in $\mathbb H$" computes the wrong quantity and uses a map...
- [ ] 34. E-AHBVF — expansion uses the reciprocal of the cosine argument
- [ ] 35. E-AOQLK — wrong residue at infinity
- [ ] 36. E-GRXN4 — misjudged true/false item on products of poles
- [ ] 37. E-LZTNT, a<0 case of the sequence for $e^{1/z^2}\to a$ — 
- [ ] 38. E-MCTII, misdirected conformal map for the Schwarz bound — 
- [ ] 39. E-NIPUY, proves uniform continuity of the wrong function — 
- [x] 40. E-P7SIB, incorrect $\sin(4\theta)$ identity — duplicate of finding
  15; fixed there on 2026-09-04.
- [ ] 41. E-PQ7NC, overclaimed image of the Joukowski map $z+1/z$ — 
- [ ] 42. E-RGDJ7, factor-of-2 error in $\int_{S^1} 2\sinh(z)/z^n\,dz$ for even $n$ — 
- [ ] 43. E-U2A4C, wrong Laurent expansion in the inversion formula for $\Res_{z=\infty}\frac{z-1}{z+1}$ — 
- [x] 44. E-WAYFS, wrong residue for $1/\sin(\pi z)$ at $z=k\in\mathbb Z$ —
  duplicate of finding 16; fixed there on 2026-09-04.
- [ ] 45. E-WXHMJ, remark claims the residues of an elliptic function do not cancel — 
- [ ] 46. E-WYJ7K, wrong tangency vertex and image region for the tangent lune — 
- [ ] 47. E-YFBH5 — Analytic self-maps of the disc, zero of order $k$ at $0$, $|f|\to 1$ at boundary
- [ ] 48. E-ZQGR5 — Radius of convergence of $\sum a^{k^2} z^k$
- [ ] 49. P-3MIIY — $\int_0^\infty \frac{\log x}{1+x^n}\,dx$ (part vi)
- [ ] 50. P-5U7QZ — sharp bound on $|f'(0)|$ for $f:\mathbb{D}\to\mathbb{H}$ with $f(0)=2$
- [ ] 51. P-64ZUP — conformal map from $\{|z|<1,\ |z-1/2|>1/2\}$ to $\DD$
- [ ] 52. P-6VF7J — part (b), an $f$ analytic at $1$ whose series $\sum a_n$ diverges
- [ ] 53. P-BHLSJ — Laurent expansions of $e^{1/z}$ and $\cos(1/z)$ about $0$
- [ ] 54. P-CWXEW — wedge angle is $\pi/2$, not $\pi$
- [ ] 55. P-FY3WB — truncated exponential $\sum_{k=0}^n z^k/k!$: wrong $n=2$ argument and invalid...
- [ ] 56. P-IM6MH — inversion $1/(2z-1)$: final display labels the series as $1/(1-2z)$
- [ ] 57. P-KPCIE — midpoint recurrence $x_n=(x_{n-1}+x_{n-2})/2$: final closed form and limit ar...
- [ ] 58. P-MICNK — $az^n+z+1$ has a root in $|z|\le2$: Rouché threshold off by a factor of $4^n$
- [ ] 59. P-N6W5L — zeros of $z^3-z+1$ in $\Re z>0$: the listed roots of $z^3+1$ are wrong
- [ ] 60. P-P7IWV — one root of $z^4+2z^3-2z+10$ in each quadrant: wrong imaginary part of $f(it)...
- [ ] 61. P-R2D54 — truncated exponentials have no zeros in the unit disk: the $f_2$ factorizatio...
- [ ] 62. P-RMZDG part 2 — bounded $f$ vanishing on a sector as $|z|\to1$: the $\eps$-bound is taken in...
- [ ] 63. P-RMZDG part 4 (MMP version) — bounded real part: "attains $M$ in some disk" does not follow
- [ ] 64. P-SFDLG part 2 — discontinuity of the principal logarithm: the furnished sequence shows no dis...
- [ ] 65. P-UQOCE — the integration-by-parts recursion for the generalization carries a spurious...
- [ ] 66. P-WB56B — a C1 two-threshold argument for the uncountable split point, with a false con...

## Findings (as scanned)

### 1. `corpus/problems/Algebra/E-6AOD7.md` — Centralizer/center confusion in the class equation

Title: "Applications of the class equation"

Lines 30 and 32 reduce the class equation mod `p` and write the surviving
term as `Z(g)`:

- Line 30: "Reducing mod p yields 0 = Z(g) + 0"
- Line 32: "So p divides Z(g), making Z(g) nontrivial."

After summing over the nontrivial classes, each term `[G : Z(g)]` is a
multiple of `p` and vanishes mod `p`; the surviving term is the center
`Z(G)`. Lines 30 and 32 should read `Z(G)`, not `Z(g)`. (Line 28 correctly
uses `Z(g)` as the centralizer inside `[G : Z(g)]`; the confusion enters
only where the residual center term is meant.)

Conclusion of the argument (nontrivial center) is correct; the notation on
lines 30–32 is wrong.

### 2. `corpus/theory/Topology/T-BRWA7.md` — Five-lemma proof is garbled

Title: "The five lemma"

The theorem statement (with the standard injectivity/surjectivity column
assumptions) is correct. The proof body is not:

- Line 24 (injectivity): "Let x ∈ B with n(x) = 0. Then p(n(x)) = 0 ..." —
  `n` maps the middle column `B → B'`, so `n(x) ∈ B'`. But `p` maps
  `C' → D'`. The composition `p(n(x))` is ill-typed; the proof conflates
  the middle and third columns.
- Line 26 (surjectivity): "since p is surjective, p(y) = p(n(x))" with
  `y ∈ B'` and `n(x) ∈ B'` — again `p` does not act on `B'`-elements.
  Later it writes `y - n(x) = n'(m(w))` where `n'` is never defined and
  the exact-column bookkeeping does not line up.

The two-instances-of-the-four-lemma structure is the right idea, but the
typing and exactness steps as written are wrong and should be redone.

### 3. `corpus/theory/Real_Analysis/FR-EDJWQ.md` — Difference quotient set equal to the derivative

Title: "Relationship between continuity and differentiability"

Line 20:
```
f(x) - f(x0) = (x-x0) * (f(x)-f(x0))/(x-x0) = (x-x0) f'(x0) -> 0
```
The second equality is false: for `x != x0` the difference quotient is not
equal to `f'(x0)`, only convergent to it. The chain should use a limit on
the quotient factor (`-> f'(x0)`), not an equality. This is the standard
mistake that the differentiability-to-continuity derivation is meant to
avoid; as written the card asserts the wrong equality.

### 4. `corpus/problems/Complex_Analysis/E-J3QMJ.md` — Constancy on a closed subdisk: wrong/inadequate justification

Title: "Constancy on a closed subdisk of D implies constancy on D"

The solution invokes the maximum modulus principle so as to extend constancy
from `rD` (closure) to all of `D`. The conclusion is true, but the MMP
argument as written does not establish it: maximum modulus on `rD_closure`
only pins the maximum of `|f|` to the boundary and does not by itself force
`f` constant on the whole disk. The clean justification is the identity
theorem: `f` is constant on the nonempty open set `rD` and `D` is connected,
so `f` is constant on `D`. The card should cite identity theorem rather than
the muddled MMP step.

### 5. `corpus/problems/Complex_Analysis/E-BXDQY.md` — Bounded comparison mis-written

Title: "Rudin 10.3"

Line 23: "Write h = f/g, then |f| <= 1 is bounded." Should be
`|h| = |f/g| <= 1`. As written it claims `|f|` is bounded, which is not
what the argument uses (and not what follows from `|f| <= |g|`).

(The intended argument — `|f/g| <= 1`, removable singularities at zeros of
`g`, Liouville, `f = cg` — is otherwise sound, given `g` not identically
zero.)

### 6. `corpus/problems/Real_Analysis/P-H2AG2.md` — Kronecker-sequence index typo in statement

Title: "The Kronecker sequences ... form an orthonormal system in
l^2(Z)"

Line 22 statement: `u_k(j) = δ_{ij}` should be `δ_{kj}`. The
solution body uses `δ_{kj}` consistently, so this is a one-character typo
in the problem statement only.

### 7. `corpus/problems/Complex_Analysis/E-YAMX6.md` — Broken intermediate algebra in the keyhole-contour residue step

Title: "x^alpha/(x+1)^2"

The final answer (line 83, `pi alpha csc(pi alpha)`) is correct, and the
residue computation (lines 67-75) is correct. But the manipulation that gets
from the residue to the answer has a broken step:

- Line 81: `-2 pi i alpha * 1/(e^{-i pi alpha} - e^{i pi alpha})`
- Line 82: `= 2 pi i alpha * 1/(e^{-i pi alpha} - e^{-i pi alpha})`

At line 82 the denominator becomes `e^{-i pi alpha} - e^{-i pi alpha} = 0`
(both terms identical) and the sign in front flips from `-` to `+`. Line 81
already reduces directly to the correct answer — `e^{-i pi alpha}-
e^{i pi alpha} = -2 i sin(pi alpha)` gives `(2 pi i alpha)/(2 i sin(pi alpha))
= pi alpha csc(pi alpha)` — so line 82 is a spurious and incorrect
intermediate. It should be deleted rather than "fixed", since line 81 already
reaches the result.

### 8. `corpus/problems/Algebra/E-AMD-TSJ7AKE5.md` — Statement conflates the conjugate union with the conjugate count

Title: "The number of conjugates of H equals [G : N_G(H)]"

Line 22 defines `S(H) = union over g of gHg^{-1}` and then asserts
"so |S(H)| is the number of conjugates to H". As written this is false:
the union `S(H)` is a set of group elements, and its cardinality is not the
number of distinct conjugate subgroups of H. The correct object is the
*set of conjugate subgroups* `{gHg^{-1} : g in G}`, whose size is
`[G : N_G(H)]` by orbit-stabilizer.

The solution body (steps 2-3) correctly uses the set of conjugate subgroups
and gets the right result, so this is a problem-statement framing error, not
an error in the proof. The statement's phrase "so |S(H)| is the number of
conjugates" should be corrected.

### 9. `corpus/problems/Complex_Analysis/E-OUBBQ.md` — Wrong difference-quotient factorization for `x^n`

Title: "Uniform continuity of x^n"

Line 23 writes
```
|x^n - y^n| = |y-x| * |  sum_{1<=k<=n} x^k y^{n-k} |  <= n M^{n-1} |y-x|
```
The sum is mis-written. The correct factorization is
`x^n - y^n = (x-y)(x^{n-1} + x^{n-2}y + cdots + y^{n-1})`, i.e.
`(x-y) * sum_{k=0}^{n-1} x^k y^{n-1-k}`, whose terms are each bounded by
`M^{n-1}` (giving the written bound `n M^{n-1}`).

The sum as written, `sum_{k=1}^n x^k y^{n-k} = xy^{n-1} + cdots + x^n`, is
not equal to `(x^n-y^n)/(x-y)`, and its terms are each bounded by `M^n`
(not `M^{n-1}`), so the displayed bound `n M^{n-1}` does not follow from the
displayed sum either. The factorization indices need correcting.

### 10. `corpus/problems/Topology/E-ZXKDY.md` — Degree not defined for the factorization maps

Title: "Degree of a non-surjective map S^n to S^n is zero"

The solution factors `f` as `f2 ∘ f1` with `f1 : S^n -> S^n\set{pt}
(≅ R^n)` and then argues "H_*(f1) = 0 and deg f1 = 0; apply deg f =
(deg f1)(deg f2)". This is not a valid reduction:

- `f1` maps `S^n` to `R^n`, not `S^n` to `S^n`, so its "degree" is
  undefined, and there is no degree product rule `deg(f2 ∘ f1) =
  (deg f1)(deg f2)` across maps to and from a contractible space.

The correct argument is that the factorization through the contractible
`R^n` makes `f` null-homotopic, hence `deg f = 0`. The conclusion is true;
the stated mechanism is wrong.

### 11. `corpus/theory/Complex_Analysis/T-77SHB.md` — Cayley transform direction is backwards

Title: "Cayley Transform"

Line 17 states:

```
F(z) = (i-z)/(i+z) maps D -> H  with inverse G(w) = i(1-w)/(1+w)
```

The direction is wrong. `F(z) = (i-z)/(i+z)` maps the *upper half-plane*
onto the *unit disc*: `F(i) = 0`, `F(2i) = -1/3` (in `D`), and `F` sends the
real axis (the boundary of `H`) to the unit circle. It is *not* a map
`D -> H` — for example `F(0) = 1`, whose imaginary part is `0`, so `0 in D`
is not sent into the open upper half-plane.

The inverse relationship is correct as a pair: `G(w) = i(1-w)/(1+w)` is the
standard Cayley map sending `D -> H` (with `G(0) = i`), and `F` is its
inverse (`H -> D`). So the two formulas are mutual inverses, but the card
assigns each its direction backwards: it should read "`G` maps `D -> H` with
inverse `F` (which maps `H -> D`)."

### 12. `corpus/problems/Complex_Analysis/E-ZCPKK.md` — Cross-multiplication step is mis-written

Title: "Purely imaginary if on circle"

The conclusion — `(z-1)/(z+1)` is purely imaginary iff `|z|^2 = 1` — is
correct, but the displayed algebra proving it is not:

Line 26:
```
(z-1)/(z+1) = -(z_bar - 1)/(z_bar + 1)
   <=> (z-1)(1+z) = (1-z_bar)(1+z_bar)
   <=> 2 - 2|z|^2 = 0
```

The cross-multiplication is wrong. `-(z_bar-1)/(z_bar+1) = (1-z_bar)/(1+z_bar)`,
so the correct equivalence is
```
(z-1)/(z+1) = (1-z_bar)/(1+z_bar)
   <=> (z-1)(1+z_bar) = (1-z_bar)(1+z)
   <=> z + |z|^2 - 1 - z_bar = z + 1 - |z|^2 - z_bar
   <=> |z|^2 = 1.
```
The card replaces `(1+z)` on the left and `(1+z)` on the right with `(1+z_bar)`
in both factors, losing the conjugation where it matters. As written, the
card's middle equation is `z^2 + z_bar^2 = 2`, which is not equivalent to
`|z|^2 = 1` (e.g. `z = i` gives `z^2 + z_bar^2 = -2 != 2` while `|z| = 1`).

### 13. `corpus/problems/Complex_Analysis/E-AIQEU.md` — Final answer `sec`/`csc` slip; pole-location formula wrong

Title: "e^{ax} sech(z)" (integral of `e^{ax}/cosh(x)`)

The derivation is long but the main computation is sound, and line 143 reaches
the correct value `pi / cos(a pi / 2)`. There are two genuine errors:

- **Line 144** relabels the just-computed value as `pi csc(a pi / 2)`. The
  correct value is `pi sec(a pi / 2)` (line 20, the problem statement itself,
  asserts `pi sec(a pi/2)`; and `1/cos = sec`, not `csc`). The final displayed
  answer is wrong.

- **Line 31** gives the poles of `cosh` as `z = i pi k / 2`. The correct
  locations are `z = i pi (2k+1) / 2` (odd multiples of `i pi/2`); the zeros of
  `cosh` are `e^(2z) = -1`, i.e. `2z = i pi (2k+1)`. As written the formula
  includes the even multiples too, which are not poles. (The later use — the
  single enclosed pole `z_0 = i pi / 2` — is the correct odd-multiple zero.)

### 14. `corpus/problems/Complex_Analysis/E-WNTXK.md` — Wrong function composition in the Cayley argument

Title: "An entire function with values in H is constant"

Line 24: "Write `T: C -> D` for the Cayley map, then `F = f ∘ T`". Two
mistakes:

- The Cayley map is `T: H -> D` (upper half-plane to unit disc), not
  `C -> D`.
- With `f: C -> H`, the bounded composition is `F = T ∘ f : C -> D`, not
  `f ∘ T`. As written the two lines even contradict: "`F = f∘T`" but then
  "`F(C) = T(f(C))`", which are different functions.

The intended argument is correct — `F = T ∘ f` is bounded entire, hence
constant, so `f = T^{-1}(const)` is constant — but the composition direction
as written is wrong.

### 15. `corpus/problems/Complex_Analysis/E-P7SIB.md` — `sin(4θ)` formula missing the factor 4 and a sign

Title: "Trig identities"

The `cos(4θ)` line is correct. But line 34–35 concludes

```
sin(4θ) = cos^3(θ) sin(θ) + cos(θ) sin^3(θ)
```

From the expansion on line 28, the imaginary part is

```
4 cos^3(θ) sin(θ) - 4 cos(θ) sin^3(θ)
```

so the card drops the factor of 4 and changes the minus to a plus. The
correct identity is `sin(4θ) = 4(sin θ cos^3 θ - sin^3 θ cos θ)`.

### 16. `corpus/problems/Complex_Analysis/E-WAYFS.md` — Residue of `csc(πz)` wrong

Title: "Zeros of sin(πz) and singularities of csc(πz)"

The zeros argument is correct, but line 41 gives the residue wrongly:

```
Res_{z=k} csc(πz) = lim_(z->k) (z-k) csc(πz) =LH sec(kπ) = (-1)^(k+1)
```

The correct residue is

```
Res_{z=k} csc(πz) = lim_(z->k) (z-k)/sin(πz) = 1/(π cos(πk)) = (-1)^k / π.
```

Two errors: the `1/π` factor is dropped (the residue is `(-1)^k / π`,
not `(-1)^k`), and the sign is wrong (`sec(kπ) = 1/cos(kπ) = (-1)^k`, and the
residue carries that same sign, `(-1)^k / π`, with `k=0` giving `1/π` — check:
near `z=0`, `sin(πz) ≈ πz`, so `csc(πz) ≈ 1/(πz)`, residue `1/π`, not `-1`).

### 17. `corpus/problems/Topology/E-P3RLK.md` — Solution proves the converse theorem, not the stated exercise

Title: "Closed subsets of compact spaces are compact"

The exercise (line 15) asks: if `A` is closed and `X` is compact, show `A` is
compact. The solution does not prove this. It opens (line 20) "Let `A` be a
compact subset of `X` a Hausdorff space, we will show `X\A` is open" and then
proves that a compact subset of a Hausdorff space is closed — the opposite
theorem, with different hypotheses (`X` Hausdorff and `A` compact, neither
assumed in the exercise).

The two theorems are distinct and neither implies the other from the stated
assumptions: "closed subset of a compact space is compact" (this exercise,
correct proof in `E-JSCGD`); "compact subset of a Hausdorff space is closed"
(correct proof in `E-3YP6K`). This card's solution should prove the former.

### 18. `corpus/problems/Real_Analysis/E-ASWCD.md` — flawed subtraction step in the proof of continuity from below for outer measure

Title: "Continuity of outer measure from above and below"

The exercise asks to prove continuity from below for an outer measure. The
statement is true, but step <2>2 of the proof (line 34) asserts, for an
increasing chain $E_1 \subseteq E_2 \subseteq \cdots$:

$$\sum_{n=1}^N \mu^*(E_n \setminus E_{n-1}) \le \mu^*(E_N),$$

justifying it by "monotonicity and finiteness of each term" and the fact that
$E_n \setminus E_{n-1} \subseteq E_n$. This requires the inequality
$\mu^*(E_n \setminus E_{n-1}) \le \mu^*(E_n) - \mu^*(E_{n-1})$, i.e. treating
$\mu^*$ as subtractive. For an outer measure only the reverse is guaranteed:
finite subadditivity gives $\mu^*(E_n) \le \mu^*(E_{n-1}) + \mu^*(E_n \setminus
E_{n-1})$, hence $\mu^*(E_n \setminus E_{n-1}) \ge \mu^*(E_n) - \mu^*(E_{n-1})$.
The subtraction (and the identity $\mu^*(F_n) = \mu^*(E_1) - \mu^*(E_n)$ used
again in <1>2, line 55) is valid only when the smaller set is $\mu^*$-measurable,
which is not assumed here.

A correct proof of continuity from below for an outer measure reduces to the
measure case via measurable (Carathéodory) envelopes of the $E_n$; it does not
run through naive subtraction. The displayed step is invalid as written, and the
same subtraction error recurs in the continuity-from-above half.

### 19. `corpus/problems/Complex_Analysis/E-2HIKG.md` — spurious factor of 2 and inconsistent simplification in the semicircular-contour derivation

Title: "$x^? / 1+x^2$" — computes $\int_0^\infty x^{1/3}/(1+x^2)\,dx = \pi/\sqrt3$

The final value $\pi/\sqrt3$ is correct, but the semicircular-contour derivation
reaches it through three separate algebraic slips. Starting from the true
relation (line 53/56)

$$2\pi i\cdot \frac{1}{2e^{i\pi/3}} = \left(1+e^{i\pi/3}\right)I
\quad\Longrightarrow\quad
I = \frac{i\pi}{e^{i\pi/3}\left(1+e^{i\pi/3}\right)},$$

line 59 instead writes an extra factor of 2:

$$I = \frac{i\pi}{2e^{i\pi/3}\left(1+e^{i\pi/3}\right)},$$

which evaluates to $\pi/(2\sqrt3)$, not $\pi/\sqrt3$. The subsequent steps
compound the slip: line 63 drops the $\frac14$ pre-factor produced by the
balancing (writing "$i\pi e^{-3i\omega/2}\frac1{\cos(\omega/2)}$" instead of
$\frac{i\pi}{4}e^{-3i\omega/2}\frac1{\cos(\omega/2)}$), line 64 then equals
$2\pi/\sqrt3$, and line 65 silently drops a factor of 2 again to reach
$\pi/\sqrt3$. The derivation's own algebra contradicts its final value by a
factor of 2 at line 59; the correct intermediate is $I =
\frac{i\pi}{e^{i\pi/3}(1+e^{i\pi/3})}$, which simplifies directly to
$\pi/\sqrt3$. (The keyhole variant on the same card reaches the same value but
has its own notational slips, e.g. line 101 writes $\pi(e^{\pi/6}-1)$ where the
following line needs $\pi(e^{i\pi/6}-i)$.)

### 20. `corpus/problems/Complex_Analysis/E-AKNDW.md` — wrong numerical value (`π/4` for `π/2`) in the main derivation of `∫ 1/(1+x²)² dx`

Title: "$1/(1+x^2)^2$" — computes $\int_\mathbb{R} \frac{dx}{(1+x^2)^2} = \pi/2$.

The stated value $\pi/2$ is correct, and the residue $-\frac i4$ at $z=i$ (line
49) is correct. But line 54, which solves for the real-axis integral, reads

$$2\pi i\left(-\frac i4\right) = \int_{C_1} f + \int_{C_R} f
=: I_R + \int_{C_R} f \implies I_R = \frac\pi4 - \int_{C_R} f.$$

There are two slips. First, $2\pi i \cdot (-\frac i4) = 2\pi\cdot\frac14 = \frac\pi2$,
not $\frac\pi4$; since the left side equals $\int_{I_R} f + \int_{C_R} f$, the
correct conclusion is $\int_{I_R} f = \frac\pi2 - \int_{C_R} f$. Second, $I_R$
is here reused both for the real-axis segment and, confusingly, for the single
real summand; the arc term is then independently subtracted. Taking $R\to\infty$
in the printed relation would give $\frac\pi4$, not the correct $\pi/2$. The
older solution at the bottom of the same card (line 98) does the computation
correctly and obtains $\pi/2$.

### 21. `corpus/problems/Complex_Analysis/E-3B2YA.md` — wrong value and wrong identity for the cube root of unity in the annotation

Title: "Evaluating integrals" — computes several integrals by Cauchy's integral
formula.

The six integral values are all correct (the last, $\int_{|z|=2}
\frac{dz}{z^2+z+1}=0$, is right because the two cube-root poles $e^{\pm 2\pi i/3}$
both lie inside $|z|=2$ and their residues cancel). But the note at line 58 that
justifies the factorization is factually wrong in two places:

$$\zeta_3 = e^{2\pi i/3} = -1 + i\sqrt3 \qquad\text{(should be } -\tfrac12 + i\tfrac{\sqrt3}2\text{)}$$

and

$$\zeta_3\bar\zeta_3 = 2\Re(\zeta_3) = 2\cdot\tfrac12 = 1.$$

The product is $\zeta_3\bar\zeta_3 = |\zeta_3|^2 = 1$ (true because $|\zeta_3|=1$),
but $\zeta_3\bar\zeta_3 \ne 2\Re(\zeta_3)$: the identity that holds is
$\zeta_3 + \bar\zeta_3 = 2\Re(\zeta_3) = -1$, since $\Re(\zeta_3)=\cos(2\pi/3)=-\frac12$.
The annotation conflates the sum and the product and gives the wrong real part.
The intended fact (that the two roots are conjugates in the unit circle) still
holds, so the final value is unaffected.

### 22. `corpus/problems/Complex_Analysis/E-3OJLH.md` — circular Schwarz-lemma application; `F(0)=0` is false

Title: "The equality case" — Schwarz lemma: for $f:\mathbb D\to\mathbb D$, $f(0)=0$,
show $|f(z)+f(-z)|\le 2|z|^2$, with equality only if $f(z)=\lambda z^2$, $|\lambda|=1$.

The stated inequality and its equality case are true. But the solution's setup
is wrong: it defines $F(z)=\frac{f(z)+f(-z)}{2z^2}$ and asserts "$F(0)=0$ and thus
Schwarz applies", concluding $|F|\le 1$, i.e. the very inequality to be proved.
Two problems: (i) $F(0)$ need not be $0$ — since $f(z)+f(-z)$ is the even part of
$f$, $F(0)=\tfrac12 f''(0)$; for example $f(z)=\lambda z^2$ gives $F\equiv\lambda$ with
$F(0)=\lambda\neq 0$ and $|F|=1$ (so $F$ is not even a Schwarz function into
$\mathbb D$); (ii) $|F|\le 1$ is exactly the claim, so invoking Schwarz to get it
is circular. The equality-case paragraph is also not grounded in the hypotheses:
it asserts $|f(re^{it})|\to 1$ as $r\to 1$ (Schwarz-pick passage to the boundary)
which is not assumed. A correct proof writes $f(z)+f(-z)=z^2 w(z)$ with $w$
holomorphic, applies Schwarz–Pick to the even quotient, and uses the
equality-characterization of Schwarz.

### 23. `corpus/problems/Complex_Analysis/E-CLSFF.md` — false claim that the remaining entire function $Q$ is constant

The exercise is: the only meromorphic functions on $\mathbb{CP}^1$ are rational.
The solution decomposes $f(z) = \sum_{k\le n} P_k(z) + Q(z)$ with $P_k$ the
principal parts at the finite poles $z_k$ and $Q$ entire, then claims "$Q$ is
constant", justified by "$\mathbb{CP}^1$ is compact and $g$ is continuous, thus
bounded, so Liouville applies". This is wrong twice over. First, $Q$ is entire on
$\mathbb C$ but need not extend continuously to $\infty$: it has at most a pole
there (since $f$ and $\sum P_k$ are meromorphic on $\mathbb{CP}^1$), so it is a
*polynomial*, not necessarily a constant — e.g. $f(z)=z$ is meromorphic on
$\mathbb{CP}^1$ (a simple pole at $\infty$), has no finite poles, so
$P_k$ empty and $Q(z)=z$, which is nonconstant. Second, applying Liouville
requires boundedness on all of $\mathbb C$; the "compactness of $\mathbb{CP}^1$"
does not give it because $Q$ is not a genuine continuous function on the compact
surface. The correct conclusion is that $Q$ is a polynomial (entire with at most a
pole at $\infty$), so $f = \sum P_k + Q$ is rational; the theorem is true but the
proof's stated claim and its justification are false.

### 24. `corpus/problems/Complex_Analysis/E-CFTRQ.md` — two slips in the proof that $\mathrm{Aut}(\mathbb{CP}^1)$ is the set of fractional linear transformations

In the norm-conformality discussion, the card writes
"$\frac{d}{dz} \frac{bc-ad}{c} z + \frac{a}{c} = \frac{bc-ad}{c}$, which is nonzero
(making the map conformal) precisely when $bd-ad \neq 0$". The condition printed
on the right, "$bd-ad \neq 0$", is wrong — it should be $bc-ad \neq 0$ (or
$ad-bc \neq 0$, as in the statement); the symbol $d$ appears where $c$ belongs.
Later, in the $\subseteq$ direction, the card writes that $F(z) = 1/f(1/z)$
satisfies "$F(0)=0$ but $F'(0)\neq 0$, making zero a pole of $F$ of order one".
That is backwards: $F(0)=0$ with $F'(0)\neq 0$ makes $0$ a *zero* of $F$ of order
one, not a pole (this corresponds to $f$ having a simple pole at $\infty$, which
is the intended and correct conclusion).

### 25. `corpus/problems/Complex_Analysis/E-EOMTI.md` — the semicircular-reduction solution computes the wrong auxiliary integral

The exercise is $\int_0^\infty \log(x)/(1+x^2)^2\,dx$ (true value $-\pi/4$). The
"real reduction trick" solution splits the negative-real-axis contribution
$\gamma_2$ into $I + i\pi A$, where $A = \int_0^\infty 1/(x^2+1)^2\,dx$ is the
integral appearing at line 38. But the paragraph that claims to handle this
"auxiliary integral" computes the *wrong* integral: line 42 writes
$\int_0^\infty 1/(z^2+1)\,dz$ — dropping the square — and line 48 concludes it
equals $\pi/2$. That value does not appear in the final combination. When the
contour result is assembled into
$2\pi i\,\mathrm{Res}_{z=i}f = \int_\Gamma f = I + (I + i\pi^2/4)$, the imaginary
part $i\pi^2/4 = i\pi\cdot(\pi/4)$ silently uses the *correct* auxiliary value
$A=\pi/4$ for the squared integrand, not the $\pi/2$ just computed. Because the
answer is solved out of an inconsistent system (the printed $\pi/2$ auxiliary is
never actually used), the headline $-\pi/4$ is still right, but the auxiliary
computation as printed is both the wrong integrand and inconsistent with the
value the very next lines depend on.

### 26. `corpus/problems/Complex_Analysis/E-FS7GZ.md` — wrong distance-to-branch-cut for the second center

The exercise asks for the radius of convergence of the power series of
$\sqrt z$ (principal branch, cut on $\mathbb R_{\le 0}$) about $z_0=4+3i$ and
$z_1=-4+3i$. The card computes, correctly, $R=5$ for $z_0$ (distance to the
branch point $0$). For $z_1=-4+3i$ it states "the distance to the branch is 4,
so $R=4$". This distance is wrong: the branch cut is the ray
$\mathbb R_{\le 0}$, and the foot of the perpendicular from $z_1=(-4,3)$ onto
the real axis is $(-4,0)$, which lies on that ray, so the distance from $z_1$
to the cut is $3$, not $4$. Therefore the disc about $z_1$ that avoids the cut
has radius $R=3$ (the cut is nearer than the branch point at distance $5$);
the stated value $R=4$ is incorrect.

### 27. `corpus/problems/Complex_Analysis/E-FUIDU.md` — Schwarz–Pick bound computed as $7/2$ instead of $7/12$

The exercise asks whether a map $f:\mathbb D\to\mathbb D$ can satisfy
$f(1/2)=3/4$ and $f'(1/2)=2/3$. The card applies Schwarz–Pick correctly in
principle but miscomputes the right-hand side:
$\frac{1-|f(1/2)|^2}{1-|1/2|^2}
= \frac{1-(3/4)^2}{1-(1/2)^2}
= \frac{7/16}{3/4}
= 7/12$, not the printed $7/2$. As written, the displayed inequality
"$\frac{1-|f(1/2)|^2}{1-|1/2|^2}=\frac72< \frac23$" is false ($7/2\approx3.5$ is not
less than $2/3$). The intended conclusion still holds — the true bound
$|f'(1/2)|\le 7/12<2/3$ (with $7/12\approx0.58$) rules out $f'(1/2)=2/3$ — but
the printed bound and the printed comparison are both numerically wrong.

### 28. `corpus/problems/Complex_Analysis/E-FVXIT.md` — wrong chain-rule formula in the computation of the sharp bound on $|f'(0)|$

The card sets up $F=C\circ g\circ f:\mathbb D\to\mathbb D$ with $g(z)=\frac12 iz$
(so $f(0)=2\mapsto i$) and $C$ the Cayley map $\mathbb H\to\mathbb D$
($i\mapsto 0$); $F(0)=0$, so Schwarz gives $|F'(0)|\le 1$. But the displayed
derivative is wrong: line 38 states
$F'(z)=f'((g\circ C)(z))\,g'(C(z))\,C'(z)$. The derivative of $C\circ g\circ f$
is, by the chain rule, $C'(g(f(z)))\,g'(f(z))\,f'(z)$ — the card composes the
maps in the wrong order and evaluates the factors at the wrong points. The
evaluation paragraph is likewise garbled (it writes $F'(i)$, $g'(0)$, and claims
$g(C(z))=0$ yields $z=i$, none of which is the correct $z=0$, $z=g(2)=$ after
$f$). The final bound $|f'(0)|\le 4$ is nonetheless correct, because the
numerator factors happen to have the same moduli ($|g'|=1/2$ and $|C'(i)|=1/2$)
independent of the mislabelled evaluation points; the displayed formula itself
is false.

### 29. `corpus/problems/Complex_Analysis/E-GAGCW.md` — wrong right-hand side in the Schwarz–Pick rearrangement

The proof derives the correct claim
$|f(w)-f(z)|/|1-\bar w z|$ directly. Taking $z\to w$ in the displayed line
$|f(z)-f(w)|/(|z-w|\,|1-\bar{f(w)}f(z)|)\le |1/(1-\bar w z)|$ gives a right-hand
side of $1/|1-|w|^2|=1/(1-|w|^2)$. But line 63 writes the right-hand side as
$1/|w|^2$ instead:
$|f'(w)|/(1-|f(w)|^2)\le 1/|w|^2$. This is wrong (the printed
$1/|w|^2$ is not what the limit produces), and the very next line would then
force the false conclusion $|f'(w)|\le(1-|f(w)|^2)/|w|^2$; instead line 65 prints
the correct $|f'(w)|\le(1-|f(w)|^2)/(1-|w|^2)$, silently using $1/(1-|w|^2)$
rather than the $1/|w|^2$ just written. The final statement is right; the
intermediate right-hand side $1/|w|^2$ is not.

### 30. `corpus/problems/Complex_Analysis/E-GFNDF.md` — non-equicontinuity argued at the wrong point

The exercise asks for a non-equicontinuous family; the card gives $\{z^k\}$ on
$[0,1]$ and justifies it by "fix any $z_0\in[0,1)$, then
$|f_k(1)-f_k(x_0)|\to 1$ as $k\to\infty$". This does not establish
non-equicontinuity: equicontinuity at $z_0$ is tested only at points within a
small $\delta$ of $z_0$, and $1$ is at fixed distance $|1-z_0|$ from $z_0$, not
a nearby point. In fact $\{z^k\}$ is equicontinuous at every *interior* point of
$[0,1)$ (on a small neighborhood $[z_0-\delta,z_0+\delta]\subset(0,1)$ the
supremum $|x^k-z_0^k|\le 2(z_0+\delta)^k\to 0$ uniformly in $k$), and at $0$ it
is equicontinuous too. The only point where it fails is the endpoint $1$, where
$|1-x^k|\to 1$ as $k\to\infty$ regardless of how close $x<1$ is to $1$. The
conclusion (non-equicontinuous family) is true, but the stated demonstration is
fallacious: it uses a point at fixed distance and would falsely implicate the
interior, where the family is in fact equicontinuous.

### 31. `corpus/problems/Complex_Analysis/E-GPCW2.md` — sign of the stated value of $\int_{-1}^1 dx/((x-a)\sqrt{1-x^2})$

The card asserts $\int_{-1}^1 dx/((x-a)\sqrt{1-x^2})=\pi/\sqrt{a^2-1}$ and
derives it from a residue circuit returning $2\pi i\,\mathrm{Res}_{z=a}=
2\pi/\sqrt{a^2-1}$ (taking $\sqrt{1-a^2}=i\sqrt{a^2-1}$). The sign is wrong for
$a>1$ (the natural, pole-free reading). On the real interval the principal
$\sqrt{1-x^2}>0$, so for $a>1$ the integrand $1/((x-a)\sqrt{1-x^2})$ is negative
throughout, and the integral must be negative; direct substitution
$x=\cos\theta$ gives $-\int_0^\pi d\theta/(a-\cos\theta)=-\pi/\sqrt{a^2-1}$.
Thus for $a>1$ the integral equals $-\pi/\sqrt{a^2-1}$, not $+\pi/\sqrt{a^2-1}$
(the plus sign matches $a<-1$, not $a>1$). The residue-based derivation has the
wrong sign for the branch/contour combination used.

### 32. `corpus/problems/Complex_Analysis/E-GPFKM.md` — wrong inverse Cayley map in applying Schwarz

The card sets $g(z)=i(1+z)/(1-z):\mathbb D\to\mathbb H$ and $F=f\circ g$,
correct. But line 28 uses $g^{-1}$ as $z\mapsto(z+i)/(z-i)$ and claims
$f(2i)=F((z+i)/(z-i)|_{z=2i})=F(1/3)$. Both the formula and the evaluation are
wrong: the true inverse is $g^{-1}(w)=(w-i)/(w+i)$ with
$g^{-1}(2i)=(2i-i)/(2i+i)=i/(3i)=1/3$, whereas the written $(z+i)/(z-i)$
evaluates at $z=2i$ to $(3i)/(i)=3$, not $1/3$. The intended result
$|f(2i)|\le 1/3$ is correct, but the displayed inverse map and its numerical
evaluation at $z=2i$ are both false.

### 33. `corpus/problems/Complex_Analysis/E-4H3JY.md` — "why the image is in $\mathbb H$" computes the wrong quantity and uses a map to the lower half-plane

The card aims to produce a conformal map $\mathbb D\to\mathbb H$. Its first
part gives the inverse Cayley map $f(w)=-i(w+1)/(w-1)$, which is correct.
But the verification block ("Why the image is in $\mathbb H$") switches to a
different function, writing $\Im(f(z)) = \Re((1-z)/(1+z))$ and concluding the
image is in $\mathbb H$ because $(1-x^2-y^2)/(1+x^2+y^2)>0$. This is doubly
false. The expression $(1-x^2-y^2)/(1+x^2+y^2)$ is the *real* part of
$(1-z)/(1+z)$, not its imaginary part, so asserting it shows $\Im>0$ mislabels
the quantity. Moreover $(1-z)/(1+z)$ maps the unit disk into the *lower*
half-plane: for $z=x+iy$, $\Im((1-z)/(1+z))=-2y/\big((1+x)^2+y^2\big)<0$ for
$y>0$. A correct disk-to-upper-half-plane map needs a factor of $i$, e.g.
$f(z)=i(1-z)/(1+z)$ (or the inverse Cayley map already given). As written, the
card's positivity argument proves nothing, and the letter function it analyzes
sends $\mathbb D$ to the wrong half-plane.

### 34. `corpus/problems/Complex_Analysis/E-AHBVF.md` — expansion uses the reciprocal of the cosine argument

The card is asked to expand $f(z)=z^2\cos(z/3)$ about $z=0$. The solution
instead expands $z^2\cos(1/(3z))$, i.e. it replaces $z/3$ by $1/(3z)$:
$$f(z)=z^2\big(1+\tfrac1{2!}\big(\tfrac1{3z}\big)^2+\tfrac1{4!}\big(\tfrac1{3z}\big)^4\big)=z^2+\tfrac1{2!\cdot3^2}+\tfrac1{4!\cdot3^4}\,z^{-2}+\cdots.$$
The negative-power terms only appear because the argument was inverted. The
correct expansion of $z^2\cos(z/3)$ is a Taylor series in purely nonnegative
powers,
$$f(z)=z^2\left(1-\frac{(z/3)^2}{2!}+\frac{(z/3)^4}{4!}-\cdots\right)=z^2-\frac{z^4}{2!\cdot3^2}+\frac{z^6}{4!\cdot3^4}-\cdots,$$
with no $z^{-k}$ terms; the function is entire, so it has no Laurent
expansion about $0$. As written the card gives the expansion of a different
function.

### 35. `corpus/problems/Complex_Analysis/E-AOQLK.md` — wrong residue at infinity

For $f(z)=z^3/(1+z^2)$, the card writes $f(z)=z-\tfrac{1/2}{z+i}-\tfrac{1/2}{z-i}$
(both correct) and then claims
$\operatorname{Res}_{z=\infty} f(z)=-1$. This is incorrect. The two finite
poles give residues $-1/2+(-1/2)=-1$, and since the residues of a meromorphic
function (finite poles plus the point at infinity) always sum to zero, the
residue at infinity must be $+1$. Equivalently,
$\operatorname{Res}_\infty(f)=-\operatorname{Res}_0\big((1/z^2)f(1/z)\big)=
-\operatorname{Res}_0(1/(z^3(1+z^2)))=-(-1)=+1$. The card's value $-1$ has the
wrong sign.

### 36. `corpus/problems/Complex_Analysis/E-GRXN4.md` — misjudged true/false item on products of poles

The second true/false statement reads: "If $f,g$ have a pole at $a$, then $fg$
has a pole at $a$." This statement is **true**: writing
$f=(z-a)^{-m}F$ and $g=(z-a)^{-n}G$ with $F,G$ holomorphic and nonvanishing
near $a$, the product is $(z-a)^{-(m+n)}FG$, a pole of order $m+n$. The card
marks the item **False** and gives the "counterexample" $f(z)=g(z)=1/z$, which
yields $fg=1/z^2$ -- but $1/z^2$ has a pole of order $2$ at $z=0$. The
proffered example therefore confirms the statement instead of refuting it. The
product of two poles is always a pole; cancellation is possible only for a
*sum* of poles (the preceding item), not for a product.

### 37. E-LZTNT, a<0 case of the sequence for $e^{1/z^2}\to a$

Card: for $a\in\RR_{<0}$, take $z_k\da {1\over \Log(a) + 2\pi i k - {\pi i \over 2}}$, "Then $f(z_k) = a$ for all $k$ but $z_k\to 0$."

The formula is wrong: the denominator is not squared, so $f(z_k)=e^{1/z_k^2}=e^{(w_k)^2}$ where $w_k=\Log(a)+2\pi ik-\pi i/2$. With principal $\Log(a)=\ln|a|+i\pi$, we get $w_k=\ln|a|+i\pi(1/2+2k)$, hence $f(z_k)=e^{(\ln|a|+i\pi(1/2+2k))^2}$, which equals $|a|\cdot i$ (a purely imaginary value), not $a$. The $-\pi i/2$ offset is also spurious: a negative real value requires $1/z^2$ to have imaginary part an odd multiple of $\pi$, i.e. argument $\pi\cdot\text{odd}$.

Correct: want $1/z_k^2=\ln|a|+(2k+1)\pi i$, so take $z_k=\bigl(\ln|a|+(2k+1)\pi i\bigr)^{-1/2}$ (any consistent square-root branch); then $f(z_k)=a$ and $z_k\to0$.

### 38. E-MCTII, misdirected conformal map for the Schwarz bound

Card: "Use the conformal map $g: z\mapsto -1{z+1\over z-1}$ to map $\Re(z)>0$ to $\DD$."

This map does not map the right half-plane to the disk. For example $g(2)=-(2+1)/(2-1)=-3$, and $|-3|=3\not<1$, so $g(2)$ lies outside $\DD$ (indeed on the negative real axis, where $f$ is not even defined). The map $z\mapsto -(z+1)/(z-1)$ sends the half-plane to the exterior of the unit disk; it is a Cayley-type reciprocal, not the Cayley map.

Correct setup: use $\phi(w)=\frac{1+w}{1-w}$, which is a conformal bijection $\DD\to\{\Re>0\}$ with $\phi(0)=1$. Then $F=f\circ\phi:\DD\to\DD$ has $F(0)=f(1)=0$, so Schwarz gives $|F(w)|\le|w|$. With $\phi^{-1}(z)=(z-1)/(z+1)$, we get $f(2)=F(\phi^{-1}(2))=F(1/3)$ and $|f(2)|\le 1/3$ -- the card's final number is right, but the map it names is wrong.

### 39. E-NIPUY, proves uniform continuity of the wrong function

Problem: "Show $f(x) = x^{-n}$ for $n\in \ZZ_{\geq 0}$ is uniformly continuous on $[0, \infty)$."

This statement is false as stated: for $n\ge 1$, $x^{-n}$ is not even continuous at $x=0$ (it blows up as $x\to0^+$) and is unbounded on $[0,\infty)$, so it is not uniformly continuous there. The solution does not prove this statement; it proves uniform continuity of $x^{1/n}$, the $n$-th root:

"$x^{1\over n} - y^{1\over n} \leq (x-y)^{1\over n}$"

which is uniform continuity of $x\mapsto x^{1/n}$ on $[0,\infty)$ (via subadditivity of the concave power), a different function from the $x^{-n}$ in the problem. If the intended function was $x^{-n}$, the claim is wrong; if it was $x^{1/n}$, the problem statement and title must be corrected. Additionally the cited inequality "$(a+b)^m \geq a^m + b^m$" has the wrong direction: for $m=1/n\le1$ subadditivity gives $(a+b)^m \le a^m+b^m$.

### 40. E-P7SIB, incorrect $\sin(4\theta)$ identity

Card derives correctly, from $(x+iy)^4$ with $x=\cos\theta,\ y=\sin\theta$, that
$$\sin(4\theta) = 4\cos^3(\theta)\sin(\theta) - 4\cos(\theta)\sin^3(\theta)$$
(the imaginary part $4x^3y-4xy^3$ of the expansion), but then prints:

"$\sin(4\theta) = \cos^3(\theta)\sin(\theta) + \cos(\theta)\sin^3(\theta)$"

This is wrong on two counts: it drops the factor $4$ on both terms, and it uses $+$ where the coefficient of $\cos\theta\sin^3\theta$ must be $-4$. The correct identity is $4\cos^3\theta\sin\theta - 4\cos\theta\sin^3\theta$ (equivalently $4\sin\theta\cos\theta\cos 2\theta$).

### 41. E-PQ7NC, overclaimed image of the Joukowski map $z+1/z$

Problem: conformal map $\DD^c\intersect\HH\to\HH$. Card claims $f(z)=z+1/z$ maps $\DD^c\intersect\HH$ onto all of $\HH$: "for $1<r<\infty$, these sweep out all of $\CC\sm\DD$ ... top halves of ellipses which sweep out all of $\HH$".

This is false. The classical Joukowski map $f(z)=z+1/z$ maps the exterior $\abs{z}>1$ biholomorphically onto $\CC\sm[-2,2]$. Restricting to the upper half of the exterior therefore gives the image $\HH\sm(0,2]$ (the upper half-plane with the real interval $(0,2]$ deleted), not all of $\HH$. The real segment $(0,2]$ is omitted: for $w\in(0,2]$ real, the roots of $z^2-wz+1=0$ satisfy $\abs{z}\le 1$, so no exterior point maps to $w$ (e.g. $w=1.5$ gives $\abs{z}\approx 0.999<1$).

The card's ellipse argument only establishes coverage of the imaginary axis (at $\theta=\pi/2$, $\cos\theta=0$, so $x=0$); it does not show that e.g. a point with large real and small imaginary part is in the image.

Secondary error on the same card: the derivative is stated as $f'(z)=1+\frac1{r^2}$ "which vanishes only at $z=\pm1$" -- but $1+1/r^2$ never vanishes, and the true derivative is $f'(z)=1-\frac1{z^2}$, which vanishes at $z=\pm1$ (on the boundary of the exterior, so $f$ is conformal on $\abs{z}>1$).

### 42. E-RGDJ7, factor-of-2 error in $\int_{S^1} 2\sinh(z)/z^n\,dz$ for even $n$

The card sets $f(z)=2\sinh(z)=e^z-e^{-z}$ and applies the generalised Cauchy formula
$$\int_{S^1}\frac{f(z)}{z^n}\,dz=\frac{2\pi i}{(n-1)!}f^{(n-1)}(0).$$
For even $n$, $n-1$ is odd, so $f^{(n-1)}(0)=2\sinh^{(n-1)}(0)=2\cosh(0)=2$, giving the integral $4\pi i/(n-1)!$ -- but the boxed answer states ${2\pi i\over(n-1)!}$ for $n$ even, dropping the factor $2$ (a concrete check: $n=4$ gives $\int=2\pi i\,f'''(0)/3!=2\pi i\cdot2/6=2\pi i/3$, not $\pi i/3$). The card's own intermediate line already evaluates to $4\pi i/(n-1)!$, so the boxed value is internally inconsistent. Correct answer: $4\pi i/(n-1)!$ for $n$ even, $0$ for $n$ odd.

### 43. E-U2A4C, wrong Laurent expansion in the inversion formula for $\Res_{z=\infty}\frac{z-1}{z+1}$

The card's integral formula gives the correct value $2$, but the accompanying inversion expansion is wrong. Correctly,
$$\frac1{z^2}\cdot\frac{\frac1z-1}{\frac1z+1}=\frac1{z^2}\cdot\frac{1-z}{1+z}=\frac1{z^2}\left(1-2z+2z^2-\cdots\right)=z^{-2}-2z^{-1}+2-2z+\cdots,$$
so the coefficient of $z^{-1}$ is $-2$ and $\Res_{z=\infty}f=-(-2)=2$. The card instead writes
$$z^{-2}+2z^{-1}-2+2z-\mathcal O(z^2),$$
with the wrong sign on every non-leading term; read literally its coefficient $+2$ would give $\Res=-2$, contradicting the card's own integral method and the true value $2$. The displayed expansion is wrong even though the boxed answer happens to be right.

### 44. E-WAYFS, wrong residue for $1/\sin(\pi z)$ at $z=k\in\mathbb Z$

The card gets the zeros correct ($\sin(\pi z)$ vanishes simply on $\mathbb Z$) but computes
$$\Res_{z=k}\csc(\pi z)=\lim_{z\to k}(z-k)\csc(\pi z)=\sec(k\pi)=(-1)^{k+1}.$$
For a simple zero of the denominator, $\Res_{z=k}1/f(z)=1/f'(k)$, and $\frac{d}{dz}\sin(\pi z)=\pi\cos(\pi z)$, so the residue is $1/(\pi\cos(\pi k))=(-1)^k/\pi$ -- the card drops the factor $1/\pi$ and flips the sign. (Check: $k=0$ gives residue $1/\pi$, since $1/\sin(\pi z)\sim 1/(\pi z)$; the card's $-1$ is wrong.) The correct residue is $(-1)^k/\pi$, matching the card E-V2VS5. Also $\sec(k\pi)=1/\cos(\pi k)=(-1)^k$, not $(-1)^{k+1}$.

### 45. E-WXHMJ, remark claims the residues of an elliptic function do not cancel

The main proof correctly shows an elliptic function has at least two poles: if it had exactly one, $\int_{\partial P}f=2\pi i\,\Res\neq0$, contradicting $\int_{\partial P}f=0$ (opposite edges of the fundamental parallelogram cancel). But the closing remark inverts the correct conclusion, stating "the residues *can not* cancel, i.e. $\sum_k\Res_{z=z_k}f(z)\neq0$" and that $\int_{\partial P}f$ "may be zero or nonzero." For any elliptic function the periodic-cancellation argument gives $\int_{\partial P}f=0$, and $\int_{\partial P}f=2\pi i\sum_k\Res$, so the residues always sum to zero. The remark asserts the exact opposite of the fact that the argument just proved.

### 46. E-WYJ7K, wrong tangency vertex and image region for the tangent lune

The boundary circles $|z-i|=1$ and $|z-i/2|=1/2$ are internally tangent, and their unique intersection point is $z=0$ (both centers lie on the imaginary axis, center distance $=|1-\tfrac12|=\tfrac12$). The card states the vertex is at $z=i$ and uses $f(z)=\frac{z+i}{z-i}$ to send $i\to\infty$. But $z=i$ is the center of the outer circle, not on it. Under $f$, the inner circle $|z-i/2|=1/2$ does map to the line $\Re w=-1$, but the outer circle $|z-i|=1$ maps (it does not pass through $z=i$) to the circle $|w-1|=2$, not to the imaginary axis as the card claims. So the image is not the strip $-1<\Re w<0$, and the map does not work. Correct approach: send the actual tangency point $z=0$ to $\infty$ (e.g. $w=1/z$); then $|z-i|=1\to\Im w=-1/2$ and $|z-i/2|=1/2\to\Im w=-1$, giving a genuine horizontal strip.

### 47. E-YFBH5 — Analytic self-maps of the disc, zero of order $k$ at $0$, $|f|\to 1$ at boundary

Erroneous line: "Then $f(z) = \lambda z^n$."

The problem declares the single zero has order $k$ (the exponent $n$ is never defined anywhere in the card). The correct conclusion is $f(z)=\lambda z^k$ with $|\lambda|=1$, since $f(z)=z^k g(z)$ where $g$ is nonvanishing. The card's proof step is also invalid: it claims (lines 25–29) that $|g(z)|=|f(z)|r^{-k}\leq r^{-k}\to 1$, hence "$|g(z)|\leq 1$ on $\DD$ by the MMP." But on $|z|=r<1$ one has $r^{-k}>1$, so this gives only the trivial bound $|g(z)|<|z|^{-k}$; it does not yield $|g|\leq 1$. The valid route is to note $|g(z)|\to 1$ as $|z|\to 1$ (since $|f(z)|\to 1$ and $|z|^k\to 1$), so $1/g$ is bounded by $1$ on $\DD$ by the limiting maximum modulus principle, giving $|g|\geq 1$; combined with the boundary limit this forces $g$ constant with $|\lambda|=1$, so $f(z)=\lambda z^k$.

### 48. E-ZQGR5 — Radius of convergence of $\sum a^{k^2} z^k$

Erroneous line: "$R=\infty$ if $\abs{a}< 1$, $R=0$ if $\abs{a}<1$, and $R=1$ if $\abs{a} = 1$."

The case split is self-contradictory: it assigns both $R=\infty$ and $R=0$ to $\abs{a}<1$. Using Cauchy–Hadamard, $1/R=\limsup |a^{k^2}|^{1/k}=\limsup |a|^{k}$, so $R=\infty$ when $|a|<1$ (since $|a|^k\to 0$) but $R=0$ when $|a|>1$ (since $|a|^k\to\infty$), and $R=1$ when $|a|=1$. The second condition should read $|a|>1$, not $|a|<1$.

### 49. P-3MIIY — $\int_0^\infty \frac{\log x}{1+x^n}\,dx$ (part vi)

Erroneous line: "<1>6. (vi) $\int_0^\infty \frac{\log x}{1 + x^n}\,dx = -\frac{\pi^2}{n^2}\cot\qty(\frac{\pi}{n})$ for $n \ge 2$."

This heading drops a factor. Differentiating $\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx=\frac{\pi}{n\sin(\pi a/n)}$ in $a$ (as the card itself does at lines 68–70) and evaluating at $a=1$ gives the correct value

$$\int_0^\infty \frac{\log x}{1+x^n}\,dx = -\frac{\pi^2}{n^2}\cot\qty(\frac{\pi}{n})\csc\qty(\frac{\pi}{n}) = -\frac{\pi^2}{n^2}\frac{\cos(\pi/n)}{\sin^2(\pi/n)},$$

which differs by the $\csc(\pi/n)$ factor. Verified numerically: for $n=3$, $I=-0.7310818\ldots = -(\pi^2/9)\cot(\pi/3)\csc(\pi/3)$, whereas $-(\pi^2/9)\cot(\pi/3)=-0.6331\ldots$. The two agree at $n=2$ only because $\csc(\pi/2)=1$ and both $\cot(\pi/2),\,\cot(\pi/2)\csc(\pi/2)=0$ vanish, masking the error.

### 50. P-5U7QZ — sharp bound on $|f'(0)|$ for $f:\mathbb{D}\to\mathbb{H}$ with $f(0)=2$

Erroneous premise: "Suppose $f: \DD\to \HH$ is analytic and satisfies $f(0) = 2$," where $\HH$ is the upper half-plane $\{z:\Im z>0\}$.

No such analytic map exists: $2$ is real, so $\Im 2=0$ and $2\notin\HH$. A map $f:\DD\to\HH$ must take the value $f(0)$ inside the open upper half-plane. The stated sharp bound $|f'(0)|\le 4$ is correct only for the well-posed variant $f(0)=2i$: writing $C(w)=(w-i)/(w+i)$ and applying Schwarz--Pick to $C\circ f:\DD\to\DD$ with $(C\circ f)(0)=C(2i)=i/3$ gives $|f'(0)|\le(1-|C(2i)|^2)\,|2i+i|^2/2=(8/9)(9)/2=4$.

The proof also uses a false step: "Define $g: \HH \to \HH$ by $g(z) = \tfrac{i}{2} z$... multiplication by $i/2$ rotates by $90^\circ$... preserving the upper half-plane." This is false. Multiplication by $i/2$ sends $z=re^{i\theta}$ to $(r/2)e^{i(\theta+\pi/2)}$; for $0<\theta<\pi$ the argument $\theta+\pi/2$ lies in $(\pi/2,3\pi/2)$, i.e. $\Re<0$, which is not in $\HH$. So $g$ does not preserve $\HH$ and the chain-rule structure $F=C\circ g\circ f$ is not a valid $\DD\to\DD$ contraction.

### 51. P-64ZUP — conformal map from $\{|z|<1,\ |z-1/2|>1/2\}$ to $\DD$

Erroneous line: "The map $\eta = e^{\pi \zeta}$ sends the strip $\{0 < \operatorname{Re} \zeta < 1\}$ to the upper half-plane."

This is false. For $\zeta=x+iy$ with $0<x<1$ and $y\in\RR$, one has $e^{\pi\zeta}=e^{\pi x}e^{i\pi y}$ with $e^{\pi x}\in(1,e^\pi)$ and $e^{i\pi y}$ sweeping the full circle. So $\zeta$ in the vertical strip maps onto the annulus $\{1<|\eta|<e^\pi\}$, not the upper half-plane. (Indeed a conformal image of the simply-connected strip cannot be the doubly-connected annulus.) Consequently the displayed final map (line 64), $z\mapsto\frac{e^{\pi(2/(1-z)-1)}-i}{e^{\pi(2/(1-z)-1)}+i}$, is not a conformal map of $D$ to $\DD$.

Correct fix: rotate the vertical strip to a horizontal one before exponentiating. Since $\eta'=i\zeta$ sends the vertical strip $\{0<\operatorname{Re}\zeta<1\}$ to the horizontal strip $\{0<\operatorname{Im}\eta'<1\}$, the map $e^{\pi i\zeta}$ sends it to the upper half-plane; then compose with the Cayley map. The first half of the solution (the strip $1/2<\operatorname{Re}w<1$ via $w=1/(1-z)$, verified by $\operatorname{Re}w=1/2$ on $|z|=1$ and $\operatorname{Re}w=1$ on $|z-1/2|=1/2$) is correct.

### 52. P-6VF7J — part (b), an $f$ analytic at $1$ whose series $\sum a_n$ diverges

Erroneous example: "Take $\sum {z^n \over n}$"; "$z=1$ yields the harmonic series, which diverges."

This fails the requirement that $f$ be *analytic at $1$*. The sum is $f(z)=\sum_{n\ge1}z^n/n=-\log(1-z)$, which has a logarithmic branch point at $z=1$: along the real axis $f(r)=-\log(1-r)\to+\infty$ as $r\to 1^-$, so $f$ is not continuous at $1$, let alone analytic there.

Correct example: $f(z)=\frac{1}{1+z}=\sum_{n=0}^\infty(-1)^n z^n$. This series has radius of convergence $1$ (singularity at $z=-1$), $f$ is analytic at $z=1$, and $\sum_{n\ge0} a_n=\sum_{n\ge0}(-1)^n$ diverges (partial sums $1,0,1,0,\ldots$). So it satisfies all of part (b). The card's $\sum z^n/n$ satisfies only the divergence clause.

### 53. P-BHLSJ — Laurent expansions of $e^{1/z}$ and $\cos(1/z)$ about $0$

Erroneous: the problem asks for the Laurent expansions about $0$ of $e^{1/z}$ and $\cos(1/z)$, but the entire solution block computes, instead, the Laurent expansions of a different function $f(z)=\frac{z+1}{z(z-1)}$ about $z=0$ and $z=1$ (the expansions used are those of $\frac{z+1}{z(z-1)}$, correctly, but for the wrong function). The requested expansions are:

$$e^{1/z}=\sum_{n=0}^{\infty}\frac{z^{-n}}{n!},\qquad \cos(1/z)=\sum_{m=0}^{\infty}\frac{(-1)^m}{(2m)!}z^{-2m},$$

both valid on $0<|z|<\infty$ ($e^{1/z}$ has an essential singularity and nonzero residue $c_{-1}=1$; $\cos(1/z)$ has an essential singularity and residue $0$). The card provides none of this.

### 54. P-CWXEW — wedge angle is $\pi/2$, not $\pi$

Erroneous: the solution asserts (Step 2.3) that $T_1(z)=\frac{z-i}{z+i}$ maps the lens $L=\{\abs{z-1}<\sqrt2,\ \abs{z+1}<\sqrt2\}$ conformally onto the wedge
$$W=\set{w\mid \pi/2<\arg w<3\pi/2},$$
a sector of angle $\pi$. The lens $L$ is the intersection of two disks of radius $\sqrt2$ whose centers ($1$ and $-1$) are a distance $2$ apart; the two circles meet at $\pm i$ with interior angle $\pi/2$ (the radii to the two centers at a vertex are orthogonal), so the image of $L$ under the Möbius map (which sends $i\mapsto0$, $-i\mapsto\infty$) is a wedge of angle $\pi/2$ at $0$, not $\pi$. Since the subsequent steps hinge on $T_2=−w$ rotating the (claimed) $\pi$-wedge to a half-plane and $T_3=\zeta^2$ opening that half-plane to $\mathbb{C}\setminus(-\infty,0]$, the whole chain and the final formula $f(z)=\frac{2e^{i\pi/4}\sqrt{z}}{z+i}$ are invalid for this domain. (Minor independent slip: the slit $[0,i)$, i.e.\ $z=it$ with $t\in[0,1)$, maps via $T_1(it)=\frac{t-1}{t+1}$ to $[-1,0)$, not the card's $(-1,0]$.)

### 55. P-FY3WB — truncated exponential $\sum_{k=0}^n z^k/k!$: wrong $n=2$ argument and invalid Rouch\'e for $n\ge3$

Erroneous ($n=2$): the solution states $f_2(z)=1+z+z^2$ and factors it as $(z-\zeta_3^2)(z-\zeta_3^{-2})$. But $f_2(z)=\sum_{k=0}^2 z^k/k! = 1+z+\frac12z^2$ (the problem's series has $1/k!$ coefficients), and moreover $(z-\zeta_3^2)(z-\zeta_3^{-2})=z^2+z+1$, so the factorization is of a different polynomial than the one written. The actual zeros of $f_2$ are the roots of $z^2+2z+2=0$, i.e.\ $z=-1\pm i$, of modulus $\sqrt2>1$, so the conclusion (no zeros in $\DD$) is nonetheless true.

Erroneous ($n\ge3$): the solution applies Rouch\'e with $M(z)=1+z$ and $m(z)=\sum_{k=2}^n z^k/k!$ on $\abs z=1$. This fails because $\abs{M(z)}=\abs{1+z}$ vanishes at $z=-1$ on the unit circle, so $\abs M>\abs m$ does not hold there (Rouch\'e cannot be applied). The accompanying claims are also wrong: $\abs m$ is not the constant $2$ on the circle, and the bound $\abs m\le\sum_{k\ge n+1}1/k!$ (and the value $\approx0.718$) bounds the wrong tail — $m$ is the finite sum $k=2,\dots,n$, not the tail $k\ge n+1$. (The theorem is nevertheless true: the partial sums of $e^z$ have all zeros outside the unit disk; $n=1$ is handled correctly.)

### 56. P-IM6MH — inversion $1/(2z-1)$: final display labels the series as $1/(1-2z)$

Erroneous: the card computes the correct coefficients $b_0=-1,\ b_1=-2,\ b_2=-4,\ b_3=-8$ for $A(z)=2z-1$ (using the recurrence for the inverse), but the final display reads
$$\frac{1}{1-2z} = -1 - 2z - 4z^2 - 8z^3\cdots = -\sum_{k\ge0}(2z)^k.$$
The series written is the expansion of $\frac{1}{2z-1}=-\frac1{1-2z}=-\sum_{k\ge0}(2z)^k$, not of $\frac{1}{1-2z}$, which equals $+\sum_{k\ge0}(2z)^k=1+2z+4z^2+\cdots$ and contradicts the computed $b_0=-1$. The equality as displayed is therefore false. (The coefficients $b_n$ above the display are correct; only the argument $"1-2z"$ in the display is wrong — it should be $"2z-1"$.)

### 57. P-KPCIE — midpoint recurrence $x_n=(x_{n-1}+x_{n-2})/2$: final closed form and limit are wrong ($\tfrac13(a+b)$ instead of $\tfrac13 a+\tfrac23 b$)

Erroneous: after solving the recurrence, the solution writes
$$x_n=\frac23(a-b)\left(-\frac12\right)^n+\frac13(a+b)\xrightarrow{n\to\infty}\frac13(a+b).$$
The matrix step just above actually gives the correct value $c_2=\frac13 a+\frac23 b$ (the inverse matrix is right, and substituting $c_1=a-c_2$ into $b=-c_1/2+c_2$ yields $c_2=\frac{a+2b}{3}$). The final line replaces $c_2$ with $\frac13(a+b)$, which is a different constant, and the claimed limit $\frac13(a+b)$ is false. The correct general solution is
$$x_n=\frac23(a-b)\left(-\frac12\right)^n+\frac{a+2b}{3},\qquad \lim_{n\to\infty}x_n=\frac{a+2b}{3}.$$
Numerical check: $a=0,\ b=3$ gives $x_0=0,\ x_1=3,\ x_2=3/2,\ x_3=9/4,\ x_4=15/8,\ldots\to 2=\frac{a+2b}{3}$, not $1=\frac{a+b}{3}$. The card's title repeats the same wrong limit $\frac{a+b}{3}$.

### 58. P-MICNK — $az^n+z+1$ has a root in $|z|\le2$: Rouché threshold off by a factor of $4^n$

Erroneous: in the Rouché case the solution sets $g(z)=z+1$ and $h(z)=az^n$ on $|z|=2$, requiring $|h|<|g|$ there, i.e.\ $|a|\,2^n<|z+1|$. Since on $|z|=2$ the sharp lower bound is $|z+1|\ge1$ (attained at $z=-2$), this needs $|a|\,2^n<1$, i.e.\ $\boxed{|a|<2^{-n}}$. The card instead states "if $|a|<2^n$, this holds because $|a||z|^n<{1\over 2^n}2^n=1$", which uses the right estimate with the wrong threshold: from $|a|<2^n$ one gets only $|a|\,2^n<4^n$, not $<1$. The correct case split is at $|a|=2^{-n}$: Rouché gives exactly one root (of $z+1$) inside $|z|<2$ when $|a|<2^{-n}$, and the product-of-roots estimate $\prod_k|z_k|=1/|a|$ gives a root in $|z|\le2$ when $|a|>2^{-n}$. With the stated split ($|a|<2^n$ vs. $|a|\ge2^n$) the Rouché branch is invalid for the range it claims to cover, and $|a|\in[2^{-n},2^n)$ is left to neither stated case. (The case-2 product argument itself is sound because $1/|a|\le 2^{-n}<2^n$ rules out all roots having modulus $>2$.)

### 59. P-N6W5L — zeros of $z^3-z+1$ in $\Re z>0$: the listed roots of $z^3+1$ are wrong

Erroneous: applying Rouch\'e on the right-half-plane contour with $M(z)=z^3+1$ and $m(z)=-z$ is correct, and $|1-it^3|>|it|$ on the imaginary axis because $t^6-t^2+1>0$ for all $t$. But the solution then identifies
$$z^3+1\ \text{has roots}\ \omega_3,\ \omega_3^2,\ \omega_3^3=-1,\qquad \omega_k=e^{i\pi/k}.$$
The roots of $z^3+1$ (zeros of $z^3=-1=e^{i(\pi+2\pi k)}$) are $e^{i\pi/3},\ -1,\ e^{i5\pi/3}=e^{-i\pi/3}$; in particular $\omega_3^2=e^{i2\pi/3}$ is NOT a root (it is a root of $z^3-1$). The stated third root should be $e^{i5\pi/3}$, not $\omega_3^2$. The count in the right half-plane is nonetheless still $2$, since the two true roots with positive real part are $e^{\pm i\pi/3}$.

### 60. P-P7IWV — one root of $z^4+2z^3-2z+10$ in each quadrant: wrong imaginary part of $f(it)$ in the "older" solution

Erroneous: the primary (argument-principle) solution is correct and gives $f(it)=t^4+10+i(-2t^3-2t)$, with real part $t^4+10>0$, so no winding about $0$ on the imaginary axis. But the retained "older" solution states
$$f(it)=t^4-it^3-2it+10.$$
This is wrong: $(it)^3=-it^3$ enters with coefficient $2$, so $f(it)=(it)^4+2(it)^3-2(it)+10 = t^4-2it^3-2it+10$, whose imaginary part is $-2t^3-2t$, not $-t^3-2t$. The conclusion $\Arg(f(it))\sim 0$ is unaffected (as $t\to\infty$ the argument is dominated by the positive real part $t^4+10$), so the stated quadrant count of one remains correct.

### 61. P-R2D54 — truncated exponentials have no zeros in the unit disk: the $f_2$ factorization is of a different polynomial

Erroneous: with $f_n(z)=\sum_{k=0}^n z^k/k!$, the solution writes for $n=2$
$$f_2(z)=1+z+\tfrac12z^2=(z-(1+i))(z-(1-i)).$$
The right side expands to $z^2-2z+2$, which is not a constant multiple of $f_2=1+z+\tfrac12z^2$ (note $\tfrac12(z^2+2z+2)=1+z+\tfrac12z^2$). The actual zeros of $f_2$ are the roots of $z^2+2z+2=0$, namely $z=-1\pm i$, of modulus $\sqrt2>1$. The conclusion (no zeros in the open unit disk) is nonetheless true; the stated factorization is of the wrong polynomial. (Same defect is logged separately for P-FY3WB as finding 55; the remainder of this card is an unfinished Rouch\'e sketch.)

### 62. P-RMZDG part 2 — bounded $f$ vanishing on a sector as $|z|\to1$: the $\eps$-bound is taken in the wrong annulus

Erroneous: the hypothesis is that $f$ converges uniformly to $0$ IN THE SECTOR as $|z|\to1$, i.e. for every $\eps>0$ there is $\rho<1$ with $|f(z)|<\eps$ for all $z\in S$ with $\rho<|z|<1$ (smallness near the boundary, $|z|$ large). The solution instead asserts "choose $r<1$ small enough so that $|f(z)|<\eps$ for $|z|<r$ in $S$", placing the smallness near $|z|=0$. This is the reverse direction and does not follow from the hypothesis; as written the rotated-sector product argument collapses (it would need $|f|$ small on a full disk $|z|<r$ to force $g=f\prod_k f(\zeta^k z)\equiv0$, but convergence near the boundary gives smallness only in an annulus $\{|z|>\rho\}$ near $S^1$). The conclusion ($f\equiv0$) is a true standard theorem, but this proof step is false as written.

### 63. P-RMZDG part 4 (MMP version) — bounded real part: "attains $M$ in some disk" does not follow

Erroneous: the solution argues "if $|u|\le M$ on $\mathbb C$, then there is some disc where $|u|=M$ for some point in the interior; by the MMP for harmonic functions, $u$ is constant." The intermediate claim is false: a bounded harmonic function need not attain its supremum $M$ anywhere (boundedness alone gives $\le M$, not $=M$). The conclusion is true by Liouville's theorem for harmonic functions on $\mathbb C$ (a bounded harmonic function on $\mathbb C$ is constant), but the stated route through an attained maximum is invalid. (The card's other proof of part 4, via $g=e^f$ and Liouville, is correct — note also the written "$\Re(z)$" there should read "$\Re(f(z))$".)

### 64. P-SFDLG part 2 — discontinuity of the principal logarithm: the furnished sequence shows no discontinuity

Erroneous: to show $\Log z$ is discontinuous across the negative real axis, the card takes $w_k=1\cdot e^{i(2\pi-1/k)}$ and claims $\Log(w_k)=i(2\pi-1/k)\not\to0$. But $2\pi-1/k>\pi$, so the PRINCIPAL argument of $w_k=e^{i(2\pi-1/k)}=e^{-i/k}$ is $-1/k\in(-\pi,0)$, not $2\pi-1/k$; hence $\Log(w_k)=i(-1/k)\to0=\Log(1)$, and this sequence converges continuously (to $1$ from below). To exhibit the discontinuity one must approach a point of the cut $(-\infty,0)$, e.g. $z_k^\pm=e^{\pm i(\pi-1/k)}\to-1$ from the two sides, giving $\Log(z_k^+)\to i\pi$ and $\Log(z_k^-)\to-i\pi$, two different limits — which is what actually proves $\Log$ is not continuous at $-1$.

### 65. P-UQOCE — the integration-by-parts recursion for the generalization carries a spurious factor $1/(k+1)$

Erroneous: for the higher-order analogue the card states
\[
\oint_\gamma \frac{f^{(k)}(z)}{(z-z_0)^m}\,dz = \frac{m}{k+1}\oint_\gamma \frac{f^{(k-1)}(z)}{(z-z_0)^{m+1}}\,dz \qquad (k\ge 1).
\]
The correct recursion (from $d\bigl(f^{(k-1)}(z)/(z-z_0)^m\bigr) = \frac{f^{(k)}(z)}{(z-z_0)^m}dz - m\frac{f^{(k-1)}(z)}{(z-z_0)^{m+1}}dz$ integrated around the closed loop) has no $1/(k+1)$ factor:
\[
\oint_\gamma \frac{f^{(k)}(z)}{(z-z_0)^m}\,dz = m\oint_\gamma \frac{f^{(k-1)}(z)}{(z-z_0)^{m+1}}\,dz .
\]
Iterating gives $m(m+1)\cdots(m+k-1)$, which is exactly what the card's own next step (<2>2) correctly writes. So the displayed recursion is wrong, and following it literally would produce the incorrect coefficient $\prod_{j=1}^{k}\frac{m+j-1}{j}$ instead of $\frac{(m+k-1)!}{(m-1)!}$. The final stated generalization $\oint_\gamma \frac{f^{(k)}(z)}{(z-z_0)^m}dz=\frac{(m+k-1)!}{(m-1)!}\oint_\gamma \frac{f(z)}{(z-z_0)^{m+k}}dz$ is correct (both sides equal $\frac{2\pi i}{(m-1)!}n(\gamma,z_0)f^{(m+k-1)}(z_0)$), so the error is confined to the intermediate recursion displayed in <2>1.

### 66. P-WB56B — a C1 two-threshold argument for the uncountable split point, with a false condensation-point claim

Erroneous: the card's step <1>4, after producing $t$ with $E\cap(-\infty,t)$ at most countable and $E\cap(t,\infty)$ uncountable, asserts (in <2>5--<2>6) that "by the Cantor--Bendixson Theorem / condensation points, $E$ has a condensation point $t^* \in (0,1)$ where every open neighborhood $(t^*-\varepsilon,t^*+\varepsilon)\cap E$ is uncountable," and that "for any such condensation point $t^*$, both $E\cap(-\infty,t^*)$ and $E\cap(t^*,\infty)$ are uncountable." The final clause is false: a condensation point $c$ is a point whose every punctured neighborhood meets $E$ uncountably, and that does not force uncountably many $E$-points on each side of $c$. Example: $E = \{0\}\cup\bigl\{2^{-n}+\text{small}\bigr\}$ cannot be used directly, but take $E = \{1\}\cup A$ where $A$ is an uncountable set accumulating at $1$ only from the left (e.g. a set with condensation point at $1$ lying in $(0,1)$); then $c=1$ has uncountably many points in every left neighborhood but $E\cap(1,\infty)=\varnothing$. So "both sides uncountable" does not follow from being a condensation point. The conclusion of the problem is true, and an alternative route in the card (choosing $t^*\in(t,t')$ between the left-countable threshold $t$ and right-countable threshold $t'$) is the sound way to get both sides uncountable; but the assertion as stated at <2>6 is false and is presented as a standalone reason, not as something the alternative route recovers.
