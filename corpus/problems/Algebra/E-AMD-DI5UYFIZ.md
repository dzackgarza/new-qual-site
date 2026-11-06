---
schema: qual/card@1
id: E-AMD-DI5UYFIZ
kind: problem
title: $-1$ is the unique element of order $2$ in the quaternion group
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard computation, no repair needed), and the existing prose against a fresh
    re-derivation: (-1)^2 = 1 with -1 distinct from 1, so -1 has order 2; 1 has order
    1; and for u in {i,j,k} the element +-u has square u^2 = -1, so its order is
    neither 1 nor 2 while its fourth power is 1, hence its order is 4. Correct. The
    prose asserted (+-u)^2 = u^2 without comment; the proof obtains it from (-u)(-u)
    = (-1)^2 u^2, and states why -1 and 1 are distinct (the eight elements of Q_8 are
    distinct). No source solution is retained for this card, so no source comparison
    was made. What was not checked: any printed source.
---

::: {.exercise}
Show that the Quaternion group has only one element of order 2, namely $-1$.
:::

::: {.solution}
The quaternion group is $Q_8=\theset{\pm1,\pm i,\pm j,\pm k}$, the eight elements being distinct, with multiplication determined by $i^2=j^2=k^2=-1$ and $ij=k$, $jk=i$, $ki=j$.

::: pf

::: {.pf-step #squares}
$i^2=j^2=k^2=-1$ and $(-u)^2=u^2$ for $u\in\theset{i,j,k}$.

::: pf-proof
The first identities are part of the presentation. For the second, $(-u)(-u)=(-1)^2u^2=1\cdot u^2=u^2$, using that $-1$ is central of square $1$.
:::

:::

::: {.pf-step #minus-one}
$-1$ has order $2$ and $1$ has order $1$.

::: pf-proof
$(-1)^2=1$ and $-1\neq1$ because the eight elements $\pm1,\pm i,\pm j,\pm k$ are distinct, so $2$ is the least positive power of $-1$ equal to the identity. The identity has order $1$ by definition.
:::

:::

::: {.pf-step #others}
Each of $\pm i,\pm j,\pm k$ has order $4$.

::: pf-proof
Let $u\in\theset{i,j,k}$ and consider $\pm u$. By step [](#squares){.pf-ref}, $(\pm u)^2=u^2=-1\neq1$, so the order of $\pm u$ is not $1$ and not $2$; and $(\pm u)^4=\bigl((\pm u)^2\bigr)^2=(-1)^2=1$. The order of an element divides any exponent killing it, so the order of $\pm u$ divides $4$; it is neither $1$ nor $2$, hence it is $4$.
:::

:::

::: {.pf-step}
The unique element of order $2$ in the quaternion group is $-1$.

::: pf-proof
The eight elements are $1$, $-1$, and the six elements $\pm i,\pm j,\pm k$. By steps [](#minus-one){.pf-ref} and [](#others){.pf-ref} their orders are $1$, $2$, and $4$ respectively, so exactly one element, namely $-1$, has order $2$.
:::

:::

:::
:::
