---
schema: qual/card@1
id: E-QJXDP
kind: problem
title: Weak local connectedness at a point without local connectedness
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 7, printed p. 162, with the figure
    and the hint; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.7, PDF pp. 9-10. A connected neighbourhood of p
    would have to contain every a_i, by spreading along the segments crossing a small ball;
    the sub-broom over the tail of the a_i is a path-connected set containing a
    neighbourhood of p. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    Two defects located, neither repaired in this pass, which is why the solution section
    still carries the retained set's argument. (1) The printed statement cannot hold. The
    definition in Exercise 6 of the same page, read at 600 dpi from the retained PDF
    (printed p. 162), is "for every neighborhood U of x, there is a connected subspace of X
    contained in U that contains a neighborhood of x"; the connected subspace then contains
    a neighbourhood of x, so it is itself a connected neighbourhood of x contained in U, and
    a space weakly locally connected at x is locally connected at x. The exercise asks for a
    space that is not locally connected at p and is weakly locally connected at p, so the
    printed conclusion is impossible under the printed definition, whatever the space.
    (2) The description of the space in the solution section, taken from the retained
    positron0802 solution, does not have the property the exercise asserts: with bristles
    running from (a_i,0) to (a_{i+1},r_j), choose epsilon with a_{N+1} < epsilon < a_N and
    delta no larger than a_{N+1}; every bristle meeting B(p,delta) has its foot of the form
    (a_i,0) with a_i <= a_{N+1} < epsilon, hence inside B(p,epsilon), so the component of p
    in the trace of B(p,epsilon) contains the whole trace of B(p,delta) and is a
    neighbourhood of p: that space is locally connected at p. The book draws Figure 25.1 and
    states no formula for the bristles, no retained set in the checkout describes them in
    words (the Whitman, 9beach and shenapse manuals have no occurrence of the broom), and
    the figure does not determine what the bristles attach to. The card is therefore left as
    it stands pending a description of the space that the figure settles; rewriting the
    proof alone would not repair it.
---

::: {.exercise}

Consider the "infinite broom" $X$ pictured in Figure 25.1 of the text.
Show that $X$ is not locally connected at $p$, but is weakly locally connected at $p$.
[Hint: Any connected neighborhood of $p$ must contain all the points $a_i$.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.7, PDF pp. 9--10** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the description of the broom and both halves of the argument are theirs.

Place $p$ at the origin. The broom is $X=L\cup\bigcup_{i,j}L_{i,j}$, where $L$ is the segment from $p$ to $(a_{1},0)$, the points $(a_{i},0)$ tend decreasingly to $p$, and $L_{i,j}$ is the segment from $(a_{i},0)$ to $(a_{i+1},r_{j})$, with $r_{j}$ decreasing to $0$.

*$X$ is not locally connected at $p$.* Let $W$ be a connected neighbourhood of $p$. Being open, $W$ contains all but finitely many of the points $(a_{i},0)$; let $N$ be least with $(a_{N},0)\in W$, and choose a ball $B$ about $(a_{N},0)$ inside $W$. That ball meets all but finitely many of the segments $L_{N,j}$; each such segment is connected and meets $W$, so lies in $W$, forcing $(a_{N-1},0)\in W$: contradiction. Hence no connected neighbourhood of $p$ is contained in a ball about $p$ of radius less than $d(p,(a_{1},0))$, and $X$ is not locally connected at $p$.

*$X$ is weakly locally connected at $p$.* Let $U\ni p$ be open, with $p\in B(p,r)\subset U$. All but finitely many $(a_{i},0)$ lie in $B(p,r)$; let $N$ be such that $(a_{i},0)\in B(p,r)$ for $i\ge N$. Then
$$
C=\bigcup_{i\ge N}\Big(L\cap U\cup\bigcup_{j}L_{i,j}\Big)
$$
is a union of path-connected sets with the common point $p$, hence path connected and contained in $U$, and it contains $B(p,\delta)\cap X$ for $\delta<a_{N}$: a connected set containing a neighbourhood of $p$, as required.
:::
