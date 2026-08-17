---
schema: qual/card@1
id: P-34ALC
kind: problem
title: Functions on the Riemann sphere with a simple pole at $2$ and a double pole at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - meromorphic-functions
  - poles
  - riemann-surfaces
relations: []
review: draft
solved: true
---

::: problem
Find all functions on the Riemann sphere that have a simple pole at $z=2$ and a double pole at $z=\infty$, but are analytic elsewhere.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Find all functions on the Riemann sphere $\widehat{\CC}$ that have a simple pole at $z = 2$ and a double pole at $z = \infty$, and are analytic elsewhere.

<1>1. A function meromorphic on the sphere with poles only at $2$ and $\infty$ is a rational function with those poles.
Proof: On the sphere, meromorphic functions are rational (a function holomorphic on the sphere minus finitely many points, with poles there, is a rational function by the theory of meromorphic functions on compact Riemann surfaces / the standard theorem that meromorphic functions on $\widehat\CC$ are rational).

<1>2. The pole at $z = 2$ is simple, so $f(z) = \frac{A}{z - 2} + g(z)$ where $g$ is holomorphic near $2$ (indeed $g$ has no pole at $2$). Proof: Laurent expansion at $z = 2$: principal part is $A/(z-2)$ with $A \neq 0$ (simple pole).

<1>3. The only other pole is a double pole at $\infty$; combined with rationality, $f(z) = \frac{A}{z-2} + Bz + C$.
Proof: A rational function with a simple pole at $2$ and a pole at $\infty$ only: the pole at $\infty$ being double means $f(z) = P(z) + \frac{A}{z-2}$ where $P$ is a polynomial.
Since the pole at $\infty$ is of order exactly 2, $P$ has degree exactly 2? No — a double pole at $\infty$ means $f(1/w)$, as a function of $w$, has a double pole at $w = 0$; with $f(z) = P(z) + A/(z-2)$, the growth at $\infty$ is governed by $\deg P$: $f(z) \sim \text{leading term of } P$.
Hence $\deg P = 2$.
Write $P(z) = bz^2 + cz + d$; subtracting constants doesn't change poles, so $f(z) = \frac{A}{z-2} + bz^2 + cz + d$ with $A \neq 0$, $b \neq 0$.

<1>4. Q.E.D. Proof: <1>3 gives the general form: $f(z) = \frac{A}{z-2} + bz^2 + cz + d$, $A \neq 0$, $b \neq 0$, with $c, d \in \CC$ arbitrary.
These are all the functions analytic except for a simple pole at $2$ and a double pole at $\infty$.
:::
