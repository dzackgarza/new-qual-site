---
schema: qual/card@1
id: T-RA-WORKSHOP-D7-6-3
kind: theorem
title: Uniform limits of Riemann--Stieltjes integrable functions
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $a<b$, let $\alpha\colon[a,b]\to\RR$ be monotonically increasing, and let $\mathcal R(\alpha)$ denote the set of bounded functions $[a,b]\to\RR$ that are Riemann--Stieltjes integrable with respect to $\alpha$ on $[a,b]$.
Let $f_n\in\mathcal R(\alpha)$ for $n\geq1$, and let $f\colon[a,b]\to\RR$.
If $f_n\to f$ [[D-RA-WORKSHOP-D7-CONVERGENCE|uniformly]] on $[a,b]$, then $f\in\mathcal R(\alpha)$, the limit $\lim_{n\to\infty}\int_a^b f_n\,d\alpha$ exists, and
$$
\lim_{n\to\infty}\int_a^b f_n\,d\alpha=\int_a^b f\,d\alpha.
$$
:::
