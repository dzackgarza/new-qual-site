---
schema: qual/card@1
id: P-UCLAB07F-10
kind: problem
title: Dual bases and eigenvectors of the adjoint
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Suppose $\{v_j\}_{j=1}^n$ is a basis of $\mathbb C^n$.

(a) Show that there is a basis $\{w_j\}_{j=1}^n$ such that $(w_j,v_k)=\delta_{jk}$ for the standard Hermitian inner product.

(b) If the $v_j$ are eigenvectors of a linear transformation $T$ of $\mathbb C^n$, show that the $w_j$ are eigenvectors of the adjoint $T^*$.
:::

::: {.solution}
Let
\[
V=
\begin{pmatrix}
|&&|\\
v_1&\cdots&v_n\\
|&&|
\end{pmatrix}.
\]
Since the $v_j$ form a basis, $V$ is invertible.

<1>1. Define
\[
W=(V^{-1})^*,
\]
and let $w_1,\ldots,w_n$ be the columns of $W$.
Then
\[
(w_j,v_k)=\delta_{jk}.
\]

::: {.proof}
With the convention in the problem,
\[
(u,v)=u^*v.
\]
Since
\[
W^*V
=
\bigl((V^{-1})^*\bigr)^*V
=
V^{-1}V
=I,
\]
the $(j,k)$ entry of $W^*V$ is
\[
w_j^*v_k
=(w_j,v_k),
\]
and this entry equals $\delta_{jk}$.
:::

<1>2. The vectors $w_1,\ldots,w_n$ form a basis of $\mathbb C^n$.

::: {.proof}
The matrix
\[
W=(V^{-1})^*
\]
is invertible because $V^{-1}$ is invertible. Hence its columns form a basis.
:::

<1>3. Suppose
\[
Tv_k=\lambda_kv_k
\]
for $k=1,\ldots,n$. Then
\[
(T^*w_j,v_k)=\lambda_k\delta_{jk}.
\]

::: {.proof}
For the standard Hermitian inner product,
\[
(T^*u,v)=(u,Tv).
\]
Therefore
\[
\begin{aligned}
(T^*w_j,v_k)
&=
(w_j,Tv_k)\\
&=
(w_j,\lambda_kv_k)\\
&=
\lambda_k(w_j,v_k)\\
&=
\lambda_k\delta_{jk},
\end{aligned}
\]
using linearity in the second argument and step <1>1.
:::

<1>4. For every $j$,
\[
\boxed{T^*w_j=\overline{\lambda_j}\,w_j}.
\]

::: {.proof}
For every $k$, step <1>3 gives
\[
(T^*w_j,v_k)=\lambda_j\delta_{jk}.
\]
Because the inner product is conjugate-linear in the first argument,
\[
(\overline{\lambda_j}w_j,v_k)
=
\lambda_j(w_j,v_k)
=
\lambda_j\delta_{jk}.
\]
Hence
\[
(T^*w_j-\overline{\lambda_j}w_j,v_k)=0
\]
for every $k$.
Since $v_1,\ldots,v_n$ span $\mathbb C^n$, the vector
\[
T^*w_j-\overline{\lambda_j}w_j
\]
is orthogonal to every vector in $\mathbb C^n$, so it is zero.
:::

<1>5. Thus each $w_j$ is an eigenvector of $T^*$.

::: {.proof}
By step <1>2, each $w_j$ is nonzero. Step <1>4 shows that it is an eigenvector of $T^*$ with eigenvalue $\overline{\lambda_j}$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove part (a), and steps <1>3--<1>5 prove part (b).
:::
:::
