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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, one per part, each checking T1 and the continuity of
    the two operations (the group axioms are the familiar ones and are not re-derived).
    Pages added where the prose cited by number only, each verified against the book: the
    definition of a topological group and this exercise on printed p. 145; Theorem 21.5 on
    printed p. 131; Theorem 18.4 on printed p. 110; Theorem 16.3 on printed p. 89; and
    Exercise 21.12 on printed p. 136, whose parts (a), (b) and (c) are exactly addition,
    multiplication and reciprocals, so the citations the earlier note made are the right
    ones. Two steps sharpened: for (c) the earlier prose reached multiplication through the
    logarithm, while multiplication on the positive reals is the restriction of the
    continuous multiplication on R, which is what is now used, the subspace and product
    topologies being matched by Theorem 16.3; and for (d) and (e) the continuity of a map
    into a product of coordinates is now attributed to Theorem 18.4 rather than left
    implicit in "polynomial in the coordinates". For (e) it is noted that GL(n) is open in
    R^{n^2}, being the preimage of R - {0} under the continuous determinant. No repair to
    the statement.
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
The argument is the retained published solution, **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.2, printed pp. 260--264** (`tmp/sources/munkres-solutions-whitman.pdf`), restructured into steps, with the continuity statements cited by their page in Munkres.

A topological group is a group that is also a topological space satisfying the $T_1$ axiom, in which multiplication $G\times G\to G$ and inversion $G\to G$ are continuous (Supplementary Exercises: Topological Groups, printed p. 145); the exercise is Exercise 2 there, printed p. 145. In each part below, the group axioms are the familiar ones for the operation named and are not re-derived; what is checked is $T_1$ and the continuity of the two maps. Three tools are used repeatedly: a subspace of a metric space is $T_1$; sums, differences, products and quotients of continuous real-valued functions are continuous, and a quotient $f/g$ is continuous where $g$ never vanishes (Theorem 21.5, printed p. 131); and a map into a product is continuous exactly when its component functions are (Theorem 18.4, printed p. 110), the product of subspaces carrying the subspace topology of the product (Theorem 16.3, printed p. 89).

::: pf

::: {.pf-step #integers}
(a) $(\ZZ,+)$ is a topological group.

::: pf-proof
$\ZZ$ is a subspace of the metric space $\RR$, hence $T_1$. It is discrete, since for $n\in\ZZ$ the set $\{n\}=\ZZ\cap(n-1,n+1)$ is open in $\ZZ$. A map out of a discrete space is continuous, so addition $\ZZ\times\ZZ\to\ZZ$ is continuous, $\ZZ\times\ZZ$ being discrete as a product of discrete spaces, and negation $\ZZ\to\ZZ$ is continuous.
:::

:::

::: {.pf-step #reals}
(b) $(\RR,+)$ is a topological group.

::: pf-proof
$\RR$ is a metric space, hence $T_1$. Addition $\RR\times\RR\to\RR$ is continuous (Exercise 21.12(a), printed p. 136), and negation $x\mapsto -x$ is an isometry of $\RR$, hence continuous.
:::

:::

::: {.pf-step #positive}
(c) $(\RR_+,\cdot)$ is a topological group.

::: pf-proof
$\RR_+$ is the set of positive reals (printed p. 31), on which multiplication is an operation with identity $1$ and inverse $1/u$. As a subspace of the metric space $\RR$ it is $T_1$. Multiplication $\RR_+\times\RR_+\to\RR_+$ is the restriction of the continuous multiplication $\RR\times\RR\to\RR$ (Exercise 21.12(b), printed p. 136) to the subspace $\RR_+\times\RR_+$, which by Theorem 16.3 (printed p. 89) carries the product of the subspace topologies, so it is continuous. Inversion $u\mapsto 1/u$ is the restriction to $\RR_+$ of the continuous map $x\mapsto 1/x$ on $\RR-\{0\}$ (Exercise 21.12(c), printed p. 136), hence continuous.
:::

:::

::: {.pf-step #circle}
(d) $(S^1,\cdot)$ is a topological group.

::: pf-proof
$S^1$ is the group of complex numbers of modulus $1$, a subspace of $\CC=\RR^2$ and hence $T_1$ as a subspace of a metric space. Write $z_j=x_j+iy_j$ with $x_j,y_j$ the coordinate functions on the $j$-th factor of $S^1\times S^1$, which are continuous. The product has coordinates
$$
(x_1x_2-y_1y_2,\ x_1y_2+y_1x_2),
$$
and each of these two real-valued functions is continuous on $S^1\times S^1$ by Theorem 21.5 (printed p. 131), products and differences of the continuous coordinate functions; so the product map $S^1\times S^1\to S^1$ is continuous by Theorem 18.4 (printed p. 110). Inversion is $z\mapsto\overline{z}=(x,-y)$, the restriction to $S^1$ of the continuous map $z\mapsto\overline{z}$ of $\CC$, so it is continuous.
:::

:::

::: {.pf-step}
(e) $(\mathrm{GL}(n),\cdot)$ is a topological group.

::: pf-proof
$\mathrm{GL}(n)$ is the set of nonsingular matrices, a subspace of $\RR^{n^2}$ and hence $T_1$; it is even open there, being the preimage under the continuous determinant of $\RR-\{0\}$. Each entry of a product $AB$ is a finite sum of products of an entry of $A$ with an entry of $B$, hence a continuous real-valued function of the $2n^2$ entries by Theorem 21.5 (printed p. 131); so multiplication is continuous by Theorem 18.4 (printed p. 110). The inverse is $A^{-1}=\operatorname{adj}(A)/\det(A)$: the entries of the adjugate are polynomials in the entries of $A$ and $\det$ is such a polynomial, while $\det(A)\ne0$ on $\mathrm{GL}(n)$, so each entry of $A^{-1}$ is a quotient of continuous functions with nonzero denominator, hence continuous by Theorem 21.5 (printed p. 131), and inversion is continuous by Theorem 18.4.
:::

:::

:::
:::
