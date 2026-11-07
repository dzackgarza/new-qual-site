---
schema: qual/card@1
id: E-HAT-3.1-7
kind: problem
title: $\operatorname{Hom}(H_n(X),\ZZ)$ is not a cohomology theory
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the cochain, exact-sequence, and universal-coefficient calculations directly.
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 7; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the counterexample: for $X=M(\ZZ_m,1)$ the segment of the pair reads
    $0\to\operatorname{Hom}(\ZZ,\ZZ)\to\operatorname{Hom}(\ZZ,\ZZ)\to0$ after applying
    $\operatorname{Hom}(-,\ZZ)$, since $\operatorname{Hom}(\ZZ_m,\ZZ)=0$, and the middle map is
    multiplication by $m$, which is not onto for $m>1$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 7 (p.205). Rechecked the counterexample: for X = S^1 with a 2-cell attached by a degree-m map, Theorem 2.35 and the Cellular Boundary Formula (pp.139, 141) give partial = multiplication by m, so h^1(X) = Hom(Z_m,Z) = 0, h^1(A) = h^2(X,A) = Z with the connecting map multiplication by m, and h^2(X) = Hom(H_2 X,Z) = 0; the resulting 0 -> Z ->^m Z -> 0 cannot be exact. Citations added: Theorem 2.16 p.117 for the sequence of the pair and p.160 for the axioms. Not covered: the exercise asks only for failure on CW complexes, and only the exactness axiom is tested.
---

::: {.problem}
Show that the functors $h^n(X) = \operatorname{Hom}(H_n(X), \ZZ)$ do not define a cohomology theory on the category of CW complexes.
:::

::: {.solution}
The functors
$$
h^n(X)=\operatorname{Hom}(H_n(X),\ZZ)
$$
fail the exactness axiom.

::: pf

::: pf-step

Let $X=M(\ZZ_m,1)$ be obtained from $S^1=A$ by attaching a $2$-cell by a map of degree $m>1$.
Then
$$
H_1(A)=\ZZ,\qquad H_1(X)=\ZZ_m,\qquad H_2(X,A)=\ZZ.
$$
The boundary map
$$
\partial:H_2(X,A)\to H_1(A)
$$
is multiplication by $m$.

::: pf-proof

Theorem 2.35 (p.139) with the Cellular Boundary Formula (p.141): with one $1$-cell and one $2$-cell attached by a map of degree $m$, the cellular boundary $H_2(X,A)\to H_1(A)$ is multiplication by $m$, since the only incidence number is the degree of the attaching map. This is the Moore space $M(\ZZ_m,1)$ of Exercise 11 (p.205).

:::

:::

::: pf-step

Applying $\operatorname{Hom}(-,\ZZ)$ gives
$$
h^1(X)=0,\qquad h^1(A)=\ZZ,\qquad h^2(X,A)=\ZZ,\qquad h^2(X)=0,
$$
and the map induced by $\partial$ is multiplication by $m$:
$$
\ZZ\xrightarrow{\,m\,}\ZZ.
$$

::: pf-proof

One has $\operatorname{Hom}(\ZZ_m,\ZZ)=0$ and $\operatorname{Hom}(\ZZ,\ZZ)=\ZZ$. Contravariance sends multiplication by $m$ to multiplication by $m$.

:::

:::

::: pf-step

If the $h^n$ formed a cohomology theory in the sense of the axioms on p.160, the long exact sequence of the pair (Theorem 2.16, p.117) would contain
$$
0=h^1(X)\longrightarrow h^1(A)=\ZZ
\xrightarrow{\,m\,}h^2(X,A)=\ZZ
\longrightarrow h^2(X)=0,
$$
which would have to be exact.

::: pf-proof

Exactness at $h^2(X,A)$ would require multiplication by $m$ to be surjective, which it is not for $m>1$.

:::

:::

:::

Hence these functors do not define a cohomology theory.
:::
