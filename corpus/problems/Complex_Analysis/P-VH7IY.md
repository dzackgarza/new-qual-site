---
schema: qual/card@1
id: P-VH7IY
kind: problem
title: Polar Cauchy–Riemann equations and holomorphy of the principal logarithm
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Complex Logarithm
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
a. Show that in polar coordinates, the Cauchy-Riemann equations take the form
\[
\frac{\partial u}{\partial r}=\frac{1}{r} \frac{\partial v}{\partial \theta} \text { and } \frac{\partial v}{\partial r}=-\frac{1}{r} \frac{\partial u}{\partial \theta}
.\]

b. Use (a) to show that the logarithm function, defined as 
\[
\log z=\log r+i \theta \text { where } z=r e^{i \theta} \text { with }-\pi<\theta<\pi
.\]
is holomorphic on the region $r> 0, -\pi < \theta < \pi$.

Also show that this function is not continuous in $r>0$.
:::

::: {.solution}
**Goal:** (a) Derive the polar form of the Cauchy–Riemann equations; (b) use it to show the principal logarithm $\log z = \log r + i\theta$ ($z = re^{i\theta}$, $-\pi < \theta < \pi$) is holomorphic on the slit plane, and show this function is not continuous on all of $r > 0$.

<1>1. Chain rule in polar coordinates: $u_r = u_x \cos\theta + u_y \sin\theta$ and $u_\theta = r(-u_x \sin\theta + u_y \cos\theta)$; same for $v$.
    Proof: With $x = r\cos\theta$, $y = r\sin\theta$, $dr = \cos\theta\,dx + \sin\theta\,dy$ and $d\theta = -r\sin\theta\,dx + r\cos\theta\,dy$ by the chain rule.

<1>2. (a): $u_r = \frac{1}{r} v_\theta$ and $v_r = -\frac{1}{r} u_\theta$.
    Proof: The Cauchy–Riemann equations $u_x = v_y$, $u_y = -v_x$ imply, by <1>1, $u_r = u_x\cos\theta + u_y\sin\theta = v_y\cos\theta - v_x\sin\theta = \frac{1}{r}\qty(-v_x r\sin\theta + v_y r\cos\theta) = \frac{1}{r} v_\theta$. Similarly $v_r = v_x\cos\theta + v_y\sin\theta = -u_y\cos\theta + u_x\sin\theta = -\frac{1}{r}\qty(-u_x r\sin\theta + u_y r\cos\theta) = -\frac{1}{r} u_\theta$.

<1>3. (b): For $\log z = \log r + i\theta$ on $\theset{r > 0, -\pi < \theta < \pi}$, $u = \log r$ and $v = \theta$ satisfy the polar Cauchy–Riemann equations of <1>2.
    Proof: $u_r = \frac{1}{r}$, $u_\theta = 0$, $v_r = 0$, $v_\theta = 1$, so $u_r = \frac{1}{r} = \frac{1}{r}\cdot 1 = \frac{1}{r} v_\theta$ and $v_r = 0 = -\frac{1}{r} u_\theta$.

<1>4. (b): $\log z$ is holomorphic on $\theset{r > 0, -\pi < \theta < \pi}$.
    Proof: $u, v$ are $C^1$ there (on the slit plane, $\theta$ is a smooth single-valued function of $z$, and $\log r$ is smooth), and they satisfy the Cauchy–Riemann equations in polar form by <1>3; by the standard criterion, $\log z$ is holomorphic, with derivative $e^{-i\theta}\qty(u_r + i v_r) = \frac{e^{-i\theta}}{r} = \frac{1}{z}$.

<1>5. (b): $\log z$ is not continuous on the set $\theset{r > 0}$ (all of $\CC \setminus \theset{0}$).
    Proof: The principal branch cuts along the negative real axis: fix $z_0 = -r_0$ with $r_0 > 0$ and approach it from the upper half-plane, $z = r_0 e^{i\theta}$ with $\theta \to \pi^-$: $\log z \to \log r_0 + i\pi$. Approaching from the lower half-plane, $\theta \to -\pi^+$: $\log z \to \log r_0 - i\pi$. These two limits differ (by $2\pi i$), so $\log z$ has no limit as $z \to z_0$ and is discontinuous at every point of the negative real axis.

<1>6. Q.E.D.
    Proof: <1>2 proves (a), and <1>4–<1>5 prove (b) (holomorphicity on the slit plane and discontinuity in $r > 0$).

:::
