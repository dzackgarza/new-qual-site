---
schema: qual/card@1
id: P-ALGF17B
kind: problem
title: Matrix group presentation $\langle a,b \mid a^4=e,\, a^2=b^2,\, a^{-1}ba=b^{-1}\rangle$
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $G$ be the following subgroup of $2 \times 2$ matrices over the complex numbers:
\[
G = \left\{
\pm\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},\;
\pm\begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix},\;
\pm\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix},\;
\pm\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}
\right\}
\]
(You don't have to show this is a group).
Prove that $G$ has the following presentation
\[
\langle a, b \mid a^4 = e,\; a^2 = b^2,\; a^{-1}ba = b^{-1} \rangle.
\]
:::

::: {.solution}
<1>1. $G$ has $8$ elements as listed.
::: {.proof}
check closure.
:::

<1>2. Put $a=\begin{pmatrix}i&0\\0&-i\end{pmatrix}$, $b=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$.
::: {.proof}
define.
:::

<1>3. $a^4=I$, $a^2=b^2=-I$, $a^{-1}ba=b^{-1}$.
::: {.proof}
compute.
:::

<1>4. So $G$ satisfies relations, and $|G|=8$ implies presentation is $G$.
::: {.proof}
<1>3 and order.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
