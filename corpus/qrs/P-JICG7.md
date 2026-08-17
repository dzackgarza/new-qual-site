---
schema: qual/card@1
id: P-JICG7
kind: problem
title: An entire function with $f(z)/z^n\to 0$ at infinity is a polynomial of degree at most $n-1$
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - liouville-s-theorem
  - cauchy-estimates
relations: []
review: draft
solved: true
---

::: problem
Suppose $f$ is entire and suppose that for some integer $n\geq 1$,
\[
\lim_{z\to \infty} {f(z) \over z^n} = 0
.\]

Prove that $f$ is a polynomial of degree at most $n-1$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $f$ is entire and $\lim_{z\to\infty} \frac{f(z)}{z^n} = 0$ for some integer $n \geq 1$, prove $f$ is a polynomial of degree at most $n-1$.

<1>1. For every $\varepsilon > 0$ there is $R_\varepsilon$ such that $\abs{f(z)} \leq \varepsilon \abs{z}^n$ for all $\abs{z} \geq R_\varepsilon$.
    Proof: This is the definition of $f(z)/z^n \to 0$ as $z \to \infty$.

<1>2. For each $k \geq n$, the Taylor coefficient $\frac{f^{(k)}(0)}{k!} = 0$.
    Proof: By the Cauchy estimates applied on $\abs{z} = R$ for $R \geq R_\varepsilon$, $\abs{f^{(k)}(0)} \leq \frac{k!}{R^k} \max_{\abs{z} = R}\abs{f(z)} \leq k!\, \varepsilon R^{n-k}$ using <1>1. Since $k \geq n$, letting $R \to \infty$ gives $\abs{f^{(k)}(0)} \leq 0$ (as $R^{n-k} \to 0$), so $f^{(k)}(0) = 0$. (More precisely, fix $\varepsilon$ and take the limit $R\to\infty$: $\abs{f^{(k)}(0)} \leq \liminf k!\varepsilon R^{n-k} = 0$.)

<1>3. $f(z) = \sum_{k=0}^{n-1} \frac{f^{(k)}(0)}{k!} z^k$, a polynomial of degree $\leq n-1$.
    Proof: The Taylor series of the entire function $f$ about $0$ converges to $f$ everywhere; by <1>2 all terms with $k \geq n$ vanish.

<1>4. Q.E.D.
    Proof: <1>3 proves the claim.

:::
