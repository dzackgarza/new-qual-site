---
schema: qual/card@1
id: FF-UQZNR
kind: fact
title: 'Inverting series: ${1\over \sin(z) } = \cdots$'
prompts:
- What is the Laurent expansion of $1/\sin(z)$ at the origin?
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Trigonometry
  - Power Series
relations: []
review: draft
---

::: {.fact}
$$
{1\over \sin(z)} = \frac{1}{z}+\frac{1}{3 !} z+\frac{7}{360} z^{3}+\mathrm{O}\left(z^{5}\right)
.$$
:::
