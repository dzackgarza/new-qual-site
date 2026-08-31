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

::: problem
Compute the following integral via residues
$$
\int_0^\infty \frac{1 - \cos x}{x^2}\,dx.
$$
Please explain the necessary estimates.
:::

::: {.solution}
<1>1. Symmetry and contour setup:
<2>1. The integrand $\frac{1 - \cos x}{x^2}$ is an even, non-negative continuous function on $\mathbb{R}$ (with removable singularity at $x=0$, $\lim_{x\to 0} \frac{1-\cos x}{x^2} = \frac{1}{2}$).
Thus:
\[
\int_0^\infty \frac{1 - \cos x}{x^2} \, dx = \frac{1}{2} \int_{-\infty}^\infty \frac{1 - \cos x}{x^2} \, dx = \frac{1}{2} \operatorname{Re} \left( \int_{-\infty}^\infty \frac{1 - e^{ix}}{x^2} \, dx \right).
\]
::: {.proof}
symmetry and $\operatorname{Re}(1 - e^{ix}) = 1 - \cos x$.
:::
<2>2. Let $f(z) = \frac{1 - e^{iz}}{z^2}$.
Consider the closed indented contour $\Gamma_{R, \epsilon}$ in the upper half-plane consisting of:
- $[-R, -\epsilon]$ along the real axis,
- $C_\epsilon$: clockwise semicircle centered at $0$ from $-\epsilon$ to $\epsilon$ of radius $\epsilon$,
- $[\epsilon, R]$ along the real axis,
- $C_R$: counterclockwise semicircle centered at $0$ in the upper half-plane of radius $R$.
::: {.proof}
standard indented contour.
:::
<2>3. Since $f(z)$ is holomorphic on $\mathbb{C} \setminus \{0\}$, it has no poles inside the region bounded by $\Gamma_{R, \epsilon}$.
By Cauchy’s Integral Theorem:
\[
\oint_{\Gamma_{R, \epsilon}} f(z) \, dz = \int_{-R}^{-\epsilon} f(x) \, dx + \int_{C_\epsilon} f(z) \, dz + \int_\epsilon^R f(x) \, dx + \int_{C_R} f(z) \, dz = 0.
\]
::: {.proof}
Cauchy's Integral Theorem on simply connected domain.
:::

<1>2. Contour estimates:
<2>1. **Large semicircle estimate on $C_R$:**
For $z = R e^{i\theta}$ with $\theta \in [0, \pi]$, we have $\operatorname{Im}(z) = R \sin \theta \ge 0$, so $|e^{iz}| = e^{-R \sin \theta} \le 1$.
Thus $|1 - e^{iz}| \le 1 + |e^{iz}| \le 2$.
The integral along $C_R$ is bounded by:
\[
\left| \int_{C_R} f(z) \, dz \right| \le \frac{2}{R^2} \cdot \pi R = \frac{2\pi}{R} \xrightarrow{R \to \infty} 0.
\]
::: {.proof}
ML-inequality.
:::
<2>2. **Small indented semicircle limit on $C_\epsilon$:**
Expanding $e^{iz} = 1 + iz - \frac{z^2}{2} + O(z^3)$ near $z = 0$:
\[
f(z) = \frac{1 - (1 + iz + O(z^2))}{z^2} = -\frac{i}{z} + O(1).
\]
Thus $f(z)$ has a simple pole at $z = 0$ with residue $\operatorname{Res}(f, 0) = -i$.
Integrating along the clockwise semicircle $C_\epsilon$:
\[
\lim_{\epsilon \to 0} \int_{C_\epsilon} f(z) \, dz = -\pi i \operatorname{Res}(f, 0) = -\pi i (-i) = -\pi.
\]
::: {.proof}
Fractional Residue Lemma for simple poles.
:::

<1>3. Evaluation of the integral:
<2>1. Taking $R \to \infty$ and $\epsilon \to 0^+$ in Cauchy’s Theorem:
\[
\int_{-\infty}^\infty \frac{1 - e^{ix}}{x^2} \, dx + (-\pi) + 0 = 0 \implies \int_{-\infty}^\infty \frac{1 - e^{ix}}{x^2} \, dx = \pi.
\]
::: {.proof}
taking limits of the contour components.
:::
<2>2. Taking the real part yields:
\[
\int_0^\infty \frac{1 - \cos x}{x^2} \, dx = \frac{1}{2} \operatorname{Re}(\pi) = \frac{\pi}{2}.
\]
::: {.proof}
<1>1 (<2>1).
:::

<1>4. Conclusion:
$\int_0^\infty \frac{1 - \cos x}{x^2} \, dx = \frac{\pi}{2}$. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
