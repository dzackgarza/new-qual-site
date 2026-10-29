---
schema: qual/card@1
id: E-AMD-JGCVGZJE
kind: problem
title: $\units{R}$ need not be closed under addition
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the verbose counterexample by the universal nonzero-ring obstruction.
---

::: {.exercise}
Show that $R^\times$ need not be closed under addition.
:::

::: {.solution}
Take any nonzero ring $R$ with identity.
Both $1$ and $-1$ are units, while
$$
1+(-1)=0
$$
is not a unit.
Hence $R^\times$ need not be closed under addition.
In particular, in $\ZZ$ the units are $\pm1$, and the sums of two units are $-2$, $0$, and $2$, none of which is a unit.
:::
