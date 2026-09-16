---
schema: qual/card@1
id: FT-OGS76
kind: theorem
title: Egorov's theorem
prompts:
- State Egorov's theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Egorov
  - Convergence of Functions
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $m$ be Lebesgue measure on $\RR^n$, let $E\subseteq \RR^n$ be [[D-MDJII|Lebesgue measurable]] with $m(E) < \infty$, and let $f_n\colon E\to\RR$ for $n\geq1$ and $f\colon E\to\RR$ be [[D-DHFN4|measurable]] with $f_n \to f$ almost everywhere on $E$.
Then for every $\varepsilon > 0$ there exists a closed set $F\subseteq E$ such that $m(E\setminus F)<\varepsilon$ and $f_n\to f$ [[D-YZC3C|uniformly]] on $F$.
:::
