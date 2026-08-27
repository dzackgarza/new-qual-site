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

::: problem
Evaluate the following by the method of residues: $\int_0^{\pi /2} \frac{1}{3+\sin^2x}dx$
:::

::: {.solution}
**Goal:** Evaluate the definite trigonometric integral $I = \int_0^{\pi/2} \frac{1}{3 + \sin^2 x} \, dx$ using the method of residues.

* * *

### Step 1: Symmetry and Double-Angle Reduction

<1>1. **Express the integral over $[0, 2\pi]$ in terms of $\cos(2x)$.** <2>1. Use the half-angle identity $\sin^2 x = \frac{1 - \cos(2x)}{2}$.
*Proof:* Standard trigonometric identity.
<2>2. The denominator becomes: $$3 + \sin^2 x = 3 + \frac{1 - \cos(2x)}{2} = \frac{7 - \cos(2x)}{2}.$$ *Proof:* Algebraic simplification.
<2>3. Thus $I = \int_0^{\pi/2} \frac{2}{7 - \cos(2x)} \, dx$.
*Proof:* Substitution into $I$.
<2>4. Substitute $\theta = 2x$, so $d\theta = 2\,dx$ and as $x$ ranges from $0$ to $\pi/2$, $\theta$ ranges from $0$ to $\pi$: $$I = \int_0^\pi \frac{d\theta}{7 - \cos\theta}.$$ *Proof:* Change of variable $\theta = 2x$.
<2>5. Since $\cos\theta$ is even and symmetric on $[0, 2\pi]$ ($\cos(2\pi - \theta) = \cos\theta$): $$I = \frac{1}{2} \int_0^{2\pi} \frac{d\theta}{7 - \cos\theta}.$$ *Proof:* Symmetry: $\int_0^{2\pi} g(\cos\theta)\,d\theta = 2 \int_0^\pi g(\cos\theta)\,d\theta$.
<2>6. Q.E.D.

* * *

### Step 2: Convert to a Unit Circle Contour Integral

<1>2. **Substitute $z = e^{i\theta}$ on the unit circle $C = \{z \in \mathbb{C} : |z| = 1\}$.** <2>1. For $z = e^{i\theta}$, $dz = i e^{i\theta} d\theta = i z d\theta \implies d\theta = \frac{dz}{i z}$.
*Proof:* Parametrization of unit circle.
<2>2. $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2} = \frac{z + z^{-1}}{2} = \frac{z^2 + 1}{2z}$.
*Proof:* Euler's formula.
<2>3. The integrand becomes: $$\frac{1}{7 - \cos\theta} = \frac{1}{7 - \frac{z^2+1}{2z}} = \frac{2z}{14z - (z^2+1)} = \frac{-2z}{z^2 - 14z + 1}.$$ *Proof:* Algebraic rearrangement.
<2>4. The integral becomes: $$I = \frac{1}{2} \oint_C \frac{-2z}{z^2 - 14z + 1} \cdot \frac{dz}{iz} = -\frac{1}{i} \oint_C \frac{dz}{z^2 - 14z + 1} = i \oint_C \frac{dz}{z^2 - 14z + 1}.$$ *Proof:* $-1/i = i$.
<2>5. Q.E.D.

* * *

### Step 3: Find Singularities and Enclosed Residue

<1>3. **Find the roots of $z^2 - 14z + 1 = 0$.** <2>1. By the quadratic formula: $$z = \frac{14 \pm \sqrt{196 - 4}}{2} = \frac{14 \pm \sqrt{192}}{2} = \frac{14 \pm 8\sqrt{3}}{2} = 7 \pm 4\sqrt{3}.$$ *Proof:* Solving quadratic equation.
<2>2. Let $z_1 = 7 - 4\sqrt{3}$ and $z_2 = 7 + 4\sqrt{3}$.
*Proof:* Denoting roots.
<2>3. Since $4\sqrt{3} = \sqrt{48} \approx 6.928$: $$|z_1| = 7 - 4\sqrt{3} \approx 0.0718 < 1, \qquad |z_2| = 7 + 4\sqrt{3} \approx 13.928 > 1.$$ *Proof:* Arithmetic estimation ($48 < 49$). <2>4. Therefore, only $z_1 = 7 - 4\sqrt{3}$ lies inside the unit circle $|z| < 1$.
*Proof:* $z_1 \in \mathbb{D}$ and $z_2 \notin \mathbb{D}$.
<2>5. Q.E.D.

<1>4. **Compute the residue at $z_1$.** <2>1. Since $z_1$ is a simple pole of $f(z) = \frac{1}{z^2 - 14z + 1} = \frac{1}{(z - z_1)(z - z_2)}$: $$\text{Res}(f, z_1) = \lim_{z \to z_1} (z - z_1) f(z) = \frac{1}{z_1 - z_2} = \frac{1}{(7 - 4\sqrt{3}) - (7 + 4\sqrt{3})} = \frac{1}{-8\sqrt{3}} = -\frac{1}{8\sqrt{3}}.$$ *Proof:* Standard simple pole residue calculation.
<2>2. Q.E.D.

* * *

### Step 4: Final Evaluation

<1>5. **Evaluate the contour integral $I$.** <2>1. By the Cauchy Residue Theorem: $$\oint_C \frac{dz}{z^2 - 14z + 1} = 2\pi i \, \text{Res}(f, z_1) = 2\pi i \left( -\frac{1}{8\sqrt{3}} \right) = -\frac{\pi i}{4\sqrt{3}}.$$ *Proof:* Application of the Residue Theorem to the single enclosed pole $z_1$.
<2>2. From <1>2.<2>4, $I = i \oint_C \frac{dz}{z^2 - 14z + 1}$: $$I = i \left( -\frac{\pi i}{4\sqrt{3}} \right) = -i^2 \frac{\pi}{4\sqrt{3}} = \frac{\pi}{4\sqrt{3}} = \frac{\pi\sqrt{3}}{12}.$$ *Proof:* $-i^2 = 1$.
<2>3. Q.E.D.
:::
