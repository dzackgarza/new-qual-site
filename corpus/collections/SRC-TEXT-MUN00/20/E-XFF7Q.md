---
schema: qual/card@1
id: E-XFF7Q
kind: problem
title: Uniform balls are not products of intervals
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $\bar{\rho}$ be the uniform metric on $\mathbb{R}^\omega$.
Given $\mathbf{x} = (x_1, x_2, \ldots) \in \mathbb{R}^\omega$ and given $0 < \epsilon < 1$, let

$$
U(\mathbf{x}, \epsilon) = (x_1 - \epsilon, x_1 + \epsilon) \times \dots \times (x_n - \epsilon, x_n + \epsilon) \times \dots.
$$

(a) Show that $U(\mathbf{x}, \epsilon)$ is not equal to the $\epsilon$-ball $B_{\bar{\rho}}(\mathbf{x}, \epsilon)$.

(b) Show that $U(\mathbf{x}, \epsilon)$ is not even open in the uniform topology.

(c) Show that

$$
B_{\bar{\rho}}(\mathbf{x}, \epsilon) = \bigcup_{\delta < \epsilon} U(\mathbf{x}, \delta).
$$
:::

::: {.solution}
For $0<\varepsilon<1$, the uniform metric is
\[
\bar\rho(\mathbf x,\mathbf y)=\sup_i\min\{|x_i-y_i|,1\}.
\]

(a) Define
\[
y_i=x_i+\varepsilon\left(1-\frac1{i+1}\right).
\]
Then $|y_i-x_i|<\varepsilon$ for every $i$, so $\mathbf y\in U(\mathbf x,\varepsilon)$. But
\[
\bar\rho(\mathbf x,\mathbf y)=\sup_i|x_i-y_i|=\varepsilon,
\]
so $\mathbf y\notin B_{\bar\rho}(\mathbf x,\varepsilon)$. Thus the two sets are not equal.

(b) Use the same $\mathbf y\in U(\mathbf x,\varepsilon)$. Given any $r>0$, choose $i$ so large that
\[
\varepsilon-|y_i-x_i|<r/2.
\]
Alter only the $i$th coordinate, increasing it by some $s<r$ large enough that the new coordinate lies outside $(x_i-\varepsilon,x_i+\varepsilon)$. The resulting point $\mathbf z$ satisfies
\[
\bar\rho(\mathbf y,\mathbf z)<r
\]
but $\mathbf z\notin U(\mathbf x,\varepsilon)$. Hence no uniform ball about $\mathbf y$ lies inside $U(\mathbf x,\varepsilon)$, so this set is not uniform-open.

(c) If $\mathbf y\in U(\mathbf x,\delta)$ for some $\delta<\varepsilon$, then
\[
\bar\rho(\mathbf x,\mathbf y)\le\delta<\varepsilon,
\]
so $\mathbf y$ lies in the $\varepsilon$-ball. Conversely, if
\[
s=\bar\rho(\mathbf x,\mathbf y)<\varepsilon,
\]
choose $\delta$ with $s<\delta<\varepsilon$. Since $\delta<1$, the inequality defining $s$ implies
\[
|x_i-y_i|<\delta
\]
for every $i$. Thus $\mathbf y\in U(\mathbf x,\delta)$. Therefore
\[
B_{\bar\rho}(\mathbf x,\varepsilon)=\bigcup_{\delta<\varepsilon}U(\mathbf x,\delta).
\]
:::
