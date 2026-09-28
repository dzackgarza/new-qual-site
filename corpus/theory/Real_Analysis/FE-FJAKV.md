---
schema: qual/card@1
id: FE-FJAKV
kind: example
title: The indicator of $\QQ\cap[0,1]$ is Lebesgue integrable but not Riemann integrable
prompts:
- Give a function that is Lebesgue integrable but not Riemann integrable.
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
  - Counterexamples
relations: []
review: draft
---

::: {.example}
Let $f\coloneqq\chi_{\QQ\cap[0,1]}\colon[0,1]\to\RR$, the Dirichlet function on $[0,1]$.

- The set $\QQ\cap[0,1]$ is countable, hence has Lebesgue measure $0$, so $f$ is Lebesgue measurable, $f = 0$ almost everywhere, and $\int_{[0,1]} f\,dm = 0$; in particular $f$ is [[D-R5DL3|integrable]].

- Every subinterval of $[0,1]$ of positive length contains both rational and irrational points, so for every partition $P$ of $[0,1]$ the upper Darboux sum is $U(f,P) = 1$ and the lower Darboux sum is $L(f,P) = 0$. Hence $f$ is not Riemann integrable.
:::
