---
schema: qual/card@1
id: E-HAT-3.3-28
kind: problem
title: Nondegeneracy on large subspaces
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that a nonsingular symmetric or skew-symmetric bilinear pairing over a field $F$, of the form $F^n \times F^n \to F$, cannot be identically zero when restricted to all pairs of vectors $\nu, w$ in a $k$-dimensional subspace $V \subset F^n$ if $k > n/2$.
:::

::: {.solution}
Let $B$ be the pairing and let $V^\perp$ be the set of vectors $x$ such that $B(x,v)=0$ for every $v\in V$. Nonsingularity identifies $F^n$ with its dual, so the restriction map $F^n\to V^*$ is surjective. Its kernel is $V^\perp$, and rank-nullity gives $\dim V^\perp=n-k$.

If $B$ vanishes on $V\times V$, then $V\subseteq V^\perp$. Thus $k\le n-k$, or $k\le n/2$. This contradicts $k>n/2$.
:::
