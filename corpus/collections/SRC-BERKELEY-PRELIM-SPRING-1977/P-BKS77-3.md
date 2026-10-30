---
schema: qual/card@1
id: P-BKS77-3
kind: problem
title: Product of chord lengths from one vertex of a regular polygon
classification: {areas: [prelim], topics: [Complex Analysis]}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained source prints a missing-PostScript message for its illustration, but the regular-polygon construction and all segment lengths needed by the problem are specified in the text.
---

::: {.problem}
(a) Evaluate $P_{n-1}(1)$, where
$$
P_{n-1}(x)=\frac{x^n-1}{x-1}.
$$

(b) Let $Q_1,\ldots,Q_n$ be the vertices of a regular $n$-gon inscribed in a unit circle. For $i=2,\ldots,n$, let $\lambda_i$ be the length of the chord $Q_1Q_i$.
Prove that
$$
\prod_{i=2}^n\lambda_i=n.
$$
:::

::: {.solution}
::: pf

::: {.pf-step #polynomial-value}
One has
$$
\boxed{P_{n-1}(1)=n}.
$$

::: pf-proof
For $x\neq1$,
$$
\frac{x^n-1}{x-1}
=
1+x+\cdots+x^{n-1}.
$$
The right-hand side is a polynomial and therefore gives the polynomial extension of $P_{n-1}$ to $x=1$. Substituting $x=1$ gives
$$
P_{n-1}(1)
=
\underbrace{1+\cdots+1}_{n\text{ terms}}
=n.
$$
:::

:::

::: {.pf-step #polygon-coordinates}
Let
$$
\zeta\coloneqq e^{2\pi i/n}.
$$
After rotating the polygon if necessary, its vertices may be taken to be
$$
Q_j=\zeta^{j-1},
\qquad
1\leq j\leq n,
$$
on the unit circle.

::: pf-proof
Multiplication by a complex number of modulus $1$ is a Euclidean rotation, so it preserves all chord lengths. A regular $n$-gon on the unit circle has vertices obtained by successive rotations through angle $2\pi/n$, hence after one such overall rotation they have the displayed form.
:::

:::

::: {.pf-step #chord-lengths}
For $i=2,\ldots,n$,
$$
\lambda_i
=
\abs{1-\zeta^{i-1}}.
$$

::: pf-proof
By [](#polygon-coordinates){.pf-ref},
$$
Q_1=1,
\qquad
Q_i=\zeta^{i-1}.
$$
The Euclidean distance between two complex numbers is the modulus of their difference, so
$$
\lambda_i
=
\abs{Q_i-Q_1}
=
\abs{\zeta^{i-1}-1}
=
\abs{1-\zeta^{i-1}}.
$$
:::

:::

::: {.pf-step #root-factorization}
The factorization of $x^n-1$ gives
$$
P_{n-1}(x)
=
\prod_{k=1}^{n-1}(x-\zeta^k).
$$

::: pf-proof
The $n$ distinct roots of $x^n-1$ are
$$
1,\zeta,\zeta^2,\ldots,\zeta^{n-1}.
$$
Hence
$$
x^n-1
=(x-1)\prod_{k=1}^{n-1}(x-\zeta^k).
$$
Dividing by $x-1$ yields the displayed identity of polynomials.
:::

:::

::: pf-step
The product of the chord lengths is
$$
\boxed{\prod_{i=2}^n\lambda_i=n}.
$$

::: pf-proof
By [](#chord-lengths){.pf-ref},
$$
\prod_{i=2}^n\lambda_i
=
\prod_{k=1}^{n-1}\abs{1-\zeta^k}
=
\abs{
\prod_{k=1}^{n-1}(1-\zeta^k)
}.
$$
By [](#root-factorization){.pf-ref}, the product inside the modulus equals $P_{n-1}(1)$. [](#polynomial-value){.pf-ref} gives
$$
P_{n-1}(1)=n,
$$
so
$$
\prod_{i=2}^n\lambda_i
=\abs{n}
=n.
$$
:::

:::

:::

:::
