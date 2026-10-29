---
schema: qual/card@1
id: P-USAQT
kind: problem
title: Every proper ideal is contained in a maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
relations: []
review: draft
---

::: {.problem}
Let rings be commutative with identity. Show that every proper ideal is contained in a maximal ideal.
:::

::: {.solution}
Let $I\subsetneq R$ be a proper ideal, and let $\Sigma$ be the set of proper ideals of $R$ containing $I$, ordered by inclusion.

::: pf

::: {.pf-step #chains}

Every chain in $\Sigma$ has an upper bound in $\Sigma$.

::: pf-proof

$\Sigma$ is nonempty because $I\in\Sigma$, so the empty chain is bounded. The union of a nonempty chain of ideals is an ideal containing $I$, since any two of its elements lie in a common member of the chain. It is proper: if it contained $1$, then one member of the chain would contain $1$.

:::

:::

::: pf-qed

By step [](#chains){.pf-ref} and Zorn's lemma, $\Sigma$ has a maximal element $\mathfrak m$. Any proper ideal containing $\mathfrak m$ contains $I$, so lies in $\Sigma$ and equals $\mathfrak m$. Hence $\mathfrak m$ is a maximal ideal containing $I$.

:::

:::

:::
