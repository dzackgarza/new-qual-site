---
schema: qual/card@1
id: FF-UQZNR
kind: fact
title: Laurent series of $1/\sin z$ at $0$
slogan: '$\csc z$ has principal part $1/z$ at $0$, and $\csc z-1/z=z/6+7z^3/360+O(z^5)$ is odd and holomorphic on $\abs{z}<\pi$.'
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
