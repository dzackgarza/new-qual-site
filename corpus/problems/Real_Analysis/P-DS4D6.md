---
schema: qual/card@1
id: P-DS4D6
kind: problem
title: Continuous functions on compact sets are uniformly continuous
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Compactness
  - Continuity
relations: []
review: draft
---

::: {.problem}
Show that a continuous function on a compact set is uniformly continuous.
:::

::: {.solution}
Let $(K,d)$ be a compact metric space, $f\colon K \to \RR$ continuous, and $\eps > 0$.

<1>1. For each $z \in K$ there is $\delta_z > 0$ with $|f(x) - f(z)| < \eps/2$ whenever $d(x,z) < \delta_z$.

::: {.proof}
This is continuity of $f$ at $z$.
:::

<1>2. There are $z_1, \ldots, z_m \in K$ with $K = \bigcup_{i=1}^m B(z_i, \delta_{z_i}/2)$.

::: {.proof}
The balls $B(z, \delta_z/2)$, $z \in K$, form an open cover of the compact space $K$.
:::

<1>3. Q.E.D.

::: {.proof}
Put $\delta = \min_i \delta_{z_i}/2 > 0$ and let $d(x,y) < \delta$. By step <1>2, $d(x, z_i) < \delta_{z_i}/2$ for some $i$, and then $d(y, z_i) < \delta + \delta_{z_i}/2 \le \delta_{z_i}$. By step <1>1, $|f(x) - f(y)| \le |f(x) - f(z_i)| + |f(z_i) - f(y)| < \eps$.
:::
:::

::: {.solution title="Sequential compactness"}
Suppose, toward a contradiction, that $f$ is not uniformly continuous on a compact metric space $K$. Then there is $\eps > 0$ such that for every $n \in \NN$ there exist $x_n, y_n \in K$ with $d(x_n, y_n) < 1/n$ but $|f(x_n) - f(y_n)| \ge \eps$. Compactness of $K$ gives a subsequence $x_{n_j} \to x \in K$; then $d(y_{n_j}, x) \le d(y_{n_j}, x_{n_j}) + d(x_{n_j}, x) \to 0$, so $y_{n_j} \to x$ as well. Continuity of $f$ at $x$ forces $|f(x_{n_j}) - f(y_{n_j})| \to 0$, contradicting $|f(x_{n_j}) - f(y_{n_j})| \ge \eps$.
:::
