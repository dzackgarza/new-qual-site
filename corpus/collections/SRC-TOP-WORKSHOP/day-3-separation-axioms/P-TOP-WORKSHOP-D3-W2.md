---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-W2
kind: problem
title: The separation-axiom implication chain (workshop warm-up)
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
$$T_4\Longrightarrow T_3\Longrightarrow T_2\Longrightarrow T_1\Longrightarrow T_0.$$
:::

::: {.solution}
We use the standard conventions: \(T_1\) means all singletons are closed, \(T_2\) means Hausdorff, \(T_3\) means regular \(+T_1\), and \(T_4\) means normal \(+T_1\).

A normal \(T_1\) space is regular: given \(x\notin F\) with \(F\) closed, normality separates the disjoint closed sets \(\{x\}\) and \(F\). Hence \(T_4\Rightarrow T_3\).

If \(X\) is regular \(T_1\) and \(x\ne y\), the set \(\{y\}\) is closed. Choose disjoint open neighborhoods of \(x\) and \(\{y\}\). Hence \(X\) is Hausdorff, so \(T_3\Rightarrow T_2\).

If \(X\) is Hausdorff and \(x\ne y\), there is an open neighborhood of \(x\) not containing \(y\). Thus
\[
X\setminus\{y\}=\bigcup_{x\ne y}U_x
\]
is open, so every singleton is closed. Hence \(T_2\Rightarrow T_1\).

Finally, if \(X\) is \(T_1\) and \(x\ne y\), then \(X\setminus\{y\}\) is an open set containing \(x\) but not \(y\). Thus the two points are topologically distinguishable, so \(T_1\Rightarrow T_0\).

Therefore
\[
T_4\Longrightarrow T_3\Longrightarrow T_2\Longrightarrow T_1\Longrightarrow T_0.
\]
:::
