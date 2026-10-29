---
schema: qual/card@1
id: D-3V3SP
kind: definition
title: Symplectic group $\operatorname{Sp}_{2n}(F)$
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
Let $F$ be a field, let $n\geq 1$, and let
$$
J \coloneqq
\begin{bmatrix}
0 & I_n
\\
-I_n & 0
\end{bmatrix}
\in \GL_{2n}(F).
$$
The \dfn{symplectic group} is
$$
\operatorname{Sp}_{2n}(F) \coloneqq \theset{ A \in \GL_{2n}(F) \st A^tJA = J }.
$$
:::

::: {.remark}
The matrix $J$ is skew-symmetric, $J^t = -J$, so $\operatorname{Sp}_{2n}(F)$ is the group of invertible matrices preserving the alternating bilinear form $\omega(x,y) = x^tJy$ on $F^{2n}$.
Replacing $J$ by the symmetric matrix $\begin{bmatrix} 0 & I_n \\ I_n & 0 \end{bmatrix}$ gives instead the orthogonal group of the symmetric bilinear form $x^t\begin{bmatrix} 0 & I_n \\ I_n & 0 \end{bmatrix}y$.
:::
