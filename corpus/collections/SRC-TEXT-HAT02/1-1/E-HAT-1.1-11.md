---
schema: qual/card@1
id: E-HAT-1.1-11
kind: problem
title: Inclusion of path-component induces isomorphism on $\pi_1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Path Components
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
If $X_0$ is the path-component of a space $X$ containing the basepoint $x_0$, show that the inclusion $i: X_0 \hookrightarrow X$ induces an isomorphism $i_*: \pi_1(X_0, x_0) \to \pi_1(X, x_0)$.
:::

::: {.solution}

::: pf

::: pf-step
Every loop in $X$ based at $x_0$ has image in $X_0$.

::: pf-proof
For any point $\gamma(t)$ on such a loop, the restriction of $\gamma$ to $[0,t]$ is a path from $x_0$ to $\gamma(t)$. Thus $\gamma(t)$ lies in the path component $X_0$. Every class in $\pi_1(X,x_0)$ therefore has a representative in $X_0$, so $i_*$ is surjective.
:::

:::

::: pf-step
Any two loops in $X_0$ based at $x_0$ that are homotopic in $X$ are homotopic in $X_0$.

::: pf-proof
Let $H:I^2\to X$ be a homotopy relative to the basepoint between the loops. For any $(s,t)\in I^2$, a path in $I^2$ from $(0,0)$ to $(s,t)$ maps under $H$ to a path from $x_0$ to $H(s,t)$. Hence $H(I^2)\subseteq X_0$, and $H$ is a homotopy in $X_0$. Thus $i_*$ is injective.
:::

:::

::: pf-step
The inclusion induces an isomorphism $i_*:\pi_1(X_0,x_0)\to\pi_1(X,x_0)$.

::: pf-proof
The first two steps show that the induced homomorphism is surjective and injective.
:::

:::

:::

:::
