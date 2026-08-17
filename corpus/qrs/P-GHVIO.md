---
schema: qual/card@1
id: P-GHVIO
kind: problem
title: An entire function with $|f(z)|\le|z|^{1/2}$ for $|z|>10$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - liouville-s-theorem
  - cauchy-estimates
relations: []
review: draft
solved: true
---

::: problem
Suppose $f: \CC\to \CC$ is entire and
\[
\abs{f(z)} \leq \abs{z}^{1\over 2} \quad\text{ when } \abs{z} > 10
.\]

Prove that $f$ is constant.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Suppose $f: \CC \to \CC$ is entire and $|f(z)| \le |z|^{1/2}$ when $|z| > 10$. Prove that $f$ is constant.

<1>1. For every $R > 10$, $M(R) := \max_{|z| = R}|f(z)| \le R^{1/2}$.
    Proof: the maximum modulus principle and the given bound on $|z| > 10$: the maximum on $|z| = R$ is attained on the circle, where the hypothesis applies.

<1>2. For every $n \ge 1$, $f^{(n)}(0) = 0$.
    Proof: Cauchy's estimate on $|z| = R$ gives $|f^{(n)}(0)| \le \frac{n!\, M(R)}{R^n} \le \frac{n!\, R^{1/2}}{R^n} = \frac{n!}{R^{n - 1/2}} \to 0$ as $R \to \infty$ (since $n - \tfrac12 \ge \tfrac12 > 0$); letting $R \to \infty$, $f^{(n)}(0) = 0$.

<1>3. $f$ is constant.
    Proof: $f$ is entire, so its Taylor series at $0$ converges on all of $\CC$; by <1>2 all coefficients of order $\ge 1$ vanish, so $f \equiv f(0)$.

<1>4. Q.E.D.
    Proof: <1>1–<1>3 prove the claim.
:::
