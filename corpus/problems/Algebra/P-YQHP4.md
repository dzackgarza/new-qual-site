---
schema: qual/card@1
id: P-YQHP4
kind: problem
title: An ideal containing a unit is the whole ring
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Rings
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source labels the parts (1) and (2); they are labelled (a) and (b).
---

::: {.problem}
(a) Let $R$ be a ring with identity $1 \ne 0$, and let $I \trianglelefteq R$ be an ideal of $R$.
Prove that if $I$ contains a unit $u \in R^\times$, then $I = R$.

(b) Prove that the group of units $R^\times$ need not be closed under addition, and provide concrete examples in standard rings.
:::

::: {.solution}

::: pf

::: pf-step
(a) $\boxed{I=R}$.

::: pf-proof
Since $I$ is an ideal containing $u$, it contains $u^{-1}u=1$, and then $r=r\cdot1\in I$ for every $r\in R$.
:::

:::

::: pf-step
(b) $R^\times$ is never closed under addition when $1\ne0$; for example $1+1=2\notin\ZZ^\times=\{\pm1\}$.

::: pf-proof
If $u$ is a unit, so is $-u$, with inverse $-u^{-1}$, but $u+(-u)=0$ is not a unit because $0\cdot r=0\ne1$.
The example in $\ZZ$ is direct.
:::

:::

:::

:::
