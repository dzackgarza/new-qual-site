---
schema: qual/card@1
id: P-AMD-2NXEX5LK
kind: problem
title: Maximal ideals are prime; the converse fails
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Maximal $\implies$ prime, but generally not the converse.
:::


::: {.solution}
Assume rings are commutative with identity.

<1>1. Every maximal ideal is prime.
::: {.proof}
Let $\mathfrak m$ be maximal. Then $R/\mathfrak m$ is a field, hence an integral domain. An ideal is prime exactly when its quotient ring is an integral domain. Therefore $\mathfrak m$ is prime.
:::

<1>2. The converse fails in general.
::: {.proof}
In $\ZZ$, the zero ideal $(0)$ is prime because $\ZZ$ is an integral domain. But $(0)$ is not maximal, since
\[
(0)\subsetneq (2)\subsetneq \ZZ.
\]
Thus a prime ideal need not be maximal.
:::
:::
