---
schema: qual/card@1
id: P-P2W6W
kind: problem
title: A continuous function vanishing at $\pm\infty$ is uniformly continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Suppose $f: \mathbb{R} \to \mathbb{R}$ is continuous and $\lim_{x \to \pm \infty} f(x) = 0$.
Prove that $f$ is uniformly continuous on $\mathbb{R}$.
:::

::: solution
Fix $\varepsilon>0$. Since
\[
f(x)\longrightarrow0
\qquad(x\to\pm\infty),
\]
choose $M>0$ such that
\[
|x|\ge M\implies |f(x)|<\varepsilon/2.
\]

<1>1. By Heine--Cantor, $f$ is uniformly continuous on the compact interval
\[
[-M-1,M+1].
\]
Hence there is $\delta_0>0$ such that for $x,y$ in this interval,
\[
|x-y|<\delta_0\implies |f(x)-f(y)|<\varepsilon.
\]
Set
\[
\delta=\min\{1,\delta_0\}.
\]

<1>2. Let $|x-y|<\delta$.
<2>1. If both $x,y\in[-M-1,M+1]$, the compact-interval estimate applies.
<2>2. Otherwise, suppose for example $x>M+1$. Since $|x-y|<1$, one has $y>M$, so
\[
|f(x)-f(y)|\le |f(x)|+|f(y)|<\varepsilon.
\]
The case $x<-M-1$ is identical, and the same argument applies if $y$ is the point outside the compact interval.

Thus the same $\delta$ works for all $x,y\in\mathbb R$, so $f$ is uniformly continuous.
:::
