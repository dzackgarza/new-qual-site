---
schema: qual/card@1
id: P-6URED
kind: problem
title: $S_4$ is solvable and nonabelian
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Permutations
  - Subgroup Series
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
Prove that the symmetric group $S_4$ is a **non-abelian** and **solvable** group.
:::

::: solution
The group $S_4$ is nonabelian because, for example,
\[
(12)(23)=(123)\ne(132)=(23)(12).
\]

For solvability, consider
\[
1\triangleleft V_4\triangleleft A_4\triangleleft S_4,
\]
where
\[
V_4=\{e,(12)(34),(13)(24),(14)(23)\}.
\]
The subgroup $A_4$ is normal of index $2$ in $S_4$. The subgroup $V_4$ is normal in $S_4$ because conjugation preserves cycle type, hence is normal in $A_4$ as well. The factors are
\[
V_4,\qquad A_4/V_4\cong C_3,\qquad S_4/A_4\cong C_2,
\]
all abelian. Therefore $S_4$ is solvable.

Thus $S_4$ is solvable but nonabelian.
:::
