---
schema: qual/card@1
id: E-L4NKO
kind: problem
title: Locally compact Hausdorff spaces are regular
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

Show that every locally compact Hausdorff space is regular.
:::

::: {.solution}
Let \(X\) be locally compact Hausdorff, let \(A\subset X\) be closed, and let \(x\notin A\). The open set \(U=X\setminus A\) is a neighborhood of \(x\). By the compact-closure neighborhood lemma from §29, there is a neighborhood \(V\) of \(x\) such that
\[
\overline V\text{ is compact and }\overline V\subset U.
\]
Then
\[
V\quad\text{and}\quad X\setminus\overline V
\]
are disjoint open sets containing \(x\) and \(A\), respectively. Thus \(X\) is regular.
:::
