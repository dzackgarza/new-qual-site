---
schema: qual/card@1
id: P-WESCA05-I7
kind: problem
title: "State Liouville's Theorem"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 7 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
State Liouville's Theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Liouville's theorem states:
$$
\boxed{\text{Every bounded entire function }f:\CC\to\CC\text{ is constant}.}
$$


::: pf-proof

Equivalently, if $f$ is analytic on all of $\CC$ and there is $M<\infty$ such that
$$
|f(z)|\le M
\qquad
\text{for every }z\in\CC,
$$
then there is $c\in\CC$ with $f(z)=c$ for every $z\in\CC$. This is the statement of Liouville's theorem.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested theorem statement.

:::

:::

:::
