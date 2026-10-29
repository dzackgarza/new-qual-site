---
schema: qual/card@1
id: P-QJKMC
kind: problem
title: Jordan form of an operator on a $6$-dimensional space with $T^6=0$ and $T^5\neq
  0$, and similarity of any two such operators
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Nilpotence
  - Canonical Forms
relations: []
review: draft
---

::: {.problem}
Suppose $V$ is $6$-dimensional and $T\in\operatorname{End}(V)$ satisfies
$$
T^6=0,
\qquad
T^5\ne0.
$$

(a) Determine the Jordan canonical form of $T$.

(b) Show that any two such operators are similar.
:::

::: {.solution}
::: pf

::: {.pf-step #jordan-form}
(a) The Jordan form of $T$ is $\boxed{J_6(0)}$, a single nilpotent Jordan block of size $6$.

::: pf-proof
Since $T^6=0$, the only eigenvalue of $T$ is $0$, so $T$ has a Jordan form over the base field and every Jordan block is $J_k(0)$ for some $k$. The block $J_k(0)$ satisfies $J_k(0)^5\ne0$ exactly when $k\ge6$, so $T^5\ne0$ forces a block of size at least $6$. The block sizes sum to $\dim V=6$, so that block is the only one.
:::

:::

::: pf-step
(b) Any two operators $S,T$ on $V$ with $S^6=T^6=0$ and $S^5,T^5\ne0$ are similar.

::: pf-proof
By step [](#jordan-form){.pf-ref} there are invertible $P,Q$ with $T=PJ_6(0)P^{-1}$ and $S=QJ_6(0)Q^{-1}$. With $A\coloneqq QP^{-1}$ we get $ATA^{-1}=QJ_6(0)Q^{-1}=S$.
:::

:::

:::
:::
