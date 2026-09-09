---
schema: qual/card@1
id: E-FB9OZ
kind: problem
title: Closure of the eventually-zero sequences in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Closure
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $\mathbb{R}^\infty$ be the subset of $\mathbb{R}^\omega$ consisting of all sequences that are eventually zero.
What is the closure of $\mathbb{R}^\infty$ in $\mathbb{R}^\omega$ in the uniform topology?
Justify your answer.
:::

::: {.solution}
Let $c_0$ denote the set of sequences converging to $0$. We claim
\[
\overline{\mathbb R^\infty}^{\,\bar\rho}=c_0.
\]

First take $x=(x_i)\in c_0$. Given $0<\varepsilon<1$, choose $N$ such that
\[
|x_i|<\varepsilon\qquad(i>N).
\]
Let
\[
y=(x_1,\dots,x_N,0,0,\dots)\in\mathbb R^\infty.
\]
Then
\[
\bar\rho(x,y)=\sup_{i>N}|x_i|<\varepsilon,
\]
so every uniform neighborhood of $x$ meets $\mathbb R^\infty$.

Conversely, suppose $x$ does not converge to $0$. Then there is $\varepsilon\in(0,1)$ such that $|x_i|\ge\varepsilon$ for infinitely many $i$. For any eventually-zero $y$, choose such an $i$ beyond the last nonzero coordinate of $y$. Then
\[
\bar\rho(x,y)\ge\min\{|x_i|,1\}\ge\varepsilon.
\]
Hence the uniform ball $B_{\bar\rho}(x,\varepsilon)$ contains no eventually-zero sequence. Thus $x$ is not in the closure.
:::
