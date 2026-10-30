---
schema: qual/card@1
id: P-Q3X6W
kind: problem
title: No group of order $90$ is simple
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
Suppose, for a contradiction, that $G$ is simple of order $90=2\cdot3^2\cdot5$, and let $n_5$ be the number of Sylow $5$-subgroups of $G$.

::: pf

::: {.pf-step #n5}
$n_5=6$.

::: pf-proof
By the Sylow theorems, $n_5\equiv1\pmod5$ and $n_5\mid18$, so $n_5\in\{1,6\}$. If $n_5=1$, the Sylow $5$-subgroup is a proper nontrivial normal subgroup, which simplicity excludes.
:::

:::

::: {.pf-step #in-a6}
$G$ is isomorphic to a subgroup of $A_6$, of index $4$.

::: pf-proof
Conjugation on the six Sylow $5$-subgroups of step [](#n5){.pf-ref} gives a homomorphism $\rho:G\to S_6$. It is nontrivial because the action is transitive on six points, so its kernel is a proper normal subgroup and hence trivial. Identify $G$ with $\rho(G)\le S_6$. The kernel of $\operatorname{sgn}\restrict_G$ is normal of index at most $2$; since $\abs{G}=90$ is not prime, $G$ is not cyclic of order $2$, so simplicity forces the kernel to be $G$. Hence $G\le A_6$, and $[A_6:G]=360/90=4$.
:::

:::

::: pf-step
This is a contradiction.

::: pf-proof
The action of $A_6$ on the four left cosets of $G$ from step [](#in-a6){.pf-ref} gives a homomorphism $A_6\to S_4$, nontrivial because the action is transitive. Since $A_6$ is simple, it is injective, which is impossible because $\abs{A_6}=360>24=\abs{S_4}$.
:::

:::

:::

:::
