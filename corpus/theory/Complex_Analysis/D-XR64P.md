---
schema: qual/card@1
id: D-XR64P
kind: definition
title: Dirichlet problem
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
Let $\Omega\subseteq\RR^2$ be a bounded domain with boundary $\bd\Omega$, and let $u\colon\bd\Omega\to\RR$ be continuous.
The \dfn{Dirichlet problem} on $\Omega$ with boundary data $u$ asks for a function $\tilde u\colon\overline\Omega\to\RR$ that is continuous on $\overline\Omega$, [[D-CFBSA|harmonic]] on $\Omega$, and equal to $u$ on $\bd\Omega$.
A \dfn{solution} of the Dirichlet problem is such a function $\tilde u$.

The problem is named and posed in [@Ahl73, ch. 6, §4, The Dirichlet Problem] as that of finding a harmonic function with given boundary values.
:::

::: {.remark}
For the unit disc and continuous boundary data on $S^1$, Poisson's formula gives the solution, and for a bounded region whose boundary consists of finitely many analytic arcs the problem is solved in [@Ahl73, ch. 6, §4, The Dirichlet Problem].
When $u$ is continuous on $\bd\Omega$, the boundary condition says that $\tilde u$ extends continuously to $\overline\Omega$ with the prescribed values.
:::
