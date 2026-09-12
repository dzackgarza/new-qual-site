---
schema: qual/card@1
id: P-HGRO35
kind: problem
title: Normal terms in a composition series for S4
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Which groups in a composition series for $S_4$ are normal in $S_4$?
:::

::: solution
For the composition series
\[
1\triangleleft C_2\triangleleft V_4\triangleleft A_4\triangleleft S_4,
\qquad
C_2=\langle(12)(34)\rangle,
\]
the terms normal in the whole group $S_4$ are
\[
1,\qquad V_4,\qquad A_4,\qquad S_4.
\]
The subgroup $C_2$ is not normal in $S_4$.

<1>1. The groups $1$, $V_4$, $A_4$, and $S_4$ are normal in $S_4$.
::: proof
The trivial subgroup and $S_4$ are normal. The alternating group $A_4$ is the
kernel of the sign homomorphism, hence normal. The Klein four subgroup
\[
V_4=\{e,(12)(34),(13)(24),(14)(23)\}
\]
is preserved by conjugation because conjugation preserves cycle type, so it is
normal in $S_4$.
:::

<1>2. The subgroup $C_2=\langle(12)(34)\rangle$ is not normal in $S_4$.
::: proof
For example,
\[
(123)(12)(34)(123)^{-1}=(23)(14),
\]
which is not in $C_2$. Hence a conjugate of $C_2$ differs from $C_2$.
:::

<1>3. Therefore precisely the four displayed terms are normal in $S_4$.
::: proof
Combine <1>1 and <1>2.
:::
:::
