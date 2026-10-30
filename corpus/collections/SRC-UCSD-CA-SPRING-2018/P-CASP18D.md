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
Let $u_n$ be a sequence of harmonic functions in $\DD$ that are continuous in $\overline{\DD}$.
Assume that $u_n$ converges uniformly on $\partial \DD$ to a function $f$.
Show that $u_n$ converges in the space of harmonic functions in $\DD$ to a harmonic function $u$ that is continuous in $\overline{\DD}$ and equal to $f$ on $\partial \DD$.
:::

::: {.solution}
Because $u_n-u_m$ is harmonic in $\DD$ and continuous on
$\overline{\DD}$, the maximum principle gives
$$
\sup_{\overline{\DD}}\abs{u_n-u_m}
\le
\sup_{\partial\DD}\abs{u_n-u_m}.
$$
The boundary sequence converges uniformly, so the right-hand side tends to
$0$ as $n,m\to\infty$. Hence $(u_n)$ is uniformly Cauchy on
$\overline{\DD}$ and converges uniformly there to a continuous function
$u$.

On every compact subset of $\DD$ the convergence is therefore uniform.
Locally uniform limits of harmonic functions are harmonic, so $u$ is harmonic
in $\DD$. On the boundary, uniform convergence gives
$$
u\restrict_{\partial\DD}=f.
$$
Thus $u_n\to u$ in the harmonic-function topology on $\DD$, and $u$ has
the required continuous extension to the closed disk.
:::
