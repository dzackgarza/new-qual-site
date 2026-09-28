---
schema: qual/card@1
id: D-HJR7M
kind: definition
title: Companion matrix
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Matrices
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field and let $p(x) = a_0 + a_1 x + \cdots + a_{n-1} x^{n-1} + x^n\in k[x]$ be a monic polynomial of degree $n\geq 1$.
The \dfn{companion matrix} of $p$ is
$$
C_p \coloneqq
\begin{bmatrix}
0 & 0 & \cdots & 0 &-a_0 \\
1 & 0 & \cdots & 0 & -a_1 \\
0 & 1 & \cdots & 0 & -a_2 \\
\vdots & & \ddots & & \vdots \\
0 & 0 & \cdots & 1 & -a_{n-1}
\end{bmatrix}
\in\Mat_{n\times n}(k).
$$
:::
