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

This is the Laurent development of [@Ahl73, ch. 5, §1.3, The Laurent Series] on the annulus $0<\abs z<\pi$: the section gives the coefficients of $\sum A_n(z-a)^n$ by its formula (3) and those of the negative powers by the integral that follows it, both taken on a circle about $a=0$ inside the annulus. The principal part is the single term $1/z$ because $\sin z$ has a simple zero at $0$, and the odd coefficients are those integrals evaluated on a small circle.
:::
