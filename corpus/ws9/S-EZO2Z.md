---
schema: qual/card@1
id: S-EZO2Z
kind: solution
title: Solution to P-MIAAZ
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
relations:
- kind: solves
  target: P-MIAAZ
review: draft
---

:::{.solution}
At first, Since $X$ is reflexive, then $X$ is isomorphic to $X^{**}$. By Alaoglu's theorem, The unit ball of $X^{**}$ is $w^*$-compact, which implies that the unit ball of $X$, $B$ is weak compact. Then, we know that any function is lower semi-continuous convex iff it is weak lower-semi continuous convex. (This is a classical result in convex analysis. The epigraph is used in its proof or Mazur's lemma?) Thus $f$ is weak-lower-semi-continuous. Thus it can achieve the minimum since $B$ is weak compact.
:::
