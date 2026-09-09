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
Take the dual-number algebra
\[
A=\CC[\varepsilon]/(\varepsilon^2).
\]

<1>1. The ideal $J=(\varepsilon)$ is nonzero and nilpotent.
::: {.proof}
The class of $\varepsilon$ is nonzero in $A$, while
\[
J^2=(\varepsilon^2)=0.
\]
Thus $J$ is a nonzero nilpotent ideal.
:::

<1>2. The algebra $A$ is not semisimple.
::: {.proof}
A finite-dimensional semisimple algebra has zero Jacobson radical. Every nilpotent ideal lies in the Jacobson radical, so <1>1 gives
\[
0\ne J\subseteq \operatorname{Jac}(A).
\]
Hence $\operatorname{Jac}(A)\ne0$, and therefore $A$ is not semisimple.
:::

<1>3. Therefore $\CC[\varepsilon]/(\varepsilon^2)$ is a $\CC$-algebra that is not semisimple.
::: {.proof}
This is exactly <1>2.
:::
:::
