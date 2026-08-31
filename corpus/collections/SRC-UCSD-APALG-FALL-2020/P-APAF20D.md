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

::: {.solution}
**Goal.** (a) Fill in the missing row $\chi_6$. (b) Compute $\dim \operatorname{Hom}_G(V_2 \otimes V_5, V_3 \otimes V_5)$.

<1>1. (a) Determine $\chi_6$.
<2>1. $\chi_6(\gamma_1) = 6$.
::: {.proof}
the sum of squares of the degrees is $|G| = 168$; $1^2 + 3^2 + 3^2 + 7^2 + 8^2 = 132$, so $\chi_6(\gamma_1)^2 = 168 - 132 = 36$, giving $\chi_6(\gamma_1) = 6$.
:::
<2>2. $\chi_6(\gamma_2) = 0$.
::: {.proof}
column orthogonality for $\gamma_2$ (centralizer order $3$): $\sum_i |\chi_i(\gamma_2)|^2 = 3$; the known values give $1^2 + 0^2 + 0^2 + 1^2 + (-1)^2 = 3$, so $|\chi_6(\gamma_2)|^2 = 0$.
:::
<2>3. $\chi_6(\gamma_4) = \pm 1$.
::: {.proof}
column orthogonality for $\gamma_4$ (centralizer order $7$): $\sum_i |\chi_i(\gamma_4)|^2 = 7$; the known values give $1^2 + |\frac{-1+\sqrt{-7}}2|^2 + |\frac{-1-\sqrt{-7}}2|^2 + 0^2 + 1^2 = 1 + 2 + 2 + 0 + 1 = 6$, so $|\chi_6(\gamma_4)|^2 = 1$, giving $\chi_6(\gamma_4) = \pm 1$.
:::
<2>4. $\chi_6(\gamma_5) = 2$.
::: {.proof}
column orthogonality for $\gamma_5$ (centralizer order $8$): $\sum_i |\chi_i(\gamma_5)|^2 = 8$; known values give $1 + 1 + 1 + 1 + 0 = 4$, so $|\chi_6(\gamma_5)|^2 = 4$, giving $\chi_6(\gamma_5) = \pm 2$.
:::
<2>5. Row orthogonality with $\chi_1$ pins down the signs: $\chi_6(\gamma_4) = -1$ and $\chi_6(\gamma_5) = 2$.
::: {.proof}
$\langle \chi_6, \chi_1\rangle = 0$ gives $6 + 24(-1) + 24\chi_6(\gamma_4) + 21\chi_6(\gamma_5) = 0$, i.e. $24\chi_6(\gamma_4) + 21\chi_6(\gamma_5) = 18$; the only solution with $\chi_6(\gamma_4) = \pm 1$, $\chi_6(\gamma_5) = \pm 2$ is $\chi_6(\gamma_4) = -1$, $\chi_6(\gamma_5) = 2$.
:::
<2>6. Hence $\chi_6 = (6, 0, -1, -1, 2, 0)$.
::: {.proof}
collect <1>2.1–<1>2.5.
:::

<1>2. (b) $\dim \operatorname{Hom}_G(V_2 \otimes V_5, V_3 \otimes V_5) = \langle \chi_2 \chi_5, \chi_3 \chi_5\rangle$.
<2>1. $\dim \operatorname{Hom}_G(V_2 \otimes V_5, V_3 \otimes V_5) = \langle \chi_{V_2 \otimes V_5}, \chi_{V_3 \otimes V_5}\rangle = \langle \chi_2 \chi_5, \chi_3 \chi_5\rangle$.
::: {.proof}
the character of a tensor product is the product of characters, and the dimension of $\operatorname{Hom}_G$ is the inner product of characters.
:::
<2>2. Compute $\langle \chi_2 \chi_5, \chi_3 \chi_5\rangle = \frac{1}{168}\sum_j |\gamma_j| \chi_2(\gamma_j)\chi_5(\gamma_j)\overline{\chi_3(\gamma_j)\chi_5(\gamma_j)}$.
::: {.proof}
definition of the inner product.
:::
<2>3. The value is $3$.
::: {.proof}
Compute the product characters: $\chi_2\chi_5 = (24, 0, \frac{-1-\sqrt{-7}}{2}, \frac{-1+\sqrt{-7}}{2}, 0, 0)$ and $\chi_3\chi_5 = (24, 0, \frac{-1+\sqrt{-7}}{2}, \frac{-1-\sqrt{-7}}{2}, 0, 0)$.
Only the classes $\gamma_1, \gamma_3, \gamma_4$ contribute (the others have a zero factor), so
\[
\langle \chi_2\chi_5, \chi_3\chi_5\rangle
= \frac{1}{168}\left[1\cdot 24\cdot 24 + 24\cdot \frac{-1-\sqrt{-7}}{2}\cdot \frac{-1-\sqrt{-7}}{2} + 24\cdot \frac{-1+\sqrt{-7}}{2}\cdot \frac{-1+\sqrt{-7}}{2}\right].
\]
Here $\overline{\frac{-1+\sqrt{-7}}{2}} = \frac{-1-\sqrt{-7}}{2}$, and
\[
\left(\frac{-1-\sqrt{-7}}{2}\right)^2 = \frac{-3+\sqrt{-7}}{2}, \qquad
\left(\frac{-1+\sqrt{-7}}{2}\right)^2 = \frac{-3-\sqrt{-7}}{2}.
\]
Therefore
\[
\langle \chi_2\chi_5, \chi_3\chi_5\rangle
= \frac{1}{168}\left[576 + 24\cdot\frac{-3+\sqrt{-7}}{2} + 24\cdot\frac{-3-\sqrt{-7}}{2}\right]
= \frac{1}{168}\left[576 - 36 - 36\right]
= \frac{504}{168} = 3.
\]
:::

<1>3. Q.E.D.
::: {.proof}
<1>2.6 gives $\chi_6 = (6,0,-1,-1,2,0)$; <1>2.3 gives $\dim \operatorname{Hom}_G(V_2 \otimes V_5, V_3 \otimes V_5) = 3$.
:::
:::
