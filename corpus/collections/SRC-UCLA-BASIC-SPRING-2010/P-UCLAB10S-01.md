---
schema: qual/card@1
id: P-UCLAB10S-01
kind: problem
title: A small perturbation of an orthonormal basis remains independent
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 1. Let $u_1,\ldots,u_n$ be an orthonormal basis of $\RR^n$, and let $y_1,\ldots,y_n\in\RR^n$ satisfy
\[
\sum_i\|y_i\|^2<1.
\]
Prove that $u_1+y_1,\ldots,u_n+y_n$ are linearly independent.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose
\[
\sum_{i=1}^n a_i(u_i+y_i)=0
\]
for some scalars
\[
a_1,\ldots,a_n\in\RR.
\]


::: pf-proof

To prove linear independence, it suffices to show that every such linear relation has all coefficients zero.

:::

:::

::: {.pf-step #s1-2}

The relation in step [](#s1-1){.pf-ref} implies
\[
\sum_{i=1}^n a_i u_i
=
-\sum_{i=1}^n a_i y_i.
\]


::: pf-proof

Move the perturbation sum to the right-hand side.

:::

:::

::: {.pf-step #s1-3}

Since $u_1,\ldots,u_n$ is orthonormal,
\[
\left\|
\sum_{i=1}^n a_i u_i
\right\|^2
=
\sum_{i=1}^n a_i^2.
\]


::: pf-proof

Expand the squared norm:
\[
\left\|
\sum_i a_i u_i
\right\|^2
=
\sum_{i,j}a_ia_j\langle u_i,u_j\rangle.
\]
Orthonormality gives
\[
\langle u_i,u_j\rangle=\delta_{ij},
\]
so only the diagonal terms remain.

:::

:::

::: {.pf-step #s1-4}

By Cauchy--Schwarz,
\[
\left\|
\sum_{i=1}^n a_i y_i
\right\|
\le
\left(
\sum_{i=1}^n a_i^2
\right)^{1/2}
\left(
\sum_{i=1}^n\|y_i\|^2
\right)^{1/2}.
\]


::: pf-proof

Using the triangle inequality,
\[
\left\|
\sum_i a_i y_i
\right\|
\le
\sum_i|a_i|\,\|y_i\|.
\]
Apply the scalar Cauchy--Schwarz inequality to the sequences
\[
(|a_i|)
\quad\text{and}\quad
(\|y_i\|).
\]

:::

:::

::: {.pf-step #s1-5}

Let
\[
A=
\left(
\sum_{i=1}^n a_i^2
\right)^{1/2}
\]
and
\[
\eta=
\left(
\sum_{i=1}^n\|y_i\|^2
\right)^{1/2}.
\]
Then
\[
A\le A\eta.
\]


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref},
\[
A
=
\left\|
\sum_i a_i u_i
\right\|
=
\left\|
\sum_i a_i y_i
\right\|
\le
A\eta.
\]

:::

:::

::: {.pf-step #s1-6}

One has
\[
\eta<1.
\]


::: pf-proof

The hypothesis gives
\[
\sum_i\|y_i\|^2<1.
\]
Taking square roots yields
\[
\eta<1.
\]

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
A=0.
\]


::: pf-proof

If
\[
A>0,
\]
then step [](#s1-5){.pf-ref} allows division by $A$, giving
\[
1\le\eta,
\]
contradicting step [](#s1-6){.pf-ref}.
Hence
\[
A=0.
\]

:::

:::

::: {.pf-step #s1-8}

Thus
\[
a_1=\cdots=a_n=0.
\]


::: pf-proof

By definition,
\[
A^2=\sum_{i=1}^n a_i^2.
\]
Step [](#s1-7){.pf-ref} gives
\[
\sum_i a_i^2=0.
\]
Each term is nonnegative, so every coefficient vanishes.

:::

:::

::: {.pf-step #s1-9}

Therefore
\[
\boxed{u_1+y_1,\ldots,u_n+y_n\text{ are linearly independent}.}
\]


::: pf-proof

Step [](#s1-8){.pf-ref} shows that the only linear relation among these vectors is the trivial one.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required conclusion.

:::

:::

:::
