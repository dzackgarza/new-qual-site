---
schema: qual/card@1
id: E-3RLT2
kind: exercise
title: A sequentially compact metric space is totally bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: exercise
Show that a sequentially compact space is totally bounded.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $(X, d)$ be a sequentially compact metric space.
We want to prove that $X$ is totally bounded: for every $\varepsilon > 0$, $X$ can be covered by finitely many open balls of radius $\varepsilon$.

Suppose towards a contradiction that $X$ is not totally bounded for some $\varepsilon_0 > 0$.
We construct a sequence $(x_n)_{n=1}^\infty$ inductively as follows:
1. Choose an arbitrary point $x_1 \in X$.
2. Since $B(x_1, \varepsilon_0)$ does not cover $X$, choose $x_2 \in X \setminus B(x_1, \varepsilon_0)$.
   Then $d(x_2, x_1) \geq \varepsilon_0$.
3. Inductively, given $x_1, x_2, \ldots, x_k$ such that $d(x_i, x_j) \geq \varepsilon_0$ for all $1 \leq i < j \leq k$:
   Since $\bigcup_{i=1}^k B(x_i, \varepsilon_0)$ is a finite union of $\varepsilon_0$-balls and $X$ is not covered by any finite collection of $\varepsilon_0$-balls, there exists:
   $$
   x_{k+1} \in X \setminus \bigcup_{i=1}^k B(x_i, \varepsilon_0).
   $$
   By construction, $d(x_{k+1}, x_i) \geq \varepsilon_0$ for all $1 \leq i \leq k$.

In this way, we obtain an infinite sequence $(x_n)_{n=1}^\infty$ in $X$ such that:
$$
d(x_n, x_m) \geq \varepsilon_0 \quad \text{for all } n \neq m.
$$

Since $X$ is sequentially compact, the sequence $(x_n)$ must contain a convergent subsequence $(x_{n_k})_{k=1}^\infty$.
Every convergent sequence in a metric space is Cauchy, so there exists $N \in \mathbb{N}$ such that for all $j, k \geq N$:
$$
d(x_{n_j}, x_{n_k}) < \varepsilon_0.
$$
However, taking $j \neq k$, our sequence satisfies $d(x_{n_j}, x_{n_k}) \geq \varepsilon_0$, a direct contradiction.

Therefore, $X$ must be totally bounded.
:::
