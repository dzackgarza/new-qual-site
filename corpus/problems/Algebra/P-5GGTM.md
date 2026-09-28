---
schema: qual/card@1
id: P-5GGTM
kind: problem
title: Every field is a simple ring
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that every field is simple.
:::

::: {.solution}
Let $F$ be a field and let $I\trianglelefteq F$. If $I=(0)$ there is nothing to prove. Otherwise choose $0\ne x\in I$. Since $x$ is a unit,
\[
1=x^{-1}x\in I.
\]
Therefore every $a\in F$ satisfies $a=a\cdot1\in I$, so $I=F$. Thus the only ideals of $F$ are $(0)$ and $F$, and every field is a simple ring.
:::
