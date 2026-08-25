---
schema: qual/card@1
id: P-APAF20D
kind: problem
title: Missing character row for a group of order $168$ and equivariant maps of tensors
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: problem
Here is the character table for a group $G$ of size $168$ with $1$ of its rows missing (rows are characters, the columns are conjugacy classes):
\[
\begin{array}{c|cccccc}
 & \gamma_1 & \gamma_2 & \gamma_3 & \gamma_4 & \gamma_5 & \gamma_6 \\
\hline
\chi_1 & 1 & 1 & 1 & 1 & 1 & 1 \\
\chi_2 & 3 & 0 & \dfrac{-1-\sqrt{-7}}{2} & \dfrac{-1+\sqrt{-7}}{2} & -1 & 1 \\
\chi_3 & 3 & 0 & \dfrac{-1+\sqrt{-7}}{2} & \dfrac{-1-\sqrt{-7}}{2} & -1 & 1 \\
\chi_4 & 7 & 1 & 0 & 0 & -1 & -1 \\
\chi_5 & 8 & -1 & 1 & 1 & 0 & 0 \\
\chi_6 & ? & ? & -1 & ? & ? & 0
\end{array}
\]
The sizes of the conjugacy classes are $|\gamma_1|=1$, $|\gamma_2|=56$, $|\gamma_3|=|\gamma_4|=24$, $|\gamma_5|=21$, $|\gamma_6|=42$.

(a) Fill in the correct values for $\chi_6$.

(b) For $1\le i\le 6$, let $V_i$ be a representation of $G$ whose character is $\chi_i$.
Compute the dimension of the space of $G$-equivariant linear maps from $V_2\otimes V_5$ to $V_3\otimes V_5$.
:::
