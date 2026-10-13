---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-13
kind: problem
title: A norm induces a metric $d(x,y)=\|x-y\|$, but not every metric on a vector
  space arises from a norm
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Verify the remark following the definition of normed space: Every normed space $(X,\lVert\cdot\rVert)$ is a metric space by taking $d(x,y)=\lVert x-y\rVert$, while the converse is not true in general—even if $X$ is a vector space.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every normed vector space $X$, the function $d(x,y)=\lVert x-y\rVert$ is a metric.

::: pf-proof

The norm axioms give $d(x,y)\geq0$ with equality exactly when $x=y$. Absolute homogeneity yields $d(y,x)=\lVert -(x-y)\rVert=d(x,y)$. Finally, the norm triangle inequality yields
\[
d(x,z)=\lVert (x-y)+(y-z)\rVert\leq d(x,y)+d(y,z).
\]
These are precisely the metric axioms.

:::

:::

::: {.pf-step #s2}

The discrete metric on $\mathbb R$ is not induced by any norm.

::: pf-proof

Define $\delta(x,y)=0$ for $x=y$ and $\delta(x,y)=1$ otherwise. Non-negativity, separation, and symmetry are immediate. If $x\ne z$, at least one of $x\ne y$ and $y\ne z$ holds, so $\delta(x,z)\leq\delta(x,y)+\delta(y,z)$; thus $\delta$ is a metric. Suppose a norm induced $\delta$. For any $x\ne0$, absolute homogeneity would give
\[
1=\delta(2x,0)=\lVert2x\rVert=2\lVert x\rVert=2\delta(x,0)=2,
\]
a contradiction. In fact $\delta$ is translation-invariant, but not homogeneous; failure of homogeneity is the obstruction.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the forward assertion, while step [](#s2){.pf-ref} supplies a metric on a vector space that is not induced by a norm.

:::

:::

:::
