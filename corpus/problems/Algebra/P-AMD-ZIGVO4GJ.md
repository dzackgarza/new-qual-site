---
schema: qual/card@1
id: P-AMD-ZIGVO4GJ
kind: problem
title: $R/\nilrad{R}$ is reduced
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $R$ be a commutative ring and let $\operatorname{nil}(R) = \sqrt{(0)}$ be its nilradical (the ideal of all nilpotent elements in $R$).
Prove that the quotient ring $R / \operatorname{nil}(R)$ is reduced (i.e. has no non-zero nilpotent elements).
:::

::: solution
Let \(N=\operatorname{nil}(R)\). Suppose \(x+N\in R/N\) is nilpotent. Then for some \(m\ge1\),
\[
(x+N)^m=N,
\]
so \(x^m\in N\). Hence \((x^m)^k=0\) for some \(k\ge1\), and therefore \(x^{mk}=0\). Thus \(x\in N\), so \(x+N=0\) in \(R/N\).

Hence \(R/N\) has no nonzero nilpotent elements and is reduced.
:::
