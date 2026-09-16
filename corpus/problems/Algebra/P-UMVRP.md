---
schema: qual/card@1
id: P-UMVRP
kind: problem
title: Groups with nontrivial automorphisms
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Groups
relations: []
review: draft
---

::: {.problem}
Which groups have trivial automorphism group?
:::

::: {.solution}
The only groups with trivial automorphism group are
\[
1\qquad\text{and}\qquad C_2.
\]

Suppose $\operatorname{Aut}(G)=1$. Every inner automorphism is then trivial, so
\[
\operatorname{Inn}(G)=1.
\]
Hence
\[
G/Z(G)=1,
\]
and therefore $G$ is abelian.

For an abelian group, inversion
\[
x\longmapsto x^{-1}
\]
is an automorphism. Since every automorphism is trivial, inversion must be the identity, so
\[
x=x^{-1}
\]
for every $x\in G$. Thus every element has order dividing $2$, and $G$ is a vector space over $\FF_2$.

If its dimension were at least $2$, a nontrivial linear automorphism could interchange two basis vectors. Therefore the dimension is at most $1$, giving
\[
G=1\quad\text{or}\quad G\cong C_2.
\]

Conversely, both $1$ and $C_2$ plainly have only the identity automorphism.
:::
