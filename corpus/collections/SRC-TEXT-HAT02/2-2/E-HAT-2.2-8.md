---
schema: qual/card@1
id: E-HAT-2.2-8
kind: problem
title: Degree of one-point compactification of polynomial equals degree as polynomial; local degree at roots equals multiplicity
classification:
  areas:
  - topology
  topics:
  - Degree
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 8; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete degree/cellular proof checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof: properness of a polynomial extends it to $S^2$ by $\hat f(\infty)=\infty$; the
    homotopy $f_t$ keeps the leading coefficient, so it is uniformly proper and extends as well;
    $a_mz^m$ has degree $m$ because a regular value has $m$ preimages each of local degree $+1$;
    and the local degree at a root is the winding number of $(z-z_0)^kg(z)$, the factor $g$
    contributing none since it is nonzero on the disc.
---

::: {.problem}
A polynomial $f(z)$ with complex coefficients, viewed as a map $\CC \to \CC$, can always be extended to a continuous map of one-point compactifications $\hat{f}: S^2 \to S^2$.
Show that the degree of $\hat{f}$ equals the degree of $f$ as a polynomial.
Show also that the local degree of $\hat{f}$ at a root of $f$ is the multiplicity of the root.
:::

::: {.solution}
Let
$$
f(z)=a_mz^m+a_{m-1}z^{m-1}+\cdots+a_0,
\qquad a_m\ne0.
$$
If $m=0$, extend the nonzero constant map to be constant at $\infty$ as well. Its map degree and polynomial degree are both zero, and it has no roots. Assume $m\ge1$ below.

::: pf

::: {.pf-step #s1}

The map $f:\CC\to\CC$ is proper and therefore extends continuously to one-point compactifications by setting
$$
\widehat f(\infty)=\infty.
$$

::: pf-proof

As $\abs{z}\to\infty$,
$$
\abs{f(z)}\ge \abs{a_m}\abs{z}^m-\sum_{j<m}\abs{a_j}\abs{z}^j\longrightarrow\infty.
$$
Hence inverse images of compact sets are bounded and closed, therefore compact. This is exactly the condition for extension to the one-point compactifications.

:::

:::

::: pf-step

The map $\widehat f$ is homotopic to the compactification of the leading monomial $a_mz^m$.

::: pf-proof

Consider
$$
f_t(z)=a_mz^m+t(a_{m-1}z^{m-1}+\cdots+a_0),
\qquad0\le t\le1.
$$
The leading coefficient is independent of $t$, so the estimate in step [](#s1){.pf-ref} is uniform in $t$ outside a sufficiently large disk. Thus the $f_t$ extend to a continuous based homotopy of one-point compactifications.

:::

:::

::: pf-step

The compactified map $z\mapsto a_mz^m$ has degree $m$.

::: pf-proof

Multiplication by $a_m\ne0$ is orientation preserving as a real linear map of $\CC$, so it has degree $+1$. For a nonzero regular value $w$, the equation
$$
z^m=w
$$
has exactly $m$ distinct roots. Near each root the derivative $mz^{m-1}$ is nonzero and complex multiplication by a nonzero number preserves the real orientation, so each of the $m$ points of the finite preimage of the regular value $w$ contributes local degree $+1$; by Proposition 2.30 (Hatcher p. 136) the degree of the compactified map is the sum of the local degrees over the finite preimage of $w$, so the total degree is $m$.

Therefore
$$
\boxed{\deg\widehat f=m=\deg(f)\text{ as a polynomial}.}
$$

:::

:::

::: pf-step

If $z_0$ is a root of multiplicity $k$, then the local degree of $\widehat f$ at $z_0$ is $k$.

::: pf-proof

Factor
$$
f(z)=(z-z_0)^k g(z),
\qquad g(z_0)\ne0.
$$
Choose a small circle $\abs{z-z_0}=\varepsilon$ on which $g$ has no zero, and let $D$ be the disk it bounds. By the definition of local degree (Hatcher p. 136) the local degree of $\widehat f$ at $z_0$ is the degree of the map $f/\abs{f}:\partial D\to S^1$ for $\varepsilon$ small enough that $f$ maps $D$ into a disk around $0$ containing no other zero, with $H_2(S^2)\cong\ZZ$ from Corollary 2.14 (p. 114); that degree is the winding number around $0$ of the image loop. The factor $(z-z_0)^k$ winds exactly $k$ times about $0$. The loop $g(z)$ is homotopic in $\CC^\times$ to the constant loop $g(z_0)$, for $\varepsilon$ small, by the straight-line homotopy through $g$ restricted to $\partial D$, which avoids $0$; so it contributes winding number $0$. Hence the total winding number, and therefore the local degree, is $k$.

:::

:::

:::

:::
