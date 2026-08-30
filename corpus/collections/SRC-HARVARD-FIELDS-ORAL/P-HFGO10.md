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
---

::: problem
What can be said about the degree of a field in its algebraic closure?
:::

::: {.solution}
<1>1. If $F$ algebraically closed, $[\bar F:F]=1$ finite.
Proof: $F=\bar F$.

<1>2. If $F$ not algebraically closed, there is irreducible $f$ degree $>1$, adjoining root gives proper finite extension; iterating gives infinite tower, so $[\bar F:F]=\infty$.
Proof: infinite.

<1>3. Hence degree is $1$ if $F$ algebraically closed, else $\infty$.
Proof: <1>1 and <1>2.

<1>4. Q.E.D.
Proof: <1>3.
:::
