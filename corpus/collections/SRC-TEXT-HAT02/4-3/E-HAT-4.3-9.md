---
schema: qual/card@1
id: E-HAT-4.3-9
kind: problem
title: "Linear projection is fibration but not fiber bundle"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.3 Exercise 9 (AT.txt 20779-20780) and repaired. The fibration half
    is correct: in the card's own coordinates the fibre-preserving retraction r(x,y) = (x, min{y,
    lambda(x)}) of a product bundle onto the simplex gives homotopy lifting. The reason given for "not
    a fiber bundle" was false as stated: the card claimed the fibres over both endpoints are points,
    but if the third vertex projects to an endpoint of the base edge there is no such thing -- for
    p(x,y) = x on conv{(0,0),(1,0),(0,1)} the fibre over 0 is the edge {0} x [0,1]. The card now argues
    from its own model: the fibre over x is the interval {x} x [0, lambda(x)], the third vertex gives
    some s with lambda(s) > 0, and at least one endpoint x_0 differs from s, where the fibre is the
    single vertex of the base edge. A point is not homeomorphic to a nondegenerate interval, and the
    fibres of a bundle over the connected edge are all homeomorphic (AT.txt 20067-20068). Not checked:
    nothing outside this exercise.

---

::: {.problem}
Show that a linear projection of a 2-simplex onto one of its edges is a fibration but not a fiber bundle. [Use the preceding problem.]
:::

::: {.solution}
Choose affine coordinates in which the simplex is
$$
\Delta=\{(x,y):0\le x\le1,\ 0\le y\le \lambda(x)\}
$$
for a continuous piecewise-linear function $\lambda\ge0$, and the projection is
$$
p(x,y)=x
$$
onto the base edge $I=[0,1]$. Embed $\Delta$ in the trivial bundle
$$
I\times[0,M]\to I
$$
for $M\ge\max\lambda$. There is a fiber-preserving retraction
$$
r:I\times[0,M]\to\Delta,
\qquad
r(x,y)=(x,\min\{y,\lambda(x)\}).
$$

Given any homotopy lifting problem for $p:\Delta\to I$, first regard the initial lift as a map into the product bundle. Lift the base homotopy there, then compose the lift with $r$. Since $r$ preserves the base coordinate and restricts to the identity on $\Delta$, this gives a lift with the prescribed initial map. Thus
$$
\boxed{p:\Delta\to I\text{ is a fibration}.}
$$

It is not a fiber bundle. In the coordinates above the fiber over $x\in[0,1]$ is the interval $\{x\}\times[0,\lambda(x)]$, because $p$ is linear and convexity makes the fiber the convex hull of the vertices lying over $x$. The third vertex $v_2$ projects to a point $s\in[0,1]$ with $\lambda(s)>0$, so the fiber over $s$ is a nondegenerate interval. A vertex of the base edge lies over an endpoint of the base edge, and since $s$ is a single point at least one endpoint $x_0\in\{0,1\}$ satisfies $x_0\ne s$; then $v_2$ does not lie over $x_0$, and the only vertex of $\Delta$ lying over $x_0$ is the vertex of the base edge itself, so the fiber over $x_0$ is that single point. Hence some fiber is a point and some fiber is a nondegenerate interval. These fibers are not homeomorphic, whereas all fibers of a bundle over the connected edge would be homeomorphic. Hence $p$ is not a fiber bundle.
:::
