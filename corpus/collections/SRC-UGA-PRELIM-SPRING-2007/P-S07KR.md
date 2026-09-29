---
schema: qual/card@1
id: P-S07KR
kind: problem
title: $\dim\ker A$ and $\dim\operatorname{im} A$ for a given $3\times 3$ matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Maps
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $A = \begin{bmatrix} 1 & -1 & 2 \\ -1 & 2 & -5 \\ 2 & -1 & 1 \end{bmatrix} \in M_3(\mathbb{R})$, and let $T_A: \mathbb{R}^3 \to \mathbb{R}^3$ be the linear transformation $T_A(\vec{x}) = A\vec{x}$.
Find $\dim_{\mathbb{R}}(\ker(A))$, and use this to determine $\dim_{\mathbb{R}}(\operatorname{im}(A))$.
:::

::: {.solution}

::: pf

::: pf-step

Row reduction gives
\[
\begin{pmatrix}
1&-1&2\\
-1&2&-5\\
2&-1&1
\end{pmatrix}
\sim
\begin{pmatrix}
1&-1&2\\
0&1&-3\\
0&1&-3
\end{pmatrix}
\sim
\begin{pmatrix}
1&-1&2\\
0&1&-3\\
0&0&0
\end{pmatrix}.
\]

::: pf-proof

Use $R_2\leftarrow R_2+R_1$, $R_3\leftarrow R_3-2R_1$, and then $R_3\leftarrow R_3-R_2$.

:::

:::

::: {.pf-step #s2}

The kernel is one-dimensional:
\[
\ker A=\operatorname{span}\left\{\begin{pmatrix}1\\3\\1\end{pmatrix}\right\}.
\]

::: pf-proof

The reduced equations are
\[
y-3z=0,
\qquad
x-y+2z=0.
\]
Thus $y=3z$ and $x=z$, so every kernel vector is
\[
z(1,3,1)^t.
\]
Hence $\dim\ker A=1$.

:::

:::

::: pf-step

Therefore
\[
\boxed{\dim\ker A=1,
\qquad
\dim\operatorname{im}A=2.}
\]

::: pf-proof

The rank--nullity theorem for $T_A:\mathbb R^3\to\mathbb R^3$ gives
\[
\dim\ker A+\dim\operatorname{im}A=3.
\]
Using step [](#s2){.pf-ref} yields $1+\dim\operatorname{im}A=3$.

:::

:::

:::

:::
