---
schema: qual/card@1
id: T-RA-WORKSHOP-D6-5-3
kind: theorem
title: Reduction of a Stieltjes integral to a Riemann integral
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Riemann Integrability
relations: []
review: draft
---

::: {.theorem}
Let $a<b$, let $\alpha\colon[a,b]\to\RR$ be monotonically increasing and differentiable with $\alpha'$ Riemann integrable on $[a,b]$, and let $f\colon[a,b]\to\RR$ be bounded.
Then $f\in\mathcal R(\alpha)$ on $[a,b]$ if and only if $f\alpha'$ is Riemann integrable on $[a,b]$, and in that case
$$
\int_a^b f\,d\alpha=\int_a^b f(x)\alpha'(x)\,dx.
$$
[@Rud76].
:::
