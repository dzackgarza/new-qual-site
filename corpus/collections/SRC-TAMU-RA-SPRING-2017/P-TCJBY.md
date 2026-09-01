---
schema: qual/card@1
id: P-TCJBY
kind: problem
title: A $C[0,1]$ subspace closed in both $\|\cdot\|_\infty$ and $\|\cdot\|_2$ is
  finite-dimensional
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
Let $S$ be a closed subspace of $(C[0,1], \|\cdot\|_\infty)$.
If $S$ is also closed under $\|\cdot\|_2$, then show $S$ is finite-dimensional.
(This is question 66 in Folland on page 178, see also mathoverflow 52509 for other solutions.)
:::

::: {.solution}
Consider the identity map $id : (S,\|\cdot\|_\infty) \to (S,\|\cdot\|_2)$ is bounded since $\|f\|_2 \le \|f\|_\infty$ in general (see problem 8 in Jan 2016). Then by open mapping theorem.
$\|\cdot\|_2$ is equivalent to $\|\cdot\|_\infty$ on $S$, say for all $f \in S$, $\|f\|_\infty \le C\|f\|_2$.
Note that $S$ is a Hilbert space.
Let $\{f_n\}_{n\in I}$ be an orthonormal basis of $S$.
For all $f \in S$, $x \in [0,1]$.
The evaluation map $\delta_x(f) = f(x)$ is bounded and linear w.r.t $\|\cdot\|_2$.
Indeed, $|\delta_x(f)| = |f(x)| \le \|f\|_\infty \le C\|f\|_2$.
Then, by Riesz's lemma, there is a function $g_x \in C[0,1]$ such that $f(x) = \langle f, g_x\rangle$ with $\|g_x\| \le C$

Thus, $\sum_{n\in I} |f(x)|^2 = \sum_{n\in I} |\langle f, g_x\rangle|^2 = \|g_x\|_2^2 \le C^2$.
Then integration implies that $|I| \le C^2$.
:::
