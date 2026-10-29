---
schema: qual/card@1
id: P-YNF6T
kind: problem
title: Proper subgroups of a group of order $pq$ are cyclic
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Cyclic Groups
  - Cosets and Lagrange
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
Suppose $\abs{G} = pq$ with $p, q \geq 2$ prime, and let $H \le G$ be a proper subgroup.
Prove that $H$ must be cyclic.
:::

::: {.solution}

::: pf

::: {.pf-step #order}
$\abs{H}\in\{1,p,q\}$.

::: pf-proof
By Lagrange's theorem $\abs{H}$ divides $pq$, and $\abs{H}\ne pq$ because $H$ is proper.
:::

:::

::: pf-step
$H$ is cyclic.

::: pf-proof
If $\abs{H}=1$, $H$ is trivial.
Otherwise $\abs{H}$ is prime by step [](#order){.pf-ref}; any $h\in H$ with $h\ne e$ has order greater than $1$ dividing $\abs{H}$, so its order is $\abs{H}$ and $H=\langle h\rangle$.
:::

:::

:::

:::
