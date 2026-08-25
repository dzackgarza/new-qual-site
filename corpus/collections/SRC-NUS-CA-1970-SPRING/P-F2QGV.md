---
schema: qual/card@1
id: P-F2QGV
kind: problem
title: Biholomorphism from the strip $1<\Re z<3$ to the upper half-disk
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
relations: []
review: draft
---

::: problem
Find an analytic isomorphism from the open region between $x = 1$ and $x = 3$ to the upper half unit disk $\{|z| < 1,\Im z > 0\}$.
(You may leave your result as a composition of functions)
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Find an analytic isomorphism (biholomorphism) from the vertical strip $\Omega = \{z = x+iy \in \mathbb{C} : 1 < x < 3\}$ to the upper half unit disk $\mathbb{D}^+ = \{w \in \mathbb{C} : |w| < 1 \text{ and } \text{Im}(w) > 0\}$.

* * *

### Step 1: Affine Map to the Standard Horizontal Strip

<1>1. **The affine transformation $\phi_1(z) = \frac{\pi}{2}(i z - i)$ maps the vertical strip $\Omega$ conformally onto the horizontal strip $S = \{\zeta \in \mathbb{C} : 0 < \text{Im}(\zeta) < \pi\}$.** <2>1. For $z = x+iy$ with $1 < x < 3$ and $y \in \mathbb{R}$: $$\phi_1(z) = \frac{\pi}{2} i(x - 1 + iy) = -\frac{\pi}{2} y + i \frac{\pi}{2}(x - 1).$$ *Proof:* Algebraic expansion of $i(z-1)$.
<2>2. The imaginary part is $\text{Im}(\phi_1(z)) = \frac{\pi}{2}(x - 1)$.
Since $1 < x < 3$, $0 < x - 1 < 2$, which implies $0 < \text{Im}(\phi_1(z)) < \pi$.
*Proof:* Scaling the inequality $1 < x < 3$ by $\pi/2$.
<2>3. The real part is $\text{Re}(\phi_1(z)) = -\frac{\pi}{2}y$, which takes all values in $\mathbb{R}$ as $y$ ranges over $\mathbb{R}$.
*Proof:* Linear surjection from $\mathbb{R}$ to $\mathbb{R}$.
<2>4. $\phi_1$ is an affine map with non-zero slope $\frac{i\pi}{2} \neq 0$, hence a biholomorphism from $\Omega$ onto $S$.
*Proof:* Invertible complex linear map.
<2>5. Q.E.D.

* * *

### Step 2: Exponential Map to the Upper Half-Plane

<1>2. **The exponential map $\phi_2(\zeta) = e^\zeta$ maps the horizontal strip $S$ conformally onto the upper half-plane $\mathbb{H} = \{u \in \mathbb{C} : \text{Im}(u) > 0\}$.** <2>1. For $\zeta = \xi + i\eta \in S$ with $\xi \in \mathbb{R}$ and $\eta \in (0, \pi)$: $$e^\zeta = e^\xi e^{i\eta} = e^\xi(\cos\eta + i\sin\eta).$$ *Proof:* Euler's formula.
<2>2. Since $e^\xi > 0$ and $\sin\eta > 0$ for $\eta \in (0, \pi)$, $\text{Im}(e^\zeta) = e^\xi \sin\eta > 0$.
*Proof:* Product of positive real numbers.
<2>3. The map $\zeta \mapsto e^\zeta$ is a biholomorphism from the strip $S = \{\xi + i\eta : \xi \in \mathbb{R}, 0 < \eta < \pi\}$ onto $\mathbb{H}$.
*Proof:* Standard property of the complex exponential function.
<2>4. Q.E.D.

* * *

### Step 3: Conformal Map from the Upper Half-Plane to the Upper Half Unit Disk

<1>3. **The inverse Joukowsky map $\phi_3(u) = -u + \sqrt{u^2 - 1}$ (with principal square root) maps $\mathbb{H}$ conformally onto the upper half unit disk $\mathbb{D}^+$.** <2>1. Recall that the Joukowsky map $J(w) = -\frac{1}{2}(w + 1/w)$ maps $\mathbb{D}^+$ biholomorphically onto $\mathbb{H}$.
*Proof:* Verified in standard conformal mapping theory: for $w = r e^{i\theta} \in \mathbb{D}^+$ ($0 < r < 1, 0 < \theta < \pi$), $\text{Im}(J(w)) = \frac{1}{2}(1/r - r)\sin\theta > 0$.
<2>2. Solving $J(w) = u \iff -\frac{1}{2}(w + 1/w) = u \iff w^2 + 2u w + 1 = 0$ yields two roots $w = -u \pm \sqrt{u^2 - 1}$.
*Proof:* Quadratic formula.
<2>3. The branch $\phi_3(u) = -u + \sqrt{u^2 - 1}$ that takes values with $|w| < 1$ and $\text{Im}(w) > 0$ for $u \in \mathbb{H}$ provides the biholomorphic inverse $J^{-1}: \mathbb{H} \to \mathbb{D}^+$.
*Proof:* Product of the two roots is $1$, and exactly one root lies in $\mathbb{D}^+$ when $u \in \mathbb{H}$.
<2>4. Q.E.D.

* * *

### Step 4: Full Composite Analytic Isomorphism

<1>4. **Conclusion: The composite map $F = \phi_3 \circ \phi_2 \circ \phi_1$ is an analytic isomorphism from $\Omega$ to $\mathbb{D}^+$.** <2>1. Explicitly, let $u(z) = \phi_2(\phi_1(z)) = \exp\left(\frac{i\pi}{2}(z - 1)\right) = -i \exp\left(\frac{i\pi z}{2}\right)$.
*Proof:* $\phi_1(z) = \frac{i\pi(z-1)}{2}$ and $e^{-i\pi/2} = -i$.
<2>2. Then $F(z) = \phi_3(u(z)) = -u(z) + \sqrt{u(z)^2 - 1}$, where $u(z) = \exp\left(\frac{i\pi(z-1)}{2}\right)$.
*Proof:* Composition of the maps.
<2>3. As a composition of biholomorphic maps $\Omega \xrightarrow{\phi_1} S \xrightarrow{\phi_2} \mathbb{H} \xrightarrow{\phi_3} \mathbb{D}^+$, $F$ is an analytic isomorphism from $\Omega$ to $\mathbb{D}^+$.
*Proof:* Composition of biholomorphisms is a biholomorphism.
<2>4. Q.E.D.
:::
