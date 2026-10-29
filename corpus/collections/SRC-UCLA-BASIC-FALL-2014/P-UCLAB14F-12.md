---
schema: qual/card@1
id: P-UCLAB14F-12
kind: problem
title: Positive definiteness of the Hilbert matrix
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 12. Let $A=(a_{ij})_{1\leq i,j\leq n}$, where
$$
a_{ij}=\frac1{i+j-1}.
$$
Prove that $A$ is positive definite.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $1\le i,j\le n$,
$$
a_{ij}
=
\int_0^1 x^{i+j-2}\,dx.
$$


::: pf-proof

Since
$$
i+j-2\ge0,
$$
one has
$$
\int_0^1x^{i+j-2}\,dx
=
\left[
\frac{x^{i+j-1}}{i+j-1}
\right]_0^1
=
\frac1{i+j-1}.
$$

:::

:::

::: {.pf-step #s1-2}

Let
$$
c=
\begin{pmatrix}
c_1\\
\vdots\\
c_n
\end{pmatrix}
\in\RR^n.
$$
Then
$$
c^tAc
=
\int_0^1
\left(
\sum_{i=1}^n c_i x^{i-1}
\right)^2
\,dx.
$$


::: pf-proof

Using step [](#s1-1){.pf-ref},
$$
\begin{aligned}
c^tAc
&=
\sum_{i,j=1}^n c_i a_{ij}c_j\\
&=
\sum_{i,j=1}^n
c_ic_j
\int_0^1x^{i+j-2}\,dx\\
&=
\int_0^1
\sum_{i,j=1}^n
c_ic_jx^{i-1}x^{j-1}
\,dx\\
&=
\int_0^1
\left(
\sum_{i=1}^n c_ix^{i-1}
\right)^2
\,dx.
\end{aligned}
$$
The interchange of finite sums and the integral is immediate.

:::

:::

::: {.pf-step #s1-3}

If $c\ne0$, then the polynomial
$$
p_c(x)=\sum_{i=1}^n c_i x^{i-1}
$$
is not identically zero.


::: pf-proof

If $p_c$ were the zero polynomial, all of its coefficients
$$
c_1,\ldots,c_n
$$
would vanish.
That would imply $c=0$, contrary to hypothesis.

:::

:::

::: {.pf-step #s1-4}

If $c\ne0$, then
$$
\int_0^1 p_c(x)^2\,dx>0.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, the polynomial $p_c$ is nonzero.
A nonzero polynomial has only finitely many roots.
Hence there is some
$$
x_0\in[0,1]
$$
with
$$
p_c(x_0)\ne0.
$$
By continuity, there is a nontrivial interval around $x_0$ on which
$$
|p_c(x)|\ge\eta>0
$$
for some $\eta$.
Therefore
$$
\int_0^1p_c(x)^2\,dx>0.
$$

:::

:::

::: {.pf-step #s1-5}

For every nonzero $c\in\RR^n$,
$$
\boxed{c^tAc>0}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{A\text{ is positive definite}}.
$$


::: pf-proof

The defining condition for positive definiteness of a real symmetric matrix is that
$$
c^tAc>0
$$
for every nonzero vector $c$.
Step [](#s1-5){.pf-ref} verifies this condition.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
