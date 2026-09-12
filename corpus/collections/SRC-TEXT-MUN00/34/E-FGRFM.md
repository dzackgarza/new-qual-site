---
schema: qual/card@1
id: E-FGRFM
kind: problem
title: Metrizability of the one-point compactification
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a locally compact Hausdorff space.
Let $Y$ be the one-point compactification of $X$.
Is it true that if $X$ has a countable basis, then $Y$ is metrizable?
Is it true that if $Y$ is metrizable, then $X$ has a countable basis?
:::

::: {.solution}
Both implications are true.

Assume first that \(X\) has a countable basis. Since \(X\) is locally compact Hausdorff, each point has a relatively compact open neighborhood. Refining the given countable basis, choose a countable cover
\[
U_1,U_2,\dots
\]
of \(X\) by open sets with compact closures. Put
\[
K_n=\overline{U_1}\cup\cdots\cup\overline{U_n}.
\]
Then each \(K_n\) is compact and \(K_n\subset K_{n+1}\), while \(\bigcup_nK_n=X\). If \(K\subset X\) is compact, the open cover \(\{U_n\}\) of \(K\) has a finite subcover, hence \(K\subset K_N\) for some \(N\). Therefore the neighborhoods
\[
Y\setminus K_n
\]
form a countable local basis at the point at infinity in the one-point compactification \(Y\). Together with a countable basis for \(X\), they give a countable basis for \(Y\). Since \(Y\) is compact Hausdorff, the compact-Hausdorff metrization theorem yields that \(Y\) is metrizable.

Conversely, if \(Y\) is metrizable, then compactness of \(Y\) implies \(Y\) is second countable: for each \(n\), choose a finite \(1/n\)-net and take balls with rational radii around the countable union of all chosen centers. Since \(X=Y\setminus\{\infty\}\) is an open subspace, it inherits a countable basis.
:::
