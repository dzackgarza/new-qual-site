---
schema: qual/card@1
id: P-Q3X6W
kind: problem
title: No group of order 90 is simple
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
relations: []
review: draft
---

::: {.problem}
Prove that no group of order $90$ is simple.
:::

::: {.solution}
Suppose for contradiction that $G$ is simple of order
\[
90=2\cdot 3^2\cdot 5.
\]

Let $n_5$ be the number of Sylow $5$-subgroups. Sylow's theorem gives
\[
n_5\equiv1\pmod5,
\qquad
n_5\mid18,
\]
so $n_5\in\{1,6\}$. Simplicity rules out $n_5=1$, hence $n_5=6$.

Conjugation on the six Sylow $5$-subgroups gives a homomorphism
\[
\rho:G\to S_6.
\]
Its kernel is normal. The action is nontrivial, so simplicity implies that $\rho$ is injective. Thus we may regard $G$ as a subgroup of $S_6$ of order $90$.

The sign homomorphism restricted to $G$ has normal kernel. Since $G$ is nonabelian simple, it admits no nontrivial quotient of order $2$, so the sign is trivial on $G$. Hence
\[
G\le A_6.
\]
But then
\[
[A_6:G]=\frac{360}{90}=4.
\]
The action of $A_6$ on the four left cosets of $G$ gives a homomorphism
\[
A_6\to S_4.
\]
Since $A_6$ is simple and the coset action is nontrivial, this map would be injective, impossible because
\[
|A_6|=360>|S_4|=24.
\]
Therefore no simple group of order $90$ exists.
:::
