---
schema: qual/card@1
id: E-RZLC7
kind: problem
title: Connected metric spaces with more than one point are uncountable
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

Show that a connected metric space having more than one point is uncountable.
:::

::: {.solution}
Let \(X\) be connected and let \(a\ne b\) in \(X\). Put \(r=d(a,b)>0\). The function
\[
f:X\to\mathbb R,\qquad f(x)=d(a,x)
\]
is continuous. Since \(X\) is connected, \(f(X)\) is connected in \(\mathbb R\), hence an interval. It contains \(0=f(a)\) and \(r=f(b)\), so
\[
[0,r]\subset f(X).
\]
Thus there is a surjection from \(X\) onto the uncountable set \([0,r]\). A countable set cannot surject onto an uncountable set. Therefore \(X\) is uncountable.
:::
