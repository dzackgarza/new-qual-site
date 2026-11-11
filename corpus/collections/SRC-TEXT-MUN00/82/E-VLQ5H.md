---
schema: qual/card@1
id: E-VLQ5H
kind: problem
title: The uncountable fundamental group of the infinite earring
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 82 Supplementary Exercise 5, printed p. 500. The infinite earring is compact Hausdorff and second countable, and its fundamental group is uncountable, by the retractions onto the circles and an uncountable family of loops. Checked against Example 1 of Section 80 and Corollary 58.6. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. The previous note cited "Corollary 58.6", a statement about the fundamental group of a wedge used nowhere here; the citation is withdrawn and replaced by the ones used. Citations added: Example 1 of §80 (printed p. 487) for the earring and the retractions onto its circles, Theorem 27.3 (printed p. 173) for closed and bounded implying compact in the plane, Theorem 31.2 (printed p. 196) for a subspace of a Hausdorff space being Hausdorff, Theorem 30.2 (printed p. 191) for a subspace of a second-countable space being second countable, Theorem 54.5 (printed p. 345) for the fundamental group of a circle, and Theorem 18.3 (printed p. 108) for continuity of a map glued from two closed pieces. Corrected: continuity of the loop $f_a$ was attributed to the diameters of the circles tending to 0 alone, which is a statement about the values near $t=1$ only; the proof now also covers the junction points $t=1-2^{-k}$, where the two adjacent arcs meet at $p$, by the pasting lemma. Corrected: closedness of the earring in the plane was argued as "the only possible accumulation point of the family is $p$", which does not exhibit a neighbourhood of an arbitrary point outside $X$; the proof now does, separating $y\notin X$, $y\ne p$, from all but finitely many circles by radius and from the rest by closedness. What the certificate does not cover: the uncountability of $\{0,1\}^{\NN}$ is taken as known.
---

::: {.exercise}

Let $X$ be the infinite earring (see Example 1 of §80). Show that $X$ is a compact Hausdorff space with a countable basis whose fundamental group is uncountable.
[Hint: Let $r_n: X \to C_n$ be a retraction. Given a sequence $a_1, a_2, \ldots$ of zeros and ones, show there exists a loop $f$ in $X$ such that, for each $n$, the element $(r_n)_*[f]$ is trivial if and only if $a_n = 0$.]

:::

::: {.solution}

Let the infinite earring be
$$
X=\bigcup_{n\ge1}C_n,
$$
the union of the circles of Example 1 of §80 (printed p. 487), where $C_n$ has radius $1/n$, passes through the common point $p$, and has diameter $2/n$.

$X$ is compact. It is bounded, lying in the disk of radius $2$ about $p$. It is closed in $\RR^2$: given $y\in\RR^2\setminus X$ with $y\ne p$, put $d=\abs{y-p}>0$; the circles with $2/n<d/2$ lie in the disk of radius $d/2$ about $p$, which is disjoint from the ball of radius $d/2$ about $y$, and the finitely many remaining circles are closed and do not contain $y$, so a small enough ball about $y$ meets no circle. Since $p\in X$, this proves $X$ closed. A closed and bounded subspace of $\RR^2$ is compact (Theorem 27.3, printed p. 173). As a subspace of $\RR^2$ it is Hausdorff (Theorem 31.2, printed p. 196) and second countable (Theorem 30.2, printed p. 191).

For each $n$, let
$$
r_n:X\to C_n
$$
be the retraction equal to the identity on $C_n$ and sending every other circle to $p$, as in Example 1 of §80. It is continuous: continuity is immediate away from $p$, and near $p$ all sufficiently small circles lie in any prescribed neighbourhood of $p$.

Now let $a=(a_1,a_2,\ldots)\in\{0,1\}^{\NN}$. Divide $[0,1]$ into the intervals
$$
I_n=[1-2^{-(n-1)},\,1-2^{-n}]
$$
accumulating at $1$. On $I_n$, let $f_a$ traverse $C_n$ once if $a_n=1$, and stay at $p$ if $a_n=0$; at the junction points $1-2^{-k}$ and at $0$ the two adjacent definitions both give $p$; set $f_a(1)=p$. The map $f_a$ is continuous: at a point interior to $I_n$ it agrees with a path in $C_n$; at a junction point $1-2^{-k}$ its two one-sided restrictions are continuous maps on the closed intervals $I_k$ and $I_{k+1}$ agreeing at the common point, so it is continuous there by the pasting lemma (Theorem 18.3, printed p. 108); and at $t=1$ continuity follows from $\operatorname{diam}(C_n)\to0$, the values being $p$ at $t=1$. So $f_a$ is a loop in $X$ based at $p$.

For each $n$,
$$
(r_n)_*[f_a]=
\begin{cases}
0,&a_n=0,\\
1\in\pi_1(C_n,p)\cong\ZZ,&a_n=1,
\end{cases}
$$
because $r_n$ collapses every circle but $C_n$ to $p$ (Theorem 54.5, printed p. 345 for the fundamental group of a circle). Therefore if $a\ne b$, choose $n$ with $a_n\ne b_n$; then
$$
(r_n)_*[f_a]\ne(r_n)_*[f_b],
$$
so $[f_a]\ne[f_b]$ in $\pi_1(X,p)$. Thus
$$
\{0,1\}^{\NN}\hookrightarrow\pi_1(X,p).
$$
The left side is uncountable, hence $\pi_1(X,p)$ is uncountable.

:::
