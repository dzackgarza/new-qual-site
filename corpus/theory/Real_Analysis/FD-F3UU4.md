---
schema: qual/card@1
id: FD-F3UU4
kind: definition
title: Uniform convergence of a sequence of functions
prompts:
- What does it mean for $f_n$ to converge uniformly to $f$ on $E$?
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
Let $E$ be a set, and let $f_n\colon E\to\RR$ for $n\geq 1$ and $f\colon E\to\RR$ be functions.
The sequence $(f_n)$ \dfn{converges uniformly} to $f$ on $E$ if for every $\varepsilon>0$ there exists $N=N(\varepsilon)$ such that $\abs{f_n(x) - f(x)} < \varepsilon$ for all $n\geq N$ and all $x\in E$.
:::

::: {.remark}
With $\norm{g}_\infty \coloneqq \sup_{x\in E}\abs{g(x)}$ for $g\colon E\to\RR$, the sequence $(f_n)$ converges uniformly to $f$ on $E$ if and only if $\norm{f_n - f}_\infty\to 0$ as $n\to\infty$.
:::
