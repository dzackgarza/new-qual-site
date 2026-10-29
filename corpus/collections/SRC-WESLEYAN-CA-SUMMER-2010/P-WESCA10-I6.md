---
schema: qual/card@1
id: P-WESCA10-I6
kind: problem
title: 'Define a branch of the logarithm'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Theorems and Definitions, item 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $D\subset\CC$ be a domain with $0\notin D$.
Define what it means for a function to be a branch of the logarithm on $D$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A branch of the logarithm on $D$ is a holomorphic function
$L:D\to\CC$ such that
$$
\boxed{e^{L(z)}=z\qquad\text{for every }z\in D.}
$$


::: pf-proof

The complex exponential maps $\CC$ to $\CC^\times$.
Thus a branch of the logarithm on $D$ is precisely a holomorphic right inverse
of the exponential along the inclusion $D\hookrightarrow\CC^\times$.
Equivalently, for every $z\in D$, the value $L(z)$ is a logarithm of $z$ and
the choices vary holomorphically with $z$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition.

:::

:::

:::
