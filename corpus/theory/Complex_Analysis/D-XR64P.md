---
schema: qual/card@1
id: D-XR64P
kind: definition
title: Dirichlet problem on the unit disc
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - PDEs
relations: []
review: draft
---

::: {.definition}
Let $u\colon S^1\to\RR$ be bounded and piecewise continuous.
The \dfn{Dirichlet problem} on $\DD$ with boundary data $u$ asks for a bounded [[D-CFBSA|harmonic]] function $\tilde u\colon\DD\to\RR$ such that
$$
\lim_{\substack{z\to\zeta\\ z\in\DD}}\tilde u(z)=u(\zeta)
$$
at every point $\zeta\in S^1$ where $u$ is continuous.
A \dfn{solution} of the Dirichlet problem is such a function $\tilde u$.
:::

::: {.remark}
When $u$ is continuous on $S^1$, the boundary condition says that $\tilde u$ extends to a continuous function on $\overline{\DD}$ that equals $u$ on $S^1$.
:::
