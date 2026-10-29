---
schema: qual/card@1
id: P-5VEUZ
kind: problem
title: Monotone pointwise convergence to $0$ of continuous functions on $[0,1]$ is
  uniform
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Compactness
  - Continuity
relations: []
review: draft
---

::: {.problem}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of continuous functions $f_n: [0, 1]\to \RR$ such that
$$
f_n(x) \geq f_{n+1}(x) \geq 0 \quad \forall n\in \NN,\, \forall x\in [0, 1].
$$
Prove that if $\theset{f_n}$ converges pointwise to $0$ on $[0, 1]$ then it converges to $0$ uniformly on $[0, 1]$.
:::

::: {.solution}
Fix $\varepsilon>0$.

::: pf

::: {.pf-step #local}
Each $x\in[0,1]$ has an open neighbourhood $U_x$ and an index $M_x$ such that $0\le f_n(y)<\varepsilon$ for all $y\in U_x\cap[0,1]$ and all $n\ge M_x$.

::: pf-proof
By pointwise convergence choose $M_x$ with $f_{M_x}(x)<\varepsilon$.
Since $f_{M_x}$ is continuous, there is an open $U_x\ni x$ with $f_{M_x}(y)<\varepsilon$ for $y\in U_x\cap[0,1]$.
For $n\ge M_x$, monotonicity gives $0\le f_n(y)\le f_{M_x}(y)<\varepsilon$.
:::

:::

::: pf-step
There is $N$ with $\sup_{x\in[0,1]}\abs{f_n(x)}<\varepsilon$ for all $n\ge N$, so $f_n\to0$ uniformly.

::: pf-proof
The sets $U_x$ of step [](#local){.pf-ref} cover the compact set $[0,1]$, so finitely many $U_{x_1},\ldots,U_{x_m}$ cover it.
Let $N\coloneqq\max_i M_{x_i}$.
Each $y\in[0,1]$ lies in some $U_{x_i}$, and $n\ge N\ge M_{x_i}$ gives $0\le f_n(y)<\varepsilon$.
:::

:::

:::

:::
