---
schema: qual/card@1
id: FD-ZTRHG
kind: definition
title: Uniform convergence of a sequence of functions
prompts:
- What does uniform convergence of $\theset{f_n}$ to $f$ on $E$ require of $N$?
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
Let $E$ be a set, and let $f_n\colon E\to\CC$ for $n\geq 1$ and $f\colon E\to\CC$ be functions.
The sequence $(f_n)$ \dfn{converges uniformly} to $f$ on $E$ if for every $\varepsilon>0$ there exists $N\in\NN$ such that $\abs{f_n(x) - f(x)} < \varepsilon$ for all $n\geq N$ and all $x\in E$.
:::

::: {.proposition}
Let $E$, $(f_n)$, and $f$ be as in the definition, and put $\norm{f_n - f}_\infty \coloneqq \sup_{x\in E}\abs{f_n(x) - f(x)}\in[0,\infty]$.
Then $(f_n)$ converges uniformly to $f$ on $E$ if and only if $\norm{f_n - f}_\infty\to 0$ as $n\to\infty$.
:::

::: {.proof}
If $(f_n)$ converges uniformly to $f$, then for $\varepsilon>0$ and $N$ as in the definition, $\norm{f_n - f}_\infty \leq \varepsilon$ for all $n\geq N$, so $\norm{f_n - f}_\infty\to 0$.
Conversely, if $\norm{f_n - f}_\infty\to 0$, then for $\varepsilon>0$ there exists $N$ with $\norm{f_n - f}_\infty < \varepsilon$ for all $n\geq N$, and then $\abs{f_n(x) - f(x)}\leq\norm{f_n - f}_\infty<\varepsilon$ for all $n\geq N$ and $x\in E$.
:::
