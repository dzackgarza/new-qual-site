---
schema: qual/card@1
id: P-CAFA20C
kind: problem
title: "Convergence of the series of derivatives of an entire function"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f: \mathbb{C} \to \mathbb{C}$ be an entire function.
Show that the series $$\sum_{n=0}^{\infty} \frac{f^{(n)}(z)}{n!}$$ converges uniformly on compact subsets of $\mathbb{C}$.
:::

::: {.solution}

::: pf

::: pf-step

Pointwise convergence to $f(z + 1)$:

::: pf-proof

::: pf-step

For any $z \in \mathbb{C}$, the Taylor series of the entire function $f$ centered at $z$ is:
\[
f(z + w) = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!} w^n.
\]
Because $f$ is entire, the radius of convergence of this series is $R = \infty$.

::: pf-proof

Taylor theorem for entire functions.

:::

:::

::: pf-step

Setting $w = 1$, the series converges pointwise to $f(z + 1)$ for every $z \in \mathbb{C}$:
\[
\sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!} = f(z + 1).
\]

::: pf-proof

evaluating the power series at $w = 1$.

:::

:::

:::

:::

::: {.pf-step #s2}

Cauchy estimates on compact sets:

::: pf-proof

::: pf-step

Let $K \subset \mathbb{C}$ be a compact subset.
Since $K$ is bounded, there exists $R > 0$ such that $|z| \le R$ for all $z \in K$.

::: pf-proof

compactness implies boundedness.

:::

:::

::: pf-step

Choose a radius $r > 1$ (e.g. $r = 2$).
For any $z \in K$, the circle $C_z = \{\zeta \in \mathbb{C} \mid |\zeta - z| = r\}$ is contained in the closed disk $\overline{B(0, R + r)}$.

::: pf-proof

triangle inequality $|\zeta| \le |z| + |\zeta - z| \le R + r$.

:::

:::

::: pf-step

Since $f$ is continuous and $\overline{B(0, R + r)}$ is compact, the supremum:
\[
M = \sup_{|\zeta| \le R + r} |f(\zeta)| < \infty.
\]

::: pf-proof

Extreme Value Theorem for continuous functions on compact sets.

:::

:::

::: pf-step

By Cauchy's Integral Formula for derivatives applied to the contour $C_z$:
\[
\frac{f^{(n)}(z)}{n!} = \frac{1}{2\pi i} \int_{C_z} \frac{f(\zeta)}{(\zeta - z)^{n+1}} \, d\zeta.
\]
Thus for all $z \in K$:
\[
\left| \frac{f^{(n)}(z)}{n!} \right| \le \frac{1}{2\pi} \frac{M}{r^{n+1}} (2\pi r) = \frac{M}{r^n}.
\]

::: pf-proof

ML inequality for contour integrals.

:::

:::

:::

:::

::: {.pf-step #s3}

Weierstrass $M$-test:

::: pf-proof

::: pf-step

Since $r > 1$, the geometric series $\sum_{n=0}^\infty \frac{M}{r^n} = \frac{M}{1 - 1/r}$ converges.

::: pf-proof

convergence of geometric series with common ratio $\frac{1}{r} < 1$.

:::

:::

::: pf-step

By the Weierstrass $M$-test, the series $\sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}$ converges uniformly on $K$.
Since $K$ was arbitrary, the series converges uniformly on all compact subsets of $\mathbb{C}$.

::: pf-proof

Weierstrass $M$-test.

:::

:::

:::

:::

::: pf-step

Conclusion:
$\sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}$ converges uniformly on compact subsets of $\mathbb{C}$ (to $f(z + 1)$). Q.E.D.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
