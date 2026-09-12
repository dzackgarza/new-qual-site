---
schema: qual/card@1
id: E-AMD-EBIC3Z5S
kind: problem
title: If $\spec(R)\subseteq\maxspec(R)$ then $R$ is a UFD
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Factorization
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
Show that if $\operatorname{Spec}(R) \subseteq \operatorname{MaxSpec}(R)$ and $R$ is an integral domain, then $R$ is a UFD.
:::

::: {.solution}
Because \(R\) is an integral domain, the zero ideal \((0)\) is prime. Hence
\[
(0)\in\operatorname{Spec}(R).
\]
By hypothesis every prime ideal is maximal, so \((0)\) is maximal. Therefore
\[
R/(0)\cong R
\]
is a field.

Every field is a UFD. Thus
\[
\boxed{R\text{ is a UFD}.}
\]
:::
