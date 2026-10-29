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

::: {.problem}
(a) Show that in polar coordinates, the Cauchy-Riemann equations take the form
$$
\frac{\partial u}{\partial r}=\frac{1}{r} \frac{\partial v}{\partial \theta} \text { and } \frac{\partial v}{\partial r}=-\frac{1}{r} \frac{\partial u}{\partial \theta}.
$$

(b) Use (a) to show that the logarithm function, defined as
$$
\log z=\log r+i \theta \text { where } z=r e^{i \theta} \text { with }-\pi<\theta<\pi,
$$
is holomorphic on the region $r> 0, -\pi < \theta < \pi$.

Show also that this branch cannot be extended continuously across the negative
real axis to all of $\CC\setminus\{0\}$.
:::

::: {.solution}
Let $u, v$ be $C^1$ functions of $(x, y)$ on an open set not containing $0$, and regard them as functions of $(r, \theta)$ through $x = r\cos\theta$, $y = r\sin\theta$. Abbreviate $c = \cos\theta$ and $s = \sin\theta$.

::: pf

::: {.pf-step #chain}

$u_r = c\,u_x + s\,u_y$ and $u_\theta = r(-s\,u_x + c\,u_y)$, and likewise for $v$.

::: pf-proof

This is the chain rule, using $x_r = c$, $y_r = s$, $x_\theta = -rs$ and $y_\theta = rc$.

:::

:::

::: {.pf-step #polar-cr}

(a) For $r > 0$, the Cauchy--Riemann equations $u_x = v_y$, $u_y = -v_x$ hold if and only if $u_r = \frac{1}{r} v_\theta$ and $v_r = -\frac{1}{r} u_\theta$.

::: pf-proof

Put $A = u_x - v_y$ and $B = u_y + v_x$. By step [](#chain){.pf-ref},
$$
\begin{aligned}
u_r - \tfrac{1}{r}v_\theta &= c\,u_x + s\,u_y + s\,v_x - c\,v_y = cA + sB, \\
v_r + \tfrac{1}{r}u_\theta &= c\,v_x + s\,v_y - s\,u_x + c\,u_y = cB - sA.
\end{aligned}
$$
The vector $(cA + sB,\ cB - sA)$ is the rotation of $(A, B)$ through $-\theta$, so it vanishes exactly when $A = B = 0$.

:::

:::

::: {.pf-step #log-hol}

(b) The principal logarithm is holomorphic on $\{r > 0, -\pi < \theta < \pi\}$, with derivative $1/z$.

::: pf-proof

On this slit plane, $(r, \theta)$ are smooth functions of $(x, y)$, so $u = \log r$ and $v = \theta$ are $C^1$. They satisfy $u_r = \frac1r = \frac1r v_\theta$ and $v_r = 0 = -\frac1r u_\theta$, so by step [](#polar-cr){.pf-ref} they satisfy the Cauchy--Riemann equations. A $C^1$ function satisfying the Cauchy--Riemann equations is holomorphic, and its derivative is $u_x + i v_x = e^{-i\theta}(u_r + i v_r) = \frac{1}{re^{i\theta}} = \frac1z$.

:::

:::

::: pf-step

(b) The principal branch has no continuous extension to $\CC\setminus\{0\}$.

::: pf-proof

Fix $z_0 = -r_0$ with $r_0 > 0$. Along $z = r_0 e^{i\theta}$ with $\theta \to \pi^-$, $\log z \to \log r_0 + i\pi$; with $\theta \to -\pi^+$, $\log z \to \log r_0 - i\pi$. The two limits differ by $2\pi i$, so no value at $z_0$ makes the extension continuous.

:::

:::

:::

:::
