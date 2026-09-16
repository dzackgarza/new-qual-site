---
schema: qual/card@1
id: PR-FKJCO
kind: proposition
title: The closed unit ball of $C([0,1])$ is not compact
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Function Spaces
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
Let $C([0,1])$ be the space of continuous functions $[0,1]\to\RR$ with the norm $\norm{f}_\infty\coloneqq\sup_{x\in[0,1]}\abs{f(x)}$.
The closed unit ball $B\coloneqq\theset{f\in C([0,1]) : \norm{f}_\infty\leq1}$ is not [[D-EILKJ|compact]].
:::

::: {.proof}
Let $f_n(x)\coloneqq x^n$, so $f_n\in B$.
If a subsequence $(f_{n_k})$ converged in $\norm{\cdot}_\infty$ to some $g\in C([0,1])$, then it would converge pointwise to $g$, so $g(x)=0$ for $0\leq x<1$ and $g(1)=1$, and $g$ would not be continuous.
Hence $(f_n)$ has no convergent subsequence, and the metric space $B$ is not sequentially compact, hence not compact.
:::
