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
$$
a_{11}^2+a_{12}^2+a_{21}^2+a_{22}^2<\frac1{10}.
$$
Prove that $I+A$ is invertible.
:::

::: {.solution}

Let
$$
\|A\|_F
=
\left(
a_{11}^2+a_{12}^2+a_{21}^2+a_{22}^2
\right)^{1/2}
$$
be the Frobenius norm.

::: pf

::: {.pf-step #s1-1}

The hypothesis gives
$$
\|A\|_F<\frac1{\sqrt{10}}<1.
$$


::: pf-proof

Take square roots of
$$
a_{11}^2+a_{12}^2+a_{21}^2+a_{22}^2
<
\frac1{10}.
$$

:::

:::

::: {.pf-step #s1-2}

For every
$$
x\in\RR^2,
$$
one has
$$
\|Ax\|_2
\le
\|A\|_F\|x\|_2.
$$


::: pf-proof

Write
$$
x=
\begin{pmatrix}
x_1\\x_2
\end{pmatrix}.
$$
For each row $i$, Cauchy--Schwarz gives
$$
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
$$
Sum over
$$
i=1,2.
$$
Then
$$
\|Ax\|_2^2
\le
\|A\|_F^2\|x\|_2^2.
$$
Take square roots.

:::

:::

::: {.pf-step #s1-3}

Suppose
$$
(I+A)x=0.
$$
Then
$$
x=-Ax.
$$


::: pf-proof

Rearrange the equation
$$
x+Ax=0.
$$

:::

:::

::: {.pf-step #s1-4}

If
$$
x\ne0,
$$
then steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give a contradiction.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\|x\|_2
=
\|Ax\|_2.
$$
Step [](#s1-2){.pf-ref} gives
$$
\|Ax\|_2
\le
\|A\|_F\|x\|_2.
$$
Thus
$$
\|x\|_2
\le
\|A\|_F\|x\|_2.
$$
If
$$
x\ne0,
$$
divide by
$$
\|x\|_2>0
$$
to obtain
$$
1\le\|A\|_F,
$$
contradicting step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\ker(I+A)=\{0\}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} rules out every nonzero vector in the kernel.

:::

:::

::: {.pf-step #s1-6}

Since $I+A$ is a linear map
$$
\RR^2\to\RR^2,
$$
trivial kernel implies invertibility.


::: pf-proof

For an endomorphism of a finite-dimensional vector space, injectivity is equivalent to surjectivity.
Step [](#s1-5){.pf-ref} gives injectivity.
Therefore
$$
\boxed{I+A\text{ is invertible}.}
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
