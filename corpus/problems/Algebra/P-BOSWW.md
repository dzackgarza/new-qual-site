---
schema: qual/card@1
id: P-BOSWW
kind: problem
title: $A_n$ is normal in $S_n$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- Prove that $A_n$ is normal in $S_n$.
:::


::: {.solution}
Consider the sign homomorphism
\[
\operatorname{sgn}:S_n\longrightarrow\{\pm1\}.
\]
Its kernel is exactly $A_n$. Kernels of group homomorphisms are normal, hence
\[
A_n\trianglelefteq S_n.
\]
Equivalently, $A_n$ has index $2$ in $S_n$, and every subgroup of index $2$ is normal.
:::
