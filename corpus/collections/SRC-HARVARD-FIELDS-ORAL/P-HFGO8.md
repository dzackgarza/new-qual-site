---
schema: qual/card@1
id: P-HFGO8
kind: problem
title: Algebraically closed fields and splitting polynomials
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Define an algebraically closed field.
Define what it means for a polynomial to split over a field.
:::

::: {.solution}
<1>1. A field $F$ is **algebraically closed** if every nonconstant polynomial in $F[x]$ has a root in $F$.
::: {.proof}
Equivalently, every nonconstant polynomial in $F[x]$ splits completely into linear factors over $F$.
Indeed, once a root $a\in F$ is found, the factor theorem writes $f(x)=(x-a)g(x)$ with $g\in F[x]$, and induction on the degree gives a complete linear factorization.
The converse is immediate.
:::

<1>2. A nonzero polynomial $f(x)\in F[x]$ of degree $n$ **splits over $F$** if there exist $c\in F^\times$ and $a_1,\ldots,a_n\in F$ such that
\[
f(x)=c\prod_{i=1}^n (x-a_i).
\]
::: {.proof}
Thus all roots of $f$ lie in $F$, with the list $a_1,\ldots,a_n$ recording multiplicities.
Equivalently, every irreducible factor of $f$ over $F$ has degree $1$.
:::
:::
