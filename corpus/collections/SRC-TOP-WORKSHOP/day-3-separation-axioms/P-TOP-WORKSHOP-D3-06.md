---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-06
kind: problem
title: Countable dense products in the product topology
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $X$ and $Y$ be two topological spaces and let $X\times Y$ be endowed with the product topology.
Prove that if $X$ and $Y$ each have a countable dense subset, then so does $X\times Y$.
:::

::: {.solution}
Let \(D_X\subset X\) and \(D_Y\subset Y\) be countable dense subsets. Then \(D_X\times D_Y\) is countable.

Every nonempty basic open set in the product topology has the form \(U\times V\) with \(U\subset X\) and \(V\subset Y\) nonempty and open. Density gives points \(x\in U\cap D_X\) and \(y\in V\cap D_Y\). Hence
\[
(x,y)\in (U\times V)\cap(D_X\times D_Y).
\]
Thus \(D_X\times D_Y\) meets every nonempty basic open set and is therefore dense in \(X\times Y\). So \(X\times Y\) has a countable dense subset.
:::
