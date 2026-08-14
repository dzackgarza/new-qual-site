---
schema: qual/card@1
id: E-M3IWM
kind: exercise
title: "Stein/Shakarchi 1.20: Series convergence on the circle"
classification:
  areas:
  - complex-analysis
  topics:
  - convergence-tests
  - power-series
  - series-of-functions
relations: []
review: draft
---
:::{.exercise title="Stein/Shakarchi 1.20: Series convergence on the circle"}
Show that

1. $\sum kz^k$ diverges on $S^1$.
2. $\sum k^{-2} z^k$ converges on $S^1$.
3. $\sum k\inv z^k$ converges on $S^1\sm\ts{1}$ and diverges at $1$.
:::

:::{.solution}

1. Use that $\abs{z^k} = 1$ and $\sum c_kz^k < \infty \implies \abs{c_k} \to 0$, but $\abs{kz^k} = \abs{k} \to \infty$ on $S^1$.
2. Use that absolutely convergent implies convergent, and $\sum \abs{k^{-2} z^k} = \sum \abs{k^{-2}}$ converges by the $p\dash$test.
3. If $z=1$, this is the harmonic series. 
  Otherwise take $a_k = 1/k, b_k = e^{i k \theta}$ where $\theta \in (0, 2\pi)$ is some constant, and apply Dirichlet's test.
  It suffices to bound the partial sums of the $b_k$.
  Recalling that $\sum_{k\leq N} r^k = (1-r^{N+1}) / (1-r)$,
  \[
  \norm{ \sum_{k\leq m} e^{ik\theta } } = \norm{1 - e^{i(m+1)\theta} \over 1 - e^{i\theta}} \leq {2 \over \norm{ 1- e^{i\theta}}} \da M
  ,\]
  which is a constant.
  Here we've used that two points on $S^1$ are at most distance 2 from each other.
:::

