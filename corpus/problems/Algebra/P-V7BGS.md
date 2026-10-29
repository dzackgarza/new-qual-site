---
schema: qual/card@1
id: P-V7BGS
kind: problem
title: Groups of prime order are cyclic
classification:
  areas:
  - algebra
  topics:
  - Cyclic Groups
  - Classification
  - Cosets and Lagrange
relations: []
review: draft
---

::: {.problem}
Show that every group of prime order is cyclic.
:::

::: {.solution}
Let $\abs{G}=p$ with $p$ prime. Since $p>1$, choose a nonidentity element $g\in G$.

::: pf

::: {.pf-step #order}

$\abs{\langle g\rangle}=p$.

::: pf-proof

By Lagrange's theorem, $\abs{\langle g\rangle}$ divides $p$. It is not $1$ because $g\ne e$.

:::

:::

::: pf-qed

By step [](#order){.pf-ref}, $\langle g\rangle$ is a subgroup of $G$ with $\abs{G}$ elements, so $G=\langle g\rangle$ is cyclic.

:::

:::

:::
