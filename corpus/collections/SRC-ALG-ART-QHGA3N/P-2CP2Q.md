---
schema: qual/card@1
id: P-2CP2Q
kind: problem
title: Galois group of $x^3-3x-3$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Splitting Fields
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
Compute the Galois group of $f(x) = x^3-3x -3\in \QQ[x]/\QQ$.
:::

::: {.solution}
<1>1. The polynomial $f(x)=x^3-3x-3$ is irreducible over $\QQ$.
::: {.proof}
A reducible cubic over $\QQ$ has a rational root. By the rational-root theorem, any
rational root of this monic polynomial must be one of $\pm1,\pm3$. Direct substitution
gives
\[
f(1)=-5,\quad f(-1)=-1,\quad f(3)=15,\quad f(-3)=-21,
\]
so there is no rational root.
:::

<1>2. The discriminant of $f$ is $-135$, which is not a square in $\QQ$.
::: {.proof}
For a depressed cubic $x^3+ax+b$, the discriminant is
\[
\Delta=-4a^3-27b^2.
\]
Here $a=-3$ and $b=-3$, so
\[
\Delta=-4(-3)^3-27(-3)^2=108-243=-135.
\]
Since $-135<0$, it is not a square in $\QQ$.
:::

<1>3. The Galois group of the splitting field of $f$ over $\QQ$ is $S_3$.
::: {.proof}
For an irreducible separable cubic over a field of characteristic different from $2$,
the Galois group acts transitively on the three roots, so it is either $A_3$ or $S_3$.
It is contained in $A_3$ exactly when the discriminant is a square in the base field. By
<1>1 and <1>2, the polynomial is irreducible and its discriminant is not a square, hence
\[
\operatorname{Gal}(f/\QQ)\cong S_3.
\]
:::
:::
