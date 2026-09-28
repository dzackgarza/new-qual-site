---
schema: qual/card@1
id: E-52RYU
kind: problem
title: Irreducible with a root in a splitting field splits completely
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Field Extensions
  - Irreducibility Criteria
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
Let $F$ be the splitting field of $f \in K[x]$ over $K$.
Prove that if $g \in K[x]$ is irreducible and has a root in $F$, then $g$ splits into linear factors over $F$.
:::

::: {.solution}
A splitting field is a normal algebraic extension. Thus $F/K$ is normal.

Let $g\in K[x]$ be irreducible and suppose $g$ has a root $\alpha\in F$. By the defining irreducible-polynomial criterion for normality, every irreducible polynomial over $K$ having one root in $F$ splits completely over $F$.

Applying this criterion to $g$ gives
\[
\boxed{g\text{ splits into linear factors in }F[x].}
\]
:::
