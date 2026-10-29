---
schema: qual/card@1
id: D-YZC3C
kind: definition
title: Uniform convergence
prompts:
- What does it mean for $f_n$ to converge uniformly to $f$ on $S$?
- What does uniform convergence of $\theset{f_n}$ to $f$ on $S$ require of $n_0$?
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
relations: []
review: draft
---

::: {.definition}
Let $S$ be a set, and let $f_n\colon S\to\CC$ for $n\geq 1$ and $f\colon S\to\CC$ be functions.
The sequence $(f_n)$ \dfn{converges uniformly} to $f$ on $S$ if
$$
(\forall \varepsilon>0)\,(\exists n_0 = n_0(\varepsilon))\,(\forall x \in S)\,(\forall n>n_0)\quad \abs{f_n(x)-f(x)}<\varepsilon.
$$
:::

::: {.remark}
Negating the quantifiers, $(f_n)$ does not converge uniformly to $f$ on $S$ if and only if
$$
(\exists \varepsilon>0)\,(\forall n_0)\,(\exists x = x(n_0) \in S)\,(\exists n>n_0)\quad \abs{f_n(x)-f(x)} \geq \varepsilon.
$$
The point $x$ at which the estimate fails may depend on $n_0$.
:::

::: {.remark}
With $\norm{g}_\infty \coloneqq \sup_{x\in S}\abs{g(x)}$ for $g\colon S\to\CC$, the sequence $(f_n)$ converges uniformly to $f$ on $S$ if and only if $\norm{f_n - f}_\infty\to 0$ as $n\to\infty$, where $\norm{f_n-f}_\infty\in[0,\infty]$.
:::

::: {.remark title="Series"}
For functions $f_n\colon S\to\CC$, the series $\sum_{n=1}^{\infty}f_n$ \dfn{converges uniformly} to $f$ on $S$ if the partial sums $\sum_{n=1}^{N}f_n$ converge uniformly to $f$ on $S$ as $N\to\infty$.
:::
