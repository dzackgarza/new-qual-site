---
schema: qual/card@1
id: P-AGH512QUADRICHYP
kind: problem
title: Rank normal form, irreducibility, and singular locus of a quadric hypersurface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quadratic Forms
  - Singularities
  - Projective Varieties
  - Cones
relations: []
review: draft
---

::: {.problem}
Assume $\operatorname{char} k \neq 2$, and let $f$ be a homogeneous polynomial of degree $2$ in $x_0, \ldots, x_n$.

1. Show that after a suitable linear change of variables, $f$ can be brought into the form $f = x_0^2 + \cdots + x_r^2$ for some $0 \leq r \leq n$.

2. Show that $f$ is irreducible if and only if $r \geq 2$.

3. Assume $r \geq 2$, and let $Q$ be the quadric hypersurface in $\PP^n$ defined by $f$.
   Show that the singular locus $Z = \Sing Q$ of $Q$ is a linear variety of dimension $n - r - 1$.
   In particular, $Q$ is nonsingular if and only if $r = n$.

4. In case $r < n$, show that $Q$ is a cone with axis $Z$ over a nonsingular quadric hypersurface $Q' \subseteq \PP^r$.

Here, if $Y$ is a closed subset of $\PP^r$ and $Z$ is a linear subspace of dimension $n - r - 1$ in $\PP^n$, embed $\PP^r$ in $\PP^n$ so that $\PP^r \intersect Z = \emptyset$; the *cone over $Y$ with axis $Z$* is the union of all lines joining a point of $Y$ to a point of $Z$.
:::
