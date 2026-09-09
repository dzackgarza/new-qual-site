---
schema: qual/card@1
id: P-CYSD6
kind: problem
title: Disjoint cycles commute
classification:
  areas:
  - algebra
  topics:
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
- Show that disjoint cycles commute.
:::


::: {.solution}
Let
\[
\sigma=(a_1\,\dots\,a_r),\qquad \tau=(b_1\,\dots\,b_s)
\]
be disjoint cycles.

<1>1. For every point $x$, one has
\[
\sigma\tau(x)=\tau\sigma(x).
\]
::: {.proof}
There are three cases.

If $x$ lies in the support of $\sigma$, then $x$ is fixed by $\tau$ because the supports are disjoint. Also $\sigma(x)$ still lies in the support of $\sigma$, so it is fixed by $\tau$. Hence
\[
\sigma\tau(x)=\sigma(x)=\tau\sigma(x).
\]

If $x$ lies in the support of $\tau$, the same argument with the roles reversed gives
\[
\sigma\tau(x)=\tau(x)=\tau\sigma(x).
\]

If $x$ lies in neither support, both cycles fix $x$, so both composites fix $x$.
:::

<1>2. Therefore $\sigma\tau=\tau\sigma$.
::: {.proof}
Two permutations are equal when they agree on every point, and <1>1 shows exactly that.
:::
:::
