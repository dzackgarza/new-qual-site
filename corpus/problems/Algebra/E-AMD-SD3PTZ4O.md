---
schema: qual/card@1
id: E-AMD-SD3PTZ4O
kind: exercise
title: The union of two ideals need not be an ideal
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Show that the union of two ideals need not be an ideal.
:::

::: {.solution}
**Goal.** Show the union of two ideals need not be an ideal.

<1>1. Counterexample in $\ZZ$.
<2>1. Take the ideals $I = 2\ZZ$ and $J = 3\ZZ$.
::: {.proof}
these are ideals of $\ZZ$.
:::
<2>2. $2 \in I$ and $3 \in J$, so $2, 3 \in I \cup J$.
::: {.proof}
each lies in its own ideal.
:::
<2>3. $2 + 3 = 5 \notin I \cup J$.
::: {.proof}
$5$ is not divisible by $2$ (so $5 \notin 2\ZZ$) and not divisible by $3$ (so $5 \notin 3\ZZ$).
:::
<2>4. Hence $I \cup J$ is not closed under addition, so it is not an ideal.
::: {.proof}
an ideal must be closed under addition.
:::

<1>2. Q.E.D.
::: {.proof}
<1>1 gives a union of two ideals that is not an ideal.
:::
:::
