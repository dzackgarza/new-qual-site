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
---

::: {.problem}
Let $f(z)$ be a non-constant analytic function in $|z|>0$ such that $f(z_n) = 0$ for infinite many points $z_n$ with $\lim_{n \rightarrow \infty} z_n =0$.

Show that $z=0$ is an essential singularity for $f(z)$.

> Hint: an example of such a function is $f(z) = \sin (1/z)$.
:::

::: {.solution}
The point $z=0$ is not a removable singularity: otherwise $f$ would extend to a holomorphic function on $\abs z<\infty$ with $f(0) = \lim f(z_n) = 0$, so the zeros $z_n$ would accumulate at the point $0$ of the domain, and the identity theorem would force $f\equiv 0$, contradicting that $f$ is nonconstant.

The point $z=0$ is not a pole: otherwise $\abs{f(z)}\to \infty$ as $z\to0$, whereas $f(z_n) = 0$ with $z_n\to0$.

Hence $z=0$ is an essential singularity.
:::
