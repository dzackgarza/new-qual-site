---
schema: qual/card@1
id: P-YZNJU
kind: problem
title: The sum $\sum_{k=1}^n\sin kx$ via de Moivre's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Series of Numbers
relations: []
review: draft
---

::: problem
Use de Moivre's theorem (i.e. $\left(e^{i \theta}\right)^{n}==\cos n \theta+i \sin n \theta$, or $\left.(\cos \theta+i \sin \theta)^{n}=\cos n \theta+i \sin n \theta\right)$ to find the sum

$$
\sin x+\sin 2 x+\cdots+\sin n x
$$
:::

::: solution
For $e^{ix}\ne1$, the geometric-series identity gives
\[
\sum_{k=1}^n e^{ikx}
=e^{ix}\frac{1-e^{inx}}{1-e^{ix}}.
\]
Using
\[
1-e^{it}=-2i e^{it/2}\sin(t/2),
\]
this becomes
\[
\sum_{k=1}^n e^{ikx}
=e^{i(n+1)x/2}\frac{\sin(nx/2)}{\sin(x/2)}.
\]
Taking imaginary parts yields
\[
\boxed{
\sum_{k=1}^n\sin(kx)
=\frac{\sin(nx/2)\sin((n+1)x/2)}{\sin(x/2)}}
\]
whenever $x\notin2\pi\mathbb Z$. If $x\in2\pi\mathbb Z$, every summand is
zero, so the sum is $0$.
:::
