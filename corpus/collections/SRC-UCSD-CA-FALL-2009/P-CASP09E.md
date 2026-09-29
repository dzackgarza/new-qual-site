---
schema: qual/card@1
id: P-CASP09E
kind: problem
title: "Uniform limit of analytic functions is analytic and derivatives converge on compacts"
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
Suppose $\{f_n(z)\}_{n \geq 1}$ is a sequence of analytic functions on a region $A$ which converges uniformly on $A$ to a function $f(z)$.
Show that $f(z)$ is analytic on $A$ and that the sequence of derivatives $\{f_n'(z)\}_{n \geq 1}$ converges uniformly to $f'(z)$ on compact subsets of $A$.
:::

::: {.solution}

::: pf

::: pf-step
$f$ is continuous on $A$:

::: pf-proof

::: pf-step
Each $f_n$ is analytic on $A$, hence continuous on $A$.

::: pf-proof
differentiable functions are continuous.
:::

:::

::: pf-step
$f_n \to f$ uniformly on $A$.

::: pf-proof
hypothesis.
:::

:::

::: pf-step
The uniform limit of continuous functions is continuous, so $f$ is continuous on $A$.

::: pf-proof
uniform limit theorem for continuous functions.
:::

:::

:::

:::

::: {.pf-step #s2}
$f$ is analytic on $A$ by Morera’s Theorem:

::: pf-proof

::: pf-step
Let $T \subset A$ be any closed triangle whose interior is contained in $A$.

::: pf-proof
setup for Morera's Theorem.
:::

:::

::: pf-step
For each $n \ge 1$, by Cauchy’s Integral Theorem for analytic functions on simply connected domains:
\[
\oint_{\partial T} f_n(z)\,dz = 0.
\]

::: pf-proof
Cauchy–Goursat Theorem.
:::

:::

::: pf-step
Since $\partial T$ is compact and $f_n \to f$ uniformly on $A$, $f_n \to f$ uniformly on $\partial T$.

::: pf-proof
restriction of uniform convergence to a compact subset.
:::

:::

::: pf-step
Integration and uniform limits commute:
\[
\oint_{\partial T} f(z)\,dz = \lim_{n\to\infty} \oint_{\partial T} f_n(z)\,dz = \lim_{n\to\infty} 0 = 0.
\]

::: pf-proof
$|\oint_{\partial T} (f_n - f)\,dz| \le \sup_{z\in\partial T}|f_n(z) - f(z)| \cdot \operatorname{length}(\partial T) \to 0$.
:::

:::

::: pf-step
By Morera’s Theorem, the continuous function $f$ is analytic on $A$.

::: pf-proof
Morera's Theorem.
:::

:::

:::

:::

::: {.pf-step #s3}
$f_n' \to f'$ uniformly on compact subsets $K \subset A$:

::: pf-proof

::: pf-step
Let $K \subset A$ be an arbitrary compact subset.

::: pf-proof
setup.
:::

:::

::: pf-step
Since $A$ is open, $r_0 = \operatorname{dist}(K, \mathbb{C} \setminus A) > 0$.
Choose $r = r_0 / 2 > 0$.

::: pf-proof
distance between a compact set and a disjoint closed set in a metric space is positive.
:::

:::

::: pf-step
For any $z \in K$, the circle $\gamma_z = \{\zeta \in \mathbb{C} : |\zeta - z| = r\}$ and its interior disk $D(z, r)$ are completely contained in $A$.

::: pf-proof
definition of $r = r_0 / 2 < r_0$.
:::

:::

::: pf-step
By Cauchy’s Integral Formula for the derivative applied to $f_n - f$:
\[
f_n'(z) - f'(z) = \frac{1}{2\pi i} \oint_{\gamma_z} \frac{f_n(\zeta) - f(\zeta)}{(\zeta - z)^2}\,d\zeta.
\]

::: pf-proof
Cauchy's differentiation formula for analytic functions.
:::

:::

::: pf-step
Let $\varepsilon_n = \sup_{\zeta \in A} |f_n(\zeta) - f(\zeta)|$.
By uniform convergence of $f_n \to f$ on $A$, $\lim_{n\to\infty} \varepsilon_n = 0$.

::: pf-proof
definition of uniform convergence.
:::

:::

::: pf-step
For all $\zeta \in \gamma_z$, $|\zeta - z| = r$.
Applying the $ML$-inequality:
\[
|f_n'(z) - f'(z)| \le \frac{1}{2\pi} \frac{\varepsilon_n}{r^2} (2\pi r) = \frac{\varepsilon_n}{r}.
\]

::: pf-proof
$ML$-inequality with length $(\gamma_z) = 2\pi r$.
:::

:::

::: {.pf-step #s3-7}
Since the bound $\varepsilon_n / r$ is independent of $z \in K$:
\[
\sup_{z \in K} |f_n'(z) - f'(z)| \le \frac{\varepsilon_n}{r} \xrightarrow[n\to\infty]{} 0.
\]

::: pf-proof
$\lim \varepsilon_n = 0$ and $r > 0$ is fixed.
:::

:::

::: pf-step
Thus $\{f_n'\}$ converges uniformly to $f'$ on $K$.

::: pf-proof
step [](#s3-7){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Conclusion: $f$ is analytic on $A$, and $f_n' \to f'$ uniformly on compact subsets of $A$.

::: pf-proof
step [](#s2){.pf-ref} and step [](#s3){.pf-ref}.
:::

:::

:::
:::
