---
schema: qual/card@1
id: FT-XIVPL
kind: theorem
title: Lusin's theorem
slogan: 'A measurable function on a set of finite measure has a continuous restriction to a closed subset whose complement has arbitrarily small measure.'
prompts:
- State Lusin's theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Continuity
relations: []
review: draft
---

::: {.theorem}
Let $m$ be Lebesgue measure on $\RR^n$, let $E\subseteq\RR^n$ be [[D-MDJII|Lebesgue measurable]] with $m(E) < \infty$, and let $f\colon E\to\RR$ be [[D-DHFN4|measurable]].
Then for every $\varepsilon>0$ there exists a closed set $F\subseteq E$ such that $m(E\setminus F) < \varepsilon$ and the restriction $f|_F$ is continuous.
:::
