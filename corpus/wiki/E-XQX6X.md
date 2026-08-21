---
schema: qual/card@1
id: E-XQX6X
kind: exercise
title: Liouville
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Schwarz Lemma
  - Entire Functions
relations: []
review: draft
solved: true
---

:::{.exercise title="Liouville"}
Use a version of the Schwarz lemma to prove Liouville's theorem.

:::

:::{.solution}
Suppose $f$ is entire and bounded, we'll show $f$ is constant.
If $f$ is bounded by $M$, then $f(\CC) \subseteq \DD_M(0)$.
Without loss of generality, replace $f$ with $g(z) \da f(z) - f(0)$, so $g(0) = 0$ and is still bounded by $M' \da M + \abs{f(0)}$ by the triangle inequality.
This is still finite since $0$ is not a singularity since $f$ is entire.

By the radius $R$ variant of the Schwarz lemma, for every $\DD_R(0)$,
\[
\abs{g(z)} \leq {M\over R}\abs{z} \qquad \text{for } z\in \DD_R(0)
.\]
Using that $g(0) = 0$,
\[
\abs{g(z) - g(0) \over z} \leq {M\over R}\convergesto{R\to\infty}0
,\]
where dividing by $z$ is not an issue since $z=0$ is a zero of $g$ of at least order one.
This forces $g(z) = g(0) = 0$ for all $z$, so $f(z) = f(z_0)$ is constant.
:::
