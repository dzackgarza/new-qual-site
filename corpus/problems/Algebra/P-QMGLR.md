---
schema: qual/card@1
id: P-QMGLR
kind: problem
title: $\alpha\pm\beta$ and $\alpha\beta^{\pm 1}$ are algebraic over $F$ whenever
  $\alpha$ and $\beta$ are
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Let $\alpha,\beta$ be algebraic over a field $F$. Prove that
\[
\alpha\pm\beta,
\qquad
\alpha\beta
\]
are algebraic over $F$, and if $\beta\ne0$, then so is
\[
\alpha\beta^{-1}.
\]
:::

::: {.solution}
Since $\alpha$ and $\beta$ are algebraic over $F$, the extensions
\[
F(\alpha)/F,
\qquad
F(\beta)/F
\]
are finite. Therefore the compositum
\[
F(\alpha,\beta)
\]
is finite over $F$.

Every element of a finite field extension is algebraic over the base field. Now
\[
\alpha+\beta,
\quad
\alpha-\beta,
\quad
\alpha\beta
\]
all lie in $F(\alpha,\beta)$. If $\beta\ne0$, then $\beta^{-1}\in F(\beta)\subseteq F(\alpha,\beta)$, so
\[
\alpha\beta^{-1}\in F(\alpha,\beta)
\]
as well.

Hence all the displayed elements are algebraic over $F$.
:::
