---
schema: qual/card@1
id: E-NWR5K
kind: problem
title: Countability axioms pass through open maps
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
---

::: {.exercise}

Let $f: X \to Y$ be a continuous open map.
Show that if $X$ satisfies the first or the second countability axiom, then $f(X)$ satisfies the same axiom.
:::

::: {.solution}
Replace \(Y\) by \(f(X)\), so \(f\) is surjective.

Suppose \(X\) is first countable. Fix \(y\in Y\) and choose \(x\in f^{-1}(y)\). Let \(B_1,B_2,\dots\) be a countable local basis at \(x\). Since \(f\) is open, each \(f(B_n)\) is an open neighborhood of \(y\). If \(V\) is any neighborhood of \(y\), then \(f^{-1}(V)\) is a neighborhood of \(x\), so some \(B_n\subset f^{-1}(V)\). Hence \(f(B_n)\subset V\). Thus \(Y\) is first countable.

Suppose \(X\) is second countable with basis \(\mathcal B=\{B_n:n\ge1\}\). Then \(\{f(B_n):n\ge1\}\) is a countable collection of open sets. It is a basis for \(Y\): if \(y\in V\) with \(V\) open, choose \(x\in f^{-1}(y)\). Since \(f^{-1}(V)\) is open, some basis element \(B_n\) satisfies
\[
x\in B_n\subset f^{-1}(V).
\]
Then
\[
y\in f(B_n)\subset V.
\]
So \(Y\) is second countable.
:::
