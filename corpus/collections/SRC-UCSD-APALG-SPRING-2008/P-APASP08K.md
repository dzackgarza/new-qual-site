---
schema: qual/card@1
id: P-APASP08K
kind: problem
title: "Generating function for a Diophantine system via partial fractions"
classification:
  areas:
  - applied-algebra
  topics:
  - Combinatorics
  - Generating Functions
  - Gröbner Bases
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The system is solved explicitly (adding and subtracting the two equations), each generating function is obtained from the product formula for absolutely convergent series, and the two readings of the printed word "compositions" are separated into their own steps with the relation between the two answers (a factor x_1x_2x_3x_4, a unit in the formal power series ring) stated. The card does not use the named package as a black box, since the exercise's system is small enough to solve; it records that the rational function obtained is the one such a package returns. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Use the partial fraction package of Guoce Xin to compute the generating function
$$
F_{S_2}(x_1, x_2, x_3, x_4) = \sum_{p \in S_2} x_1^{p_1}\, x_2^{p_2}\, x_3^{p_3}\, x_4^{p_4}
$$
where the sum is over the compositions $p = (p_1, p_2, p_3, p_4)$ that are solutions of the Diophantine system
$$
\begin{cases}
p_1 + p_2 - p_3 - p_4 = 0,\\
p_1 - p_2 + p_3 - p_4 = 0.
\end{cases}
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, and the partial-fraction package is not used as a black box: the Diophantine system is solved directly.

::: pf

::: {.pf-step #system}
The system $p_1+p_2-p_3-p_4=0$, $p_1-p_2+p_3-p_4=0$ is equivalent to $p_1=p_4$ and $p_2=p_3$.

::: pf-proof
Adding the two equations gives $2p_1-2p_4=0$, so $p_1=p_4$; subtracting them gives $2p_2-2p_3=0$, so $p_2=p_3$. Conversely, if $p_1=p_4$ and $p_2=p_3$ then $p_1+p_2-p_3-p_4=p_1+p_2-p_2-p_1=0$ and $p_1-p_2+p_3-p_4=p_1-p_2+p_2-p_1=0$.
:::

:::

::: {.pf-step #nonnegative}
If the parts are allowed to be $0$, the solution set is $S_2=\{(a,b,b,a):a,b\ge0\}$ and
$$
F_{S_2}=\sum_{a,b\ge0}x_1^ax_2^bx_3^bx_4^a=\frac{1}{(1-x_1x_4)(1-x_2x_3)} .
$$

::: pf-proof
By step [](#system){.pf-ref} a solution is exactly a quadruple $(a,b,b,a)$ with $a,b\ge0$. Then
$$
\sum_{a,b\ge0}x_1^ax_4^a\,x_2^bx_3^b=\Bigl(\sum_{a\ge0}(x_1x_4)^a\Bigr)\Bigl(\sum_{b\ge0}(x_2x_3)^b\Bigr)
$$
by the product formula for absolutely convergent series, and each factor is a geometric series summing to $1/(1-x_1x_4)$ and $1/(1-x_2x_3)$ respectively. This is the answer a partial-fraction/partition-analysis package returns for the nonnegative solution set.
:::

:::

::: {.pf-step #positive}
If the printed word "compositions" is read in its classical strictly positive sense, then $a,b\ge1$ and
$$
F_{S_2}=\frac{x_1x_2x_3x_4}{(1-x_1x_4)(1-x_2x_3)} .
$$

::: pf-proof
With $a,b\ge1$ put $a'=a-1$, $b'=b-1$; then $(x_1x_4)^a(x_2x_3)^b=x_1x_2x_3x_4\cdot(x_1x_4)^{a'}(x_2x_3)^{b'}$ with $a',b'\ge0$, so the sum is $x_1x_2x_3x_4$ times the series of step [](#nonnegative){.pf-ref}.
:::

:::

::: {.pf-step}
The Diophantine solution set is exactly $p=(a,b,b,a)$; the only thing the printed statement leaves open is whether the two free parameters are allowed to be $0$, and the generating function differs by the factor $x_1x_2x_3x_4$.

::: pf-proof
Step [](#system){.pf-ref} is the solution set, and steps [](#nonnegative){.pf-ref} and [](#positive){.pf-ref} give the two cases; each formula follows from the other on dividing or multiplying by $x_1x_2x_3x_4$, which is a unit in the ring of formal power series.
:::

:::

:::
:::
