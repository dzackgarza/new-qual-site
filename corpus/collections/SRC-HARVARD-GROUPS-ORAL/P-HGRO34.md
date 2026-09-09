---
schema: qual/card@1
id: P-HGRO34
kind: problem
title: A composition series for S4
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
Write down a composition series for $S_4$.
:::

::: solution
Let
\[
V_4=\{e,(12)(34),(13)(24),(14)(23)\}
\]
and let
\[
C_2=\langle(12)(34)\rangle.
\]
Then
\[
1\triangleleft C_2\triangleleft V_4\triangleleft A_4\triangleleft S_4
\]
is a composition series.

<1>1. Each term is normal in the next.
::: proof
The subgroup $C_2$ is normal in the abelian group $V_4$. The Klein four group
$V_4$ is normal in $A_4$ because it is the union of the identity and the three
double transpositions, a conjugacy-stable set. Finally $A_4$ has index $2$ in
$S_4$, hence is normal.
:::

<1>2. Each factor is simple.
::: proof
The factor orders are
\[
|C_2|=2,
\qquad
|V_4/C_2|=2,
\qquad
|A_4/V_4|=3,
\qquad
|S_4/A_4|=2.
\]
Every group of prime order is simple.
:::

<1>3. Hence the displayed chain is a composition series for $S_4$.
::: proof
By <1>1 it is a subnormal series, and by <1>2 all composition factors are
simple.
:::
:::
