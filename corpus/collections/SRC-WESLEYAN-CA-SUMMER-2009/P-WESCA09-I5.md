---
schema: qual/card@1
id: P-WESCA09-I5
kind: problem
title: 'Define a primitive of a complex-valued function'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Section I, item 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $U\subset\mathbb C$ be open and let $f:U\to\mathbb C$.
Define what it means for a function $F$ to be a primitive of $f$.
:::

::: pf

::: pf-step

A function $F:U\to\mathbb C$ is a primitive of $f$ on $U$ if $F$ is
holomorphic on $U$ and
\[
\boxed{F'(z)=f(z)\qquad\text{for every }z\in U}.
\]


::: pf-proof

This is the definition of a primitive, or antiderivative, of a complex-valued
function on an open set.

:::

:::

::: pf-qed

Step <1>1 gives the requested definition.

:::

:::
