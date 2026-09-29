---
schema: qual/card@1
id: P-S5FOO
kind: problem
title: $L^\infty$ and $L^1$ disc norms of holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Norms
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
$\displaystyle \|f\|_{(\infty, s)} = \text{sup}_{z \in D_s(z_0)}|f(z)|$ and $\displaystyle \|f\|_{(1, r)} = \int_{D_r(z_0)} |f(z)|dx dy$.
:::

::: {.solution}

::: pf

::: pf-step
Mean Value Property for holomorphic functions:

::: pf-proof

::: pf-step
Let $w \in D_s(z_0)$ and set $\rho = r - s > 0$.
For any $\zeta \in D_\rho(w)$, the triangle inequality gives:
\[
|\zeta - z_0| \le |\zeta - w| + |w - z_0| < \rho + s = (r - s) + s = r.
\]
Thus the disc $D_\rho(w)$ is entirely contained in $D_r(z_0)$.

:::

::: pf-step
By Cauchy's Integral Formula, for any radius $t \in (0, \rho)$:
\[
f(w) = \frac{1}{2\pi} \int_0^{2\pi} f(w + t e^{i\theta}) \, d\theta.
\]

:::

:::

:::

::: pf-step
Area mean value formula:

::: pf-proof

::: pf-step
Multiplying both sides of the circular mean value identity by $t$ and integrating from $t = 0$ to $t = \rho$:
\[
\int_0^\rho t f(w) \, dt = \frac{1}{2\pi} \int_0^\rho \int_0^{2\pi} f(w + t e^{i\theta}) t \, d\theta \, dt.
\]

:::

::: pf-step
Evaluating the left-hand side gives $\frac{\rho^2}{2} f(w)$, and changing to Cartesian coordinates on the right-hand side gives:
\[
\frac{\rho^2}{2} f(w) = \frac{1}{2\pi} \iint_{D_\rho(w)} f(z) \, dx \, dy \implies f(w) = \frac{1}{\pi \rho^2} \iint_{D_\rho(w)} f(z) \, dx \, dy.
\]

:::

:::

:::

::: pf-step
Norm estimate:

::: pf-proof

::: pf-step
Taking absolute values and using the sub-mean value property:
\[
|f(w)| \le \frac{1}{\pi \rho^2} \iint_{D_\rho(w)} |f(z)| \, dx \, dy.
\]

:::

::: pf-step
Since $D_\rho(w) \subseteq D_r(z_0)$ and the integrand is non-negative:
\[
\iint_{D_\rho(w)} |f(z)| \, dx \, dy \le \iint_{D_r(z_0)} |f(z)| \, dx \, dy = \|f\|_{(1, r)}.
\]

:::

::: pf-step
Substituting $\rho = r - s$:
\[
|f(w)| \le \frac{1}{\pi (r - s)^2} \|f\|_{(1, r)}.
\]
Taking the supremum over all $w \in D_s(z_0)$:
\[
\|f\|_{(\infty, s)} \le \frac{1}{\pi (r - s)^2} \|f\|_{(1, r)}.
\]

:::

:::

:::

::: pf-qed
Conclusion:
$\|f\|_{(\infty, s)} \le \frac{1}{\pi (r - s)^2} \|f\|_{(1, r)}$ for all $0 < s < r$.
:::

:::

:::
