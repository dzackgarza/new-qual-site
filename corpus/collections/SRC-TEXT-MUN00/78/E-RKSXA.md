---
schema: qual/card@1
id: E-RKSXA
kind: problem
title: The boundary of a surface with boundary is intrinsic
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Part (a) was proved by local homology, H_2 of the pair (H^2, H^2 - q) against H_2 of (R^2, R^2 - z), and
    this book never develops homology: the same objection that replaced the simplicial computation on E-II4JY.
    Part (a) is now proved by the book's means alone. The half-disc D about q is star convex after q is
    removed, hence simply connected by the straight-line homotopy to a_0. A punctured open set W - z of R^2 is
    not: the radial projection onto a small circle S about z inside W is a retraction of W - z onto S, so by
    Lemma 55.1 (printed p. 348) the inclusion of S induces an injection of pi_1(S) = Z (Theorem 54.5, printed
    p. 345, with Corollary 52.5 for the circle of radius delta). A chart carries D - q homeomorphically onto
    the punctured open set h(D) - h(q), and Corollary 52.5 (printed p. 334) makes their fundamental groups
    isomorphic, so the two paragraphs contradict each other. Checked on the page images: Lemma 55.1 (printed
    p. 348), Theorem 54.5 (printed p. 345) and Corollary 52.5 (printed p. 334); and parts
    (b) and (c), which cite part (a) and not its proof, are unchanged. Not covered: Lemma 55.1
    is cited, not reproved, and nothing is claimed about higher homology of a manifold with boundary.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §78 Exercise 2(a)-(c), printed p. 476. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved source is
    tmp/sources/gh-dyang5-MATH104-Topology-E-RKSXA.md, read whole. David Yang, MATH104: Topology, Fall 2023,
    Homework 10, treats (a) and (b) only, in HW/hw10.tex lines 122-158 of dyang5/MATH104-Topology at commit
    12686a815d58f29aeaadb90a30449ae85c0a613f. Its (a) is wrong as written: line 23 of the saved file reads
    "Removing the point y from U preserves the simply-connectedness nature of U", which is exactly what does
    not hold (a disk is simply connected and its punctured form is not), and line 24 reads "removing a point
    from an open set U' of R^2 gives us a space which has fundamental group Z", which is false for an
    annulus; the argument removes the point from a neighbourhood whose simple connectivity it has not
    established, so it assumes what it has to prove. Its (b) is a sketch in one direction and takes the
    statement of (a) as given. Nothing of it is transcribed, and the card's (a) is now proved by the book's
    own means — star convexity, the retraction of a punctured plane onto a circle, the injection that gives,
    and invariance of the fundamental group — rather than by local homology, which the book does not develop;
    see the source-corrected event that now heads this list. The card's (b) and (c) are its own. Rejected in the
    search: mse 5039847, which has no answer.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 78 Exercise 2, printed p. 476. Part (a) by local homology: H_2 of the half-plane at a boundary point is 0 and H_2 of the plane at a point is Z, with excision. Parts (b) and (c) transport the chart to the boundary line and exhibit an interval chart on the boundary. Checked against the printed parts (a), (b), (c) of the exercise. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Let $H^2$ be the subspace of $\RR^2$ consisting of all points $(x_1, x_2)$ with $x_2 \geq 0$.
A 2-manifold with boundary (or surface with boundary) is a Hausdorff space $X$ with a countable basis such that each point $x$ of $X$ has a neighborhood homeomorphic with an open set of $\RR^2$ or $H^2$.
The boundary of $X$ (denoted $\partial X$) consists of those points $x$ such that $x$ has no neighborhood homeomorphic with an open set of $\RR^2$.

(a) Show that no point of $H^2$ of the form $(x_1, 0)$ has a neighborhood (in $H^2$) that is homeomorphic to an open set of $\RR^2$.

(b) Show that $x \in \partial X$ if and only if there is a homeomorphism $h$ mapping a neighborhood of $x$ onto an open set of $H^2$ such that $h(x) \in \RR \times 0$.

(c) Show that $\partial X$ is a 1-manifold.
:::

::: {.solution}
(a) Let $q=(q_1,0)\in H^2$ and suppose that some neighbourhood of $q$ in $H^2$ were homeomorphic with an open set of $\RR^2$; we derive a contradiction. Take a homeomorphism $h:U\to V$ of such a neighbourhood onto an open set $V$ of $\RR^2$ and shrink it to a half-disc: for $\varepsilon>0$ small enough the set
$$
D=\{p\in H^2:\norm{p-q}<\varepsilon\}
$$
is a neighbourhood of $q$ in $H^2$ contained in $U$, and $h$ carries $D$ homeomorphically onto $h(D)$, which is open in $\RR^2$ because it is open in $V$. Hence
$$
D-\{q\}\cong h(D)-\{h(q)\} .
$$

The punctured half-disc $D-\{q\}$ is star convex. The point $a_0=(q_1,\varepsilon/2)$ lies in it, and for $p\in D-\{q\}$ the segment joining $a_0$ to $p$ lies in $D$, since $D$ is convex, and meets $q$ in no point: every point of that segment other than $p$ has positive second coordinate, while the second coordinate of $q$ is $0$. It is therefore simply connected: for a loop $\gamma$ in $D-\{q\}$ the straight-line homotopy $H(s,t)=(1-t)\gamma(s)+t\,a_0$ takes each value on a segment joining $a_0$ to a point of $D-\{q\}$, hence lies in $D-\{q\}$, and it carries $s=0$ and $s=1$ to the same path, so $\gamma$ is path homotopic there to the constant loop at $a_0$; and $D-\{q\}$ is path connected, every point being joined to $a_0$.

No punctured open set of $\RR^2$ is simply connected. Let $W\subseteq\RR^2$ be open and let $z\in W$; choose $\delta>0$ so that the circle $S=\{y:\norm{y-z}=\delta\}$ is contained in $W$, and let
$$
\rho:W-\{z\}\longrightarrow S,\qquad \rho(y)=z+\delta\,\frac{y-z}{\norm{y-z}},
$$
be the radial projection. It is continuous and it fixes every point of $S$, so $S$ is a retract of $W-\{z\}$, and by Lemma 55.1 (printed p. 348) the homomorphism induced by the inclusion $S\to W-\{z\}$ is injective. Since $S$ is a circle, $\pi_1(S)\cong\pi_1(S^1)\cong\ZZ$ (Corollary 52.5, printed p. 334, and Theorem 54.5, printed p. 345), so $\pi_1(W-\{z\})$ is not trivial and $W-\{z\}$ is not simply connected.

Finally $h$ restricts to a homeomorphism of $D-\{q\}$ with $h(D)-\{h(q)\}$, so by Corollary 52.5 (printed p. 334) these two spaces have isomorphic fundamental groups; but $h(D)-\{h(q)\}$ is a punctured open set of $\RR^2$, which the previous paragraph shows cannot be simply connected. Hence no neighbourhood of $q$ in $H^2$ is homeomorphic with an open set of $\RR^2$.

(b) Suppose first that a chart
$$
h:U\longrightarrow V\subset H^2
$$
satisfies $h(x)\in\RR\times\{0\}$. By part (a), $h(x)$ has no neighborhood in $H^2$ homeomorphic to an open subset of $\RR^2$; transporting this statement through $h$, neither does $x$. Hence $x\in\partial X$.

Conversely, let $x\in\partial X$. By the definition of a manifold with boundary, $x$ has a chart to an open subset of either $\RR^2$ or $H^2$. The first possibility is excluded by the definition of $\partial X$. Thus there is a half-plane chart $h:U\to V\subset H^2$. If $h(x)$ had positive second coordinate, a small Euclidean disk about $h(x)$ would lie in $H^2$, giving an ordinary $\RR^2$-neighborhood of $x$, again a contradiction. Therefore $h(x)\in\RR\times\{0\}$.

(c) Let $x\in\partial X$ and choose a chart as in (b), with $h(x)=(a,0)$. Shrinking the chart if necessary, take
$$
V=(a-\varepsilon,a+\varepsilon)\times[0,\varepsilon)
$$
inside its image. By part (b),
$$
h(U\cap\partial X)=V\cap(\RR\times\{0\})
=(a-\varepsilon,a+\varepsilon)\times\{0\}.
$$
Hence $U\cap\partial X$ is an open neighborhood of $x$ in $\partial X$ homeomorphic to an open interval. Since $\partial X$ is a subspace of the Hausdorff second-countable space $X$, it is Hausdorff and second countable. Thus $\partial X$ is a 1-manifold.
:::
