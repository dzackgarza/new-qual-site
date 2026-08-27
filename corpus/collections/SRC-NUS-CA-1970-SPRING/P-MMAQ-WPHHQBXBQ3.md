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

::: problem
Evaluate the improper integral

$\int_0^\infty \frac{x^2~dx}{(x^2+1)(x^2+4)}$
:::

::: {.solution}
**Goal:** Evaluate the improper real integral $I = \int_0^\infty \frac{x^2}{(x^2+1)(x^2+4)} \, dx$ using contour integration and residues.

* * *

### Step 1: Symmetry and Complex Rational Function

<1>1. **Symmetry over $\mathbb{R}$.** <2>1. The integrand $g(x) = \frac{x^2}{(x^2+1)(x^2+4)}$ is an even function: $g(-x) = g(x)$ for all $x \in \mathbb{R}$.
*Proof:* $(-x)^2 = x^2$.
<2>2. Therefore, $I = \frac{1}{2} \int_{-\infty}^\infty \frac{x^2}{(x^2+1)(x^2+4)} \, dx$.
*Proof:* Splitting the integral over symmetric bounds.
<2>3. Define $f(z) = \frac{z^2}{(z^2+1)(z^2+4)} = \frac{z^2}{(z-i)(z+i)(z-2i)(z+2i)}$.
*Proof:* Factorization of quadratic polynomials over $\mathbb{C}$.
<2>4. Q.E.D.

* * *

### Step 2: Contour Integration in the Upper Half-Plane

<1>2. **Set up the semicircular contour $\Gamma_R = [-R, R] \cup C_R$ where $C_R = \{R e^{i\theta} : \theta \in [0, \pi]\}$ with $R > 2$.** <2>1. The singularities of $f(z)$ are simple poles at $z = \pm i$ and $z = \pm 2i$.
*Proof:* Zeros of $(z^2+1)(z^2+4)$.
<2>2. The poles enclosed inside $\Gamma_R$ in the upper half-plane $\mathbb{H}$ are $z_1 = i$ and $z_2 = 2i$.
*Proof:* $\text{Im}(i) = 1 > 0$ and $\text{Im}(2i) = 2 > 0$, while $\text{Im}(-i) < 0$ and $\text{Im}(-2i) < 0$.
<2>3. By the Cauchy Residue Theorem: $$\oint_{\Gamma_R} f(z) \, dz = \int_{-R}^R \frac{x^2}{(x^2+1)(x^2+4)} \, dx + \int_{C_R} f(z) \, dz = 2\pi i \Big( \text{Res}(f, i) + \text{Res}(f, 2i) \Big).$$ *Proof:* Application of the residue theorem to the enclosed simple poles.
<2>4. Q.E.D.

* * *

### Step 3: Compute the Residues

<1>3. **Compute the residues at $z = i$ and $z = 2i$.** <2>1. At the simple pole $z = i$: $$\text{Res}(f, i) = \lim_{z \to i} (z - i) f(z) = \lim_{z \to i} \frac{z^2}{(z+i)(z^2+4)} = \frac{i^2}{(2i)(i^2+4)} = \frac{-1}{(2i)(3)} = \frac{-1}{6i} = \frac{i}{6}.$$ *Proof:* Standard residue formula for simple poles.
<2>2. At the simple pole $z = 2i$: $$\text{Res}(f, 2i) = \lim_{z \to 2i} (z - 2i) f(z) = \lim_{z \to 2i} \frac{z^2}{(z^2+1)(z+2i)} = \frac{(2i)^2}{((2i)^2+1)(4i)} = \frac{-4}{(-3)(4i)} = \frac{1}{3i} = -\frac{i}{3}.$$ *Proof:* Standard residue formula for simple poles.
<2>3. Sum of residues: $$\text{Res}(f, i) + \text{Res}(f, 2i) = \frac{i}{6} - \frac{i}{3} = -\frac{i}{6}.$$ *Proof:* Arithmetic sum $\frac{1}{6} - \frac{1}{3} = -\frac{1}{6}$.
<2>4. Multiply by $2\pi i$: $$2\pi i \Big( \text{Res}(f, i) + \text{Res}(f, 2i) \Big) = 2\pi i \left( -\frac{i}{6} \right) = \frac{2\pi}{6} = \frac{\pi}{3}.$$ *Proof:* $i(-i) = 1$.
<2>5. Q.E.D.

* * *

### Step 4: Vanishing of the Arc Integral

<1>4. **$\lim_{R \to \infty} \int_{C_R} f(z) \, dz = 0$.** <2>1. On $C_R$, $|z| = R > 2$.
*Proof:* Definition of $C_R$.
<2>2. By the reverse triangle inequality, $|z^2+1| \geq R^2 - 1$ and $|z^2+4| \geq R^2 - 4$.
*Proof:* Reverse triangle inequality.
<2>3. Thus on $C_R$, $|f(z)| \leq \frac{R^2}{(R^2-1)(R^2-4)}$.
*Proof:* Modulus quotient.
<2>4. By the $ML$-inequality: $$\left| \int_{C_R} f(z) \, dz \right| \leq \frac{R^2}{(R^2-1)(R^2-4)} \cdot (\pi R) = \frac{\pi R^3}{(R^2-1)(R^2-4)} \to 0 \quad \text{as } R \to \infty.$$ *Proof:* Degree of denominator (4) exceeds degree of numerator (3). <2>5. Q.E.D.

* * *

### Step 5: Final Evaluation

<1>5. **Compute the integral $I$.** <2>1. Taking the limit as $R \to \infty$ in <1>2.<2>3: $$\int_{-\infty}^\infty \frac{x^2}{(x^2+1)(x^2+4)} \, dx = \frac{\pi}{3} - 0 = \frac{\pi}{3}.$$ *Proof:* Follows from <1>3.<2>4 and <1>4.<2>4. <2>2. Therefore: $$I = \int_0^\infty \frac{x^2}{(x^2+1)(x^2+4)} \, dx = \frac{1}{2} \cdot \frac{\pi}{3} = \frac{\pi}{6}.$$ *Proof:* Halving the bilateral integral from <1>1.<2>2. <2>3. Q.E.D.
:::
