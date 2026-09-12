---
schema: qual/card@1
id: E-J8QUX
kind: problem
title: The two-dimensional CW complex is metrizable
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

Show that the space constructed in [[E-VYYH3]] is in fact metrizable.
[Hint: The quotient map is a perfect map.]
:::

::: {.solution}
Use the notation of [[E-VYYH3]]. Let
\[
q:Z=A\sqcup B_1\sqcup\cdots\sqcup B_m\longrightarrow X
\]
be the quotient map. The space \(Z\) is a finite disjoint union of compact metrizable spaces, hence compact metrizable and second countable. The preceding exercise shows that \(X\) is Hausdorff.

Since \(Z\) is compact and \(X\) is Hausdorff, every closed subset of \(Z\) is compact and therefore has closed image under \(q\). Thus \(q\) is a closed continuous surjection. Every fiber \(q^{-1}(x)\) is closed in the compact space \(Z\), hence compact. Therefore \(q\) is a perfect map.

Perfect maps preserve second countability in this situation: by Exercise 7(d) of §31, since \(Z\) has a countable basis, so does \(X\). We already know \(X\) is compact Hausdorff. By the compact-Hausdorff metrization criterion of §34, a compact Hausdorff space with a countable basis is metrizable.

Hence the two-dimensional CW complex \(X\) constructed in [[E-VYYH3]] is metrizable.
:::
