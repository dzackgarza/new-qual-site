---
schema: qual/card@1
id: P-WESCA07-I8
kind: problem
title: "Define the arc length of a path"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section I, item 8 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Define the arc length of a path $\gamma:[a,b]\to\CC$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The **arc length** of a continuous path $\gamma:[a,b]\to\CC$ is
$$
\boxed{
L(\gamma)
\coloneqq
\sup_P
\sum_{j=1}^m
\abs{\gamma(t_j)-\gamma(t_{j-1})},}
$$
where the supremum is taken over all partitions
$$
P:\quad a=t_0<t_1<\cdots<t_m=b.
$$


::: pf-proof

This is the definition of the length, or total variation, of the path. If the supremum is finite, the path is called rectifiable.

:::

:::

::: {.pf-step #s1-2}

If $\gamma$ is piecewise $C^1$, then
$$
\boxed{L(\gamma)=\int_a^b\abs{\gamma'(t)}\,dt.}
$$


::: pf-proof

For a piecewise $C^1$ path, the standard arc-length theorem identifies the partition-supremum definition in step [](#s1-1){.pf-ref} with the integral of the speed.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested definition; step [](#s1-2){.pf-ref} gives the usual formula for the paths used in contour integration.

:::

:::

:::
