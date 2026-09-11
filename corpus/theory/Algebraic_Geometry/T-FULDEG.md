---
schema: qual/card@1
id: T-FULDEG
kind: theorem
title: The degree of a projective toric variety is the normalised volume of its polytope
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Polytopes
  - Intersection Theory
relations:
- kind: uses
  target: D-TORPOLY
- kind: uses
  target: D-TORQD
review: draft
prompts:
- Compute the degree of a projective toric variety from its polytope.
- What is the degree of the toric variety of the simplex dilated by d?
---

::: {.theorem}
Let $P \subseteq M_\RR$ be a full-dimensional very ample lattice polytope of dimension $n$, embedded by the lattice points of $P$.
Then
\[
\deg X_P = n! \cdot \vol(P) ,
\]
the volume normalised so that the standard simplex has volume $1/n!$.
Equivalently $\deg X_P = D_P^{\,n}$, the top self-intersection of the ample divisor.
:::

::: {.remark title="Ehrhart, in one line"}
The statement is the leading term of the lattice-point count.
Since $h^0(X_P, \OO(kD_P)) = \size(kP \intersect M)$ and Ehrhart's theorem makes this a polynomial in $k$ of degree $n$ with leading coefficient $\vol(P)$, comparison with the Hilbert polynomial of $X_P$ gives the degree.
So the same lattice-point count that computes sections also computes the degree; only the leading coefficient is read instead of the value at $k = 1$.
:::

::: {.remark title="The checks to do aloud"}
For $P = \Delta$, the standard simplex, $\vol = 1/n!$ and $\deg \PP^n = 1$.
For $P = d\Delta$, $\vol = d^n/n!$ and $\deg = d^n$, which is the degree of the $d$-uple Veronese image of $\PP^n$.
For the unit square, $2! \cdot 1 = 2$, the degree of the quadric surface $\PP^1 \times \PP^1 \subseteq \PP^3$.
:::
