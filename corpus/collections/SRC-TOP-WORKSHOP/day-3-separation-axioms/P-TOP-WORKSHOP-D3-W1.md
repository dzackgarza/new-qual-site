---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-W1
kind: problem
title: Metric spaces are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Hausdorff Spaces
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
  date: 2026-11-19
  note: >-
    Restructured the prose solution into a structured proof under #2 and re-checked it: $r=d(x,y)/3$
    is positive by the metric axioms; a point in both balls gives $d(x,y)<2r=2d(x,y)/3$, a
    contradiction; and the two balls are open and contain their centres, which is the Hausdorff
    condition. No defect found in the statement or in the earlier solution; the card's own
    reference to "number 8" of the worksheet is left as printed. No retained solution set covers
    the item — the collection's provenance is the Day 3 worksheet — so the argument is the card's
    own. Not claimed: a citation to a publication.
---

::: {.problem}
If $(X,d)$ is a metric space, then it is Hausdorff [see number 8].
:::

::: {.solution}
No retained solution set covers this item, the collection's provenance being the worksheet itself, so the argument is the card's own. Let $(X,d)$ be a metric space and $B(x,r)=\{z\in X:d(x,z)<r\}$.

::: pf

::: {.pf-step #radius}
For distinct points $x\ne y$ of $X$, the number $r=d(x,y)/3$ is positive.

::: pf-proof
A metric takes values in $[0,\infty)$ and $d(x,y)=0$ only for $x=y$; since $x\ne y$, $d(x,y)>0$ and so $r=d(x,y)/3>0$.
:::

:::

::: {.pf-step #disjoint}
$B(x,r)\cap B(y,r)=\varnothing$.

::: pf-proof
Suppose $z$ lies in both balls. Then $d(x,z)<r$ and $d(z,y)<r$, so the triangle inequality gives
$$
d(x,y)\le d(x,z)+d(z,y)<2r=\tfrac{2}{3}d(x,y),
$$
which forces $d(x,y)<0$, impossible. Hence no such $z$ exists.
:::

:::

::: {.pf-step}
$X$ is Hausdorff.

::: pf-proof
Given distinct $x,y\in X$, step [](#radius){.pf-ref} supplies $r>0$ and step [](#disjoint){.pf-ref} shows the balls $B(x,r)$ and $B(y,r)$ are disjoint. Each ball is open and contains its centre, so they are disjoint open sets with $x\in B(x,r)$ and $y\in B(y,r)$, which is the Hausdorff condition.
:::

:::

:::
:::
