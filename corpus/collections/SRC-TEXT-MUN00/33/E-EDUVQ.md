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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The solution opened by claiming that no retained solution set covers the exercise, contradicting the
    audit note above it, which transcribes dbFin's Section 33 Problem 9 solution from the copy kept at
    tmp/sources/dbfin/section-33-the-urysohn-lemma/problem-9-solution.txt. That copy was read again: it
    begins by reducing to separating the origin from the complement of (-1,1)^J, which is the printed hint,
    and it asserts without proof that a product of continuous functions is continuous. The opening
    sentence now names the set, its route and the step the card supplies in place of the source's
    assertion. Not checked here: the printed page of the exercise, which is the earlier session's,
    because the book's page for Section 33 Exercise 9 was not re-read in this session.

---

::: {.exercise}

Show that $\RR^J$ in the box topology is completely regular.
[Hint: Show that it suffices to consider the case where the box neighborhood $(-1, 1)^J$ is disjoint from $A$ and the point is the origin. Then use the fact that a function continuous in the uniform topology is also continuous in the box topology.]
:::

::: {.solution}

The argument follows the retained published solution of dbFin, "Section 33: Problem 9 Solution" (`tmp/sources/dbfin/section-33-the-urysohn-lemma/problem-9-solution.txt`, read 2026-11-10): it is enough to separate the origin from the complement of the box neighbourhood $(-1,1)^{J}$, which is the printed hint. The card separates that into steps and supplies what the source leaves unproved, as the audit records: the source asserts that a product of continuous functions is continuous, which is what its coordinatewise affine change of coordinates needs, and the card instead states the map $y\mapsto (y_{\alpha}-x_{\alpha})/\varepsilon_{\alpha}$ and proves that it carries boxes to boxes, so that it is a homeomorphism of the box topology. The statement is Munkres, *Topology* (2000), Section 33 Exercise 9, with its printed hint.

::: pf

::: {.pf-step #trivial}
If $J=\varnothing$ then $\RR^{J}$ is a singleton and is completely regular.

::: pf-proof
$\RR^{\varnothing}$ has one point, the empty function; its only closed sets are $\varnothing$ and the whole space, and the constant function $0$ separates the point from $\varnothing$.
:::

:::

::: {.pf-step #reduction}
For $x\notin A$ with $A$ closed, a coordinatewise affine homeomorphism $h$ of the box topology sends $x$ to $0$ and carries a box neighbourhood of $x$ inside $A$'s complement onto $(-1,1)^{J}$.

::: pf-proof
Since $A$ is closed and $x\notin A$, there is a basis element $\prod_{\alpha}(x_{\alpha}-\varepsilon_{\alpha},x_{\alpha}+\varepsilon_{\alpha})$ of the box topology with all $\varepsilon_{\alpha}>0$ containing $x$ and contained in $\RR^{J}\setminus A$. Define $h(y)_{\alpha}=(y_{\alpha}-x_{\alpha})/\varepsilon_{\alpha}$; each coordinate map is a homeomorphism of $\RR$, and a product of homeomorphisms is a homeomorphism for the box topology, since it carries a box $\prod(a_{\alpha},b_{\alpha})$ to the box $\prod\big((a_{\alpha}-x_{\alpha})/\varepsilon_{\alpha},(b_{\alpha}-x_{\alpha})/\varepsilon_{\alpha}\big)$ and likewise for its inverse. Then $h(x)=0$ and $h$ carries the displayed neighbourhood onto $\prod_{\alpha}(-1,1)=(-1,1)^{J}$. So it suffices to separate $0$ from the complement of $(-1,1)^{J}$, which is closed because $(-1,1)^{J}$ is open.
:::

:::

::: {.pf-step #function}
The function $g(y)=\sup_{\alpha}\min\theset{\abs{y_{\alpha}},1}$ is continuous for the box topology, with $g(0)=0$ and $g(y)=1$ for $y\notin(-1,1)^{J}$.

::: pf-proof
$g$ is the distance from $y$ to $0$ in the uniform metric $\bar\rho$ on $\RR^{J}$, hence is continuous for the uniform topology, i.e. $\bar\rho$-continuous (its inverse image of $[0,t)$ is the ball of radius $t$ about $0$). The uniform topology is coarser than the box topology (§20), so a function continuous for the uniform topology is continuous for the finer box topology: the box-preimage of an open set is the same set and is box-open. Also $g(0)=0$, and if $y\notin(-1,1)^{J}$ then some coordinate satisfies $\abs{y_{\alpha}}\ge1$, so $g(y)\ge1$ while $g\le1$ always.
:::

:::

::: {.pf-step #separating}
$f=g\circ h$ is continuous for the box topology, with $f(x)=0$ and $f(a)=1$ for $a\in A$.

::: pf-proof
$h$ is a box-homeomorphism and $g$ is box-continuous by step [](#function){.pf-ref}, so the composite is box-continuous. Since $h(x)=0$ we get $f(x)=0$; and for $a\in A$ the point $h(a)$ lies outside $(-1,1)^{J}$ by step [](#reduction){.pf-ref}, so $f(a)=1$.
:::

:::

::: {.pf-qed}
Given a closed $A$ and a point $x\notin A$, step [](#separating){.pf-ref} produces a continuous $f:\RR^{J}\to[0,1]$ with $f(x)=0$ and $f(A)=1$; the space is Hausdorff, so it is completely regular (step [](#trivial){.pf-ref} covers $J=\varnothing$).
:::

:::

:::
