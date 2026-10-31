---
schema: qual/card@1
id: P-TCJBY
kind: problem
title: A sup-norm-closed subspace of $C[0,1]$ complete in $\norm{\cdot}_2$ is finite-dimensional
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Norms
  - Closure
relations: []
review: draft
---

Consider the space $C([0,1])$ of real-valued continuous functions on $[0,1]$, with the supremum norm $\norm{f}_\infty\coloneqq\sup_{x\in[0,1]}\abs{f(x)}$ and the $L^2$-norm $\norm{f}_2\coloneqq\left(\int_0^1\abs{f(x)}^2\,dx\right)^{1/2}$.
Let $S$ be a closed linear subspace of $(C([0,1]),\norm{\cdot}_\infty)$.
Show that if $S$ is complete in the norm $\norm{\cdot}_2$, then $S$ is finite-dimensional.
:::

::: {.solution}
Consider the identity map $id : (S,\norm{\cdot}_\infty) \to (S,\norm{\cdot}_2)$ is bounded since $\norm{f}_2 \le \norm{f}_\infty$ on $[0,1]$. Both norms are complete on $S$, so by the open mapping theorem
$\norm{\cdot}_2$ is equivalent to $\norm{\cdot}_\infty$ on $S$, say for all $f \in S$, $\norm{f}_\infty \le C\norm{f}_2$.
Note that $S$ is a Hilbert space.
Let $\{f_n\}_{n\in I}$ be an orthonormal basis of $S$.
For all $f \in S$, $x \in [0,1]$.
The evaluation map $\delta_x(f) = f(x)$ is bounded and linear w.r.t $\norm{\cdot}_2$.
Indeed, $\abs{\delta_x(f)} = \abs{f(x)} \le \norm{f}_\infty \le C\norm{f}_2$.
Then, by the Riesz representation theorem on the Hilbert space $S$, there is $g_x \in S$ such that $f(x) = \langle f, g_x\rangle$ for all $f\in S$, with $\norm{g_x}_2 \le C$.

Thus, for every finite $F\subseteq I$, Bessel gives $\sum_{n\in F} \abs{f_n(x)}^2 = \sum_{n\in F} \abs{\langle f_n, g_x\rangle}^2 \le \norm{g_x}_2^2 \le C^2$.
Integrating over $x\in[0,1]$ gives $\cardinality{F} \le C^2$ for every finite $F$, so $\cardinality{I} \le C^2$.
:::
