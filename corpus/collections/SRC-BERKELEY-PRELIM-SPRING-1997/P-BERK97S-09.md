---
schema: qual/card@1
id: P-BERK97S-09
kind: problem
title: Every ring homomorphism from a full matrix algebra is injective or zero
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $R=M_n(F)$ be the ring of $n\times n$ matrices over a field $F$. If $S$ is a ring and
\[
h:R\to S
\]
is a ring homomorphism, show that $h$ is either injective or zero.
:::

::: {.solution}
Let $E_{ij}$ denote the standard matrix unit with a $1$ in position
$(i,j)$ and zeros elsewhere.

<1>1. Every nonzero two-sided ideal of $R=M_n(F)$ is all of $R$.

::: {.proof}
Let $I\subseteq R$ be a nonzero two-sided ideal and choose
$$
0\neq A=(a_{rs})\in I.
$$
There are indices $p,q$ with $a_{pq}\neq0$. For arbitrary $i,j$,
$$
E_{ip}AE_{qj}=a_{pq}E_{ij}\in I.
$$
Because $a_{pq}$ is invertible in $F$, multiplication by the scalar matrix
$a_{pq}^{-1}I_n$ gives $E_{ij}\in I$. Hence
$$
I_n=E_{11}+\cdots+E_{nn}\in I.
$$
Since an ideal containing the identity is the whole ring, $I=R$.
:::

<1>2. The kernel of $h$ is a two-sided ideal of $R$.

::: {.proof}
The kernel is an additive subgroup. If $A\in\ker h$ and $B\in R$, then
$$
h(BA)=h(B)h(A)=0,
\qquad
h(AB)=h(A)h(B)=0.
$$
Thus $BA,AB\in\ker h$.
:::

<1>3. Therefore
$$
\boxed{h=0\quad\text{or}\quad h\text{ is injective}}.
$$

::: {.proof}
By step <1>2, $\ker h$ is a two-sided ideal of $R$, so step <1>1 gives
$$
\ker h=R
\qquad\text{or}\qquad
\ker h=0.
$$
In the first case $h$ is the zero homomorphism. In the second case $h$ is
injective.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required dichotomy.
:::
:::
