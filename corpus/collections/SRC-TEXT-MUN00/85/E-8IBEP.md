---
schema: qual/card@1
id: E-8IBEP
kind: problem
title: Free generators for the subgroup lifted over the figure eight
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 85 Exercise 3, printed p. 515. Free generators for the subgroup over the figure eight, from the covering restricted to the axes and the Euler number of the total space. Checked against Theorem 85.1 and Theorem 84.1. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. The previous note cited Theorem 85.1, which is the theorem that subgroups of free groups are free and is not used here, and the proof cited "Theorem 84.1" for the maximal-tree theorem, which is false: Theorem 84.1 is the criterion that a graph is connected exactly when its vertices can be joined by edge paths, and the maximal-tree theorem is Theorem 84.7 (printed p. 511). Both citations are corrected. Citations added and checked: Theorem 71.1 (printed p. 434) for the fundamental group of a wedge of circles, Theorem 53.2 (printed p. 338) for the restriction of a covering map to a preimage, the Definition of a linear graph (printed p. 502), Theorem 84.4 (printed p. 509) for a maximal tree containing all vertices, and Theorem 69.4 (printed p. 423) for the abelianisation of a free group. Repairs: the tree $T$ was called maximal with the justification "contains all vertices and contains no cycles", which is the converse of Theorem 84.4 and needs T to be connected as well, and the proof now exhibits its connectivity; the identification $H=[F,F]$ was stated without the step from "the total exponent of both generators is zero" to the commutator subgroup, which is now Theorem 69.4; and the answer's index set is now checked against the edges not in $T$, namely the horizontal unit segments at heights $n\ne 0$. What the certificate does not cover: the computation of the projected loops reads orientations off the standard coordinates, which is the definition of $\alpha$ and $\beta$ in the printed exercise.
---

::: {.exercise}

Let $p: \RR \to S^1$ be the standard covering map; consider the covering map $p \times p: \RR \times \RR \to S^1 \times S^1$.
Let $b_0 = (1, 0) \in S^1$; set $X = (b_0 \times S^1) \cup (S^1 \times b_0)$; let $E = (p \times p)^{-1}(X)$; and let $q: E \to X$ be the covering map obtained by restricting $p \times p$.
The fundamental group of $X$ has free generators $\alpha$ and $\beta$, where $\alpha$ is represented by a loop in $b_0 \times S^1$ and $\beta$ by a loop in $S^1 \times b_0$.
Find a system of free generators for the subgroup $q_*(\pi_1(E, e_0))$, where $e_0$ is the origin in $\RR^2$.

:::

::: {.solution}

Write $x_0 = (b_0, b_0)$ for the base point of $X$ and $H = q_*(\pi_1(E, e_0)) \le \pi_1(X, x_0)$; the map $q_*$ is injective, so a free basis of $\pi_1(E,e_0)$ maps to one of $H$ (printed p. 477).

::: pf

::: {.pf-step #space}

$X$ is the wedge of the two circles $b_0\times S^1$ and $S^1\times b_0$ at $x_0$, so $\pi_1(X,x_0)$ is free on $\alpha$ and $\beta$.

::: pf-proof

The two circles meet exactly in $x_0$, so $X$ is a wedge of two circles in the sense of the Definition of §71, and Theorem 71.1 (printed p. 434) gives that $\pi_1(X,x_0)$ is free with free generators the classes of a loop in each circle.

:::

:::

::: {.pf-step #grid}

$E=(p\times p)^{-1}(X)=(\RR\times\ZZ)\cup(\ZZ\times\RR)$, and $q:E\to X$ is a covering map of the linear graph $E$ whose edges are the unit segments between adjacent points of $\ZZ^2$.

::: pf-proof

A point $(s,t)\in\RR^2$ lies in $(p\times p)^{-1}(X)$ exactly when $p(s)=1$ or $p(t)=1$, that is, when $s\in\ZZ$ or $t\in\ZZ$. The restriction of a covering map to the preimage of a subspace is a covering map (Theorem 53.2, printed p. 338), so $q$ is a covering map. The space $E$ is a union of arcs meeting only in end points, with the coherent topology, which is the Definition of a linear graph (printed p. 502); its vertices are the points of $\ZZ^2$.

:::

:::

::: {.pf-step #subgroup}

$H=[F,F]$, the commutator subgroup of $F=\pi_1(X,x_0)$.

::: pf-proof

Let $w$ be a word in $\alpha^{\pm1},\beta^{\pm1}$ and let $\tilde w$ be the lift of the corresponding loop to a path in $E$ starting at $e_0=(0,0)$. A horizontal edge, whose first coordinate varies and whose second is an integer, projects to a loop in $S^1\times b_0$ and changes the first coordinate by $1$; a vertical edge changes the second coordinate by $1$ and projects to a loop in $b_0\times S^1$. So $\tilde w$ ends at $(a,b)\in\ZZ^2$, where $a$ and $b$ are the total exponents of $\beta$ and of $\alpha$ in $w$. Hence $w\in H$ exactly when both total exponents vanish, that is, exactly when $w$ lies in the kernel of the homomorphism $F\to\ZZ^2$ taking $\alpha$ and $\beta$ to the standard basis. Since $F/[F,F]$ is free abelian with basis the images of $\alpha$ and $\beta$ (Theorem 69.4, printed p. 423), that kernel is $[F,F]$.

:::

:::

::: {.pf-step #tree}

$T=(\RR\times\{0\})\cup(\ZZ\times\RR)$ is a maximal tree in $E$.

::: pf-proof

$T$ is connected: it is the union of the connected set $\RR\times\{0\}$ and the lines $\{m\}\times\RR$, each of which meets it in the point $(m,0)$. It contains all the vertices $\ZZ^2$, since $(m,n)\in\{m\}\times\RR$. It contains no closed reduced edge path. A reduced edge path in a single line $\RR\times\{0\}$ or $\{m\}\times\RR$ moves strictly in one direction of that line, so it visits no vertex twice. A path in $T$ that changes from one of these lines to another must pass through their single common vertex, and having left it along the second line it can meet the first line again only at that same vertex, which would make the path closed and not reduced. So no reduced edge path in $T$ is closed. So $T$ is a tree containing all vertices, and it is maximal by Theorem 84.4 (printed p. 509).

:::

:::

::: {.pf-step #basis}

$\pi_1(E,e_0)$ has the free basis $\{g_{m,n}\}$ indexed by the edges of $E$ not in $T$, and $q$ carries $g_{m,n}$ to
$$
\beta^m\alpha^n\beta\alpha^{-n}\beta^{-(m+1)} .
$$

::: pf-proof

The edges of $E$ are the unit segments of the grid. The vertical segments and the horizontal segments at height $0$ lie in $T$; the horizontal segment $e_{m,n}=[m,m+1]\times\{n\}$ lies in $T$ exactly when $n=0$. So the edges not in $T$ are exactly the $e_{m,n}$ with $m\in\ZZ$ and $n\in\ZZ\setminus\{0\}$. By Theorem 84.7 (printed p. 511) the classes of the loops $g_{m,n}=\gamma_{x}*(f_{e_{m,n}}*\overline{\gamma}_{y})$ form a system of free generators of $\pi_1(E,e_0)$, where $\gamma_x$ is the tree path from $e_0$ to the initial vertex $x=(m,n)$ of $e_{m,n}$ and $\gamma_y$ the tree path to its final vertex $y=(m+1,n)$. The tree path from $(0,0)$ to $(m,n)$ runs along $\RR\times\{0\}$ to $(m,0)$ and then up $\{m\}\times\RR$ to $(m,n)$, and projects to $\beta^m\alpha^n$. The edge $e_{m,n}$ from $(m,n)$ to $(m+1,n)$ projects to $\beta$. The reverse of the tree path from $(0,0)$ to $(m+1,n)$ projects to the reverse of $\beta^{m+1}\alpha^n$, which is $\alpha^{-n}\beta^{-(m+1)}$. Concatenating,
$$
q\circ g_{m,n}\sim\beta^m\alpha^n\beta\alpha^{-n}\beta^{-(m+1)} .
$$

:::

:::

::: {.pf-step}

A system of free generators for $H=q_*(\pi_1(E,e_0))$ is
$$
\left\{\beta^m\alpha^n\beta\alpha^{-n}\beta^{-(m+1)}\mid m\in\ZZ,\ n\in\ZZ\setminus\{0\}\right\}.
$$

::: pf-proof

By step [](#basis){.pf-ref} the classes $g_{m,n}$ freely generate $\pi_1(E,e_0)$ over the stated index set, and $q_*$ is injective, so their images freely generate $H$ over the same index set. Step [](#subgroup){.pf-ref} identifies $H$ with the commutator subgroup, which is the kernel of the exponent map, so the elements displayed are precisely the images.

:::

:::

:::

:::
