---
schema: qual/card@1
id: P-MIAAZ
kind: problem
title: A continuous convex function on the unit ball of a reflexive Banach space attains
  its minimum
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
relations: []
review: draft
---

::: {.problem}
Show that every convex continuous function defined on the closed unit ball of a reflexive Banach space achieves a minimum.
(A convex function on a convex subset $A$ of a normed space is a real valued function $f$ on $A$ such that for every $x,y\in A$ and every $0<\lambda<1$ we have $f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y)$.)
:::

::: {.solution}
At first, Since $X$ is reflexive, then $X$ is isomorphic to $X^{**}$.
By Alaoglu's theorem, The unit ball of $X^{**}$ is $w^*$-compact, which implies that the unit ball of $X$, $B$ is weak compact.
Then, we know that any function is lower semi-continuous convex iff it is weak lower-semi continuous convex.
(This is a classical result in convex analysis.
The epigraph is used in its proof or Mazur's lemma?)
Thus $f$ is weak-lower-semi-continuous.
Thus it can achieve the minimum since $B$ is weak compact.
:::
