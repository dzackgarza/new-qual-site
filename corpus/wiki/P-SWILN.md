---
schema: qual/card@1
id: P-SWILN
kind: problem
title: "Let $\\gamma$ be a smooth curve joining two distinct points $a, b\\in \\C\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Let $\gamma$ be a smooth curve joining two distinct points $a, b\in \CC$.

Prove that the function
\[
f(z) \definedas \int_\gamma {g(w) \over w-z} \,dw
\]
is analytic in $\CC\setminus\gamma$.
:::

:::{.solution}
Toward applying Morera, let $T \subseteq \CC\sm \gamma$ be a triangle, so that $z\in T$ and $w\in \gamma$ implies $z-w\neq 0$.
Then
\[
\oint_T f(z) \dz 
&= \oint_T \int_\gamma {g(w)\over w-z}\dw\dz \\
&= \int_\gamma \oint_T {g(w)\over w-z}\dz\dw \\
&= \int_\gamma g(w) \qty{ \oint_T {1 \over w-z}\dz} \dw \\
&= \int_\gamma g(w) \cdot 0 \dw \\
&= 0
,\]
where the exchange of integrals is justified by compactness of $\gamma, T$, and the inner integral vanishes because for a fixed $w\in \gamma$, the function $z\mapsto {1\over w-z}$ has a simple pole at $w$, and so is holomorphic in $\gamma^c$ and vanishes by Goursat.
:::
