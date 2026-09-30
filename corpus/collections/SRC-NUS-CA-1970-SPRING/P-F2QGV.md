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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Find an analytic isomorphism from the open region between $x = 1$ and $x = 3$ to the upper half unit disk $\{|z| < 1,\Im z > 0\}$.
(You may leave your result as a composition of functions)
:::

::: {.solution}
Let $\Omega = \{z = x+iy \in \mathbb{C} : 1 < x < 3\}$ be the vertical strip and $\mathbb{D}^+ = \{w \in \mathbb{C} : |w| < 1 \text{ and } \text{Im}(w) > 0\}$ the upper half unit disk.

* * *

### Step 1: Affine map to a horizontal strip

::: pf

::: pf-step
**The affine transformation $\phi_1(z) = \frac{\pi}{2}(i z - i)$ maps the vertical strip $\Omega$ conformally onto the horizontal strip $S = \{\zeta \in \mathbb{C} : 0 < \text{Im}(\zeta) < \pi\}$.**

::: pf-proof

::: pf-step
For $z = x+iy$ with $1 < x < 3$ and $y \in \mathbb{R}$: $$\phi_1(z) = \frac{\pi}{2} i(x - 1 + iy) = -\frac{\pi}{2} y + i \frac{\pi}{2}(x - 1).$$

::: pf-proof
*Proof:* Algebraic expansion of $i(z-1)$.
:::

:::

::: pf-step
The imaginary part is $\text{Im}(\phi_1(z)) = \frac{\pi}{2}(x - 1)$.
Since $1 < x < 3$, $0 < x - 1 < 2$, which implies $0 < \text{Im}(\phi_1(z)) < \pi$.

::: pf-proof
*Proof:* Scaling the inequality $1 < x < 3$ by $\pi/2$.
:::

:::

::: pf-step
The real part is $\text{Re}(\phi_1(z)) = -\frac{\pi}{2}y$, which takes all values in $\mathbb{R}$ as $y$ ranges over $\mathbb{R}$.

::: pf-proof
*Proof:* Linear surjection from $\mathbb{R}$ to $\mathbb{R}$.
:::

:::

::: {.pf-step #phi1-biholomorphism}
$\phi_1$ is an affine map with non-zero slope $\frac{i\pi}{2} \neq 0$, hence a biholomorphism from $\Omega$ onto $S$.

::: pf-proof
*Proof:* Invertible complex linear map.
:::

:::

::: pf-qed
Step [](#phi1-biholomorphism){.pf-ref}.
:::

:::

:::

:::

* * *

### Step 2: Exponential map to the upper half-plane

::: pf

::: pf-step
**The exponential map $\phi_2(\zeta) = e^\zeta$ maps the horizontal strip $S$ conformally onto the upper half-plane $\mathbb{H} = \{u \in \mathbb{C} : \text{Im}(u) > 0\}$.**

::: pf-proof

::: pf-step
For $\zeta = \xi + i\eta \in S$ with $\xi \in \mathbb{R}$ and $\eta \in (0, \pi)$: $$e^\zeta = e^\xi e^{i\eta} = e^\xi(\cos\eta + i\sin\eta).$$

::: pf-proof
*Proof:* Euler's formula.
:::

:::

::: pf-step
Since $e^\xi > 0$ and $\sin\eta > 0$ for $\eta \in (0, \pi)$, $\text{Im}(e^\zeta) = e^\xi \sin\eta > 0$.

::: pf-proof
*Proof:* Product of positive real numbers.
:::

:::

::: {.pf-step #phi2-biholomorphism}
The map $\zeta \mapsto e^\zeta$ is a biholomorphism from the strip $S = \{\xi + i\eta : \xi \in \mathbb{R}, 0 < \eta < \pi\}$ onto $\mathbb{H}$.

::: pf-proof
*Proof:* Standard property of the complex exponential function.
:::

:::

::: pf-qed
Step [](#phi2-biholomorphism){.pf-ref}.
:::

:::

:::

:::

* * *

### Step 3: Conformal map from the upper half-plane to the upper half unit disk

::: pf

::: pf-step
**The inverse Joukowsky map $\phi_3(u) = -u + \sqrt{u - 1}\,\sqrt{u + 1}$ (each factor the principal square root) maps $\mathbb{H}$ conformally onto the upper half unit disk $\mathbb{D}^+$.**

::: pf-proof

::: pf-step
Recall that the Joukowsky map $J(w) = -\frac{1}{2}(w + 1/w)$ maps $\mathbb{D}^+$ biholomorphically onto $\mathbb{H}$.

::: pf-proof
*Proof:* For $w = r e^{i\theta} \in \mathbb{D}^+$ ($0 < r < 1, 0 < \theta < \pi$), $\text{Im}(J(w)) = \frac{1}{2}(1/r - r)\sin\theta > 0$.
:::

:::

::: pf-step
Solving $J(w) = u \iff -\frac{1}{2}(w + 1/w) = u \iff w^2 + 2u w + 1 = 0$ yields two roots $w = -u \pm \sqrt{u^2 - 1}$.

::: pf-proof
*Proof:* Quadratic formula.
:::

:::

::: {.pf-step #phi3-biholomorphism}
The function $\phi_3(u) = -u + \sqrt{u - 1}\,\sqrt{u + 1}$ is the biholomorphic inverse $J^{-1}: \mathbb{H} \to \mathbb{D}^+$.

::: pf-proof
*Proof:* For $u \in \mathbb{H}$, both $u - 1$ and $u + 1$ lie in $\mathbb{H}$, so the principal square roots are holomorphic there and $s(u) = \sqrt{u - 1}\,\sqrt{u + 1}$ is a holomorphic function with $s(u)^2 = u^2 - 1$. Hence $\phi_3(u)$ is a root of $w^2 + 2uw + 1 = 0$. The product of the two roots is $1$, and neither root lies on $|w| = 1$ because $J$ is real there; so exactly one root lies in the open unit disk, and it lies in $\mathbb{D}^+$ because $J$ maps the lower half-disk into the lower half-plane. At $u = it$ with $t > 0$ the arguments of $\sqrt{u-1}$ and $\sqrt{u+1}$ sum to $\pi/2$, so $\phi_3(it) = i\big(\sqrt{t^2+1} - t\big) \in \mathbb{D}^+$. The set of $u \in \mathbb{H}$ with $\phi_3(u) \in \mathbb{D}^+$ is open and closed in the connected set $\mathbb{H}$ and nonempty, so it is all of $\mathbb{H}$. The single-valued principal branch of $\sqrt{u^2-1}$ is not usable here: it is discontinuous on the imaginary axis, where $u^2 - 1 < -1$.
:::

:::

::: pf-qed
Step [](#phi3-biholomorphism){.pf-ref}.
:::

:::

:::

:::

* * *

### Step 4: The composite isomorphism

::: pf

::: pf-step
**Conclusion: The composite map $F = \phi_3 \circ \phi_2 \circ \phi_1$ is an analytic isomorphism from $\Omega$ to $\mathbb{D}^+$.**

::: pf-proof

::: pf-step
Explicitly, let $u(z) = \phi_2(\phi_1(z)) = \exp\left(\frac{i\pi}{2}(z - 1)\right) = -i \exp\left(\frac{i\pi z}{2}\right)$.

::: pf-proof
*Proof:* $\phi_1(z) = \frac{i\pi(z-1)}{2}$ and $e^{-i\pi/2} = -i$.
:::

:::

::: pf-step
Then $F(z) = \phi_3(u(z)) = -u(z) + \sqrt{u(z) - 1}\,\sqrt{u(z) + 1}$, where $u(z) = \exp\left(\frac{i\pi(z-1)}{2}\right)$.

::: pf-proof
*Proof:* Composition of the maps.
:::

:::

::: {.pf-step #F-is-biholomorphism}
As a composition of biholomorphic maps $\Omega \xrightarrow{\phi_1} S \xrightarrow{\phi_2} \mathbb{H} \xrightarrow{\phi_3} \mathbb{D}^+$, $F$ is an analytic isomorphism from $\Omega$ to $\mathbb{D}^+$.

::: pf-proof
*Proof:* Composition of biholomorphisms is a biholomorphism.
:::

:::

::: pf-qed
Step [](#F-is-biholomorphism){.pf-ref}.
:::

:::

:::

:::

:::
