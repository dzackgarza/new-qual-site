---
schema: qual/card@1
id: FS-BM2PV
kind: strategy
title: How to commute a sum and an integral
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Convergence of Integrals
  - Series of Functions
relations: []
review: draft
---

::: {.strategy}
**Goal:** Given a sequence of measurable functions $f_n$ on a measure space $(X, \mu)$, justify the interchange
$$\sum_{n=1}^\infty \int_X f_n \, d\mu = \int_X \sum_{n=1}^\infty f_n \, d\mu.$$

**Method:** View the sum as an integral over the counting measure on $\mathbb{N}$ and apply Fubini–Tonelli.

<1>1. Encode the series as an integral over $\mathbb{N}$.
<2>1. Let $\nu$ be the counting measure on $\mathbb{N}$, so that $\int_{\mathbb{N}} g \, d\nu = \sum_{n=1}^\infty g(n)$ for every nonnegative (or $\nu$-integrable) function $g$.
<2>2. Define $F \colon X \times \mathbb{N} \to \mathbb{R}$ by $F(x, n) = f_n(x)$.
<2>3. Then the two sides of the desired identity are the two iterated integrals of $F$:
$$\sum_{n=1}^\infty \int_X f_n \, d\mu = \int_{\mathbb{N}} \int_X F(x, n) \, d\mu(x) \, d\nu(n), \qquad \int_X \sum_{n=1}^\infty f_n \, d\mu = \int_X \int_{\mathbb{N}} F(x, n) \, d\nu(n) \, d\mu(x).$$

<1>2. Verify the hypothesis of Tonelli's theorem.
<2>1. The hypothesis $\sum_{n=1}^\infty \int_X |f_n| \, d\mu < \infty$ states exactly that the iterated integral $\int_{\mathbb{N}} \int_X |F| \, d\mu \, d\nu$ is finite.
<2>2. Since $|F|$ is nonnegative and measurable on the product space $X \times \mathbb{N}$, Tonelli's theorem applies and gives
$$\int_{X \times \mathbb{N}} |F| \, d(\mu \times \nu) = \int_{\mathbb{N}} \int_X |F| \, d\mu \, d\nu < \infty.$$
<2>3. Hence $F \in L^1(X \times \mathbb{N}, \mu \times \nu)$.

<1>3. Apply Fubini's theorem.
<2>1. Because $F$ is integrable on the product space, Fubini's theorem permits the interchange of the two iterated integrals:
$$\int_{\mathbb{N}} \int_X F \, d\mu \, d\nu = \int_X \int_{\mathbb{N}} F \, d\nu \, d\mu.$$
<2>2. Substituting the definitions of $F$ and $\nu$ yields the desired identity
$$\sum_{n=1}^\infty \int_X f_n \, d\mu = \int_X \sum_{n=1}^\infty f_n \, d\mu.$$

**Remark.** The same argument applies verbatim to a doubly indexed family $\{f_{m,n}\}$: the hypothesis $\sum_{m,n} \int |f_{m,n}| < \infty$ justifies commuting the double sum with the integral.
:::
