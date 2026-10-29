---
schema: qual/card@1
id: P-R5BKY
kind: problem
title: $(\RR,+)\cong(\RR_{>0},\times)$, but not for $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Homomorphisms
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Is $(\RR,+)$ isomorphic to $(\RR_{>0},\times)$? Is the analogous statement true for $\QQ$ and $\QQ_{>0}$?
:::

::: {.solution}
::: pf

::: pf-step
$\boxed{\text{Yes}}$: $(\RR,+)\cong(\RR_{>0},\times)$.

::: pf-proof
$\exp:(\RR,+)\to(\RR_{>0},\times)$ is a homomorphism because $e^{x+y}=e^xe^y$, and it is bijective with inverse $\log$.
:::

:::

::: pf-step
$\boxed{\text{No}}$: $(\QQ,+)\not\cong(\QQ_{>0},\times)$.

::: pf-proof
The group $(\QQ,+)$ is divisible: for every $q\in\QQ$ and every positive integer $n$, $x=q/n$ satisfies $nx=q$. The group $(\QQ_{>0},\times)$ is not divisible, since $2$ has no square root in $\QQ_{>0}$. A group isomorphism preserves divisibility.
:::

:::

:::
:::
