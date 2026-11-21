---
schema: qual/card@1
id: E-YI3QM
kind: problem
title: The closed disk as a surface with boundary
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §78 Exercise 3, printed p. 476. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-1522925-E-YI3QM.md, read whole.
    Math Stack Exchange 1522925 has two answers. 1522970 by levap (2015-11-10) proves the exercise in general
    dimension: the closed disk has an R^2-chart at every interior point and, "using polar coordinates", a
    half-space chart at every point of the circle, and it records that the disjointness of interior and
    boundary points is the non-trivial input, which is Exercise 2(a). That answer states the construction in
    one sentence and writes no chart; the explicit chart (theta, 1-r) is the card's, and it is now stated in
    the solution that the answer supplies the construction and the card supplies the formula. 1522959 by
    Luis Vera asserts that no neighbourhood of a point of S^1 is homeomorphic to an open set of R^2 without
    proof. Rejected in the search: mse 5039847, which has no answer.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 78 Exercise 3, printed p. 476. Charts inside the disc and the explicit half-plane chart (theta, 1 - r) at a boundary point. Checked against the definition of a 2-manifold with boundary printed in the same exercise. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Show that the closed unit ball in $\RR^2$ is a 2-manifold with boundary.
:::

::: {.solution}

The construction of the boundary chart is the card's own; Math Stack Exchange answer 1522970 records the same construction for the closed ball in $\RR^{n}$ without writing a chart, and is cited at the foot of this solution rather than transcribed.

Let $D^{2}=\{(x,y)\in\RR^{2}:x^{2}+y^{2}\le1\}$ and $H^{2}=\{(u,v)\in\RR^{2}:v\ge0\}$, with $D^{2}$ carrying the subspace topology.

::: pf

::: {.pf-step #hausdorff}
$D^{2}$ is Hausdorff and has a countable basis.

::: pf-proof
$\RR^{2}$ has the countable basis of the boxes $(a,b)\times(c,d)$ with rational corners (Example 1 of §30, printed p. 190), so it is second countable, and it is Hausdorff. A subspace of a second-countable space is second countable (Theorem 30.2, printed p. 191) and a subspace of a Hausdorff space is Hausdorff (Theorem 17.11), so $D^{2}$ has both properties. Neither property is obtained here from metrizability: what is used is the countable basis of $\RR^{2}$ and the separation of $\RR^{2}$.
:::

:::

::: {.pf-step #interior-charts}
Every point $p$ with $\norm{p}<1$ has a neighbourhood homeomorphic to an open set of $\RR^{2}$.

::: pf-proof
Choose $0<\varepsilon<1-\norm{p}$. Then $B(p,\varepsilon)=\{q:\norm{q-p}<\varepsilon\}$ is contained in $D^{2}$, and it is an open subset of $\RR^{2}$; the identity carries it to an open set of the model space. So $D^{2}\cap B(p,\varepsilon)=B(p,\varepsilon)$ is a chart at $p$ modelled on $\RR^{2}$.
:::

:::

::: {.pf-step #boundary-charts}
Every point $p$ with $\norm{p}=1$ has a neighbourhood homeomorphic to an open set of $H^{2}$, carrying $p$ to the boundary line $\RR\times\{0\}$.

::: pf-proof

::: {.pf-step #rotate}
It suffices to treat $p=(1,0)$.

::: pf-proof
For $p\in S^{1}$ let $\rho$ be the rotation of $\RR^{2}$ about the origin carrying $p$ to $(1,0)$; it is a homeomorphism of $\RR^{2}$ onto itself carrying $D^{2}$ and $S^{1}$ onto themselves. If $h$ is a chart at $(1,0)$ on a neighbourhood $U$ of $(1,0)$, then $h\circ\rho$ is a homeomorphism of the neighbourhood $\rho^{-1}(U)$ of $p$ onto the same open set of $H^{2}$, and it carries $p$ to $h(1,0)$. So a chart at $(1,0)$ with values in $H^{2}$ gives a chart at $p$ with values in $H^{2}$.
:::

:::

::: {.pf-step #polar}
For $0<\delta<\pi/2$ the map $\varphi(x,y)=\big(\theta(x,y),\,1-\sqrt{x^{2}+y^{2}}\big)$, $\theta$ being the angle of $(x,y)$ with the positive $x$-axis, is a homeomorphism of the open neighbourhood
$$
W=D^{2}\cap\{x>0\}\cap\{\abs{\theta(x,y)}<\delta\}
$$
of $(1,0)$ onto $(-\delta,\delta)\times[0,1)$, which is open in $H^{2}$, and $\varphi(1,0)=(0,0)$.

::: pf-proof
On the region $x>0$ a point has unique polar coordinates $(r,\theta)\in(0,\infty)\times(-\pi/2,\pi/2)$, with $x=r\cos\theta$ and $y=r\sin\theta$, and the two formulas exhibit mutually inverse continuous maps between that region and $(0,\infty)\times(-\pi/2,\pi/2)$: continuity of $q\mapsto(\norm{q},\theta(q))$ follows from the continuity of the norm, of $\arctan(y/x)$ and of the condition $x>0$. So $q\mapsto(\theta(q),\norm{q})$ is a homeomorphism there, and $\varphi$ is its composition with $(\theta,r)\mapsto(\theta,1-r)$, a homeomorphism of $(-\delta,\delta)\times(0,1]$ onto $(-\delta,\delta)\times[0,1)$. The set $W$ is the preimage of $(-\delta,\delta)\times(0,1]$ under that homeomorphism, intersected with $D^{2}$, so $W$ is open in $D^{2}$, and its image is the open set $(-\delta,\delta)\times[0,1)$ of $H^{2}$.
:::

:::

::: {.pf-qed}
Taking $\delta$ as in step [](#polar){.pf-ref} and shrinking to $D^{2}\cap B((1,0),\delta')$ if necessary, the restriction of $\varphi$ is a homeomorphism of a neighbourhood of $(1,0)$ in $D^{2}$ onto an open set of $H^{2}$, and it sends $(1,0)$ to $(0,0)\in\RR\times\{0\}$; step [](#rotate){.pf-ref} carries this chart to any other point of $S^{1}$.
:::

:::

:::

::: {.pf-step #manifold}
$D^{2}$ is a $2$-manifold with boundary whose manifold boundary is $S^{1}$.

::: pf-proof
Every point of $D^{2}$ has a neighbourhood homeomorphic to an open set of $\RR^{2}$ or of $H^{2}$ by steps [](#interior-charts){.pf-ref} and [](#boundary-charts){.pf-ref}, and step [](#hausdorff){.pf-ref} gives the separation and countability axioms, so $D^{2}$ is a $2$-manifold with boundary. A point of $S^{1}$ has no neighbourhood homeomorphic to an open set of $\RR^{2}$, by part (a) of [[E-RKSXA]], and a chart at such a point with values in $H^{2}$ carries it to the line $\RR\times\{0\}$ by step [](#boundary-charts){.pf-ref}; a point with $\norm{p}<1$ has an $\RR^{2}$-chart by step [](#interior-charts){.pf-ref} and so is not a boundary point. Hence $\partial D^{2}=S^{1}$.
:::

:::

:::
The same example is worked through, in general dimension, by levap's answer 1522970 (https://math.stackexchange.com/a/1522970), posted 2015-11-10 to Math Stack Exchange question 1522925, "Topological Boundary vs Manifold Boundary" (https://math.stackexchange.com/questions/1522925, asked by the account posting as user153582 on the same day): for the closed unit ball $B$ in $\RR^{n}$, "using polar coordinates, you can easily construct a homeomorphism from an open neighborhood of each point $x\in B$ with $\norm{x}=1$ to an open neighborhood of $H^{n}$ mapping $x$ to $\partial H^{n}$", while a point with $\norm{x}<1$ has the open ball as an $\RR^{n}$-chart. That answer states the construction and writes no chart, the chart of step [](#polar){.pf-ref} being the card's; it also records, as the second answer 1522959 by Luis Vera does not, that the disjointness of interior and boundary points is the non-trivial part, which is parts (a) and (b) of [[E-RKSXA]].

:::
