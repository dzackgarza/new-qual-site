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

::: problem
Suppose $\{f_n(z)\}_{n \geq 1}$ is a sequence of analytic functions on a region $A$ which converges uniformly on $A$ to a function $f(z)$.
Show that $f(z)$ is analytic on $A$ and that the sequence of derivatives $\{f_n'(z)\}_{n \geq 1}$ converges uniformly to $f'(z)$ on compact subsets of $A$.
:::

::: {.solution}
<1>1. $f$ is continuous on $A$: <2>1. Each $f_n$ is analytic on $A$, hence continuous on $A$.
Proof: differentiable functions are continuous.
<2>2. $f_n \to f$ uniformly on $A$.
Proof: hypothesis.
<2>3. The uniform limit of continuous functions is continuous, so $f$ is continuous on $A$.
Proof: uniform limit theorem for continuous functions.

<1>2. $f$ is analytic on $A$ by Morera’s Theorem: <2>1. Let $T \subset A$ be any closed triangle whose interior is contained in $A$.
Proof: setup for Morera's Theorem.
<2>2. For each $n \ge 1$, by Cauchy’s Integral Theorem for analytic functions on simply connected domains:
\[
\oint_{\partial T} f_n(z)\,dz = 0.
\]
Proof: Cauchy–Goursat Theorem.
<2>3. Since $\partial T$ is compact and $f_n \to f$ uniformly on $A$, $f_n \to f$ uniformly on $\partial T$.
Proof: restriction of uniform convergence to a compact subset.
<2>4. Integration and uniform limits commute:
\[
\oint_{\partial T} f(z)\,dz = \lim_{n\to\infty} \oint_{\partial T} f_n(z)\,dz = \lim_{n\to\infty} 0 = 0.
\]
Proof: $|\oint_{\partial T} (f_n - f)\,dz| \le \sup_{z\in\partial T}|f_n(z) - f(z)| \cdot \operatorname{length}(\partial T) \to 0$.
<2>5. By Morera’s Theorem, the continuous function $f$ is analytic on $A$.
Proof: Morera's Theorem.

<1>3. $f_n' \to f'$ uniformly on compact subsets $K \subset A$: <2>1. Let $K \subset A$ be an arbitrary compact subset.
Proof: setup.
<2>2. Since $A$ is open, $r_0 = \operatorname{dist}(K, \mathbb{C} \setminus A) > 0$.
Choose $r = r_0 / 2 > 0$.
Proof: distance between a compact set and a disjoint closed set in a metric space is positive.
<2>3. For any $z \in K$, the circle $\gamma_z = \{\zeta \in \mathbb{C} : |\zeta - z| = r\}$ and its interior disk $D(z, r)$ are completely contained in $A$.
Proof: definition of $r = r_0 / 2 < r_0$.
<2>4. By Cauchy’s Integral Formula for the derivative applied to $f_n - f$:
\[
f_n'(z) - f'(z) = \frac{1}{2\pi i} \oint_{\gamma_z} \frac{f_n(\zeta) - f(\zeta)}{(\zeta - z)^2}\,d\zeta.
\]
Proof: Cauchy's differentiation formula for analytic functions.
<2>5. Let $\varepsilon_n = \sup_{\zeta \in A} |f_n(\zeta) - f(\zeta)|$.
By uniform convergence of $f_n \to f$ on $A$, $\lim_{n\to\infty} \varepsilon_n = 0$.
Proof: definition of uniform convergence.
<2>6. For all $\zeta \in \gamma_z$, $|\zeta - z| = r$.
Applying the $ML$-inequality:
\[
|f_n'(z) - f'(z)| \le \frac{1}{2\pi} \frac{\varepsilon_n}{r^2} (2\pi r) = \frac{\varepsilon_n}{r}.
\]
Proof: $ML$-inequality with length $(\gamma_z) = 2\pi r$.
<2>7. Since the bound $\varepsilon_n / r$ is independent of $z \in K$:
\[
\sup_{z \in K} |f_n'(z) - f'(z)| \le \frac{\varepsilon_n}{r} \xrightarrow[n\to\infty]{} 0.
\]
Proof: $\lim \varepsilon_n = 0$ and $r > 0$ is fixed.
<2>8. Thus $\{f_n'\}$ converges uniformly to $f'$ on $K$.
Proof: <2>7.

<1>4. Conclusion: $f$ is analytic on $A$, and $f_n' \to f'$ uniformly on compact subsets of $A$.
Q.E.D. Proof: <1>2 and <1>3.
:::
