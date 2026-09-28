---
schema: qual/card@1
id: P-CASP18D
kind: problem
title: "Uniform convergence of harmonic functions on the boundary implies convergence in the disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Poisson Kernel
  - Uniform Convergence
relations: []
review: draft
---

::: {.problem}
Let $u_n$ be a sequence of harmonic functions in $\mathbb{D}$ that are continuous in $\overline{\mathbb{D}}$.
Assume that $u_n$ converges uniformly on $\partial \mathbb{D}$ to a function $f$.
Show that $u_n$ converges in the space of harmonic functions in $\mathbb{D}$ to a harmonic function $u$ that is continuous in $\overline{\mathbb{D}}$ and equal to $f$ on $\partial \mathbb{D}$.
:::

::: {.solution}
Because $u_n-u_m$ is harmonic in $\mathbb D$ and continuous on
$\overline{\mathbb D}$, the maximum principle gives
\[
\sup_{\overline{\mathbb D}}|u_n-u_m|
\le
\sup_{\partial\mathbb D}|u_n-u_m|.
\]
The boundary sequence converges uniformly, so the right-hand side tends to
$0$ as $n,m\to\infty$. Hence $(u_n)$ is uniformly Cauchy on
$\overline{\mathbb D}$ and converges uniformly there to a continuous function
$u$.

On every compact subset of $\mathbb D$ the convergence is therefore uniform.
Locally uniform limits of harmonic functions are harmonic, so $u$ is harmonic
in $\mathbb D$. On the boundary, uniform convergence gives
\[
u|_{\partial\mathbb D}=f.
\]
Thus $u_n\to u$ in the harmonic-function topology on $\mathbb D$, and $u$ has
the required continuous extension to the closed disk.
:::
