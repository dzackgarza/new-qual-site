---
schema: qual/card@1
id: P-5UQSK
kind: problem
title: Equicontinuity on $[a,b]$ of differentiable functions with $\abs{f(a)}\le M$ and
  $\abs{f'}\le M$
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $M<\infty$ and $\mathcal{F} \subseteq C[a,b]$.
Assume that each $f \in \mathcal{F}$ is differentiable on $(a,b)$ and satisfies $\abs{f(a)} \leq M$ and $\abs{f'(x)} \leq M$ for all $x \in (a,b)$.
Prove that $\mathcal{F}$ is equicontinuous on $[a,b]$.
:::

::: {.solution}

If $\mathcal F$ is empty, equicontinuity is vacuous. Otherwise $\abs{f(a)}\le M$ for some $f$ gives $M\ge0$.

::: pf

::: {.pf-step #s1}

Every $f \in \mathcal F$ is Lipschitz with constant $M$: $\abs{f(x) - f(y)} \le M\abs{x - y}$ for all $x, y \in [a,b]$.

::: pf-proof

For $a\le x<y\le b$, continuity on $[x,y]$ and differentiability on $(x,y)$ permit the mean value theorem: there is $c\in(x,y)$ such that $f(y)-f(x)=f'(c)(y-x)$.
Taking absolute values proves the bound; the case $x=y$ is immediate.

:::

:::

::: pf-step

$\mathcal F$ is equicontinuous on $[a,b]$.

::: pf-proof

Given $\varepsilon>0$, let $\delta=\varepsilon/(M+1)>0$, which does not depend on $f$, $x$, or $y$. Whenever $x,y\in[a,b]$ satisfy $\abs{x-y}<\delta$, step [](#s1){.pf-ref} gives, for every $f\in\mathcal F$,
$$
\abs{f(x)-f(y)}\le M\abs{x-y}\le\frac{M}{M+1}\varepsilon<\varepsilon.
$$

:::

:::

:::

:::

::: {.remark}
The same Lipschitz estimate, with $\abs{f(a)}\le M$, gives the uniform bound $\abs{f(x)}\le M+M(b-a)$ for every $f\in\mathcal F$, so $\mathcal F$ is also uniformly bounded.
:::
