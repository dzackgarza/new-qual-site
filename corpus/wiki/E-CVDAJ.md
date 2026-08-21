---
schema: qual/card@1
id: E-CVDAJ
kind: exercise
title: Consequences of an abstract degree theory on spheres
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §58.10"}

Suppose that to every map $h: S^n \to S^n$ we have assigned an integer, denoted by $\deg h$ and called the degree of $h$, such that:

(i) Homotopic maps have the same degree.

(ii) $\deg(h \circ k) = (\deg h) \cdot (\deg k)$.

(iii) The identity map has degree 1, any constant map has degree 0, and the reflection map $\rho(x_1, \ldots, x_{n+1}) = (x_1, \ldots, x_n, -x_{n+1})$ has degree $-1$.

[One can construct such a function, using the tools of algebraic topology. Intuitively, $\deg h$ measures how many times $h$ wraps $S^n$ about itself; the sign tells you whether $h$ preserves orientation or not.] Prove the following:

(a) There is no retraction $r: B^{n+1} \to S^n$.

(b) If $h: S^n \to S^n$ has degree different from $(-1)^{n+1}$, then $h$ has a fixed point.
[Hint: Show that if $h$ has no fixed point, then $h$ is homotopic to the antipodal map $a(x) = -x$.]

(c) If $h: S^n \to S^n$ has degree different from 1, then $h$ maps some point $x$ to its antipode $-x$.

(d) If $S^n$ has a nonvanishing tangent vector field $v$, then $n$ is odd.
[Hint: If $v$ exists, show the identity map is homotopic to the antipodal map.]
:::
