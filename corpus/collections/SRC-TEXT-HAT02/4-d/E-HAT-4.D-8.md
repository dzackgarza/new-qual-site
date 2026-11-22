---
schema: qual/card@1
id: E-HAT-4.D-8
kind: problem
title: Thom space of a product bundle
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-04
  note: >-
    The second clause of the printed exercise asks for the homology suspension isomorphism
    H-tilde_i(B;R) = H-tilde_{n+i}(Sigma^n B;R) given by the reduced cross product; the card answered
    only in cohomology, which is a true analogue but not the statement asked. The missing homology
    form is added on top of the existing quotient and cross-product work: relative cross product in
    homology with field coefficients (Kunneth an isomorphism there) is the homology Thom isomorphism,
    and the same quotient identification gives the reduced suspension isomorphism. The existing
    statements are unchanged and were checked.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Checked against Hatcher, Section 4.D Exercise 8, printed
    p. 447 (PDF p. 456, folio 447), read in the retained text at
    tmp/sources/hatcher-2002-algebraic-topology.md:9220. Two things repaired. First, the printed
    second clause asks for the cohomology suspension isomorphism
    $H~^i(B;R) = H~^{n+i}(Sigma^n B;R)$; the card's 2026-11-04 note says the printed exercise asks
    for the homology form, which is not what the book prints, so the homology paragraph is now
    labelled as additional and not part of the statement. Second, the display that identified the
    Thom isomorphism with a reduced suspension isomorphism $H~^i(B_+) = H~^{n+i}(Sigma^n B_+)$ was
    false at $i = 0$, where both sides differ by the copy of $R$ carried by the disjoint basepoint;
    the step now states the isomorphism with unreduced cohomology on the left, $H^i(B;R) =
    H~^{n+i}(Sigma^n B_+;R)$, splits $Sigma^n B_+ = Sigma^n B v S^n$, and gives the reduced form for
    $i >= 1$ together with the $i = 0$ case. Not claimed: any statement for a non-product bundle,
    or the Gysin sequence.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.D Exercise 8, Corollary 4D.9,
    Theorem 4D.10 and the reduced cross product of §3.2. Correct: the disk bundle of the sphere bundle
    S^n -> E -> B has Thom class the suspension of a generator, the Thom isomorphism gives the shift
    by n in cohomology, and the homology analogue at the end is marked as the card's addition rather
    than as part of the printed exercise. Two page locators in the opening paragraph replaced by
    Corollary 4D.9; no mathematics changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.D Exercise 8. One slip repaired: the step called the map
    $a\mapsto a\times u$ "cap product with the Thom class"; it is the cup (cross) product, which is
    what the Thom isomorphism of Corollary 4D.9 is. The rest of the argument reads correct.
---

::: {.problem}
If $E$ is the product bundle $B \times D^n$ with $B$ a CW complex, show that the Thom space $T(E)$ is the $n$-fold reduced suspension $\Sigma^n(B_+)$, where $B_+$ is the union of $B$ with a disjoint basepoint, and that the Thom isomorphism specializes to the suspension isomorphism $\tilde{H}^i(B; R) \approx \tilde{H}^{n+i}(\Sigma^n B; R)$ given by the reduced cross product in §3.2.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none of the retained Hatcher sets solves Section 4.D Exercise 8. It is checked against Hatcher, Algebraic Topology, Section 4.D Exercise 8, against the Thom isomorphism theorem of Section 4.D, Corollary 4D.9, and against the reduced cross product of Section 3.2. The printed exercise asks for the cohomology statement $\tilde H^i(B;R)\approx\tilde H^{n+i}(\Sigma^nB;R)$; the homology analogue at the end is additional and is marked as such.

::: pf

::: {.pf-step #setup}
For the product disk bundle $E=B\times D^n$ with sphere bundle $E'=B\times S^{n-1}$, the Thom space is
$$
T(E)=\frac{B\times D^n}{B\times S^{n-1}}.
$$

::: pf-proof
The Thom space of a disk bundle is the quotient of the total space by its sphere bundle; for the product bundle the sphere bundle is $B\times S^{n-1}$.
:::

:::

::: {.pf-step #suspension}
$T(E)\cong B_+\wedge S^n=\Sigma^n(B_+)$.

::: pf-proof

::: {.pf-step #quotients}
For CW complexes $X$ and a CW pair $(Y,Y_0)$ one has $(X\times Y)/(X\times Y_0)\cong X_+\wedge(Y/Y_0)$.

::: pf-proof
The pair $(X\times Y,X\times Y_0)$ is the product of $X$ with the pair $(Y,Y_0)$, and collapsing the second factor first gives $X\times(Y/Y_0)$ with $X\times\{*\}$ collapsed to a point, which is the smash product of $X_+$ with $Y/Y_0$. Both spaces are quotients of $X\times Y$ by the same closed subspace, so they are homeomorphic.
:::

:::

::: {.pf-step #disc}
$D^n/S^{n-1}\cong S^n$.

::: pf-proof
$D^n$ modulo its boundary is the one-point compactification of the interior $\mathring D^n\cong\RR^n$, which is $S^n$.
:::

:::

::: {.pf-step}
$T(E)\cong B_+\wedge S^n$.

::: pf-proof
Apply steps [](#quotients){.pf-ref} and [](#disc){.pf-ref} with $X=B$, $Y=D^n$ and $Y_0=S^{n-1}$; by definition $\Sigma^n(B_+)=B_+\wedge S^n$.
:::

:::

:::

:::

::: {.pf-step #thomclass}
The class $1\times u\in H^n(B\times D^n,B\times S^{n-1};R)$, where $u\in H^n(D^n,S^{n-1};R)\cong R$ is the fibre orientation class, is a Thom class for $E$, and cup product with it is the Thom isomorphism $H^i(B;R)\to H^{n+i}(E,E';R)$.

::: pf-proof
The product bundle is orientable, with fibre orientation $u$; the Thom isomorphism theorem for a disk bundle with a Thom class (Corollary 4D.9) then gives that $a\mapsto a\times u$ is an isomorphism $H^i(B;R)\to H^{n+i}(E,E';R)$ for every $i$, the relative cross product being taken in the pair $(B\times D^n,B\times S^{n-1})$.
:::

:::

::: {.pf-step #specialize}
Under the quotient identification of step [](#suspension){.pf-ref}, the Thom isomorphism reads $H^i(B;R)\cong\tilde H^{n+i}(\Sigma^nB_+;R)$, which for $i\ge1$ is the reduced suspension isomorphism $\tilde H^i(B;R)\cong\tilde H^{n+i}(\Sigma^nB;R)$.

::: pf-proof
The quotient map $(E,E')\to(T(E),*)$ induces an isomorphism $H^{n+i}(E,E';R)\cong\tilde H^{n+i}(T(E);R)$, since $T(E)=E/E'$. Composing with the Thom isomorphism gives $H^i(B;R)\cong\tilde H^{n+i}(\Sigma^nB_+;R)$, and $\Sigma^nB_+=(B\wedge S^n)\vee S^n=\Sigma^nB\vee S^n$, so $\tilde H^{n+i}(\Sigma^nB_+;R)=\tilde H^{n+i}(\Sigma^nB;R)\oplus\tilde H^{n+i}(S^n;R)$. For $i\ge1$ the second summand vanishes because $n+i>n$, leaving $H^i(B;R)\cong\tilde H^{n+i}(\Sigma^nB;R)$; for $i\ge1$ the left side is reduced cohomology of $B$, so this is the suspension isomorphism. For $i=0$ the two sides of the printed statement are $\tilde H^0(B;R)$ and $\tilde H^n(\Sigma^nB;R)\cong\tilde H^0(B;R)$, equal for every $B$. Note that the Thom isomorphism is unreduced on the left: at $i=0$ it computes $H^0(B;R)\cong\tilde H^n(\Sigma^nB_+;R)$, and the extra copy of $R$ in degree $n$ is exactly the contribution of the disjoint basepoint.
:::

:::

::: {.pf-step #homology}
With field coefficients the same argument in homology gives $\tilde H_i(B;R)\cong\tilde H_{n+i}(\Sigma^nB;R)$. This is not part of the printed statement, which asks for cohomology.

::: pf-proof
The relative cross product of Section 3.2 with field coefficients is an isomorphism $H_i(B;R)\otimes H_n(D^n,S^{n-1};R)\to H_{i+n}(B\times D^n,B\times S^{n-1};R)$ by the Künneth formula over a field, and it is the homology Thom isomorphism for the product bundle; composing with the quotient identification of step [](#suspension){.pf-ref} and splitting off the $S^n$ summand of $B_+\wedge S^n$ as in step [](#specialize){.pf-ref} gives the asserted suspension isomorphism.
:::

:::

::: {.pf-step}
$T(B\times D^n)\cong\Sigma^n(B_+)$, and the Thom isomorphism specializes to the suspension isomorphism.

::: pf-proof
Steps [](#suspension){.pf-ref} and [](#specialize){.pf-ref} give both assertions of the printed exercise:
$$
\boxed{T(B\times D^n)\cong\Sigma^n(B_+),\qquad \tilde H^i(B;R)\cong\tilde H^{n+i}(\Sigma^nB;R)\text{ for }i\ge1.}
$$
:::

:::

:::
:::
