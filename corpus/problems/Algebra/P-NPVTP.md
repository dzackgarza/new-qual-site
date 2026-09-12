---
schema: qual/card@1
id: P-NPVTP
kind: problem
title: Nilpotent groups have nontrivial centers
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
- Show that nilpotent groups have nontrivial centers.
:::

::: {.solution}
Let $G\neq1$ be nilpotent. Using the lower central series
\[
\gamma_1(G)=G,\qquad \gamma_{i+1}(G)=[\gamma_i(G),G],
\]
choose the nilpotency class $c$, so that
\[
\gamma_c(G)\neq1,\qquad \gamma_{c+1}(G)=1.
\]
Then
\[
[\gamma_c(G),G]=1,
\]
so every element of $\gamma_c(G)$ commutes with every element of $G$. Thus
\[
1\neq\gamma_c(G)\le Z(G),
\]
and therefore $Z(G)\neq1$.
:::
