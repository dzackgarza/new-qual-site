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

::: problem
Let $G$ be a group with center $Z(G)$.
Show that if $G/Z(G)$ is cyclic, then $G$ is abelian.
:::

::: {.solution}
<1>1. Suppose $G/Z(G)=\langle gZ(G)\rangle$ is cyclic.
::: {.proof}
hypothesis.
:::

<1>2. Any $x\in G$ can be written $x=g^i z$ for some $i\in\ZZ$, $z\in Z(G)$.
::: {.proof}
coset $xZ(G)=g^iZ(G)$.
:::

<1>3. For $x=g^i z_1$, $y=g^j z_2$, $xy=g^i z_1 g^j z_2 = g^{i+j}z_1z_2 = g^j z_2 g^i z_1 = yx$.
::: {.proof}
$z_1,z_2$ central and powers of $g$ commute.
:::

<1>4. Hence $G$ is abelian.
::: {.proof}
<1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
