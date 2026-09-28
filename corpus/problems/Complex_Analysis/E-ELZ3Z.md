---
schema: qual/card@1
id: E-ELZ3Z
kind: problem
title: A function with bounded derivative is uniformly continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Calculus
  - Mean Value Theorem
relations: []
review: draft
---

::: {.problem}
Show that $f'$ bounded implies $f$ is uniformly continuous.

:::

::: {.solution}
Let $f$ be real-valued and differentiable on an interval, with $\abs{f'}\le M$. For $x,y$ in the interval, the mean value theorem gives $\xi$ between $x$ and $y$ with
\[
\abs{f(x) - f(y)} = \abs{f'(\xi)} \abs{x-y} \le M\abs{x-y}
.\]
Given $\eps>0$, $\delta=\eps/M$ (any $\delta$ if $M=0$) satisfies $\abs{f(x)-f(y)}<\eps$ whenever $\abs{x-y}<\delta$, independently of $x$ and $y$.

:::

