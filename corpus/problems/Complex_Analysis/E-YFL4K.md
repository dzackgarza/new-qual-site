---
schema: qual/card@1
id: E-YFL4K
kind: problem
title: Uniformly bounded but not equicontinuous
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Counterexamples
  - Sequences of Functions
relations: []
review: draft
---

::: {.exercise}
Produce a sequence that is uniformly bounded but not equicontinuous.
:::

::: {.solution}
Let $f_k(x)\coloneqq\sin(kx)$ on $(0,1)$.

::: pf

::: pf-step
$\abs{f_k}\le1$ for all $k$.

::: pf-proof
$\abs{\sin t}\le1$ for real $t$.
:::

:::

::: pf-step
The family $\{f_k\}$ is not equicontinuous at any $x_0\in(0,1)$.

::: pf-proof
Fix $\delta>0$ with $(x_0-\delta,x_0+\delta)\subseteq(0,1)$.
For $k>\pi/\delta$, the image of $(x_0-\delta,x_0+\delta)$ under $x\mapsto kx$ is an interval of length $2k\delta>2\pi$, so $f_k$ takes both values $1$ and $-1$ there.
One of these differs from $f_k(x_0)$ by at least $1$, so there is $x$ with $\abs{x-x_0}<\delta$ and $\abs{f_k(x)-f_k(x_0)}\ge1$.
Since $\delta$ is arbitrary, equicontinuity at $x_0$ fails with $\varepsilon = 1$.
:::

:::

:::

:::
