---
schema: qual/card@1
id: P-M8QNL
kind: problem
title: If $G/Z(G)$ is cyclic then $G$ is abelian
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $G$ be a group with center $Z(G)$.
Show that if $G/Z(G)$ is cyclic, then $G$ is abelian.
:::

::: {.solution}
Suppose $G/Z(G)=\langle gZ(G)\rangle$ for some $g\in G$.

::: pf

::: {.pf-step #s1}

Every $x\in G$ can be written $x=g^iz$ with $i\in\ZZ$ and $z\in Z(G)$.

::: pf-proof

The coset $xZ(G)$ lies in $\langle gZ(G)\rangle$, so $xZ(G)=g^iZ(G)$ for some $i\in\ZZ$, and then $z=g^{-i}x\in Z(G)$.

:::

:::

::: {.pf-step #s2}

Any $x,y\in G$ commute.

::: pf-proof

By step [](#s1){.pf-ref}, write $x=g^iz_1$ and $y=g^jz_2$ with $z_1,z_2\in Z(G)$.
Since $z_1,z_2$ are central and powers of $g$ commute with each other,
$$
xy=g^iz_1g^jz_2=g^{i+j}z_1z_2=g^jz_2g^iz_1=yx.
$$

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} shows that $G$ is abelian.

:::

:::

:::
