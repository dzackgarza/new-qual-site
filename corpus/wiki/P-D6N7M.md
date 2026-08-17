---
schema: qual/card@1
id: P-D6N7M
kind: problem
title: "Show that if $x_n$ is a decreasing sequence of positive real\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
  - sequences-of-numbers
  - limits
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Show that if $x_n$ is a decreasing sequence of positive real numbers such that $\sum_{n=1}^\infty x_n$ converges, then
$$
\lim_{n\to\infty} n x_n = 0.
$$

:::

:::{.solution}
> See this MSE post for many solutions: <https://math.stackexchange.com/questions/4603/if-a-n-subset0-infty-is-non-increasing-and-sum-a-n-infty-then-lim>
> Note that the "obvious" thing here is fiddly: there are bounds on the slices
\[
(N-M \pm 1) x_N \leq  \sum_{M\leq k \leq N} a_k \leq (N-M\pm 1) x_M
,\]
but arranging it so that the constants match the indices in $(N-M \pm 1)x_N \approx Nx_N$ requires something clever.

Fix $\eps>0$, we'll find $n\gg 1$ so that $nx_n < \eps$.
Find $n, m$ with $n>m$ large enough so that
\[
\eps > \sum_{m+1\leq k \leq n} x_k \geq \sum_{m+1\leq k \leq n}x_n = (m-n)x_n
.\]
Then rearrange:
\[
\eps > (m-n)x_n \implies nx_n < \eps + mx_n
.\]
Now choose $n$ large enough so that $x_n < \eps$, which holds since $\sum x_n < \infty$, to obtain
\[
nx_n < \eps + m\eps = \eps(1+m) \to 0
.\]







:::
