---
schema: qual/card@1
id: P-BKF85-6
kind: problem
title: Extreme eigenvalue bounds for a tridiagonal matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md.
---

::: {.problem}
Let $k\in\mathbb R$, let $n\ge2$, and let $A=(a_{ij})$ be the $n\times n$ matrix with
\[
a_{ii}=k,
\qquad
a_{i,i+1}=a_{i+1,i}=1,
\]
and all other entries equal to $0$.

Let $\lambda_{\min}$ and $\lambda_{\max}$ be the smallest and largest eigenvalues of $A$.
Show that
\[
\lambda_{\min}\le k-1
\qquad\text{and}\qquad
\lambda_{\max}\ge k+1.
\]
:::

::: {.solution}
<1>1. For every nonzero vector $v\in\RR^n$,
$$
\lambda_{\min}
\leq
\frac{v^TAv}{v^Tv}
\leq
\lambda_{\max}.
$$

::: {.proof}
The matrix $A$ is real symmetric, so by the spectral theorem it has an orthonormal eigenbasis
$$
u_1,\ldots,u_n
$$
with corresponding real eigenvalues
$$
\lambda_1,\ldots,\lambda_n
$$
lying between $\lambda_{\min}$ and $\lambda_{\max}$. Write
$$
v=\sum_{j=1}^n c_ju_j.
$$
Then
$$
\frac{v^TAv}{v^Tv}
=
\frac{\sum_j\lambda_j c_j^2}{\sum_jc_j^2},
$$
which is a weighted average of the eigenvalues. Hence it lies between their minimum and maximum.
:::

<1>2. One has
$$
\lambda_{\min}\leq k-1.
$$

::: {.proof}
Take
$$
v=e_1-e_2.
$$
Only the upper-left $2\times2$ block of $A$ contributes to $v^TAv$, so
$$
v^TAv
=
\begin{pmatrix}1&-1\end{pmatrix}
\begin{pmatrix}k&1\\1&k\end{pmatrix}
\begin{pmatrix}1\\-1\end{pmatrix}
=
2k-2.
$$
Since $v^Tv=2$,
$$
\frac{v^TAv}{v^Tv}=k-1.
$$
Step <1>1 therefore gives $\lambda_{\min}\leq k-1$.
:::

<1>3. One has
$$
\lambda_{\max}\geq k+1.
$$

::: {.proof}
Take
$$
w=e_1+e_2.
$$
Again using the upper-left $2\times2$ block,
$$
w^TAw
=
\begin{pmatrix}1&1\end{pmatrix}
\begin{pmatrix}k&1\\1&k\end{pmatrix}
\begin{pmatrix}1\\1\end{pmatrix}
=
2k+2.
$$
Since $w^Tw=2$,
$$
\frac{w^TAw}{w^Tw}=k+1.
$$
Step <1>1 therefore gives $\lambda_{\max}\geq k+1$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 are the required inequalities.
:::
:::
