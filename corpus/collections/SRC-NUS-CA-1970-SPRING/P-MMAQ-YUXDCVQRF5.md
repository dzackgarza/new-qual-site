---
schema: qual/card@1
id: P-MMAQ-YUXDCVQRF5
kind: problem
title: $\int_0^{\pi/2}\frac{1}{3+\sin^2 x}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Integrals
  - Residues
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Evaluate the following by the method of residues: $\int_0^{\pi /2} \frac{1}{3+\sin^2x}dx$
:::

::: {.solution}
Let $I = \int_0^{\pi/2} \frac{1}{3 + \sin^2 x} \, dx$.

* * *

### Step 1: Symmetry and double-angle reduction

::: pf

::: pf-step

**Express the integral over $[0, 2\pi]$ in terms of $\cos(2x)$.**

::: pf-proof

::: pf-step

Use the half-angle identity $\sin^2 x = \frac{1 - \cos(2x)}{2}$.

::: pf-proof

Standard trigonometric identity.

:::

:::

::: pf-step

The denominator becomes: $$3 + \sin^2 x = 3 + \frac{1 - \cos(2x)}{2} = \frac{7 - \cos(2x)}{2}.$$

::: pf-proof

Algebraic simplification.

:::

:::

::: pf-step

Thus $I = \int_0^{\pi/2} \frac{2}{7 - \cos(2x)} \, dx$.

::: pf-proof

Substitution into $I$.

:::

:::

::: pf-step

Substitute $\theta = 2x$, so $d\theta = 2\,dx$ and as $x$ ranges from $0$ to $\pi/2$, $\theta$ ranges from $0$ to $\pi$: $$I = \int_0^\pi \frac{d\theta}{7 - \cos\theta}.$$

::: pf-proof

Change of variable $\theta = 2x$.

:::

:::

::: pf-step

Since $\cos\theta$ is even and symmetric on $[0, 2\pi]$ ($\cos(2\pi - \theta) = \cos\theta$): $$I = \frac{1}{2} \int_0^{2\pi} \frac{d\theta}{7 - \cos\theta}.$$

::: pf-proof

Symmetry: $\int_0^{2\pi} g(\cos\theta)\,d\theta = 2 \int_0^\pi g(\cos\theta)\,d\theta$.

:::

:::

:::

:::

:::

* * *

### Step 2: A contour integral over the unit circle

::: pf

::: pf-step

**Substitute $z = e^{i\theta}$ on the unit circle $C = \{z \in \mathbb{C} : |z| = 1\}$.**

::: pf-proof

::: pf-step

For $z = e^{i\theta}$, $dz = i e^{i\theta} d\theta = i z d\theta \implies d\theta = \frac{dz}{i z}$.

::: pf-proof

Parametrization of unit circle.

:::

:::

::: pf-step

$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2} = \frac{z + z^{-1}}{2} = \frac{z^2 + 1}{2z}$.

::: pf-proof

Euler's formula.

:::

:::

::: pf-step

The integrand becomes: $$\frac{1}{7 - \cos\theta} = \frac{1}{7 - \frac{z^2+1}{2z}} = \frac{2z}{14z - (z^2+1)} = \frac{-2z}{z^2 - 14z + 1}.$$

::: pf-proof

Algebraic rearrangement.

:::

:::

::: {.pf-step #s2-4}

The integral becomes: $$I = \frac{1}{2} \oint_C \frac{-2z}{z^2 - 14z + 1} \cdot \frac{dz}{iz} = -\frac{1}{i} \oint_C \frac{dz}{z^2 - 14z + 1} = i \oint_C \frac{dz}{z^2 - 14z + 1}.$$

::: pf-proof

$-1/i = i$.

:::

:::

:::

:::

:::

* * *

### Step 3: Poles and the enclosed residue

::: pf

::: pf-step

**Find the roots of $z^2 - 14z + 1 = 0$.**

::: pf-proof

::: pf-step

By the quadratic formula: $$z = \frac{14 \pm \sqrt{196 - 4}}{2} = \frac{14 \pm \sqrt{192}}{2} = \frac{14 \pm 8\sqrt{3}}{2} = 7 \pm 4\sqrt{3}.$$

::: pf-proof

Solving quadratic equation.

:::

:::

::: pf-step

Let $z_1 = 7 - 4\sqrt{3}$ and $z_2 = 7 + 4\sqrt{3}$.

::: pf-proof

Denoting roots.

:::

:::

::: pf-step

Since $4\sqrt{3} = \sqrt{48} \approx 6.928$: $$|z_1| = 7 - 4\sqrt{3} \approx 0.0718 < 1, \qquad |z_2| = 7 + 4\sqrt{3} \approx 13.928 > 1.$$

::: pf-proof

Arithmetic estimation ($48 < 49$).

:::

:::

::: pf-step

Therefore, only $z_1 = 7 - 4\sqrt{3}$ lies inside the unit circle $|z| < 1$.

::: pf-proof

$z_1 \in \mathbb{D}$ and $z_2 \notin \mathbb{D}$.

:::

:::

:::

:::

::: pf-step

**Compute the residue at $z_1$.**

::: pf-proof

::: pf-step

Since $z_1$ is a simple pole of $f(z) = \frac{1}{z^2 - 14z + 1} = \frac{1}{(z - z_1)(z - z_2)}$: $$\text{Res}(f, z_1) = \lim_{z \to z_1} (z - z_1) f(z) = \frac{1}{z_1 - z_2} = \frac{1}{(7 - 4\sqrt{3}) - (7 + 4\sqrt{3})} = \frac{1}{-8\sqrt{3}} = -\frac{1}{8\sqrt{3}}.$$

::: pf-proof

Standard simple pole residue calculation.

:::

:::

:::

:::

:::

* * *

### Step 4: The value of $I$

::: pf

::: pf-step

**Evaluate the contour integral $I$.**

::: pf-proof

::: pf-step

By the Cauchy Residue Theorem: $$\oint_C \frac{dz}{z^2 - 14z + 1} = 2\pi i \, \text{Res}(f, z_1) = 2\pi i \left( -\frac{1}{8\sqrt{3}} \right) = -\frac{\pi i}{4\sqrt{3}}.$$

::: pf-proof

Application of the Residue Theorem to the single enclosed pole $z_1$.

:::

:::

::: pf-step

From step [](#s2-4){.pf-ref}, $I = i \oint_C \frac{dz}{z^2 - 14z + 1}$: $$I = i \left( -\frac{\pi i}{4\sqrt{3}} \right) = -i^2 \frac{\pi}{4\sqrt{3}} = \frac{\pi}{4\sqrt{3}} = \frac{\pi\sqrt{3}}{12}.$$

::: pf-proof

$-i^2 = 1$.

:::

:::

:::

:::

:::

:::
