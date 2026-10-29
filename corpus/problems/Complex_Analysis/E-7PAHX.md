---
schema: qual/card@1
id: E-7PAHX
kind: problem
title: Principal parts of $P/Q$ at simple and double poles
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
Let $P, Q$ be polynomials with no common zeros. Assume $a$ is a root of $Q$.
Find the principal part of $P/Q$ at $z=a$ in terms of $P$ and $Q$ if $a$ is

(1) a simple root, and

(2) a double root.
:::

::: {.solution}
Since $P(a)\neq0$, a root of $Q$ of order $m$ is a pole of $P/Q$ of order $m$.

::: pf

::: pf-step
(1) If $a$ is a simple root, the principal part is $\boxed{\frac{P(a)}{Q'(a)}\,\frac{1}{z-a}}$.

::: pf-proof
Write $Q(z)=(z-a)R(z)$ with $R$ a polynomial; then $R(a)=Q'(a)\neq0$, so $P/R$ is holomorphic near $a$ and
$$
\frac{P(z)}{Q(z)} = \frac{1}{z-a}\,\frac{P(z)}{R(z)}
= \frac{1}{z-a}\qty{\frac{P(a)}{R(a)} + \bigo(z-a)}.
$$
:::

:::

::: pf-step
(2) If $a$ is a double root, the principal part is
$$
\boxed{\frac{2P(a)}{Q''(a)}\,\frac{1}{(z-a)^2}+\qty{\frac{2P'(a)}{Q''(a)}-\frac{2P(a)Q'''(a)}{3Q''(a)^2}}\frac{1}{z-a}}.
$$

::: pf-proof
Write $Q(z)=(z-a)^2R(z)$ with $R(a)\neq0$.
Differentiating, $Q''(a)=2R(a)$ and $Q'''(a)=6R'(a)$.
The function $h\coloneqq P/R$ is holomorphic near $a$, and
$$
\frac{P(z)}{Q(z)} = \frac{h(z)}{(z-a)^2} = \frac{h(a)}{(z-a)^2} + \frac{h'(a)}{z-a} + \bigo(1),
$$
where
$$
h(a)=\frac{P(a)}{R(a)}=\frac{2P(a)}{Q''(a)},
\qquad
h'(a)=\frac{P'(a)R(a)-P(a)R'(a)}{R(a)^2}=\frac{2P'(a)}{Q''(a)}-\frac{2P(a)Q'''(a)}{3Q''(a)^2}.
$$
:::

:::

:::

:::
