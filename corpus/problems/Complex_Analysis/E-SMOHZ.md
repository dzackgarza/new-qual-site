---
schema: qual/card@1
id: E-SMOHZ
kind: problem
title: Limit point of zeros is an essential singularity
classification:
  areas:
  - complex-analysis
  topics:
  - Essential Singularities
  - Identity Theorem
  - Zeros
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Suppose $f\not\equiv 0$ is holomorphic on $\Omega\smts{z_0}$ with a sequence of zeros $z_k$ limiting to $z_0$.
Show that $z_0$ is an essential singularity of $f$.
:::

::: {.solution}
It can not be a pole: otherwise $\abs{f(z)}\to \infty$ as $z\to z_0$, but $f(z) = 0$ infinitely often in every neighborhood of $z_0$ since the $z_k$ accumulate on it.
It can not be removable: otherwise $f$ extends holomorphically over $z_0$, and continuity forces $f(z_k) \to 0$ as $z_k\to z_0$.
But then $f = 0$ on a set with an accumulation point, making $f \equiv 0$ by the identity principle.
:::
