---
schema: qual/card@1
id: D-3V3SP
kind: definition
title: Symplectic group $\operatorname{Sp}_{2n}(\CC)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Bilinear Forms
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$, and let
$$
J \coloneqq
\begin{bmatrix}
0 & I_n
\\
-I_n & 0
\end{bmatrix}
\in \GL_{2n}(\CC).
$$
The \dfn{symplectic group} is
$$
\operatorname{Sp}_{2n}(\CC) \coloneqq \theset{ A \in \GL_{2n}(\CC) \st A^tJA = J }.
$$
:::

::: {.remark}
The matrix $J$ is skew-symmetric, $J^t = -J$, so $\operatorname{Sp}_{2n}(\CC)$ is the group of invertible matrices preserving the alternating bilinear form $\omega(x,y) = x^tJy$ on $\CC^{2n}$.
Replacing $J$ by the symmetric matrix $\begin{bmatrix} 0 & I_n \\ I_n & 0 \end{bmatrix}$ gives instead the orthogonal group of the symmetric bilinear form $x^t\begin{bmatrix} 0 & I_n \\ I_n & 0 \end{bmatrix}y$.
:::
