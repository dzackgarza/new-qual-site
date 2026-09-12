---
schema: qual/card@1
id: P-E54MV
kind: problem
title: Galois group of $x^3-3x-3$ over $\QQ$ is $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Irreducibility Criteria
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
Show that the Galois group over $\QQ$ of
\[
f(x)=x^3-3x-3
\]
is isomorphic to $S_3$.
:::


::: {.solution}
<1>1. The polynomial $f$ is irreducible over $\QQ$.
::: {.proof}
Apply Eisenstein's criterion with the prime $3$. The leading coefficient is $1$, so it is not divisible by $3$. Every lower coefficient is divisible by $3$, and the constant term $-3$ is not divisible by $9$. Hence $f$ is irreducible over $\QQ$.
:::

<1>2. The discriminant of $f$ is
\[
\Delta=-135.
\]
::: {.proof}
For a depressed cubic
\[
x^3+ax+b,
\]
the discriminant is
\[
-4a^3-27b^2.
\]
Here $a=-3$ and $b=-3$, so
\[
\Delta=-4(-3)^3-27(-3)^2
=108-243
=-135.
\]
:::

<1>3. The Galois group is $S_3$.
::: {.proof}
Because $f$ is an irreducible cubic, its Galois group acts transitively on the three roots. Thus it is either $A_3$ or $S_3$.

For an irreducible cubic over a field of characteristic different from $2$, the Galois group lies in $A_3$ exactly when the discriminant is a square in the base field. Here $-135$ is not a square in $\QQ$. Therefore the Galois group is not contained in $A_3$, so it must be $S_3$.
:::
:::
