---
schema: qual/card@1
id: P-G52LZ
kind: problem
title: Every $p$-group is nilpotent
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Nilpotent Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that every $p\dash$group is nilpotent.
:::

::: {.solution}
Let $G$ be a finite $p$-group. Every nontrivial finite $p$-group has nontrivial center: by the class equation,
\[
|G|=|Z(G)|+\sum_i [G:C_G(x_i)],
\]
and every summand in the sum is divisible by $p$, hence $p\mid |Z(G)|$.

Now form the upper central series
\[
1=Z_0(G)\le Z_1(G)\le Z_2(G)\le\cdots,
\qquad Z_{i+1}(G)/Z_i(G)=Z(G/Z_i(G)).
\]
If $Z_i(G)
e G$, then $G/Z_i(G)$ is a nontrivial finite $p$-group, so its center is nontrivial. Hence
\[
Z_i(G)<Z_{i+1}(G).
\]
Each strict inclusion multiplies the order by at least $p$, so after finitely many steps the series reaches $G$. Therefore $G$ is nilpotent.
:::
