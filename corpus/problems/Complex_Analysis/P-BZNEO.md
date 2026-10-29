---
schema: qual/card@1
id: P-BZNEO
kind: problem
title: Principal part of $P/Q$ at a simple or double root of $Q$
classification:
  areas:
  - complex-analysis
  topics:
  - Principal Parts
  - Poles
  - Residues
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $P, Q$ be polynomials with no common zeros.
Assume $a$ is a root of $Q$.
Find the principal part of $P/Q$ at $z=a$ in terms of $P$ and $Q$ if $a$ is (1) a simple root, and (2) a double root.
:::

::: {.solution}

::: pf

::: pf-step
(1) If $a$ is a simple root, the principal part is
$$
\boxed{\frac{P(a)}{Q'(a)}\frac1{z-a}}.
$$

::: pf-proof
Write $Q(z)=(z-a)q(z)$ with $q(a)=Q'(a)\ne0$.
Then $P/Q=(P/q)/(z-a)$ with $P/q$ holomorphic near $a$, so the principal part is $\frac{P(a)/q(a)}{z-a}$.
:::

:::

::: pf-step
(2) If $a$ is a double root, the principal part is
$$
\boxed{
\frac{2P(a)}{Q''(a)}\frac1{(z-a)^2}
+\left(
\frac{2P'(a)}{Q''(a)}
-\frac{2P(a)Q'''(a)}{3Q''(a)^2}
\right)\frac1{z-a}.}
$$

::: pf-proof
Write $Q(z)=(z-a)^2q(z)$ with $q(a)\ne0$.
Differentiating gives $Q''(a)=2q(a)$ and $Q'''(a)=6q'(a)$.
With $h\coloneqq P/q$, holomorphic near $a$,
$$
\frac{P(z)}{Q(z)}=\frac{h(z)}{(z-a)^2}
=\frac{h(a)}{(z-a)^2}+\frac{h'(a)}{z-a}+(\text{holomorphic}),
$$
and
$$
h(a)=\frac{2P(a)}{Q''(a)},\qquad
h'(a)=\frac{P'(a)}{q(a)}-\frac{P(a)q'(a)}{q(a)^2}
=\frac{2P'(a)}{Q''(a)}-\frac{2P(a)Q'''(a)}{3Q''(a)^2}.
$$
:::

:::

:::

:::
