---
schema: qual/card@1
id: P-W8CJF
kind: problem
title: An integral domain in which every prime ideal is maximal is a field, hence a UFD
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
---

::: {.problem}
If $R$ is an integral domain and $\operatorname{Spec}R\subseteq\operatorname{MaxSpec}R$, show that $R$ is a UFD.
:::

::: {.solution}
Since $R$ is a domain, $(0)$ is prime. The hypothesis therefore makes $(0)$ maximal. Hence
\[
R/(0)=R
\]
is a field. Every field is a UFD.
:::