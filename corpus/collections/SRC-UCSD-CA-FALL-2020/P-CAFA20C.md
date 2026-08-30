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

::: problem
Let $f: \mathbb{C} \to \mathbb{C}$ be an entire function.
Show that the series $$\sum_{n=0}^{\infty} \frac{f^{(n)}(z)}{n!}$$ converges uniformly on compact subsets of $\mathbb{C}$.
:::

::: {.solution}
<1>1. Pointwise convergence to $f(z + 1)$:
<2>1. For any $z \in \mathbb{C}$, the Taylor series of the entire function $f$ centered at $z$ is:
\[
f(z + w) = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!} w^n.
\]
Because $f$ is entire, the radius of convergence of this series is $R = \infty$.
Proof: Taylor theorem for entire functions.
<2>2. Setting $w = 1$, the series converges pointwise to $f(z + 1)$ for every $z \in \mathbb{C}$:
\[
\sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!} = f(z + 1).
\]
Proof: evaluating the power series at $w = 1$.

<1>2. Cauchy estimates on compact sets:
<2>1. Let $K \subset \mathbb{C}$ be a compact subset.
Since $K$ is bounded, there exists $R > 0$ such that $|z| \le R$ for all $z \in K$.
Proof: compactness implies boundedness.
<2>2. Choose a radius $r > 1$ (e.g. $r = 2$).
For any $z \in K$, the circle $C_z = \{\zeta \in \mathbb{C} \mid |\zeta - z| = r\}$ is contained in the closed disk $\overline{B(0, R + r)}$.
Proof: triangle inequality $|\zeta| \le |z| + |\zeta - z| \le R + r$.
<2>3. Since $f$ is continuous and $\overline{B(0, R + r)}$ is compact, the supremum:
\[
M = \sup_{|\zeta| \le R + r} |f(\zeta)| < \infty.
\]
Proof: Extreme Value Theorem for continuous functions on compact sets.
<2>4. By Cauchy's Integral Formula for derivatives applied to the contour $C_z$:
\[
\frac{f^{(n)}(z)}{n!} = \frac{1}{2\pi i} \int_{C_z} \frac{f(\zeta)}{(\zeta - z)^{n+1}} \, d\zeta.
\]
Thus for all $z \in K$:
\[
\left| \frac{f^{(n)}(z)}{n!} \right| \le \frac{1}{2\pi} \frac{M}{r^{n+1}} (2\pi r) = \frac{M}{r^n}.
\]
Proof: ML inequality for contour integrals.

<1>3. Weierstrass $M$-test:
<2>1. Since $r > 1$, the geometric series $\sum_{n=0}^\infty \frac{M}{r^n} = \frac{M}{1 - 1/r}$ converges.
Proof: convergence of geometric series with common ratio $\frac{1}{r} < 1$.
<2>2. By the Weierstrass $M$-test, the series $\sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}$ converges uniformly on $K$.
Since $K$ was arbitrary, the series converges uniformly on all compact subsets of $\mathbb{C}$.
Proof: Weierstrass $M$-test.

<1>4. Conclusion:
$\sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}$ converges uniformly on compact subsets of $\mathbb{C}$ (to $f(z + 1)$). Q.E.D.
Proof: <1>2 and <1>3.
:::
