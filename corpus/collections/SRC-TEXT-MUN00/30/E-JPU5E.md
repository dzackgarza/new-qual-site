---
schema: qual/card@1
id: E-JPU5E
kind: problem
title: Lindelofness and separability pass to continuous images
classification:
  areas:
  - topology
  topics:
  - Countability
  - Continuous Functions
relations: []
review: draft
---

::: {.exercise}

Let $f: X \to Y$ be continuous.
Show that if $X$ is Lindelöf, or if $X$ has a countable dense subset, then $f(X)$ satisfies the same condition.
:::

::: {.solution}
Write \(Z=f(X)\) with the subspace topology.

If \(X\) is Lindelöf and \(\{U_i\}_{i\in I}\) is an open cover of \(Z\), then \(\{f^{-1}(U_i)\}_{i\in I}\) is an open cover of \(X\). Choose a countable subcover \(f^{-1}(U_{i_1}),f^{-1}(U_{i_2}),\dots\). Surjectivity of \(f:X\to Z\) implies \(U_{i_1},U_{i_2},\dots\) cover \(Z\). Hence \(Z\) is Lindelöf.

If \(D\subset X\) is countable and dense, then \(f(D)\) is countable. It is dense in \(Z\): if \(W\subset Z\) is nonempty open, then \(f^{-1}(W)\) is nonempty open in \(X\), so it meets \(D\); hence \(W\) meets \(f(D)\). Thus \(Z\) is separable.
:::
