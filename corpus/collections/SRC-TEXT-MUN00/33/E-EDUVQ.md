---
schema: qual/card@1
id: E-EDUVQ
kind: problem
title: Box products of the line are completely regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: dbFin, "Section 33: Problem 9 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-33-the-urysohn-lemma/problem-9-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-33-the-urysohn-lemma/problem-9-solution.txt), checked against
    Munkres, Topology (2000), Section 33 Exercise 9, printed p. 213, and its printed hint, together
    with Exercise 18.8 and the fact that the box topology is finer than the uniform topology. Its
    route is the card's: a box neighbourhood of x is sent to (-1,1)^J by a coordinatewise affine map,
    the uniform distance g(y) = sup min(|y_alpha|,1) vanishes only at the origin and equals 1 off
    (-1,1)^J, and a function continuous for the uniform topology is continuous for the finer box
    topology. What was corrected: the source writes "It seems a more general result is true: a
    product of continuous functions is continuous (so, that the product of homeomorphisms is a
    homeomorphism)" and leaves that unproved, which is what the affine change of coordinates needs;
    the card states the coordinatewise affine map and notes that it carries boxes to boxes, so that
    it is a box-topology homeomorphism.
---

::: {.exercise}

Show that $\RR^J$ in the box topology is completely regular.
[Hint: Show that it suffices to consider the case where the box neighborhood $(-1, 1)^J$ is disjoint from $A$ and the point is the origin. Then use the fact that a function continuous in the uniform topology is also continuous in the box topology.]
:::

::: {.solution}
If $J=\varnothing$, the product is a singleton and is completely regular. Assume $J\neq\varnothing$. The box topology is Hausdorff. To prove complete regularity, let $A\subset\RR^J$ be closed and $x\notin A$. Choose a basic box neighborhood
$$
U=\prod_{\alpha\in J}(x_\alpha-\varepsilon_\alpha,x_\alpha+\varepsilon_\alpha)
$$
of $x$ disjoint from $A$, with each $\varepsilon_\alpha>0$. The coordinatewise affine homeomorphism
$$
h(y)_\alpha=\frac{y_\alpha-x_\alpha}{\varepsilon_\alpha}
$$
is a homeomorphism for the box topology, sends $x$ to $0$, and sends $U$ to $(-1,1)^J$.

Thus it suffices to separate $0$ from the complement of $(-1,1)^J$. Define
$$
g(y)=\sup_{\alpha\in J}\min\{\abs{y_\alpha},1\}.
$$
This is the distance from $y$ to $0$ in the uniform metric on $\RR^J$, hence is continuous in the uniform topology. The box topology is finer than the uniform topology, so $g$ is also box-continuous. We have $g(0)=0$, while $g(y)=1$ whenever $y\notin(-1,1)^J$. Therefore
$$
f=g\circ h
$$
is continuous, $f(x)=0$, and $f(a)=1$ for every $a\in A$. Hence $\RR^J$ with the box topology is completely regular.
:::
