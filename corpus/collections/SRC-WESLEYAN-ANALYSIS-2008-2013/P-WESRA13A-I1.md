---
schema: qual/card@1
id: P-WESRA13A-I1
kind: problem
title: 'State Fatou’s lemma'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
State Fatou's lemma.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Fatou's lemma states: if $(X,\mathcal A,\mu)$ is a measure space and $(f_n)$ is a sequence of nonnegative measurable functions, then
$$
\boxed{
\int_X \liminf_{n\to\infty} f_n\,d\mu
\le
\liminf_{n\to\infty}\int_X f_n\,d\mu
}.
$$
Both sides are allowed to take the value $+\infty$.


::: pf-proof

This is the statement requested in the problem.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives Fatou's lemma with its hypotheses and conclusion.

:::

:::

:::
