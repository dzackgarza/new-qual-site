---
schema: qual/card@1
id: E-HAT-3.C-9
kind: problem
title: Euler characteristic of finite H-spaces
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 9; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof, both halves. Over $\QQ$, Hopf's theorem gives an exterior algebra on odd
    generators because finite-dimensionality forbids polynomial generators, so $P_\QQ(-1)=0$ when
    there is any generator. If there is none, $H^*(X;\QQ)=\QQ$, the positive integral homology is
    torsion, and some prime $p$ has $\widetilde H^*(X;\FF_p)\ne0$. Borel's theorem then splits
    $H^*(X;\FF_p)$ into single-generator factors: an exterior factor makes $P_{\FF_p}(-1)=0$, a
    truncated factor $\FF_p[y]/(y^{p^k})$ with $\deg y$ even contributes $p^k$, and with $p=2$ and
    $\deg y$ odd the alternating sum of its $2^k$ terms is zero. Each case contradicts
    $\chi(X)=P(-1)=1$, so $\chi(X)=0$. Hopf's and Borel's theorems are the cited inputs; the case
    analysis around them is read.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §3.C Exercise 9, printed p. 291. The collection's provenance is the book, and no retained solution set covers the exercise; the argument is the card's own. Checked: the identity $\chi=P_F(-1)$; Hopf's structure theorem over $\QQ$ with no polynomial generators in finite dimension; the vanishing of $\prod(1+t^{d_i})$ at $-1$ for odd $d_i$; and the Borel case analysis over $\FF_p$, including the $p=2$ odd-generator factor whose alternating sum is zero.
---

::: {.problem}
Apply the theorems of Hopf and Borel to show that for an H-space $X$ that is a connected finite CW complex with $\tilde{H}_*(X; \ZZ) \neq 0$, the Euler characteristic $\chi(X)$ is $0$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.C Exercise 9. It is the two-theorem argument the exercise names: Hopf's theorem over $\QQ$ and Borel's over $\FF_p$.

::: pf

::: {.pf-step #euler}
For a finite CW complex $X$, $\chi(X)=P_F(-1)$ for every field $F$, where $P_F(t)=\sum_i\dim_FH^i(X;F)t^i$.

::: pf-proof
This is the coefficient-field form of the Euler characteristic identity of §2.2 Exercise 41, applied with field coefficients; for a finite complex $P_F$ is a polynomial.
:::
:::

::: {.pf-step #hopf}
$H^*(X;\QQ)\cong\Lambda_{\QQ}(x_1,\dots,x_r)$ with every $\gradeddegree{x_i}$ odd, for some $r\geq0$.

::: pf-proof
Hopf's theorem expresses the connected graded Hopf algebra $H^*(X;\QQ)$ as a tensor product of exterior algebras on odd generators and polynomial algebras on even generators. Since $X$ is a finite CW complex, $H^*(X;\QQ)$ is finite-dimensional, so no polynomial generator can occur.
:::
:::

::: {.pf-step #r-positive}
If $r>0$ then $\chi(X)=0$.

::: pf-proof
The Poincaré polynomial of the exterior algebra on generators of odd degrees $d_i$ is $\prod_i(1+t^{d_i})$, so $P_{\QQ}(-1)=\prod_i(1+(-1)^{d_i})=0$ because each $d_i$ is odd; with step [](#euler){.pf-ref} this gives $\chi(X)=0$.
:::
:::

::: {.pf-step #r-zero}
If $r=0$ then $H^*(X;\QQ)=\QQ$, so $\chi(X)=1$ and all positive-dimensional integral homology is torsion.

::: pf-proof
With no generators the exterior algebra is $\QQ$ in degree $0$, so $P_{\QQ}(t)=1$ and $\chi(X)=1$; since $\dim_{\QQ}H_i(X;\QQ)=0$ for $i>0$, each $H_i(X;\ZZ)$ with $i>0$ is a torsion group.
:::
:::

::: {.pf-step #excluded}
$r=0$ contradicts $\widetilde H_*(X;\ZZ)\neq0$.

::: pf-proof
Choose a prime $p$ with $\widetilde H^*(X;\FF_p)\neq0$: since some $H_i(X;\ZZ)$, $i>0$, has an element of order $p$, its tensor product with $\FF_p$ is nonzero, and the universal coefficient theorem then makes $H_i(X;\FF_p)$ nonzero. Borel's theorem writes the finite-dimensional Hopf algebra $H^*(X;\FF_p)$ as a tensor product of single-generator factors, each an exterior algebra on an odd generator or a truncated polynomial algebra $\FF_p[y]/(y^{p^k})$. If an exterior factor occurs, its Poincaré polynomial vanishes at $-1$ and hence $\chi(X)=0$, contradicting $\chi(X)=1$ from step [](#r-zero){.pf-ref}. Otherwise every factor is truncated polynomial: a factor of even generator degree $d$ contributes $1+t^d+\dots+t^{(p^k-1)d}$, whose value at $-1$ is $1$ when $d$ is even, so $P_{\FF_p}(-1)$ is a product of powers of $p$ and is divisible by $p$, while $P_{\FF_p}(-1)=\chi(X)=1$; when $p=2$ and the generator has odd degree the alternating sum of the $2^k$ terms is $0$, again contradicting $\chi(X)=1$.
:::
:::

::: {.pf-step}
$\chi(X)=0$ for a connected finite CW H-space with $\widetilde H_*(X;\ZZ)\neq0$.

::: pf-proof
Steps [](#hopf){.pf-ref} and [](#r-positive){.pf-ref} give the conclusion when $r>0$, and steps [](#r-zero){.pf-ref} and [](#excluded){.pf-ref} rule out $r=0$ under the hypothesis.
:::
:::

:::
:::
