---
schema: qual/card@1
id: P-HFGO10
kind: problem
title: Degree of a field's algebraic closure
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
What can be said about the degree of a field in its algebraic closure?
:::

::: {.solution}
The degree of an algebraic closure can only be
\[
[\overline F:F]\in\{1,2,\infty\}.
\]
More precisely:

::: pf

::: {.pf-step #s1}

One has $[\overline F:F]=1$ if and only if $F$ is algebraically closed.

::: pf-proof

This is immediate from the definition of an algebraic closure.

:::

:::

::: {.pf-step #s2}

If $1<[\overline F:F]<\infty$, then $F$ is real closed and
\[
[\overline F:F]=2,
\qquad
\overline F=F(i),\quad i^2=-1.
\]

::: pf-proof

This is the Artin--Schreier characterization of real closed fields: a field whose algebraic closure is a nontrivial finite extension is real closed, and its algebraic closure is obtained by adjoining $\sqrt{-1}$ and has degree $2$.

:::

:::

::: pf-step

Conversely, if $F$ is real closed, then
\[
[\overline F:F]=2.
\]

::: pf-proof

Again by the Artin--Schreier theorem, $F(i)$ is algebraically closed and $i\notin F$, so $F(i)/F$ is quadratic and is an algebraic closure of $F$.

:::

:::

::: pf-step

Therefore, for every field which is neither algebraically closed nor real closed,
\[
[\overline F:F]=\infty.
\]

::: pf-proof

If the degree were finite, steps [](#s1){.pf-ref} and [](#s2){.pf-ref} would force it to be $1$ or $2$, corresponding respectively to the algebraically closed and real closed cases.

:::

:::

:::

:::
