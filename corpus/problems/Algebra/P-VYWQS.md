---
schema: qual/card@1
id: P-VYWQS
kind: problem
title: An element of a commutative ring is noninvertible if and only if it lies in
  a maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Rings
relations: []
review: draft
---

::: {.problem}
Suppose that $R$ is a commutative ring.
Show that an element $r\in R$ is not invertible iff it is contained in a maximal ideal.
:::

::: {.solution}

::: pf

::: pf-step

If $r$ is not invertible, then $r$ lies in a maximal ideal.

::: pf-proof

The principal ideal $(r)$ is proper: if $(r)=R$, then $1=sr$ for some $s\in R$, making $r$ a unit. By Zorn's lemma, every proper ideal is contained in a maximal ideal, so there is a maximal ideal $\mathfrak m$ with $r\in(r)\subseteq\mathfrak m$.

:::

:::

::: pf-step

If $r$ lies in a maximal ideal $\mathfrak m$, then $r$ is not invertible.

::: pf-proof

If $r$ were invertible, then $1=r^{-1}r\in\mathfrak m$, so $\mathfrak m=R$, contradicting that a maximal ideal is proper.

:::

:::

:::

:::
