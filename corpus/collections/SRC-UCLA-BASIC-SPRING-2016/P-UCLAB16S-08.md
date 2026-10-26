---
schema: qual/card@1
id: P-UCLAB16S-08
kind: problem
title: Invertibility of a small perturbation of the identity
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $A=(a_{ij})$ be a real $2\times2$ matrix such that
\[
a_{11}^2+a_{12}^2+a_{21}^2+a_{22}^2<\frac1{10}.
\]
Prove that $I+A$ is invertible.
:::

Let
\[
\|A\|_F
=
\left(
a_{11}^2+a_{12}^2+a_{21}^2+a_{22}^2
\right)^{1/2}
\]
be the Frobenius norm.

::: pf

::: pf-step

The hypothesis gives
\[
\|A\|_F<\frac1{\sqrt{10}}<1.
\]


::: pf-proof

Take square roots of
\[
a_{11}^2+a_{12}^2+a_{21}^2+a_{22}^2
<
\frac1{10}.
\]

:::

:::

::: pf-step

For every
\[
x\in\mathbb R^2,
\]
one has
\[
\|Ax\|_2
\le
\|A\|_F\|x\|_2.
\]


::: pf-proof

Write
\[
x=
\begin{pmatrix}
x_1\\x_2
\end{pmatrix}.
\]
For each row $i$, Cauchy--Schwarz gives
\[
\left(
a_{i1}x_1+a_{i2}x_2
\right)^2
\le
\left(
a_{i1}^2+a_{i2}^2
\right)
\left(
x_1^2+x_2^2
\right).
\]
Sum over
\[
i=1,2.
\]
Then
\[
\|Ax\|_2^2
\le
\|A\|_F^2\|x\|_2^2.
\]
Take square roots.

:::

:::

::: pf-step

Suppose
\[
(I+A)x=0.
\]
Then
\[
x=-Ax.
\]


::: pf-proof

Rearrange the equation
\[
x+Ax=0.
\]

:::

:::

::: pf-step

If
\[
x\ne0,
\]
then steps <1>1--<1>3 give a contradiction.


::: pf-proof

By step <1>3,
\[
\|x\|_2
=
\|Ax\|_2.
\]
Step <1>2 gives
\[
\|Ax\|_2
\le
\|A\|_F\|x\|_2.
\]
Thus
\[
\|x\|_2
\le
\|A\|_F\|x\|_2.
\]
If
\[
x\ne0,
\]
divide by
\[
\|x\|_2>0
\]
to obtain
\[
1\le\|A\|_F,
\]
contradicting step <1>1.

:::

:::

::: pf-step

Therefore
\[
\ker(I+A)=\{0\}.
\]


::: pf-proof

Step <1>4 rules out every nonzero vector in the kernel.

:::

:::

::: pf-step

Since $I+A$ is a linear map
\[
\mathbb R^2\to\mathbb R^2,
\]
trivial kernel implies invertibility.


::: pf-proof

For an endomorphism of a finite-dimensional vector space, injectivity is equivalent to surjectivity.
Step <1>5 gives injectivity.
Therefore
\[
\boxed{I+A\text{ is invertible}.}
\]

:::

:::

::: pf-qed

Step <1>6 is the required conclusion.

:::

:::
