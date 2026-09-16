---
schema: qual/card@1
id: P-AZOFF-D08
kind: problem
title: Cauchy-type integrals are analytic off the curve
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Integrals and Cauchy’s theorem, Problem 8, of Azoff Problems by Topic.pdf; the source leaves g undefined, so a remark records the missing continuity hypothesis on g.
---

::: {.problem}
Let $\gamma$ be a smooth curve joining two distinct points $a, b \in \mathbb{C}$. Prove that the function defined by the formula
$$
f(z) = \int_\gamma \frac{g(w)\,dw}{w - z}
$$
is analytic off the range of $\gamma$. Justify every step.
:::

::: {.remark}
The source does not say what $g$ is.
The statement is meant for $g$ continuous on the range of $\gamma$, the standard hypothesis for Cauchy-type integrals; with that hypothesis the integral is defined for every $z$ off the range of $\gamma$.
:::
