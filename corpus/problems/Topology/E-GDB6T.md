---
schema: qual/card@1
id: E-GDB6T
kind: problem
title: Compact Hausdorff spaces are metrizable if and only if second-countable
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
  - Countability
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that a compact Hausdorff space is metrizable if and only if it is second-countable.
:::

::: {.solution}
Let $X$ be a compact Hausdorff space.

::: pf

::: pf-step

If $X$ is metrizable, then $X$ is second-countable.

::: pf-proof

Fix a metric $d$ inducing the topology.

::: {.pf-step #s1-1}

For each $m\in\NN$ there is a finite set $D_m\subseteq X$ with $X=\bigcup_{z\in D_m}B(z,1/m)$.

::: pf-proof

The balls $B(x,1/m)$, $x\in X$, form an open cover of the compact space $X$.

:::

:::

::: pf-qed

The family $\mathcal{B}=\{B(z,1/m):m\in\NN,\ z\in D_m\}$ is a countable union of finite sets, hence countable. It is a basis: let $U$ be open and $x\in U$, choose $r>0$ with $B(x,r)\subseteq U$ and $m$ with $2/m<r$, and by step [](#s1-1){.pf-ref} choose $z\in D_m$ with $x\in B(z,1/m)$. For $y\in B(z,1/m)$, $d(y,x)\le d(y,z)+d(z,x)<2/m<r$, so $x\in B(z,1/m)\subseteq U$.

:::

:::

:::

::: pf-step

If $X$ is second-countable, then $X$ is metrizable.

::: pf-proof

::: {.pf-step #s2-1}

$X$ is regular.

::: pf-proof

Let $F\subseteq X$ be closed and $y\notin F$. Each $x\in F$ has disjoint open neighborhoods $U_x\ni x$ and $V_x\ni y$ because $X$ is Hausdorff. The closed set $F$ is compact, so finitely many $U_{x_1},\ldots,U_{x_k}$ cover $F$, and then $\bigcup_iU_{x_i}$ and $\bigcap_iV_{x_i}$ are disjoint open sets containing $F$ and $y$. Points are closed because $X$ is Hausdorff.

:::

:::

::: pf-qed

By step [](#s2-1){.pf-ref} and the Urysohn metrization theorem, a second-countable regular space is metrizable.

:::

:::

:::

:::

:::
