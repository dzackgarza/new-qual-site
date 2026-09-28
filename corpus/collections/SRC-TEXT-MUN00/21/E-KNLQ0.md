---
schema: qual/card@1
id: E-KNLQ0
kind: problem
title: Uniform convergence as convergence in the uniform metric
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be a set, and let $f_n: X \to \mathbb{R}$ be a sequence of functions.
Let $\bar{\rho}$ be the uniform metric on the space $\mathbb{R}^X$.
Show that the sequence $(f_n)$ converges uniformly to the function $f: X \to \mathbb{R}$ if and only if the sequence $(f_n)$ converges to $f$ as elements of the metric space $(\mathbb{R}^X, \bar{\rho})$.
:::

::: {.solution}
The uniform metric is $\bar\rho(g,h)=\sup_{x\in X}\min\{\abs{g(x)-h(x)},1\}$.

<1>1. For $0<\varepsilon\le1$ and $g,h\colon X\to\RR$, $\bar\rho(g,h)<\varepsilon$ if and only if $\sup_x\abs{g(x)-h(x)}<\varepsilon$.

::: {.proof}
Always $\bar\rho(g,h)\le\sup_x\abs{g(x)-h(x)}$.
If $\bar\rho(g,h)<\varepsilon\le1$, then $\min\{\abs{g(x)-h(x)},1\}<1$ for every $x$, so the minimum is $\abs{g(x)-h(x)}$ and $\sup_x\abs{g(x)-h(x)}=\bar\rho(g,h)<\varepsilon$.
:::

<1>2. Q.E.D.

::: {.proof}
Uniform convergence $f_n\to f$ means that for every $\varepsilon>0$ there is $N$ with $\sup_x\abs{f_n(x)-f(x)}<\varepsilon$ for $n\ge N$, and convergence in $(\RR^X,\bar\rho)$ means the same with $\bar\rho(f_n,f)$ in place of the supremum.
It suffices to check both conditions for $\varepsilon\le1$, where step <1>1 shows that they coincide.
:::
:::
