---
schema: qual/card@1
id: P-UFRBU
kind: problem
title: "Let $\\{a_n\\}_{n=1}^\\infty \\subseteq \\mathbb{R}$"
classification:
  areas:
  - real-analysis
  topics:
  - variation
  - series-of-numbers
relations: []
review: draft
solved: true
---

::: problem
Let $\{a_n\}_{n=1}^\infty \subseteq \mathbb{R}$ and a strictly increasing sequence $\{x_n\}_{n=1}^\infty \subseteq (0,1)$ be given.
Assume that $\sum_{n=1}^\infty a_n$ is absolutely convergent, and define $\alpha \colon [0,1] \to \mathbb{R}$ by $$\alpha(x):= \begin{cases} a_n &  x=x_n \\ 0 & \text{otherwise} \end{cases}.$$ Prove or disprove: $\alpha$ has bounded variation on $[0,1]$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. $\alpha$ is bounded: $|\alpha(x)| \le \sum_n |a_n| < \infty$ for all $x$.
Proof: $\alpha(x) = a_n$ if $x = x_n$ and $0$ otherwise, so $|\alpha(x)| \le \sup_n |a_n| \le \sum_n |a_n|$, and $\sum_n |a_n|$ converges absolutely.
<1>2. Estimate the variation against a partition.
Proof: let $0 = t_0 < t_1 < \cdots < t_m = 1$ be any partition.
The value $\alpha$ takes on $\{t_0, \ldots, t_m\}$ differs from $0$ only at those $t_j$ that coincide with some $x_n$, where $\alpha(t_j) = a_n$; each $x_n$ can occur at most twice as a partition point adjacent pair boundary — precisely, the contribution of the single spike at $x_n$ to $\sum_j |\alpha(t_j) - \alpha(t_{j-1})|$ is at most $2|a_n|$ (the two differences involving the interval containing $x_n$, or the two differences at $t_j = x_n$). Hence \[ \sum_{j=1}^m |\alpha(t_j) - \alpha(t_{j-1})| \le 2\sum_n |a_n| . \] <1>3. $\alpha$ has bounded variation.
Proof: by <1>2, every partition has variation $\le 2\sum_n |a_n| < \infty$; taking the supremum, $V(\alpha) \le 2\sum_n|a_n| < \infty$.
(In fact $V(\alpha) = 2\sum_n|a_n|$: a partition through all $x_1, \ldots, x_N$ with midpoints between consecutive spikes has variation $2\sum_{n\le N}|a_n|$.)
<1>4. Q.E.D.
:::
