---
schema: qual/card@1
id: P-WESCA09-I6
kind: problem
title: 'Define when a cycle is homologous to zero'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Section I, item 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $U\subset\CC$ be open and let $\sigma$ be a cycle in $U$.
Define what it means for $\sigma$ to be homologous to zero in $U$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The cycle $\sigma$ is homologous to zero in $U$ if
\[
\boxed{n(\sigma,a)=0\qquad\text{for every }a\in\CC\setminus U},
\]
where $n(\sigma,a)$ denotes the winding number, or index, of the cycle
$\sigma$ about $a$.


::: pf-proof

Because the cycle lies in $U$, every point of $\CC\setminus U$ lies
off the image of the cycle, so its winding number about such a point is
defined. Vanishing of all these winding numbers is the definition that the
cycle is homologous to zero in the open set $U$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition.

:::

:::

:::
