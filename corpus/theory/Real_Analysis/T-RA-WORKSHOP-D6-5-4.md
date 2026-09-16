---
schema: qual/card@1
id: T-RA-WORKSHOP-D6-5-4
kind: theorem
title: First fundamental theorem of calculus
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Differentiation
  - Continuity
relations: []
review: draft
---

::: {.theorem}
Let $a<b$, let $f\colon[a,b]\to\RR$ be Riemann integrable on $[a,b]$, and define $F\colon[a,b]\to\RR$ by
$$
F(x)\coloneqq\int_a^x f(t)\,dt.
$$
Then $F$ is continuous on $[a,b]$.
If $f$ is continuous at $x_0\in[a,b]$, then $F$ is differentiable at $x_0$, one-sidedly if $x_0\in\theset{a,b}$, and $F'(x_0)=f(x_0)$.
[@Rud76].
:::
