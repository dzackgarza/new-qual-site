---
schema: qual/card@1
id: P-CAFA21A
kind: problem
title: "Residue computation of (1 - cos x)/x^2"
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
Compute the following integral via residues
$$
\int_0^\infty \frac{1 - \cos x}{x^2}\,dx.
$$
Please explain the necessary estimates.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Symmetry and contour setup:

::: pf-proof

::: pf-step

The integrand $\frac{1 - \cos x}{x^2}$ is an even, non-negative continuous function on $\mathbb{R}$ (with removable singularity at $x=0$, $\lim_{x\to 0} \frac{1-\cos x}{x^2} = \frac{1}{2}$).
Thus:
\[
\int_0^\infty \frac{1 - \cos x}{x^2} \, dx = \frac{1}{2} \int_{-\infty}^\infty \frac{1 - \cos x}{x^2} \, dx = \frac{1}{2} \operatorname{Re} \left( \int_{-\infty}^\infty \frac{1 - e^{ix}}{x^2} \, dx \right).
\]

::: pf-proof

symmetry and $\operatorname{Re}(1 - e^{ix}) = 1 - \cos x$.

:::

:::

::: pf-step

Let $f(z) = \frac{1 - e^{iz}}{z^2}$.
Consider the closed indented contour $\Gamma_{R, \epsilon}$ in the upper half-plane consisting of:
- $[-R, -\epsilon]$ along the real axis,
- $C_\epsilon$: clockwise semicircle centered at $0$ from $-\epsilon$ to $\epsilon$ of radius $\epsilon$,
- $[\epsilon, R]$ along the real axis,
- $C_R$: counterclockwise semicircle centered at $0$ in the upper half-plane of radius $R$.

::: pf-proof

standard indented contour.

:::

:::

::: pf-step

Since $f(z)$ is holomorphic on $\mathbb{C} \setminus \{0\}$, it has no poles inside the region bounded by $\Gamma_{R, \epsilon}$.
By Cauchy’s Integral Theorem:
\[
\oint_{\Gamma_{R, \epsilon}} f(z) \, dz = \int_{-R}^{-\epsilon} f(x) \, dx + \int_{C_\epsilon} f(z) \, dz + \int_\epsilon^R f(x) \, dx + \int_{C_R} f(z) \, dz = 0.
\]

::: pf-proof

Cauchy's Integral Theorem on simply connected domain.

:::

:::

:::

:::

::: {.pf-step #s2}

Contour estimates:

::: pf-proof

::: pf-step

**Large semicircle estimate on $C_R$:**
For $z = R e^{i\theta}$ with $\theta \in [0, \pi]$, we have $\operatorname{Im}(z) = R \sin \theta \ge 0$, so $|e^{iz}| = e^{-R \sin \theta} \le 1$.
Thus $|1 - e^{iz}| \le 1 + |e^{iz}| \le 2$.
The integral along $C_R$ is bounded by:
\[
\left| \int_{C_R} f(z) \, dz \right| \le \frac{2}{R^2} \cdot \pi R = \frac{2\pi}{R} \xrightarrow{R \to \infty} 0.
\]

::: pf-proof

ML-inequality.

:::

:::

::: pf-step

**Small indented semicircle limit on $C_\epsilon$:**
Expanding $e^{iz} = 1 + iz - \frac{z^2}{2} + O(z^3)$ near $z = 0$:
\[
f(z) = \frac{1 - (1 + iz + O(z^2))}{z^2} = -\frac{i}{z} + O(1).
\]
Thus $f(z)$ has a simple pole at $z = 0$ with residue $\operatorname{Res}(f, 0) = -i$.
Integrating along the clockwise semicircle $C_\epsilon$:
\[
\lim_{\epsilon \to 0} \int_{C_\epsilon} f(z) \, dz = -\pi i \operatorname{Res}(f, 0) = -\pi i (-i) = -\pi.
\]

::: pf-proof

Fractional Residue Lemma for simple poles.

:::

:::

:::

:::

::: {.pf-step #s3}

Evaluation of the integral:

::: pf-proof

::: {.pf-step #s3-1}

Taking $R \to \infty$ and $\epsilon \to 0^+$ in Cauchy’s Theorem:
\[
\int_{-\infty}^\infty \frac{1 - e^{ix}}{x^2} \, dx + (-\pi) + 0 = 0 \implies \int_{-\infty}^\infty \frac{1 - e^{ix}}{x^2} \, dx = \pi.
\]

::: pf-proof

taking limits of the contour components.

:::

:::

::: pf-step

Taking the real part yields:
\[
\int_0^\infty \frac{1 - \cos x}{x^2} \, dx = \frac{1}{2} \operatorname{Re}(\pi) = \frac{\pi}{2}.
\]

::: pf-proof

Step [](#s1){.pf-ref} (step [](#s3-1){.pf-ref}).

:::

:::

:::

:::

::: pf-step

Conclusion:
$\int_0^\infty \frac{1 - \cos x}{x^2} \, dx = \frac{\pi}{2}$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
