---
schema: qual/card@1
id: T-XDMK2
kind: theorem
title: Cauchy's theorem
classification:
  areas:
  - algebra
  topics:
  - Groups
relations:
- kind: uses
  target: T-SZRXI
review: reviewed
---

::: {.theorem}
Let $G$ be a finite group and let $p$ be prime.
If $p$ divides $\abs G$, then $G$ contains an element of order $p$, and therefore a subgroup of order $p$.
:::

::: {.remark}
By [[T-SZRXI|Lagrange's theorem]], the order of every element of $G$ divides $\abs G$; Cauchy's theorem is the converse for prime divisors of $\abs G$.
[[T-4RADG|Sylow's first theorem]] strengthens the existence statement from order $p$ to order $p^a$, where $p^a$ is the largest power of $p$ dividing $\abs G$.
:::
