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

No complete published solution of Munkres §78 Exercise 2 was located; the argument is the card's own, and the sets searched are recorded in the audit trail.

Throughout, $H^{2}=\{(u,v)\in\RR^{2}:v\ge0\}$ is a subspace of $\RR^{2}$, a chart at a point of a surface with boundary $X$ is a homeomorphism of a neighbourhood of that point onto an open set of $\RR^{2}$ or of $H^{2}$, and $\partial X$ is the set of points having no chart with values in $\RR^{2}$.

::: pf

::: {.pf-step #a}
(a) No point $(q_{1},0)$ of $H^{2}$ has a neighbourhood in $H^{2}$ homeomorphic to an open set of $\RR^{2}$.

::: pf-proof

::: {.pf-step #half-disc}
If $U$ is a neighbourhood in $H^{2}$ of $q=(q_{1},0)$ and $h:U\to V$ a homeomorphism onto an open set $V$ of $\RR^{2}$, then $h$ carries the punctured half-disc $D-\{q\}$ homeomorphically onto the punctured open set $h(D)-\{h(q)\}$ of $\RR^{2}$, for $D=\{p\in H^{2}:\norm{p-q}<\varepsilon\}$ with $\varepsilon>0$ small.

::: pf-proof
Choose $\varepsilon>0$ with $D\subset U$. The set $D$ is open in $H^{2}$, being the intersection of $H^{2}$ with the ball $B(q,\varepsilon)$ of $\RR^{2}$, so $h(D)$ is open in $V$, hence open in $\RR^{2}$. A homeomorphism restricts to a homeomorphism of a subspace with its image, and $\{q\}$ corresponds to $\{h(q)\}$, so $h$ restricts to a homeomorphism $D-\{q\}\to h(D)-\{h(q)\}$.
:::

:::

::: {.pf-step #half-disc-simply-connected}
$D-\{q\}$ is simply connected.

::: pf-proof
Let $a_{0}=(q_{1},\varepsilon/2)\in D-\{q\}$. For $p\in D-\{q\}$ the segment from $a_{0}$ to $p$ lies in $D$, which is convex, and meets $q$ in no point: a point of that segment other than $p$ has second coordinate in $(0,\varepsilon)$, while $q$ has second coordinate $0$. Hence $D-\{q\}$ is star shaped with respect to $a_{0}$, so it is path connected — every point is joined to $a_{0}$ — and every loop $\gamma$ in it is path homotopic to the constant loop at $a_{0}$ through the straight-line homotopy $H(s,t)=(1-t)\gamma(s)+t\,a_{0}$, whose values all lie on such segments. Since $\pi_{1}$ is by definition the set of path homotopy classes of loops at the base point (§51, printed p. 326), this says that $\pi_{1}(D-\{q\},a_{0})$ is trivial, and with path connectedness that is simple connectedness.
:::

:::

::: {.pf-step #punctured-not-simply}
No set $W-\{z\}$ with $W$ open in $\RR^{2}$ and $z\in W$ is simply connected.

::: pf-proof
Choose $\delta>0$ with the circle $S=\{y:\norm{y-z}=\delta\}$ contained in $W$ and let $\rho:W-\{z\}\to S$ be the radial projection $\rho(y)=z+\delta(y-z)/\norm{y-z}$; it is continuous and it fixes every point of $S$. So $S$ is a retract of $W-\{z\}$, and the homomorphism induced by the inclusion $S\to W-\{z\}$ is injective (Lemma 55.1, printed p. 348). Since $\pi_{1}(S)\cong\pi_{1}(S^{1})\cong\ZZ$ (Corollary 52.5, printed p. 334, and Theorem 54.5, printed p. 345), $\pi_{1}(W-\{z\})$ has an element of infinite order and is not trivial, so $W-\{z\}$ is not simply connected.
:::

:::

::: {.pf-qed}
Suppose that $q=(q_{1},0)$ had a neighbourhood $U$ in $H^{2}$ homeomorphic to an open set of $\RR^{2}$. By step [](#half-disc){.pf-ref}, $D-\{q\}$ is homeomorphic to $h(D)-\{h(q)\}$, a punctured open subset of $\RR^{2}$; homeomorphic spaces have isomorphic fundamental groups (Corollary 52.5, printed p. 334), so $D-\{q\}$ would not be simply connected, contradicting step [](#half-disc-simply-connected){.pf-ref} by step [](#punctured-not-simply){.pf-ref}.
:::

:::

:::

::: {.pf-step #b}
(b) $x\in\partial X$ exactly when a chart $h$ of a neighbourhood of $x$ has $h(x)\in\RR\times\{0\}$.

::: pf-proof

::: {.pf-step #b-forward}
If such a chart exists then $x\in\partial X$.

::: pf-proof
Let $h:U\to V\subset H^{2}$ be a chart with $h(x)=(a,0)$. If $x$ had a chart $g$ with values in $\RR^{2}$ on a neighbourhood $U'\subset U$, then $h\circ g^{-1}$ would be a homeomorphism of an open set of $\RR^{2}$ onto a neighbourhood of $h(x)=(a,0)$ in $H^{2}$, which part (a) forbids. So no such chart exists and $x\in\partial X$.
:::

:::

::: {.pf-step #b-backward}
If $x\in\partial X$ then every chart at $x$ has $h(x)\in\RR\times\{0\}$.

::: pf-proof
By the definition of a surface with boundary $x$ has a chart into $\RR^{2}$ or into $H^{2}$; the first alternative is excluded by the definition of $\partial X$. So there is a chart $h:U\to V\subset H^{2}$. If $h(x)=(a,t)$ with $t>0$, then $\{y\in V:\norm{y-h(x)}<t\}$ is an open ball contained in $H^{2}$, and $h$ followed by the identity is a chart at $x$ with values in $\RR^{2}$, a contradiction. Hence $t=0$.
:::

:::

:::

:::

::: {.pf-step #c}
(c) $\partial X$ is a $1$-manifold.

::: pf-proof

::: {.pf-step #c-chart}
Every point $x\in\partial X$ has a neighbourhood in $\partial X$ homeomorphic to an open interval.

::: pf-proof
Take a chart $h:U\to V\subset H^{2}$ at $x$ with $h(x)=(a,0)$, which exists by (b), and shrink it so that $V$ contains $(a-\varepsilon,a+\varepsilon)\times[0,\varepsilon)$; such an $\varepsilon>0$ exists because $V$ is open in $H^{2}$. Let $U_{0}=h^{-1}\big((a-\varepsilon,a+\varepsilon)\times[0,\varepsilon)\big)$, an open neighbourhood of $x$ in $X$. A point $y\in U_{0}$ lies in $\partial X$ exactly when its image has second coordinate $0$, by (b) applied to the chart $h$ restricted to $U_{0}$; so
$$
U_{0}\cap\partial X=h^{-1}\big((a-\varepsilon,a+\varepsilon)\times\{0\}\big),
$$
and $h$ carries it homeomorphically onto the open interval $(a-\varepsilon,a+\varepsilon)\times\{0\}$ of $\RR\times\{0\}\cong\RR$.
:::

:::

::: {.pf-step #c-axioms}
$\partial X$ is Hausdorff and has a countable basis.

::: pf-proof
$\partial X$ is a subspace of $X$, which is Hausdorff with a countable basis; a subspace of a Hausdorff space is Hausdorff (§17, printed p. 99) and a subspace of a second countable space is second countable (Theorem 30.2, printed p. 194).
:::

:::

::: {.pf-qed}
By steps [](#c-chart){.pf-ref} and [](#c-axioms){.pf-ref} every point of $\partial X$ has a neighbourhood homeomorphic to an open subset of $\RR^{1}$, and $\partial X$ is Hausdorff with a countable basis; that is the definition of a $1$-manifold.
:::

:::

:::

:::
:::
