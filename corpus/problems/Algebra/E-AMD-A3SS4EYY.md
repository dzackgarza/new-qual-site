---
schema: qual/card@1
id: E-AMD-A3SS4EYY
kind: problem
title: A ring in which every non-unit is nilpotent is local
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Nilpotence
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $R\neq 0$ is a ring in which every non-unit is nilpotent then $R$ is local.
:::

::: {.solution}
Assume $R$ is a nonzero ring with identity and every nonunit is nilpotent.

Let $x\in R$. If $x$ is a unit there is nothing to prove. If $x$ is not a unit, then $x^m=0$ for some $m\ge1$, so
\[
(1-x)(1+x+\cdots+x^{m-1})=1=(1+x+\cdots+x^{m-1})(1-x).
\]
Hence $1-x$ is a unit. Thus for every $x\in R$, either $x$ or $1-x$ is a unit.

Maximal left ideals exist by Zorn's lemma. Suppose $M$ and $N$ are two distinct maximal left ideals. Choose $a\in M\setminus N$. Since $N$ is maximal and $a\notin N$,
\[
N+Ra=R,
\]
so
\[
1=b+ra
\]
for some $b\in N$ and $r\in R$. Put $y=ra$. Then $y\in M$ and $1-y=b\in N$. Neither $y$ nor $1-y$ can be a unit, because a proper left ideal contains no units. This contradicts the preceding paragraph.

Therefore $R$ has a unique maximal left ideal, so $R$ is local.
:::
