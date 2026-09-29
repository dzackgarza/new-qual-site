---
schema: qual/card@1
id: P-MMAQ-WPHHQBXBQ3
kind: problem
title: $\int_0^\infty\frac{x^2}{(x^2+1)(x^2+4)}\,dx$
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
Evaluate the improper integral

$\int_0^\infty \frac{x^2~dx}{(x^2+1)(x^2+4)}$
:::

::: {.solution}
Let $I = \int_0^\infty \frac{x^2}{(x^2+1)(x^2+4)} \, dx$.

* * *

### Step 1: Symmetry and the rational function $f$

::: pf

::: pf-step

**Symmetry over $\mathbb{R}$.**

::: pf-proof

::: pf-step

The integrand $g(x) = \frac{x^2}{(x^2+1)(x^2+4)}$ is an even function: $g(-x) = g(x)$ for all $x \in \mathbb{R}$.

::: pf-proof

$(-x)^2 = x^2$.

:::

:::

::: {.pf-step #s1-2}

Therefore, $I = \frac{1}{2} \int_{-\infty}^\infty \frac{x^2}{(x^2+1)(x^2+4)} \, dx$.

::: pf-proof

Splitting the integral over symmetric bounds.

:::

:::

::: pf-step

Define $f(z) = \frac{z^2}{(z^2+1)(z^2+4)} = \frac{z^2}{(z-i)(z+i)(z-2i)(z+2i)}$.

::: pf-proof

Factorization of quadratic polynomials over $\mathbb{C}$.

:::

:::

:::

:::

:::

* * *

### Step 2: Contour integration in the upper half-plane

::: pf

::: pf-step

**Set up the semicircular contour $\Gamma_R = [-R, R] \cup C_R$ where $C_R = \{R e^{i\theta} : \theta \in [0, \pi]\}$ with $R > 2$.**

::: pf-proof

::: pf-step

The singularities of $f(z)$ are simple poles at $z = \pm i$ and $z = \pm 2i$.

::: pf-proof

Zeros of $(z^2+1)(z^2+4)$.

:::

:::

::: pf-step

The poles enclosed inside $\Gamma_R$ in the upper half-plane $\mathbb{H}$ are $z_1 = i$ and $z_2 = 2i$.

::: pf-proof

$\text{Im}(i) = 1 > 0$ and $\text{Im}(2i) = 2 > 0$, while $\text{Im}(-i) < 0$ and $\text{Im}(-2i) < 0$.

:::

:::

::: {.pf-step #s2-3}

By the Cauchy Residue Theorem: $$\oint_{\Gamma_R} f(z) \, dz = \int_{-R}^R \frac{x^2}{(x^2+1)(x^2+4)} \, dx + \int_{C_R} f(z) \, dz = 2\pi i \Big( \text{Res}(f, i) + \text{Res}(f, 2i) \Big).$$

::: pf-proof

Application of the residue theorem to the enclosed simple poles.

:::

:::

:::

:::

:::

* * *

### Step 3: The residues

::: pf

::: pf-step

**Compute the residues at $z = i$ and $z = 2i$.**

::: pf-proof

::: pf-step

At the simple pole $z = i$: $$\text{Res}(f, i) = \lim_{z \to i} (z - i) f(z) = \lim_{z \to i} \frac{z^2}{(z+i)(z^2+4)} = \frac{i^2}{(2i)(i^2+4)} = \frac{-1}{(2i)(3)} = \frac{-1}{6i} = \frac{i}{6}.$$

::: pf-proof

Standard residue formula for simple poles.

:::

:::

::: pf-step

At the simple pole $z = 2i$: $$\text{Res}(f, 2i) = \lim_{z \to 2i} (z - 2i) f(z) = \lim_{z \to 2i} \frac{z^2}{(z^2+1)(z+2i)} = \frac{(2i)^2}{((2i)^2+1)(4i)} = \frac{-4}{(-3)(4i)} = \frac{1}{3i} = -\frac{i}{3}.$$

::: pf-proof

Standard residue formula for simple poles.

:::

:::

::: pf-step

Sum of residues: $$\text{Res}(f, i) + \text{Res}(f, 2i) = \frac{i}{6} - \frac{i}{3} = -\frac{i}{6}.$$

::: pf-proof

Arithmetic sum $\frac{1}{6} - \frac{1}{3} = -\frac{1}{6}$.

:::

:::

::: {.pf-step #s3-4}

Multiply by $2\pi i$: $$2\pi i \Big( \text{Res}(f, i) + \text{Res}(f, 2i) \Big) = 2\pi i \left( -\frac{i}{6} \right) = \frac{2\pi}{6} = \frac{\pi}{3}.$$

::: pf-proof

$i(-i) = 1$.

:::

:::

:::

:::

:::

* * *

### Step 4: The arc integral tends to zero

::: pf

::: pf-step

**$\lim_{R \to \infty} \int_{C_R} f(z) \, dz = 0$.**

::: pf-proof

::: pf-step

On $C_R$, $|z| = R > 2$.

::: pf-proof

Definition of $C_R$.

:::

:::

::: pf-step

By the reverse triangle inequality, $|z^2+1| \geq R^2 - 1$ and $|z^2+4| \geq R^2 - 4$.

::: pf-proof

Reverse triangle inequality.

:::

:::

::: pf-step

Thus on $C_R$, $|f(z)| \leq \frac{R^2}{(R^2-1)(R^2-4)}$.

::: pf-proof

Modulus quotient.

:::

:::

::: {.pf-step #s4-4}

By the $ML$-inequality: $$\left| \int_{C_R} f(z) \, dz \right| \leq \frac{R^2}{(R^2-1)(R^2-4)} \cdot (\pi R) = \frac{\pi R^3}{(R^2-1)(R^2-4)} \to 0 \quad \text{as } R \to \infty.$$

::: pf-proof

Degree of denominator (4) exceeds degree of numerator (3).

:::

:::

:::

:::

:::

* * *

### Step 5: The value of $I$

::: pf

::: pf-step

**Compute the integral $I$.**

::: pf-proof

::: pf-step

Taking the limit as $R \to \infty$ in step [](#s2-3){.pf-ref}: $$\int_{-\infty}^\infty \frac{x^2}{(x^2+1)(x^2+4)} \, dx = \frac{\pi}{3} - 0 = \frac{\pi}{3}.$$

::: pf-proof

Follows from steps [](#s3-4){.pf-ref} and [](#s4-4){.pf-ref}.

:::

:::

::: pf-step

Therefore: $$I = \int_0^\infty \frac{x^2}{(x^2+1)(x^2+4)} \, dx = \frac{1}{2} \cdot \frac{\pi}{3} = \frac{\pi}{6}.$$

::: pf-proof

Halving the bilateral integral from step [](#s1-2){.pf-ref}.

:::

:::

:::

:::

:::

:::
