---
schema: qual/card@1
id: P-AKSSQ
kind: problem
title: A nowhere-vanishing holomorphic function of constant modulus on $\partial D$
  is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f$ be analytic on a bounded domain $D$, and assume also that $f$ that is continuous and nowhere zero on the closure $\bar{D}$.

Show that if $|f(z)|=M$ (a constant) for $z$ on the boundary of $D$, then $f(z)=e^{i \theta} M$ for $z$ in $D$, where $\theta$ is a real constant.
:::

::: {.solution}
By the maximum modulus principle, $\abs{f} \leq M$ in $\bar{D}$.
Since $f$ has no zeros in $\bar{D}$, $g\da 1/f$ is holomorphic on $D$ and continuous on $\bar{D}$.
So the maximum modulus principle applies to $g$, and $M\inv \geq \abs{g} = 1/\abs{f}$, so $\abs{f} \leq M$.
Combining these, $\abs{f(z)} = M$, so $f(z) = \lambda M$ where $\lambda$ is some constant with $\abs{\lambda}=1$.
This is on the unit circle, so $\lambda = e^{i\theta}$ for some fixed angle $\theta$.
:::
