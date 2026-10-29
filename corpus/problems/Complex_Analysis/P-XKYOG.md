---
schema: qual/card@1
id: P-XKYOG
kind: problem
title: Polar Cauchy--Riemann equations and holomorphy of the principal logarithm
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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Card began mid-sentence at "equations take the form"; QualComplex Problem 9.5.1 part (a) reads "Show that in polar coordinates, the Cauchy-Riemann equations take the form", restored. Source part (b) asked to show Log z "is not continuous in r > 0", false for a function holomorphic on its domain; the statement now asks to show Log z has no continuous extension to r > 0.'
---

::: {.problem}
(a) Show that in polar coordinates, the Cauchy--Riemann equations take the form

$$\frac{\partial u}{\partial r} = \frac{1}{r} \frac{\partial v}{\partial \theta}
\; \; \; \text{and} \; \; \;
\frac{\partial v}{\partial r} = - \frac{1}{r} \frac{\partial u}{\partial \theta}$$

(b) Use these equations to show that the logarithm function
defined by $$\log z = \log r + i \theta \; \;
\mbox{where} \; z = r e^{i \theta } \; \mbox{with} \; - \pi < \theta < \pi$$
is a holomorphic function in the region
$r>0, \; - \pi < \theta < \pi$. Also show that $\log z$ defined
above has no continuous extension to the region $r>0$.
:::

::: {.solution}
Write $f = u + iv$ with $u, v$ continuously differentiable, and $x = r\cos\theta$, $y = r\sin\theta$ for $r > 0$.

::: pf

::: {.pf-step #polar-cr}

$u_x = v_y$ and $u_y = -v_x$ hold if and only if $u_r = \frac1r v_\theta$ and $v_r = -\frac1r u_\theta$.

::: pf-proof

By the chain rule, $u_r = u_x\cos\theta + u_y\sin\theta$ and $u_\theta = r(-u_x\sin\theta + u_y\cos\theta)$, and the same with $v$. Hence
$$
u_r - \tfrac1r v_\theta = (u_x - v_y)\cos\theta + (u_y + v_x)\sin\theta,
\qquad
v_r + \tfrac1r u_\theta = (v_x + u_y)\cos\theta - (u_x - v_y)\sin\theta.
$$
Both right sides vanish for all $\theta$ if and only if $u_x - v_y = 0$ and $u_y + v_x = 0$, since the matrix $\begin{pmatrix}\cos\theta & \sin\theta\\ -\sin\theta & \cos\theta\end{pmatrix}$ is invertible.

:::

:::

::: pf-step

$\log z$ is holomorphic on $\theset{r>0,\ -\pi<\theta<\pi}$.

::: pf-proof

On this region $(r,\theta)$ are smooth coordinates, $u = \log r$ and $v = \theta$, so $u_r = 1/r$, $u_\theta = 0$, $v_r = 0$, $v_\theta = 1$. These satisfy the equations of step [](#polar-cr){.pf-ref}, so $u, v$ are continuously differentiable and satisfy the Cauchy--Riemann equations, and $\log z$ is holomorphic.

:::

:::

::: pf-step

$\log z$ has no continuous extension to $\theset{r>0} = \CC\setminus\theset0$.

::: pf-proof

Let $z_n = e^{i(\pi - 1/n)}$ and $w_n = e^{-i(\pi - 1/n)}$. Both sequences tend to $-1$, while $\Im\log z_n = \pi - 1/n \to \pi$ and $\Im\log w_n = -\pi + 1/n \to -\pi$. A continuous extension $F$ would give $F(-1) = \lim\log z_n = \lim\log w_n$, which is impossible.

:::

:::

:::

:::
