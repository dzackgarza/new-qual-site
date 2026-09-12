---
schema: qual/card@1
id: E-DWC4M
kind: problem
title: The equalizer of two maps into a Hausdorff space is closed
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Continuous Functions
relations: []
review: draft
---

::: {.exercise}

Let $f, g: X \to Y$ be continuous; assume that $Y$ is Hausdorff.
Show that $\ts{x \mid f(x) = g(x)}$ is closed in $X$.
:::

::: {.solution}
Let
\[
E=\{x\in X:f(x)=g(x)\}.
\]
The map
\[
F:X\to Y\times Y,\qquad F(x)=(f(x),g(x))
\]
is continuous. Since \(Y\) is Hausdorff, its diagonal
\[
\Delta_Y=\{(y,y):y\in Y\}
\]
is closed in \(Y\times Y\). Hence
\[
E=F^{-1}(\Delta_Y)
\]
is closed in \(X\).
:::
