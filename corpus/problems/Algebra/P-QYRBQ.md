---
schema: qual/card@1
id: P-QYRBQ
kind: problem
title: No group of order 36 is simple
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Prove that no group of order 36 is simple.
:::

::: solution
Let $|G|=36$. Sylow gives
\[
n_3\mid4,\qquad n_3\equiv1\pmod3,
\]
so $n_3=1$ or $4$.

If $n_3=1$, the Sylow $3$-subgroup is a nontrivial proper normal subgroup.

Suppose $n_3=4$. Conjugation on the four Sylow $3$-subgroups gives
\[
\rho:G\to S_4.
\]
If $\ker\rho=1$, then $G$ embeds in $S_4$, impossible because $36\nmid24$. Thus the kernel is nontrivial. It is also proper because the conjugation action is transitive and hence nontrivial. Therefore $\ker\rho$ is a nontrivial proper normal subgroup of $G$.

So no group of order $36$ is simple.
:::
