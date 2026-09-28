---
schema: qual/card@1
id: E-6ULIT
kind: problem
title: Uniform limits preserve continuity and uniform continuity; pointwise limits
  need not
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Continuity
  - Uniform Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.exercise}
Show that a uniform limit of continuous functions is continuous, and a uniform limit of uniformly continuous functions is uniformly continuous.
Show that this is not true if uniform convergence is weakened to pointwise convergence.

:::

::: {.solution}
Suppose $\norm{f_n - f}_\infty\to 0$ and fix $\eps>0$. For all $z,w$ and $n$,
\[
\abs{f(z) - f(w)} \leq \abs{f(z) - f_n(z)} + \abs{f_n(z) - f_n(w)} + \abs{f_n(w) - f(w)}
\leq 2\norm{f-f_n}_\infty+\abs{f_n(z) - f_n(w)}
.\]
Choose $n$ with $\norm{f-f_n}_\infty<\eps/3$.

- Continuity: fix $z$. Since $f_n$ is continuous at $z$, there is $\delta>0$ with $\abs{f_n(z)-f_n(w)}<\eps/3$ for $\abs{z-w}<\delta$, and then $\abs{f(z)-f(w)}<\eps$.
- Uniform continuity: if $f_n$ is uniformly continuous, there is $\delta>0$ with $\abs{f_n(z)-f_n(w)}<\eps/3$ for all $z,w$ with $\abs{z-w}<\delta$, and then $\abs{f(z)-f(w)}<\eps$ for all such $z,w$.

The choice of one $n$ for all $z$ uses $\norm{f-f_n}_\infty<\eps/3$; pointwise convergence gives an $n$ depending on the point.

Pointwise limits: on $[0,1]$, the uniformly continuous functions $f_n(x) \da x^n$ converge pointwise to $\chi_{\theset{1}}$, which is not continuous, hence not uniformly continuous.

:::

