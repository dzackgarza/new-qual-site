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
Add and subtract the two equations:
\[
\begin{aligned}
(p_1+p_2-p_3-p_4)+(p_1-p_2+p_3-p_4)&=2p_1-2p_4=0,\\
(p_1+p_2-p_3-p_4)-(p_1-p_2+p_3-p_4)&=2p_2-2p_3=0.
\end{aligned}
\]
Thus every solution satisfies
\[
p_1=p_4,
\qquad
p_2=p_3.
\]
Conversely, every quadruple with these two equalities satisfies the original system. Hence, under the standard nonnegative-integer convention for partition-analysis generating functions,
\[
S_2=\{(a,b,b,a):a,b\ge0\}.
\]
Therefore
\[
\begin{aligned}
F_{S_2}(x_1,x_2,x_3,x_4)
&=\sum_{a,b\ge0}x_1^a x_2^b x_3^b x_4^a\\
&=\left(\sum_{a\ge0}(x_1x_4)^a\right)
  \left(\sum_{b\ge0}(x_2x_3)^b\right)\\
&=\boxed{\frac{1}{(1-x_1x_4)(1-x_2x_3)}}.
\end{aligned}
\]
This is the rational function that a partial-fraction/partition-analysis package returns.

The printed problem uses the word “compositions” without stating whether zero parts are allowed. If it is instead intended in the classical strictly-positive sense, then $a,b\ge1$, and the corresponding generating function is
\[
\sum_{a,b\ge1}(x_1x_4)^a(x_2x_3)^b
=
\boxed{
\frac{x_1x_2x_3x_4}{(1-x_1x_4)(1-x_2x_3)}
}.
\]
Thus the only ambiguity is the lower bound on the two free parameters; the Diophantine solution set itself is exactly $p=(a,b,b,a)$.
:::
