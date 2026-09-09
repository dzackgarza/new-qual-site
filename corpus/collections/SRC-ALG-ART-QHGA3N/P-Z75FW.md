---
schema: qual/card@1
id: P-Z75FW
kind: problem
title: No simple group of order $148$
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Show that there exist no simple groups of order 148.
:::


::: {.solution}
<1>1. Let \(G\) be a group of order
\[
|G|=148=2^2\cdot37.
\]
If \(n_{37}\) denotes the number of Sylow \(37\)-subgroups, then
\[
n_{37}\mid4,
\qquad
n_{37}\equiv1\pmod{37}.
\]
::: {.proof}
These are the Sylow divisibility and congruence conditions.
:::

<1>2. One has \(n_{37}=1\).
::: {.proof}
The positive divisors of \(4\) are \(1,2,4\). Among these, only \(1\) is congruent to \(1\pmod{37}\).
:::

<1>3. Therefore \(G\) is not simple.
::: {.proof}
By <1>2, the Sylow \(37\)-subgroup is unique, hence normal. Its order is \(37\), so it is nontrivial and proper in \(G\). Thus \(G\) has a nontrivial proper normal subgroup and cannot be simple.
:::
:::
