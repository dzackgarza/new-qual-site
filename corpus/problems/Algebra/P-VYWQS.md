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
::: {.problem}
Let $R$ be a commutative ring with $1$. Show that $r\in R$ is noninvertible if and only if $r$ lies in a maximal ideal.
:::

::: {.solution}
Suppose first that $r$ is noninvertible. Then the principal ideal $(r)$ is proper: if $(r)=R$, then $1=sr$ for some $s\in R$, making $r$ a unit. By Zorn's lemma, every proper ideal is contained in a maximal ideal, so there exists a maximal ideal $\mathfrak m$ with
\[
r\in(r)\subseteq\mathfrak m.
\]

Conversely, suppose $r\in\mathfrak m$ for some maximal ideal $\mathfrak m$. If $r$ were invertible, then
\[
1=r^{-1}r\in\mathfrak m,
\]
which would imply $\mathfrak m=R$, contradicting maximality.

Thus $r$ is noninvertible exactly when it belongs to some maximal ideal.
:::
