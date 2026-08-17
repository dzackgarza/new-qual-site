---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-07
kind: problem
title: 'Compactness of infinite unions and attainment of distance to a compact set'
classification:
  areas:
  - real-analysis
  topics:
  - compactness
  - metric-spaces
  - counterexamples
relations: []
review: draft
---

::: {.problem title="?"}
(June 2003, #1b,c)

(b) Show by example that the union of infinitely many compact subsets of a metric space need not be compact.

(c) If $(X,d)$ is a metric space and $K\subset X$ is compact, define $$d(x_0,K)=\inf_{y\in K}d(x_0,y).$$ Prove that there exists a point $y_0\in K$ such that $d(x_0,K)=d(x_0,y_0)$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (b) Example: in the metric space $\mathbb{R}$, take $K_n = [0,\, 1 - 1/n]$ for $n \ge 2$.
    Proof: each $K_n$ is a closed bounded interval, hence compact in $\mathbb{R}$. But $\bigcup_n K_n = [0,1)$, which is not compact: the sequence $x_n = 1 - 1/n \in [0,1)$ converges to $1 \notin [0,1)$, and since $[0,1)$ is not closed in $\mathbb{R}$ (equivalently, the open cover $\{(-\infty, 1 - 1/2)\}\cup\{(1 - 1/(n+1), 1): n \ge 1\}$ has no finite subcover), it is not compact.
<1>2. (c) There is $y_0 \in K$ with $d(x_0, K) = d(x_0, y_0)$.
    Proof: by definition of the infimum there is a sequence $(y_n)$ in $K$ with $d(x_0, y_n) \to d(x_0, K)$. Since $K$ is compact (hence sequentially compact in the metric space $X$), a subsequence $y_{n_j} \to y_0 \in K$. The map $x \mapsto d(x_0, x)$ is 1-Lipschitz, hence continuous, so $d(x_0, y_0) = \lim_j d(x_0, y_{n_j}) = d(x_0, K)$.
<1>3. Q.E.D.
:::
