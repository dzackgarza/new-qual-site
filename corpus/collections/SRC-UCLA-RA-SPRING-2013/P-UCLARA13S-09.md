---
schema: qual/card@1
id: P-UCLARA13S-09
kind: problem
title: Zeros of a derivative remain in the same half-plane
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $P$ be a nonconstant polynomial all of whose zeros lie in the half-plane
\[
\{z\in\CC:\operatorname{Re}z<\sigma\}.
\]
Show that every zero of $P'$ also lies in this half-plane.
:::

::: {.solution}

Write
\[
P(z)
=
c\prod_{j=1}^n(z-a_j),
\]
where the zeros $a_j$ are listed with multiplicity. By hypothesis,
\[
\operatorname{Re}a_j<\sigma
\qquad
(1\le j\le n).
\]

::: pf

::: {.pf-step #s1-1}

If $z_0$ satisfies
\[
P'(z_0)=0
\qquad\text{and}\qquad
P(z_0)=0,
\]
then
\[
\operatorname{Re}z_0<\sigma.
\]


::: pf-proof

The condition $P(z_0)=0$ means that $z_0=a_j$ for some zero $a_j$ of $P$. Every such zero lies in the stated half-plane by hypothesis.

:::

:::

::: {.pf-step #s1-2}

For every $z$ with $P(z)\ne0$,
\[
\frac{P'(z)}{P(z)}
=
\sum_{j=1}^n\frac1{z-a_j}.
\]


::: pf-proof

Differentiate the product representation:
\[
P'(z)
=
P(z)
\sum_{j=1}^n\frac1{z-a_j}.
\]
Division by the nonzero number $P(z)$ gives the identity.

:::

:::

::: {.pf-step #s1-3}

If
\[
\operatorname{Re}z\ge\sigma,
\]
then for every $j$,
\[
\operatorname{Re}\frac1{z-a_j}>0.
\]


::: pf-proof

For any nonzero complex number $w$,
\[
\operatorname{Re}\frac1w
=
\frac{\operatorname{Re}w}{|w|^2}.
\]
Taking $w=z-a_j$ gives
\[
\operatorname{Re}\frac1{z-a_j}
=
\frac{\operatorname{Re}z-\operatorname{Re}a_j}
{|z-a_j|^2}.
\]
Because
\[
\operatorname{Re}z\ge\sigma>\operatorname{Re}a_j,
\]
the numerator is strictly positive.

:::

:::

::: {.pf-step #s1-4}

If $P(z)\ne0$ and
\[
\operatorname{Re}z\ge\sigma,
\]
then
\[
P'(z)\ne0.
\]


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref},
\[
\operatorname{Re}\frac{P'(z)}{P(z)}
=
\sum_{j=1}^n
\operatorname{Re}\frac1{z-a_j}
>
0.
\]
Hence $P'(z)/P(z)$ cannot be zero, so $P'(z)\ne0$.

:::

:::

::: {.pf-step #s1-5}

Every zero $z_0$ of $P'$ satisfies
\[
\boxed{
\operatorname{Re}z_0<\sigma
}.
\]


::: pf-proof

If $P(z_0)=0$, apply step [](#s1-1){.pf-ref}. If $P(z_0)\ne0$, step [](#s1-4){.pf-ref} rules out
\[
\operatorname{Re}z_0\ge\sigma.
\]
Thus in all cases $\operatorname{Re}z_0<\sigma$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
