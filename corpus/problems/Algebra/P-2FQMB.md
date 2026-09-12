---
schema: qual/card@1
id: P-2FQMB
kind: problem
title: A non-semisimple $\CC$-algebra
classification:
  areas:
  - algebra
  topics:
  - Semisimplicity
  - Algebras
  - Counterexamples
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
Give an example of a $\CC\dash$algebra which is not semisimple.
:::

::: {.solution}
<1>1. Let
\[
A=\mathbb C[\varepsilon]/(\varepsilon^2).
\]
Then $A$ is a two-dimensional unital $\mathbb C$-algebra with basis $1,\varepsilon$ and relation $\varepsilon^2=0$.
::: {.proof}
Every class modulo $(\varepsilon^2)$ has a unique representative $a+b\varepsilon$ with $a,b\in\mathbb C$.
:::

<1>2. The one-dimensional subspace
\[
J=\mathbb C\varepsilon
\]
is a nonzero left ideal of $A$.
::: {.proof}
For $a+b\varepsilon\in A$ and $c\varepsilon\in J$,
\[
(a+b\varepsilon)(c\varepsilon)=ac\varepsilon+bc\varepsilon^2=ac\varepsilon\in J.
\]
Also $\varepsilon\neq0$ in $A$, so $J\neq0$.
:::

<1>3. The ideal $J$ has no complementary left ideal in the regular left $A$-module $A$.
::: {.proof}
Suppose
\[
A=J\oplus K
\]
for a left ideal $K$.
Since $\dim_{\mathbb C}A=2$ and $\dim_{\mathbb C}J=1$, one has $\dim_{\mathbb C}K=1$.
Choose a nonzero element
\[
k=a+b\varepsilon\in K.
\]
Because $K$ is a left ideal,
\[
\varepsilon k=a\varepsilon\in K.
\]
If $a\neq0$, then $\varepsilon\in K$, contradicting $J\cap K=0$.
Thus $a=0$, so $k=b\varepsilon\in J$. Since $k\neq0$, this again contradicts $J\cap K=0$.
Therefore no such $K$ exists.
:::

<1>4. Hence $A$ is not semisimple.
::: {.proof}
A ring is semisimple precisely when its regular left module is semisimple; equivalently, every left ideal is a direct summand of the regular module.
By <1>2 and <1>3, the left ideal $J$ is not a direct summand of $A$.
:::
:::
