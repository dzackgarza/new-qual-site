---
schema: qual/card@1
id: T-4CDTT
kind: theorem
title: The class equation and centers of finite $p$-groups
classification:
  areas:
  - algebra
  topics:
  - Groups
relations:
- kind: uses
  target: D-WYC7C
- kind: uses
  target: T-QYDVH
- kind: uses
  target: L-DJKXL
review: reviewed
---

::: {.theorem}
Let a finite group $G$ act on itself by conjugation.
The fixed points are the elements of the [[D-NK7G7|center]] $Z(G)$, the orbit of $x$ is its [[D-HLDEY|conjugacy class]], and the stabilizer of $x$ is its [[D-PX64W|centralizer]] $C_G(x)$.
Consequently,
$$
\abs G=\abs{Z(G)}
  +\sum_i [G:C_G(x_i)],
$$
where $x_i$ runs over a set of representatives of the conjugacy classes of $G$ not contained in $Z(G)$.
:::

::: {.corollary title="Finite $p$-groups have nontrivial center"}
Let $p$ be a prime and $G$ a group with $\abs G=p^a$, $a>0$.
Then $p$ divides $\abs{Z(G)}$, so $Z(G)\neq\theset{e}$.
:::

::: {.proof}
For $x\notin Z(G)$, the conjugacy class of $x$ has size $[G:C_G(x)]>1$, which divides $p^a$ and is therefore a positive power of $p$.
Reducing the class equation modulo $p$ gives $\abs{Z(G)}\equiv\abs G\equiv0\pmod p$.
:::
