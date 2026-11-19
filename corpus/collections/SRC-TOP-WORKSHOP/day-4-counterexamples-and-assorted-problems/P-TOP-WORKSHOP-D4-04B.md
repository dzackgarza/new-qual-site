---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-04B
kind: problem
title: The unit sphere quotient by height fibers is an interval
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Homeomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct.
    Added: the continuity of the height map as a restriction of a coordinate projection, the
    bound on its values, the surjectivity witness with its explicit coordinates, the fibre
    description that makes injectivity immediate, and the closed-map reason that a continuous
    bijection from a compact space to a Hausdorff space has continuous inverse. Not claimed: a
    retained solution set; the collection's provenance is the workshop sheet only.
---

::: {.problem}
Let $X$ be the unit sphere in $\RR^3$ and define an equivalence relation on $X$ by $$ (x,y,z)\sim(x',y',z')\Longleftrightarrow z=z'.$$ Let $Z=X/\sim$ be the quotient space under this equivalence relation, with the quotient topology.
Show that $Z$ is homeomorphic to the interval $[-1,1]$.
:::

::: {.solution}
Throughout $X = S^{2} = \theset{(x,y,z) \in \RR^{3} \mid x^{2}+y^{2}+z^{2} = 1}$, the relation is $(x,y,z) \sim (x',y',z')$ exactly when $z = z'$, $Z = X/\sim$ carries the quotient topology and $q\colon X \to Z$ is the quotient map. The collection's `provenance` is the Day 4 workshop sheet, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #continuous}
The height map $h\colon X \to [-1,1]$, $h(x,y,z) = z$, is continuous and constant on each equivalence class.

::: pf-proof
$h$ is the restriction to $X$ of the projection $\RR^{3} \to \RR$ onto the third coordinate, which is continuous, so $h$ is continuous for the subspace topology of $X$. Its values lie in $[-1,1]$ because $z^{2} \le x^{2}+y^{2}+z^{2} = 1$. If $p \sim p'$ then their third coordinates agree, so $h(p) = h(p')$.

:::

:::

::: {.pf-step #factor}
There is a unique continuous $\bar h\colon Z \to [-1,1]$ with $h = \bar h \circ q$.

::: pf-proof
This is the universal property of the quotient: a continuous map out of $X$ that is constant on the classes factors uniquely through $q$, and the factor is continuous because $q$ is a quotient map. Uniqueness holds because $q$ is surjective.

:::

:::

::: {.pf-step #surjective}
$\bar h$ is surjective.

::: pf-proof
For $t \in [-1,1]$ the point $(\sqrt{1-t^{2}}, 0, t)$ lies in $X$ and has height $t$, so $t = h(p) = \bar h\bigl(q(p)\bigr)$ is in the image.

:::

:::

::: {.pf-step #injective}
$\bar h$ is injective.

::: pf-proof
If $\bar h(q(p)) = \bar h(q(p'))$ then $h(p) = h(p')$, so $p$ and $p'$ have equal third coordinates and therefore $p \sim p'$, that is $q(p) = q(p')$; a map is injective exactly when it is constant on the fibres of the quotient in this way.

:::

:::

::: {.pf-step #compact}
$Z$ is compact and $[-1,1]$ is Hausdorff.

::: pf-proof
$X = S^{2}$ is a closed and bounded subset of $\RR^{3}$, hence compact; the continuous image of a compact space is compact, and $Z = q(X)$ is such an image. The interval is a subspace of $\RR$, which is Hausdorff, and subspaces of Hausdorff spaces are Hausdorff.

:::

:::

::: pf-step
$\bar h$ is a homeomorphism, so $Z \cong \boxed{[-1,1]}$.

::: pf-proof
Step [](#factor){.pf-ref} gives a continuous map, steps [](#surjective){.pf-ref} and [](#injective){.pf-ref} make it a bijection, and step [](#compact){.pf-ref} puts a compact domain and a Hausdorff codomain around it. A continuous bijection from a compact space onto a Hausdorff space is a homeomorphism: it carries closed subsets of the compact domain, which are compact, to compact hence closed subsets of the Hausdorff codomain, so its inverse is continuous.

:::

:::

:::
:::
