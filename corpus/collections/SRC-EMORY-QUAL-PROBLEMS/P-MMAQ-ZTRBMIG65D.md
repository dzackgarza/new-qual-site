---
schema: qual/card@1
id: P-MMAQ-ZTRBMIG65D
kind: problem
title: Cauchy integral formula for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (2) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMCA2, whose solution repeats this small-circle argument."
---

::: {.problem}
State and prove the Cauchy integral formula for holomorphic functions.
:::

::: {.solution}
### Statement of the Cauchy Integral Formula

**Theorem:** Let $\Omega \subseteq \mathbb{C}$ be an open domain, and let $f: \Omega \to \mathbb{C}$ be a holomorphic function.
Let $\gamma$ be a positively oriented, simple closed rectifiable curve in $\Omega$ whose interior $\text{Int}(\gamma)$ is contained in $\Omega$.
Then for every point $z_0 \in \text{Int}(\gamma)$: $$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz.$$

* * *

### Proof

::: pf

::: pf-step

**Isolate the singularity at $z_0$ using a small circle $C_\varepsilon$.**

::: pf-proof

::: pf-step

Since $z_0 \in \text{Int}(\gamma)$ and $\text{Int}(\gamma)$ is open, there exists $\varepsilon_0 > 0$ such that the closed disk $\overline{D}(z_0, \varepsilon_0) \subset \text{Int}(\gamma)$.

::: pf-proof

$\text{Int}(\gamma)$ is an open neighborhood of $z_0$.

:::

:::

::: pf-step

For any $\varepsilon \in (0, \varepsilon_0)$, let $C_\varepsilon$ denote the circle $\{z \in \mathbb{C} : |z - z_0| = \varepsilon\}$, oriented counterclockwise.

::: pf-proof

This is a definition.

:::

:::

::: pf-step

The function $g(z) \coloneqq \frac{f(z)}{z - z_0}$ is holomorphic in the region $\Omega' = \text{Int}(\gamma) \setminus \overline{D}(z_0, \varepsilon)$.

::: pf-proof

Quotient of holomorphic functions with non-vanishing denominator on $\Omega'$.

:::

:::

::: {.pf-step #s1-4}

By Cauchy's Integral Theorem for multiply connected domains: $$\oint_\gamma \frac{f(z)}{z - z_0} \, dz = \oint_{C_\varepsilon} \frac{f(z)}{z - z_0} \, dz.$$

::: pf-proof

The boundary of $\Omega'$ is $\gamma - C_\varepsilon$, and $\oint_{\partial \Omega'} g(z)\,dz = 0$.

:::

:::

:::

:::

::: pf-step

**Evaluate the constant-numerator integral on $C_\varepsilon$.**

::: pf-proof

::: pf-step

Parametrize $C_\varepsilon$ by $z(\theta) = z_0 + \varepsilon e^{i\theta}$ for $\theta \in [0, 2\pi]$, so $dz = i \varepsilon e^{i\theta} d\theta$.

::: pf-proof

Definition of circular parametrization.

:::

:::

::: pf-step

The integral of $\frac{1}{z - z_0}$ evaluates to: $$\oint_{C_\varepsilon} \frac{dz}{z - z_0} = \int_0^{2\pi} \frac{i \varepsilon e^{i\theta}}{\varepsilon e^{i\theta}} \, d\theta = i \int_0^{2\pi} d\theta = 2\pi i.$$

::: pf-proof

Direct cancellation of $\varepsilon e^{i\theta}$.

:::

:::

::: {.pf-step #s2-3}

Multiplying by the constant $f(z_0)$: $$\oint_{C_\varepsilon} \frac{f(z_0)}{z - z_0} \, dz = f(z_0) \oint_{C_\varepsilon} \frac{dz}{z - z_0} = 2\pi i f(z_0).$$

::: pf-proof

Linearity of integration.

:::

:::

:::

:::

::: pf-step

**Split the integral into the value at $z_0$ and an error term.**

::: pf-proof

::: {.pf-step #s3-1}

Subtracting the identity from step [](#s2-3){.pf-ref}: $$\oint_\gamma \frac{f(z)}{z - z_0} \, dz - 2\pi i f(z_0) = \oint_{C_\varepsilon} \frac{f(z) - f(z_0)}{z - z_0} \, dz.$$

::: pf-proof

Follows from steps [](#s1-4){.pf-ref} and [](#s2-3){.pf-ref}.

:::

:::

:::

:::

::: pf-step

**Show that the error term vanishes as $\varepsilon \to 0^+$.**

::: pf-proof

::: pf-step

Since $f$ is holomorphic at $z_0$, $f$ is continuous at $z_0$: for any $\delta > 0$, there exists $\varepsilon > 0$ such that $|z - z_0| = \varepsilon \implies |f(z) - f(z_0)| \leq \delta$.

::: pf-proof

Continuity of $f$ at $z_0$.

:::

:::

::: pf-step

On $C_\varepsilon$, the integrand is bounded by: $$\left| \frac{f(z) - f(z_0)}{z - z_0} \right| = \frac{|f(z) - f(z_0)|}{\varepsilon} \leq \frac{\delta}{\varepsilon}.$$

::: pf-proof

$|z - z_0| = \varepsilon$.

:::

:::

::: pf-step

The length of $C_\varepsilon$ is $2\pi \varepsilon$.

::: pf-proof

Circumference of circle of radius $\varepsilon$.

:::

:::

::: pf-step

By the $ML$-inequality: $$\left| \oint_{C_\varepsilon} \frac{f(z) - f(z_0)}{z - z_0} \, dz \right| \leq \frac{\delta}{\varepsilon} \cdot (2\pi \varepsilon) = 2\pi \delta.$$

::: pf-proof

$ML$-inequality for contour integrals.

:::

:::

::: {.pf-step #s4-5}

Since the LHS of step [](#s3-1){.pf-ref} is independent of $\varepsilon$, and $\delta > 0$ can be made arbitrarily small by choosing $\varepsilon$ small, the error integral must be identically 0: $$\oint_\gamma \frac{f(z)}{z - z_0} \, dz - 2\pi i f(z_0) = 0.$$

::: pf-proof

A non-negative quantity bounded by $2\pi\delta$ for all $\delta > 0$ is 0.

:::

:::

:::

:::

::: pf-step

**Conclusion.**

::: pf-proof

::: pf-step

Dividing by $2\pi i$ gives: $$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz.$$

::: pf-proof

Rearrangement of step [](#s4-5){.pf-ref}.

:::

:::

:::

:::

:::

:::
