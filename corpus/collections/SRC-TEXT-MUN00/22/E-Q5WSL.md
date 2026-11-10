---
schema: qual/card@1
id: E-Q5WSL
kind: problem
title: Examples of topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 2, printed p. 145; the
    five examples are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.2, printed pp.
    260-264. His five cases: the discrete integers, the real line by Exercise 21.12(a), the
    positive reals through the logarithm, the circle via polynomial formulas in the two
    coordinates for multiplication and conjugation for inversion, and GL(n) via polynomial
    entries for multiplication and the adjugate over the nonzero determinant for inversion.
    (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Show that the following are topological groups:

(a) $(\ZZ, +)$

(b) $(\RR, +)$

(c) $(\RR_+, \cdot)$

(d) $(S^1, \cdot)$, where we take $S^1$ to be the space of all complex numbers $z$ for which $\abs{z} = 1$.

(e) The general linear group $\mathrm{GL}(n)$, under the operation of matrix multiplication.
($\mathrm{GL}(n)$ is the set of all nonsingular $n$ by $n$ matrices, topologized by considering it as a subset of euclidean space of dimension $n^2$ in the obvious way.)
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.2, printed pp. 260--264** (`tmp/sources/munkres-solutions-whitman.pdf`); the five cases are his; the continuity statements are those of Exercise 21.12 and Theorem 21.5, applied in each case as he applies them.

In each case one has to check that the space is a group, is $T_{1}$, and that multiplication and inversion are continuous.

(a) $(\ZZ,+)$: $\ZZ$ is a subspace of $\RR$, hence $T_{1}$, and it is discrete, so every map out of $\ZZ\times\ZZ$ and out of $\ZZ$ is continuous; in particular addition and $x\mapsto-x$.

(b) $(\RR,+)$: $T_{1}$, addition is continuous (Exercise 21.12(a)) and negation is continuous (an isometry of $\RR$).

(c) $(\RR_{+},\cdot)$: $T_{1}$, and $\log:\RR_{+}\to\RR$ is a homeomorphism with inverse $\exp$ (both continuous, Exercise 21.12(c) for the reciprocal and elementary calculus for exp), carrying multiplication to addition: $uv\mapsto\log u+\log v$ is continuous by (b), and $u\mapsto1/u$ is continuous by Exercise 21.12(c) on $\RR-\{0\}$, restricted to $\RR_{+}$.

(d) $(S^{1},\cdot)$, $S^{1}=\{z\in\CC\mid\abs{z}=1\}$: $T_{1}$ as a subspace of $\CC=\RR^{2}$. Writing $z_{j}=x_{j}+iy_{j}$, the product has coordinates
$$
(x_{1}x_{2}-y_{1}y_{2},\ x_{1}y_{2}+y_{1}x_{2}),
$$
polynomial in the four coordinates, hence continuous on $S^{1}\times S^{1}$ by Theorem 21.5. Inversion is $z\mapsto\bar z=(x,-y)$, the restriction to $S^{1}$ of a continuous map of $\CC$.

(e) $(\mathrm{GL}(n),\cdot)$: the set of nonsingular $n\times n$ matrices is a subspace of $\RR^{n^{2}}$, hence $T_{1}$. Multiplication is continuous because each entry of $AB$ is a polynomial in the entries of $A$ and $B$ (Theorem 21.5). Inversion is $A\mapsto A^{-1}=\operatorname{adj}(A)/\det(A)$: the adjugate has polynomial entries and $\det$ is a polynomial, and $\det$ never vanishes on $\mathrm{GL}(n)$, so $A^{-1}$ is continuous by Theorem 21.5 and the continuity of $t\mapsto1/t$ on $\RR-\{0\}$.
:::
