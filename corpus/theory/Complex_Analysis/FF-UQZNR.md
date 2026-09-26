---
schema: qual/card@1
id: FF-UQZNR
kind: fact
title: Laurent series of $1/\sin z$ at $0$
slogan: '$\csc z$ starts with the simple pole $z^{-1}$, followed by the odd regular terms $z/6+7z^3/360+O(z^5)$.'
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
For $0<\abs{z}<\pi$,
$$
{1\over \sin(z)} = \frac{1}{z}+\frac{1}{3 !} z+\frac{7}{360} z^{3}+O\qty{z^{5}}.
$$
:::
