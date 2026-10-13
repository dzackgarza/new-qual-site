---
schema: qual/card@1
id: P-UCLAB11F-09
kind: problem
title: Approximate eigenvector for a self-adjoint operator
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
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 9. Let $V$ be a finite-dimensional inner-product space and let $L:V\to V$ be self-adjoint.
Let $\mu\in\mathbb R$ and $\varepsilon>0$.
Suppose there is a unit vector $x\in V$ such that
\[
\|Lx-\mu x\|\le\varepsilon.
\]
Prove that $L$ has an eigenvalue $\lambda$ such that
\[
|\lambda-\mu|\le\varepsilon.
\]
:::

::: {.solution}
<1>1. Since $L$ is self-adjoint on a finite-dimensional inner-product space, there is an orthonormal basis
\[
v_1,\ldots,v_n
\]
of eigenvectors of $L$.

::: {.proof}
This is the finite-dimensional spectral theorem for self-adjoint operators. Write
\[
Lv_j=\lambda_jv_j,
\qquad
\lambda_j\in\mathbb R.
\]
:::

<1>2. Write the unit vector $x$ as
\[
x=\sum_{j=1}^n c_jv_j.
\]
Then
\[
\sum_{j=1}^n|c_j|^2=1.
\]

::: {.proof}
The expansion exists because the $v_j$ form a basis. Since they are orthonormal,
\[
\|x\|^2
=
\sum_{j=1}^n|c_j|^2.
\]
The hypothesis $\|x\|=1$ gives the displayed identity.
:::

<1>3. One has
\[
\|Lx-\mu x\|^2
=
\sum_{j=1}^n
|\lambda_j-\mu|^2|c_j|^2.
\]

::: {.proof}
Using the eigenvector equations,
\[
Lx-\mu x
=
\sum_{j=1}^n
c_j(\lambda_j-\mu)v_j.
\]
Taking the squared norm in the orthonormal basis gives the stated sum.
:::

<1>4. At least one eigenvalue $\lambda_j$ satisfies
\[
|\lambda_j-\mu|\le\varepsilon.
\]

::: {.proof}
Suppose instead that
\[
|\lambda_j-\mu|>\varepsilon
\]
for every $j$. Then by step <1>3 and step <1>2,
\[
\begin{aligned}
\|Lx-\mu x\|^2
&=
\sum_j|\lambda_j-\mu|^2|c_j|^2\\
&>
\varepsilon^2\sum_j|c_j|^2\\
&=
\varepsilon^2,
\end{aligned}
\]
so
\[
\|Lx-\mu x\|>\varepsilon,
\]
contradicting the hypothesis.
:::

<1>5. Therefore $L$ has an eigenvalue $\lambda$ with
\[
\boxed{|\lambda-\mu|\le\varepsilon}.
\]

::: {.proof}
Take $\lambda=\lambda_j$ from step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
