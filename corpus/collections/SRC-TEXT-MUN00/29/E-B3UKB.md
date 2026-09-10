---
schema: qual/card@1
id: E-B3UKB
kind: problem
title: Compact closure neighborhoods in locally compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
---

::: {.exercise}

Show that if $X$ is a Hausdorff space that is locally compact at the point $x$, then for each neighborhood $U$ of $x$, there is a neighborhood $V$ of $x$ such that $\overline{V}$ is compact and $\overline{V} \subset U$.
:::

::: {.solution}
Let \(U\) be a neighborhood of \(x\). Since \(X\) is locally compact at \(x\), there is a neighborhood \(N\) of \(x\) whose closure \(K=\overline N\) is compact. Replacing \(N\) by \(N\cap U\), we may assume \(N\subset U\), but we still need the closure inside \(U\).

The compact Hausdorff subspace \(K\) is regular. The set \(K\cap U\) is an open neighborhood of \(x\) in \(K\), so there is an open set \(W\) in \(K\) with
\[
x\in W\subset \overline W^{\,K}\subset K\cap U.
\]
Write \(W=K\cap O\) for some open \(O\subset X\), and put \(V=N\cap O\). Then \(V\) is a neighborhood of \(x\). Its closure in \(X\) satisfies
\[
\overline V\subset K\cap\overline O\subset \overline W^{\,K}\subset U.
\]
Also \(\overline V\) is closed in compact \(K\), hence compact. Thus \(V\) has the required properties.
:::
