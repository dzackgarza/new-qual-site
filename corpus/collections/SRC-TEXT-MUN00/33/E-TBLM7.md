---
schema: qual/card@1
id: E-TBLM7
kind: problem
title: Locally compact Hausdorff spaces are completely regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Show that every locally compact Hausdorff space is completely regular.
:::

::: {.solution}
Let \(X\) be locally compact Hausdorff. Its one-point compactification \(X^*=X\cup\{\infty\}\) is compact Hausdorff, hence normal.

Let \(A\subset X\) be closed and \(x\in X\setminus A\). The set
\[
A^*=A\cup\{\infty\}
\]
is closed in \(X^*\), because its complement \(X\setminus A\) is open in \(X\), hence open in \(X^*\) away from the point at infinity. By Urysohn's lemma there is a continuous
\[
F:X^*\to[0,1]
\]
with \(F(x)=0\) and \(F(A^*)=\{1\}\). Restricting \(F\) to \(X\) gives a continuous function separating \(x\) from \(A\). Therefore \(X\) is completely regular.
:::
