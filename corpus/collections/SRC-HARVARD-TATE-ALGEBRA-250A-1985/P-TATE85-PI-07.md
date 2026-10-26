---
schema: qual/card@1
id: P-TATE85-PI-07
kind: problem
title: The unique prime ideal of $B/M^n$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
(7) Let M be a maximal ideal in a ring B and let$A = B / M ^ { n }$for some integer$n > 0$Show that the only prime ideal of A is$M / M ^ { n }$

Examples:$A = \mathbb { Z } / 1 0 2 4 \mathbb { Z } , A = \mathbb { C } [ X ] / X ^ { n } \mathbb { C } [ X ]$
:::

Let
$$
q:B\to A=B/M^n
$$
be the quotient map.

::: pf

::: pf-step

The ideal $M/M^n$ is prime in $A$.


::: pf-proof

One has
$$
A/(M/M^n)\cong B/M.
$$
Since $M$ is maximal, $B/M$ is a field, hence an integral domain. Therefore $M/M^n$ is prime.

:::

:::

::: pf-step

Every prime ideal of $A$ equals $M/M^n$.


::: pf-proof

Let $\mathfrak p\subseteq A$ be prime, and let
$$
P=q^{-1}(\mathfrak p).
$$
Then $P$ is a prime ideal of $B$ containing $M^n$.

For every $x\in M$,
$$
x^n\in M^n\subseteq P.
$$
Because $P$ is prime, $x\in P$. Thus
$$
M\subseteq P.
$$
The ideal $M$ is maximal and $P$ is proper, so $P=M$. Passing to the quotient gives
$$
\mathfrak p=P/M^n=M/M^n.
$$

:::

:::

::: pf-qed

Steps <1>1 and <1>2 show that $M/M^n$ is prime and that no other prime ideal exists.

:::

:::
