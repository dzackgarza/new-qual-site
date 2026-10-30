---
schema: qual/card@1
id: P-APASP08A
kind: problem
title: "Group of order 121 is Abelian"
classification:
  areas:
  - applied-algebra
  topics:
  - Group Theory
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Show that a group of order 121 is Abelian.
:::

::: {.solution}
Let $\cardinality{G}=121=11^2$. Since $G$ is a nontrivial finite $11$-group, its center is nontrivial. Therefore
$$
\cardinality{Z(G)}\in\{11,121\}.
$$
If $\cardinality{Z(G)}=121$, then $Z(G)=G$ and $G$ is abelian.

Suppose instead that $\cardinality{Z(G)}=11$. Then
$$
\cardinality{G/Z(G)}=11,
$$
so $G/Z(G)$ is cyclic. We use the standard fact that if $G/Z(G)$ is cyclic, then $G$ is abelian: if
$$
G/Z(G)=\langle gZ(G)\rangle,
$$
then every $x,y\in G$ can be written
$$
x=g^a z_1,
\qquad
y=g^b z_2
$$
with $z_1,z_2\in Z(G)$, and hence
$$
xy=g^{a+b}z_1z_2=g^{a+b}z_2z_1=yx.
$$
Thus $G$ would be abelian, which would imply $Z(G)=G$, contradicting $\cardinality{Z(G)}=11$.

Therefore the second case is impossible, and necessarily
$$
Z(G)=G.
$$
Hence
$$
\boxed{G\text{ is abelian}.}
$$
:::
