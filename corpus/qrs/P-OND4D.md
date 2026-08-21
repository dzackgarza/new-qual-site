---
schema: qual/card@1
id: P-OND4D
kind: problem
title: Analyticity of $\int_\gamma\frac{g(w)}{w-z}\,dw$ off a smooth curve $\gamma$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Contour Integration
  - Cauchy Integral Formula
relations: []
review: draft
solved: true
---

::: problem
Let $\gamma$ be a smooth curve joining two distinct points $a, b\in \CC$.

Prove that the function
\[
f(z) \definedas \int_\gamma {g(w) \over w-z} \,dw
\]
is analytic in $\CC\setminus\gamma$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For a smooth curve $\gamma$ joining distinct points $a, b$ and continuous $g$ on $\gamma$, prove $f(z) = \int_\gamma \frac{g(w)}{w-z}\, dw$ is analytic on $\CC \setminus \gamma$.

<1>1. Fix $z_0 \notin \gamma$; let $d = \operatorname{dist}(z_0, \gamma) > 0$ and $r = d/2$.
Proof: $\gamma$ is compact and $z_0$ is not on it, so the distance $d$ between them is strictly positive.

<1>2. For $\abs{z - z_0} < r$ and $w \in \gamma$, the geometric series $\frac{1}{w - z} = \sum_{n=0}^\infty \frac{(z - z_0)^n}{(w - z_0)^{n+1}}$ converges uniformly in $w$.
Proof: $\abs{w - z_0} \geq d = 2r$ while $\abs{z - z_0} < r$, so the ratio $\abs{\frac{z - z_0}{w - z_0}} \leq \frac{r}{2r} = \frac12 < 1$ uniformly, and the geometric series converges uniformly on the compact set $\gamma$.

<1>3. $f(z) = \sum_{n=0}^\infty (z - z_0)^n \int_\gamma \frac{g(w)}{(w - z_0)^{n+1}}\, dw$ for $\abs{z - z_0} < r$.
Proof: Substitute the uniformly convergent expansion of <1>2 into the definition of $f$ and interchange sum and integral (justified by uniform convergence on $\gamma$; $g$ is continuous, hence bounded on $\gamma$).

<1>4. $f$ is analytic at $z_0$.
Proof: <1>3 represents $f$ near $z_0$ as a convergent power series in $z - z_0$, which is analytic in its disk of convergence; hence $f$ is analytic at $z_0$.
Since $z_0 \notin \gamma$ was arbitrary, $f$ is analytic on $\CC \setminus \gamma$.

<1>5. Q.E.D. Proof: <1>4 proves the claim.
:::
