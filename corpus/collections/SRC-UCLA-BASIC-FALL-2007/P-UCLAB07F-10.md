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
Suppose $\{v_j\}_{j=1}^n$ is a basis of $\CC^n$.

(a) Show that there is a basis $\{w_j\}_{j=1}^n$ such that $(w_j,v_k)=\delta_{jk}$ for the standard Hermitian inner product.

(b) If the $v_j$ are eigenvectors of a linear transformation $T$ of $\CC^n$, show that the $w_j$ are eigenvectors of the adjoint $T^*$.
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

::: pf

::: {.pf-step #s1-1}

Define
\[
W=(V^{-1})^*,
\]
and let $w_1,\ldots,w_n$ be the columns of $W$.
Then
\[
(w_j,v_k)=\delta_{jk}.
\]


::: pf-proof

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

:::

::: {.pf-step #s1-2}

The vectors $w_1,\ldots,w_n$ form a basis of $\CC^n$.


::: pf-proof

The matrix
\[
W=(V^{-1})^*
\]
is invertible because $V^{-1}$ is invertible. Hence its columns form a basis.

:::

:::

::: {.pf-step #s1-3}

Suppose
\[
Tv_k=\lambda_kv_k
\]
for $k=1,\ldots,n$. Then
\[
(T^*w_j,v_k)=\lambda_k\delta_{jk}.
\]


::: pf-proof

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
using linearity in the second argument and step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

For every $j$,
\[
\boxed{T^*w_j=\overline{\lambda_j}\,w_j}.
\]


::: pf-proof

For every $k$, step [](#s1-3){.pf-ref} gives
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
Since $v_1,\ldots,v_n$ span $\CC^n$, the vector
\[
T^*w_j-\overline{\lambda_j}w_j
\]
is orthogonal to every vector in $\CC^n$, so it is zero.

:::

:::

::: {.pf-step #s1-5}

Thus each $w_j$ is an eigenvector of $T^*$.


::: pf-proof

By step [](#s1-2){.pf-ref}, each $w_j$ is nonzero. Step [](#s1-4){.pf-ref} shows that it is an eigenvector of $T^*$ with eigenvalue $\overline{\lambda_j}$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} prove part (a), and steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} prove part (b).

:::

:::

:::
