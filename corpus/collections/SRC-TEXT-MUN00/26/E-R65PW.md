---
schema: qual/card@1
id: E-R65PW
kind: problem
title: Finite unions of compact subspaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Show that a finite union of compact subspaces of $X$ is compact.
:::

::: {.solution}
Let \(K_1,\dots,K_n\) be compact subspaces of \(X\), and let \(\mathcal U\) be an open cover of \(K_1\cup\cdots\cup K_n\). For each \(i\), the family \(\mathcal U\) covers \(K_i\), so compactness gives a finite subfamily \(\mathcal U_i\subset\mathcal U\) covering \(K_i\). Then
\[
\mathcal U_1\cup\cdots\cup\mathcal U_n
\]
is finite and covers the union. Hence every finite union of compact subspaces is compact.
:::
