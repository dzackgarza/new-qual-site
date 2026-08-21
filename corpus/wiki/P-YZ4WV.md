---
schema: qual/card@1
id: P-YZ4WV
kind: problem
title: An isolated singularity at $0$ is essential if a nonconstant analytic $f$ on
  $|z|>0$ has zeros accumulating at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Essential Singularities
  - Singularities
  - Identity Theorem
  - Zeros
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f(z)$ be a non-constant analytic function in $|z|>0$ such that $f(z_n) = 0$ for infinite many points $z_n$ with $\lim_{n \rightarrow \infty} z_n =0$.

Show that $z=0$ is an essential singularity for $f(z)$.

> Hint: an example of such a function is $f(z) = \sin (1/z)$.
:::

::: {.solution}
Note that $z=0$ can not be a removable singularity, since then $f$ would extend to a holomorphic function over $z=0$, and by continuity $0 = \lim f(z_n) = f(\lim z_n) = f(0)$.
By the identity principle, this would force $f\equiv 0$, contradicting that $f$ is nonconstant.

It can not be a pole, because then $f(z_n)\to \infty$, but $\abs{f(z_n)} = 0 < \eps$ for any $\eps$ infinitely many times.
:::
