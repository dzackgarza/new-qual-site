---
schema: qual/card@1
id: PR-LTRLV
kind: proposition
title: A differentiable function on an interval is Lipschitz if and only if its derivative is bounded
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Uniform Continuity
relations: []
review: draft
---

::: {.proposition}
Let $I\subseteq\RR$ be an interval with nonempty interior and let $f\colon I\to\RR$ be differentiable.
Then $f$ is Lipschitz, that is, there is $C\geq0$ with $\abs{f(x)-f(y)}\leq C\abs{x-y}$ for all $x,y\in I$, if and only if $f'$ is bounded on $I$.
In that case the smallest such constant is $C=\sup_{x\in I}\abs{f'(x)}$.
:::

::: {.example}
A Lipschitz function need not be differentiable: $x\mapsto\abs{x}$ on $(-1,1)$ satisfies $\abs{\abs x-\abs y}\leq\abs{x-y}$ and is not differentiable at $0$.
:::

::: {.example}
The interval hypothesis is needed: on $U\coloneqq(0,1)\cup(1,2)$, the function $f\coloneqq\chi_{(1,2)}$ is differentiable with $f'=0$, but $\abs{f(1+\delta)-f(1-\delta)}=1$ for $0<\delta<1$, so $f$ is not Lipschitz on $U$.
:::
