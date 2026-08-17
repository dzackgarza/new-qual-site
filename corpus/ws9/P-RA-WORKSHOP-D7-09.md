---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-09
kind: problem
title: 'A uniformly bounded derivative gives equicontinuity'
classification:
  areas:
  - real-analysis
  topics:
  - equicontinuity
  - differentiation
relations: []
review: draft
---

::: {.problem title="?"}
(January 2020 #4a) Let $M<\infty$ and $\mathcal F\subset C[a,b]$.
Assume that each $f\in\mathcal F$ is differentiable on $(a,b)$ and satisfies $|f(a)|\le M$ and $|f'(x)|\le M$ for all $x\in(a,b)$.
Prove that $\mathcal F$ is equicontinuous on $[a,b]$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Prove $\mathcal F \subset C[a,b]$ is equicontinuous when each $f \in \mathcal F$ is differentiable on $(a,b)$ with $|f(a)| \le M$ and $|f'(x)| \le M$.

<1>1. Every $f \in \mathcal F$ is Lipschitz with constant $M$ on $[a,b]$.
    Proof: for $a \le x < y \le b$, the Mean Value Theorem gives $f(y) - f(x) = f'(\xi)(y-x)$ for some $\xi \in (x,y) \subset (a,b)$, so $|f(y) - f(x)| \le M|y - x|$.

<1>2. Given $\varepsilon > 0$, the choice $\delta = \varepsilon/M$ works uniformly over $\mathcal F$.
    Proof: by <1>1, $|x - y| < \delta$ gives $|f(x) - f(y)| \le M|x-y| < M\delta = \varepsilon$ for every $f \in \mathcal F$ simultaneously. (If $M = 0$ take $\delta$ arbitrary, e.g. $\delta = 1$; then every $f$ is constant.)

<1>3. Q.E.D.
    Proof: <1>2 is the definition of equicontinuity on $[a,b]$ (indeed uniform equicontinuity).

:::
