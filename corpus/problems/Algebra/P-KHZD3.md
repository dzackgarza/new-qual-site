---
schema: qual/card@1
id: P-KHZD3
kind: problem
title: Whether a formal power series ring is a UFD
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Rings
  - Local Rings
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
Is a ring of formal power series $R[[x]]$ a unique factorization domain (UFD)?
:::

::: {.solution}

::: pf

::: pf-step
If $R=k$ is a field, then $k[[x]]$ is a UFD.

::: pf-proof
Every nonzero series has a unique form $f=x^m u$ with $m\ge0$ and $u$ a unit, since a series with nonzero constant term is invertible. Hence every nonzero ideal is $(x^m)$ for some $m$, so $k[[x]]$ is a discrete valuation ring, in particular a PID, and therefore a UFD.
:::

:::

::: pf-step
For a field $k$, every ring $k[[x_1,\ldots,x_n]]$ is a UFD.

::: pf-proof
It is a regular local ring, and a regular local ring is a UFD by the Auslander--Buchsbaum theorem.
:::

:::

::: pf-step
The answer is $\boxed{\text{not in general}}$: there are UFDs $R$ for which $R[[x]]$ is not a UFD.

::: pf-proof
Samuel constructed such rings [@Sam61]. So the polynomial-ring theorem of Gauss, that $R$ a UFD implies $R[x]$ a UFD, has no unrestricted formal-power-series analogue.
:::

:::

:::

:::
