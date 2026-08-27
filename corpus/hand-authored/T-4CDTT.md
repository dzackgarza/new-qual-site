---
schema: qual/card@1
id: T-4CDTT
kind: theorem
title: The class equation and centers of finite p-groups
classification:
  areas:
  - algebra
  topics:
  - Groups
relations:
- kind: uses
  target: D-WYC7C
- kind: uses
  target: T-OBPSZ
- kind: uses
  target: L-DJKXL
review: reviewed
---

::: {.theorem}
Let a finite group $G$ act on itself by conjugation. The fixed points are
$Z(G)$, the orbit of $x$ is its conjugacy class, and the stabilizer of $x$ is
its centralizer $C_G(x)$. Consequently,
$$
\abs G=\abs{Z(G)}
  +\sum_i [G:C_G(x_i)],
$$
where the sum takes one representative from each noncentral conjugacy class.
:::

::: {.corollary title="Finite p-groups have nontrivial center"}
If $\abs G=p^a$ with $a>0$, then $\abs{Z(G)}$ is divisible by $p$, so
$Z(G)\neq\theset{e}$.

::: {.proof}
Every noncentral conjugacy class has size $[G:C_G(x)]$, a nontrivial power of
$p$. Reducing the class equation modulo $p$ gives
$\abs{Z(G)}\equiv\abs G\equiv0\pmod p$.
:::
:::
