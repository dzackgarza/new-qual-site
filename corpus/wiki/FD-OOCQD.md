---
schema: qual/card@1
id: FD-OOCQD
kind: definition
title: (Lebesgue) Measurable Function
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
A function $f:X\to\bar\RR$ is **measurable** iff for all $\alpha \in \RR$, the following set is Lebesgue measurable:
$$
S_\alpha \definedas \theset{ x\in X \suchthat f(x) > \alpha}
.$$
:::
