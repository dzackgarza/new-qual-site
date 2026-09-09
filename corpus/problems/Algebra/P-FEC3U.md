---
schema: qual/card@1
id: P-FEC3U
kind: problem
title: The field with 25 elements
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
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
What's the field with 25 elements?
:::


::: {.solution}
Up to isomorphism there is a unique field with $25=5^2$ elements, namely $\FF_{25}$.
A concrete model is
\[
\FF_{25}\cong \FF_5[t]/(t^2+2).
\]

<1>1. The polynomial $t^2+2$ is irreducible over $\FF_5$.
::: {.proof}
A quadratic over a field is reducible iff it has a root. The squares in $\FF_5$ are $0,1,4$, while a root of $t^2+2$ would satisfy $t^2=3$. Since $3$ is not a square modulo $5$, there is no root.
:::

<1>2. Therefore the quotient is a field with $25$ elements.
::: {.proof}
Irreducibility makes $(t^2+2)$ maximal in $\FF_5[t]$. Every residue class has a unique representative $a+bt$ with $a,b\in\FF_5$, giving $5^2=25$ elements.
:::

Thus one may write
\[
\FF_{25}=\{a+b\alpha:a,b\in\FF_5,\ \alpha^2=3\}.
\]
:::
