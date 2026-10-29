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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Here is the character table for a group $G$ of size $168$ with $1$ of its rows missing (rows are characters, the columns are conjugacy classes):
$$
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
$$
The sizes of the conjugacy classes are $|\gamma_1|=1$, $|\gamma_2|=56$, $|\gamma_3|=|\gamma_4|=24$, $|\gamma_5|=21$, $|\gamma_6|=42$.

(a) Fill in the correct values for $\chi_6$.

(b) For $1\le i\le 6$, let $V_i$ be a representation of $G$ whose character is $\chi_i$.
Compute the dimension of the space of $G$-equivariant linear maps from $V_2\otimes V_5$ to $V_3\otimes V_5$.
:::

::: {.solution}
Write $\alpha\coloneqq\frac{-1+\sqrt{-7}}{2}$, so $\bar\alpha=\frac{-1-\sqrt{-7}}{2}$, $\abs{\alpha}^2=2$ and $\alpha^2=\frac{-3-\sqrt{-7}}{2}$. The centralizer orders $168/\abs{\gamma_j}$ are $168,3,7,7,8,4$.

::: pf

::: {.pf-step #magnitudes}

$\chi_6(\gamma_1)=6$, $\chi_6(\gamma_2)=0$, $\abs{\chi_6(\gamma_4)}=1$ and $\abs{\chi_6(\gamma_5)}=2$.

::: pf-proof

The squared degrees sum to $168$, and $1+9+9+49+64=132$, so $\chi_6(\gamma_1)^2=36$. Column orthogonality gives $\sum_i\abs{\chi_i(\gamma_j)}^2=\abs{C_G(\gamma_j)}$. For $\gamma_2$ the known entries give $1+0+0+1+1=3$, so $\chi_6(\gamma_2)=0$. For $\gamma_4$ they give $1+2+2+0+1=6$, so $\abs{\chi_6(\gamma_4)}^2=1$. For $\gamma_5$ they give $1+1+1+1+0=4$, so $\abs{\chi_6(\gamma_5)}^2=4$.

:::

:::

::: {.pf-step #chi6}

(a) $\boxed{\chi_6=(6,0,-1,-1,2,0)}$.

::: pf-proof

$\chi_6$ is the only irreducible character of degree $6$, so it equals its complex conjugate and is real-valued. With step [](#magnitudes){.pf-ref}, $\chi_6(\gamma_4)\in\{\pm1\}$ and $\chi_6(\gamma_5)\in\{\pm2\}$. Orthogonality with $\chi_1$ gives
$$
6+56\cdot0+24(-1)+24\chi_6(\gamma_4)+21\chi_6(\gamma_5)+42\cdot0=0,
$$
that is, $24\chi_6(\gamma_4)+21\chi_6(\gamma_5)=18$. Of the four sign choices only $\chi_6(\gamma_4)=-1$, $\chi_6(\gamma_5)=2$ satisfies it.

:::

:::

::: pf-step

(b) $\dim\operatorname{Hom}_G(V_2\otimes V_5,V_3\otimes V_5)=\boxed{3}$.

::: pf-proof

The dimension is $\langle\chi_2\chi_5,\chi_3\chi_5\rangle$. The products vanish on $\gamma_2,\gamma_5,\gamma_6$, and
$$
\chi_2\chi_5=(24,0,\bar\alpha,\alpha,0,0),\qquad \chi_3\chi_5=(24,0,\alpha,\bar\alpha,0,0).
$$
Hence
$$
\langle\chi_2\chi_5,\chi_3\chi_5\rangle=\frac1{168}\bigl[24^2+24\bar\alpha^2+24\alpha^2\bigr]=\frac1{168}\bigl[576+24(-3)\bigr]=\frac{504}{168}=3,
$$
because $\alpha^2+\bar\alpha^2=2\operatorname{Re}\alpha^2=-3$.

:::

:::

:::
:::
