---
schema: qual/card@1
id: E-4T2MK
kind: problem
title: Connected fibers over a connected base connect the total space
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $p: X \to Y$ be a quotient map.
Show that if each set $p^{-1}(\ts{y})$ is connected, and if $Y$ is connected, then $X$ is connected.
:::

::: {.solution}
Suppose $X=U\cup V$ with $U,V$ disjoint, nonempty, and open; we derive a separation of $Y$.

::: pf

::: {.pf-step #u-v-saturated}
$U$ and $V$ are saturated: $p^{-1}(p(U))=U$ and $p^{-1}(p(V))=V$.

::: pf-proof
For $y\in Y$, the fiber $F_y=p^{-1}(\{y\})$ is the disjoint union of the relatively open sets $F_y\cap U$ and $F_y\cap V$.
Since $F_y$ is connected, $F_y\subseteq U$ or $F_y\subseteq V$.
So a fiber that meets $U$ lies in $U$, and likewise for $V$.
:::

:::

::: {.pf-step #images-separate-y}
$p(U)$ and $p(V)$ form a separation of $Y$.

::: pf-proof
They are nonempty because $U$ and $V$ are, and their union is $p(X)=Y$ because $p$ is surjective.
By step [](#u-v-saturated){.pf-ref}, a point of $p(U)\cap p(V)$ would have its fiber in both $U$ and $V$, so they are disjoint.
By step [](#u-v-saturated){.pf-ref}, $p^{-1}(p(U))=U$ and $p^{-1}(p(V))=V$ are open, so $p(U)$ and $p(V)$ are open in the quotient topology.
:::

:::

::: pf-qed
Step [](#images-separate-y){.pf-ref} contradicts the connectedness of $Y$, so $X$ has no separation.
:::

:::

:::
