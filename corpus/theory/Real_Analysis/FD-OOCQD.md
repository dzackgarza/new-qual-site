---
schema: qual/card@1
id: FD-OOCQD
kind: definition
title: Lebesgue measurable functions
prompts:
- Which sets must be Lebesgue measurable for $f$ to be a measurable function?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $X\subseteq\RR^n$ be [[D-MDJII|Lebesgue measurable]] and let $f\colon X\to[-\infty,\infty]$.
The function $f$ is \dfn{measurable} if for every $\alpha \in \RR$ the set
$$
S_\alpha \coloneqq \theset{ x\in X \suchthat f(x) > \alpha}
$$
is Lebesgue measurable.
:::
