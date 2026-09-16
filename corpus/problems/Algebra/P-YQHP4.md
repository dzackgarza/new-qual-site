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
---

::: {.problem}
(1) Let $R$ be a ring with identity $1 \ne 0$, and let $I \trianglelefteq R$ be an ideal of $R$.
Prove that if $I$ contains a unit $u \in R^\times$, then $I = R$.
(2) Prove that the group of units $R^\times$ need not be closed under addition, and provide concrete examples in standard rings.
:::

::: {.solution}
If an ideal $I\trianglelefteq R$ contains a unit $u$, then it also contains
\[
u^{-1}u=1.
\]
Hence for every $r\in R$,
\[
r=r\cdot1\in I,
\]
so
\[
\boxed{I=R}.
\]
The same argument works for one-sided ideals using the appropriate side of the inverse.

The unit group $R^\times$ is a group under multiplication, not generally under addition. For example,
\[
\mathbb Z^\times=\{\pm1\},
\]
but
\[
1+1=2\notin\mathbb Z^\times.
\]
More universally, in any nonzero unital ring, if $u$ is a unit then so is $-u$, while
\[
u+(-u)=0
\]
is not a unit. Thus $R^\times$ need not be additively closed.
:::
