---
schema: qual/card@1
id: E-FNMUB
kind: problem
title: Uniqueness of continuous extensions into Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 13, printed p. 112; the stored
    statement is the printed one, an extension to the closure of A being meant.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.13, PDF p. 13. Two presumed extensions
    differing at a point of the closure are separated by disjoint open sets in Y, and the
    intersection of their preimages is a neighbourhood of that point meeting A, where the
    two must agree. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $A \subset X$; let $f: A \to Y$ be continuous; let $Y$ be Hausdorff.
Show that if $f$ may be extended to a continuous function $g: \overline{A} \to Y$, then $g$ is uniquely determined by $f$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.13, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs. Whitman, printed p. 189, gives the same proof.

Let $g_{1},g_{2}:\overline{A}\to Y$ be continuous and both extend $f$, so $g_{1}(x)=g_{2}(x)=f(x)$ for $x\in A$. Suppose $g_{1}(x_{0})\ne g_{2}(x_{0})$ for some $x_{0}\in\overline{A}$.

Since $Y$ is Hausdorff there are disjoint open sets $U\ni g_{1}(x_{0})$ and $V\ni g_{2}(x_{0})$. By continuity $g_{1}^{-1}(U)$ and $g_{2}^{-1}(V)$ are open in $\overline{A}$, so
$$
W=g_{1}^{-1}(U)\cap g_{2}^{-1}(V)
$$
is an open neighbourhood of $x_{0}$ in $\overline{A}$. Write $W=\overline{A}\cap O$ with $O$ open in $X$. Since $x_{0}\in\overline{A}$ and $O$ is a neighbourhood of $x_{0}$ in $X$, there is a point $y\in O\cap A$; then $y\in A\subset\overline{A}$ gives $y\in W$.

But $y\in A$, so $g_{1}(y)=g_{2}(y)=f(y)$; and $y\in g_{1}^{-1}(U)$ gives $f(y)\in U$, while $y\in g_{2}^{-1}(V)$ gives $f(y)\in V$. Thus $f(y)\in U\cap V=\varnothing$, a contradiction.

Hence $g_{1}=g_{2}$: the continuous extension of $f$ to $\overline{A}$ is unique when it exists.
:::
