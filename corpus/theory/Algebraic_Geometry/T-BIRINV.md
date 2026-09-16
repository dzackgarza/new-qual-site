---
schema: qual/card@1
id: T-BIRINV
kind: theorem
title: Plurigenera and irregularity are birational invariants
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Invariants
  - Plurigenera
  - Kodaira Dimension
relations:
- kind: uses
  target: D-G1AEH
review: draft
prompts:
- What is the plurigenus of a smooth projective variety?
- What is the irregularity of a smooth projective variety?
- What is a variety of general type?
- Show that the geometric genus, plurigenera and irregularity are birational invariants.
---

::: {.definition}
Let $X$ be a smooth projective variety of dimension $n$ over an algebraically closed field.

- The \dfn{geometric genus} is $p_g(X) = h^0(X, \omega_X)$, and the \dfn{$m$-th plurigenus} is $P_m(X) = h^0(X, \omega_X^{\otimes m})$ for $m \geq 1$.

- The \dfn{irregularity} is $q(X) = h^0(X, \Omega^1_X)$, which equals $h^1(X, \OO_X)$ in characteristic $0$.

- $X$ is of \dfn{general type} if $P_m(X)$ grows like a positive multiple of $m^n$, that is, $X$ has Kodaira dimension $n$.
:::

::: {.theorem}
If $X$ and $X'$ are birational smooth projective varieties, then $h^0(X, (\Omega^p_X)^{\otimes m}) = h^0(X', (\Omega^p_{X'})^{\otimes m})$ for all $p, m$.
In particular $p_g$, every $P_m$, and $q$ are birational invariants.
[@Har10a, Theorem II.8.19]
:::

::: {.remark}
The arithmetic genus $\chi(\OO_X)$ is also a birational invariant of smooth projective varieties in characteristic $0$, but its proof needs Hodge symmetry $h^i(\OO_X) = h^0(\Omega^i_X)$.
The self-intersection $K_X^2$ of a surface is not a birational invariant: blowing up a point lowers it by $1$.
:::
