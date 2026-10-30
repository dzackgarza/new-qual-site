---
schema: qual/card@1
id: P-TCJBY
kind: problem
title: A $C[0,1]$ subspace closed in both $\norm{\cdot}_\infty$ and $\norm{\cdot}_2$ is finite-dimensional
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

::: {.problem}
Let $S$ be a closed subspace of $(C[0,1], \norm{\cdot}_\infty)$.
If $S$ is also closed under $\norm{\cdot}_2$, then show $S$ is finite-dimensional.
(This is question 66 in Folland on page 178, see also mathoverflow 52509 for other solutions.)
:::

::: {.solution}
Consider the identity map $id : (S,\norm{\cdot}_\infty) \to (S,\norm{\cdot}_2)$ is bounded since $\norm{f}_2 \le \norm{f}_\infty$ in general (see problem 8 in Jan 2016). Then by open mapping theorem.
$\norm{\cdot}_2$ is equivalent to $\norm{\cdot}_\infty$ on $S$, say for all $f \in S$, $\norm{f}_\infty \le C\norm{f}_2$.
Note that $S$ is a Hilbert space.
Let $\{f_n\}_{n\in I}$ be an orthonormal basis of $S$.
For all $f \in S$, $x \in [0,1]$.
The evaluation map $\delta_x(f) = f(x)$ is bounded and linear w.r.t $\norm{\cdot}_2$.
Indeed, $\abs{\delta_x(f)} = \abs{f(x)} \le \norm{f}_\infty \le C\norm{f}_2$.
Then, by Riesz's lemma, there is a function $g_x \in C[0,1]$ such that $f(x) = \langle f, g_x\rangle$ with $\norm{g_x} \le C$

Thus, $\sum_{n\in I} \abs{f(x)}^2 = \sum_{n\in I} \abs{\langle f, g_x\rangle}^2 = \norm{g_x}_2^2 \le C^2$.
Then integration implies that $\cardinality{I} \le C^2$.
:::
