---
schema: qual/card@1
id: P-W8CJF
kind: problem
title: An integral domain in which every prime ideal is maximal is a field, hence a UFD
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
---

::: {.problem}
If $R$ is an integral domain and $\Spec R\subseteq\maxspec R$, show that $R$ is a UFD.
:::

::: {.solution}

::: pf

::: {.pf-step #field}

$R$ is a field.

::: pf-proof

Since $R$ is a domain, $(0)$ is prime. The hypothesis makes $(0)$ maximal, so $R\cong R/(0)$ is a field.

:::

:::

::: pf-qed

By step [](#field){.pf-ref}, every nonzero element of $R$ is a unit, so the condition of unique factorization holds vacuously and $R$ is a UFD.

:::

:::

:::
