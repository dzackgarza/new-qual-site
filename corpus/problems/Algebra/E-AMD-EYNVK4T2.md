---
schema: qual/card@1
id: E-AMD-EYNVK4T2
kind: problem
title: An $m$-cycle is odd iff $m$ is even
classification:
  areas:
  - algebra
  topics:
  - Permutations
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

::: {.exercise}
Show that an $m$-cycle is an odd permutation if and only if $m$ is an even number.
:::

::: {.solution}
If
\[
\sigma=(a_1\ a_2\ \dots\ a_m),
\]
then
\[
\sigma=(a_1\ a_m)(a_1\ a_{m-1})\cdots(a_1\ a_2),
\]
a product of exactly $m-1$ transpositions. Hence
\[
\operatorname{sgn}(\sigma)=(-1)^{m-1}.
\]
Therefore $\sigma$ is odd exactly when $m-1$ is odd, equivalently when $m$ is even.
:::
