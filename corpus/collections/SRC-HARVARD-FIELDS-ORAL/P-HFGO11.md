---
schema: qual/card@1
id: P-HFGO11
kind: problem
title: Degree of the algebraic closure of the rationals
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Determine $[\overline{\mathbb Q}:\mathbb Q]$.
:::

::: {.solution}
One has
\[
[\overline{\mathbb Q}:\mathbb Q]=\infty.
\]

<1>1. For every integer $n\ge1$, the field $\overline{\mathbb Q}$ contains a finite extension of $\mathbb Q$ of degree $n$.
::: {.proof}
The polynomial $x^n-2\in\mathbb Q[x]$ is irreducible by Eisenstein's criterion at $2$. Hence, for any root $\alpha_n\in\overline{\mathbb Q}$,
\[
[\mathbb Q(\alpha_n):\mathbb Q]=n.
\]
:::

<1>2. Therefore $[\overline{\mathbb Q}:\mathbb Q]$ is infinite.
::: {.proof}
If $[\overline{\mathbb Q}:\mathbb Q]=N<\infty$, then every intermediate finite extension $K/\mathbb Q$ would satisfy
\[
[K:\mathbb Q]\le N.
\]
Taking $K=\mathbb Q(\alpha_n)$ with $n>N$ contradicts <1>1.
:::
:::
