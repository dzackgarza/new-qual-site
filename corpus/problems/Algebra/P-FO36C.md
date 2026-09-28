---
schema: qual/card@1
id: P-FO36C
kind: problem
title: Lower and upper central series, nilpotent groups, and solvable groups
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Nilpotent Groups
  - Solvable Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Define lower central series, upper central series, nilpotent and solvable groups.
:::

::: {.solution}
For a group $G$, the **lower central series** is
\[
\gamma_1(G)=G,\qquad \gamma_{i+1}(G)=[\gamma_i(G),G].
\]
The **upper central series** is
\[
Z_0(G)=1,\qquad Z_{i+1}(G)/Z_i(G)=Z\bigl(G/Z_i(G)\bigr).
\]

The group $G$ is **nilpotent** if $\gamma_{c+1}(G)=1$ for some $c\ge0$; equivalently, $Z_c(G)=G$ for some $c$. The least such $c$ is the nilpotency class.

The **derived series** is
\[
G^{(0)}=G,\qquad G^{(i+1)}=[G^{(i)},G^{(i)}].
\]
The group $G$ is **solvable** if $G^{(r)}=1$ for some $r$.
:::
