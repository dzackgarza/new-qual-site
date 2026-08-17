---
schema: qual/card@1
id: P-BCFIC
kind: problem
title: Find an analytic isomorphism from the open region between $|z| = 1$…
classification:
  areas:
  - complex-analysis
  topics:
  - biholomorphisms
relations: []
review: draft
solved: true
---

::: problem
Find an analytic isomorphism from the open region between $|z| = 1$ and $|z -\frac 1 2| =\frac 1 2$ to the upper half plane $\Im z > 0$.
(You may leave your result as a composition of functions).
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Find an analytic isomorphism (biholomorphism) from the crescent region $\Omega = \{z \in \mathbb{C} : |z| < 1 \text{ and } |z - 1/2| > 1/2\}$ to the upper half-plane $\mathbb{H} = \{w \in \mathbb{C} : \text{Im}(w) > 0\}$.

* * *

### Step 1: Inversion to a Vertical Strip

<1>1. **The Möbius transformation $\phi_1(z) = \frac{1}{z - 1}$ maps $\Omega$ conformally onto the vertical strip $S_1 = \{w_1 \in \mathbb{C} : -1 < \text{Re}(w_1) < -\frac{1}{2}\}$.** <2>1. Both boundary circles $C_1: |z| = 1$ and $C_2: |z - 1/2| = 1/2$ pass through the point $z = 1$ (the pole of $\phi_1$), and they are tangent to each other at $z=1$ with common vertical tangent.
*Proof:* $1 \in C_1$ since $|1|=1$, and $1 \in C_2$ since $|1-1/2|=1/2$.
<2>2. Under $\phi_1(z) = \frac{1}{z-1}$, circles passing through the pole $z=1$ are mapped to straight lines in the $w_1$-plane.
*Proof:* Standard property of Möbius transformations on the Riemann sphere.
<2>3. For $z \in C_1$, $z = e^{i\theta}$: $$\text{Re}(\phi_1(e^{i\theta})) = \text{Re}\left(\frac{1}{e^{i\theta}-1}\right) = \text{Re}\left(\frac{\cos\theta - 1 - i\sin\theta}{(\cos\theta - 1)^2 + \sin^2\theta}\right) = \frac{\cos\theta - 1}{2 - 2\cos\theta} = -\frac{1}{2}.$$ *Proof:* Direct algebraic calculation for points on the unit circle.
<2>4. For $z \in C_2$, $z = \frac{1}{2} + \frac{1}{2}e^{i\theta}$, so $z - 1 = \frac{1}{2}(e^{i\theta}-1)$: $$\text{Re}(\phi_1(z)) = \text{Re}\left(\frac{2}{e^{i\theta}-1}\right) = 2 \cdot \left(-\frac{1}{2}\right) = -1.$$ *Proof:* Scaling of the result from <2>3. <2>5. The region $\Omega$ lies inside $|z| < 1$ ($\text{Re}(w_1) < -1/2$) and outside $|z - 1/2| = 1/2$ ($\text{Re}(w_1) > -1$). Testing $z = -1/2 \in \Omega$ gives $\phi_1(-1/2) = \frac{1}{-3/2} = -2/3 \in (-1, -1/2)$.
*Proof:* Connectedness and evaluation at the interior test point $z = -1/2$.
<2>6. Q.E.D.

* * *

### Step 2: Affine Transformation to a Standard Horizontal Strip

<1>2. **Map the strip $S_1$ to the standard horizontal strip $S_2 = \{w_2 \in \mathbb{C} : 0 < \text{Im}(w_2) < \pi\}$.** <2>1. Shift and scale the real part: $\psi(w_1) = 2\pi(w_1 + 1)$.
When $\text{Re}(w_1) \in (-1, -1/2)$, $\text{Re}(\psi(w_1)) \in (0, \pi)$.
*Proof:* $w_1 = -1 \implies 2\pi(0) = 0$, and $w_1 = -1/2 \implies 2\pi(1/2) = \pi$.
<2>2. Rotate by $\pi/2$ (multiply by $i$): $$\phi_2(w_1) = i \cdot 2\pi(w_1 + 1) = 2\pi i(w_1 + 1).$$ For $w_1 = u + iv$ with $-1 < u < -1/2$, $\phi_2(w_1) = -2\pi v + i 2\pi(u+1)$, so $\text{Im}(\phi_2(w_1)) = 2\pi(u+1) \in (0, \pi)$.
*Proof:* Multiplication by $i$ swaps real and imaginary parts: $\text{Im}(i Z) = \text{Re}(Z)$.
<2>3. In terms of the original variable $z$, $\phi_2(\phi_1(z)) = 2\pi i \left(\frac{1}{z-1} + 1\right) = \frac{2\pi i z}{z-1}$.
*Proof:* $\frac{1}{z-1} + 1 = \frac{z}{z-1}$.
<2>4. Q.E.D.

* * *

### Step 3: Exponential Map to the Upper Half-Plane

<1>3. **The exponential function maps $S_2$ conformally onto the upper half-plane $\mathbb{H}$.** <2>1. For $\zeta = \xi + i\eta \in S_2$, we have $\xi \in \mathbb{R}$ and $\eta \in (0, \pi)$.
*Proof:* Definition of the horizontal strip $S_2$.
<2>2. $\exp(\zeta) = e^\xi e^{i\eta}$.
Since $\xi \in \mathbb{R}$, $e^\xi \in (0, \infty)$; and since $\eta \in (0, \pi)$, $\arg(\exp(\zeta)) = \eta \in (0, \pi)$.
*Proof:* Properties of the complex exponential function.
<2>3. Thus $\phi_3(\zeta) = e^\zeta$ is a biholomorphism from $S_2$ onto $\mathbb{H} = \{w \in \mathbb{C} : \text{Im}(w) > 0\}$.
*Proof:* Standard holomorphic isomorphism between a horizontal strip of height $\pi$ and the upper half-plane.
<2>4. Q.E.D.

* * *

### Step 4: Composite Analytic Isomorphism

<1>4. **Conclusion: The composite map $F = \phi_3 \circ \phi_2 \circ \phi_1$ is an analytic isomorphism from $\Omega$ to $\mathbb{H}$.** <2>1. The explicit formula for $F(z)$ is: $$F(z) = \exp\left( \frac{2\pi i z}{z-1} \right).$$ *Proof:* Direct composition of $\phi_1, \phi_2, \phi_3$.
<2>2. As a composition of biholomorphic mappings $\Omega \xrightarrow{\phi_1} S_1 \xrightarrow{\phi_2} S_2 \xrightarrow{\phi_3} \mathbb{H}$, $F$ is an analytic isomorphism from $\Omega$ onto $\mathbb{H}$.
*Proof:* Composition of biholomorphisms is a biholomorphism.
<2>3. Q.E.D.
:::
