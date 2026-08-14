---
schema: qual/card@1
id: E-YW6CQ
kind: exercise
title: "Let $f$ and $g$ be non-zero analytic functions on a region $\\Omega$.\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - open-mapping-theorem
  - removable-singularities
  - maximum-modulus-principle
relations: []
review: draft
---

::: {.problem title="?"}
Let $f$ and $g$ be non-zero analytic functions on a region $\Omega$.
Assume $|f(z)| = |g(z)|$ for all $z$ in $\Omega$.
Show that $f(z) = e^{i \theta} g(z)$ in $\Omega$ for some $0 \leq \theta < 2 \pi$.
:::

::: {.solution}
Define $F(z) \da {f(z) \over g(z)}$.

::: {.claim}
$F$ is holomorphic on $\Omega$.
:::

::: {.proof title="of claim"}
Note that $g(a) = 0$ iff $f(a) = 0$, so $F$ has no poles.
If $F$ has a singularity at $z_0$, noting that $\abs{F(z_0)} = 1$, $F$ is bounded in a neighborhood of $z_0$ and thus the singularity must be removable.
By Riemann's removable singularity theorem, $F$ extends to a holomorphic function.
:::

Given this, note that $\abs{F(z)} = 1$ for all $z$, so $F(\Omega) \subseteq S^1$, which is codimension 1 in $\CC$ and not open.
By the open mapping theorem, $F$ must be constant, so $F(z) = \lambda$, and in particular since $\abs{F(z)} = 1$, $\lambda = e^{it}\in S^1$ for some $t$.
Then $f(z) = \lambda g(z)$.
:::
