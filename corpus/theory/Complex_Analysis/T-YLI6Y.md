---
schema: qual/card@1
id: T-YLI6Y
kind: theorem
title: Minimum modulus principle
slogan: 'A nonvanishing nonconstant holomorphic function cannot attain its minimum modulus in the interior.'
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be a connected open set and let $f$ be [[D-E7A5W|holomorphic]] and nonvanishing on $\Omega$.

(i) If $\abs{f}$ has a local minimum at some $z_0\in\Omega$, then $f$ is constant on $\Omega$.

(ii) If moreover $\Omega$ is bounded, $f$ extends continuously to $\overline{\Omega}$, and $f$ is nonconstant, then $\min_{\overline{\Omega}}\abs{f}$ is attained only at points of $\partial\Omega$.
:::

::: {.example}
The hypothesis that $f$ has no zeros is needed: $f(z) = z$ on $\DD$ has $\min_{\overline\DD}\abs f = 0$, attained only at the interior point $0$, while $\abs f = 1$ on $\bd\DD$.
:::

::: {.remark}
This is the maximum modulus principle [@SS03, Theorem 4.5 and Corollary 4.6 of Chapter 3 (p. 92)] applied to $1/f$, which is holomorphic because $f$ is nonvanishing.
:::
