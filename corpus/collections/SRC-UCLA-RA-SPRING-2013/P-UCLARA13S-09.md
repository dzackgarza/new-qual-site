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
\{z\in\mathbb C:\operatorname{Re}z<\sigma\}.
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

<1>1. If $z_0$ satisfies
\[
P'(z_0)=0
\qquad\text{and}\qquad
P(z_0)=0,
\]
then
\[
\operatorname{Re}z_0<\sigma.
\]

::: {.proof}
The condition $P(z_0)=0$ means that $z_0=a_j$ for some zero $a_j$ of $P$. Every such zero lies in the stated half-plane by hypothesis.
:::

<1>2. For every $z$ with $P(z)\ne0$,
\[
\frac{P'(z)}{P(z)}
=
\sum_{j=1}^n\frac1{z-a_j}.
\]

::: {.proof}
Differentiate the product representation:
\[
P'(z)
=
P(z)
\sum_{j=1}^n\frac1{z-a_j}.
\]
Division by the nonzero number $P(z)$ gives the identity.
:::

<1>3. If
\[
\operatorname{Re}z\ge\sigma,
\]
then for every $j$,
\[
\operatorname{Re}\frac1{z-a_j}>0.
\]

::: {.proof}
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

<1>4. If $P(z)\ne0$ and
\[
\operatorname{Re}z\ge\sigma,
\]
then
\[
P'(z)\ne0.
\]

::: {.proof}
By steps <1>2 and <1>3,
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

<1>5. Every zero $z_0$ of $P'$ satisfies
\[
\boxed{
\operatorname{Re}z_0<\sigma
}.
\]

::: {.proof}
If $P(z_0)=0$, apply step <1>1. If $P(z_0)\ne0$, step <1>4 rules out
\[
\operatorname{Re}z_0\ge\sigma.
\]
Thus in all cases $\operatorname{Re}z_0<\sigma$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
