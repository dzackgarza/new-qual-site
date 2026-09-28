---
schema: qual/card@1
id: P-XKYOG
kind: problem
title: equations take the form
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Complex Logarithm
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
equations take the form

$$\frac{\partial u}{\partial r} = \frac{1}{r} \frac{\partial v}{\partial \theta}
\; \; \; \text{and} \; \; \;
\frac{\partial v}{\partial r} = - \frac{1}{r} \frac{\partial u}{\partial \theta}$$

(b) Use these equations to show that the logarithm function
defined by $$\log z = \log r + i \theta \; \;
\mbox{where} \; z = r e^{i \theta } \; \mbox{with} \; - \pi < \theta < \pi$$
is a holomorphic function in the region
$r>0, \; - \pi < \theta < \pi$. Also show that $\log z$ defined
above is not continuous in $r>0$.
:::

::: {.solution}
The beginning of the card is truncated. The missing part asks for the polar
Cauchy--Riemann equations. If $x=r\cos\theta$, $y=r\sin\theta$, then the chain
rule together with $u_x=v_y$ and $u_y=-v_x$ gives
\[
u_r={1\over r}v_\theta,
\qquad
v_r=-{1\over r}u_\theta.
\]

For
\[
\Log z=\log r+i\theta,
\qquad r>0,\quad -\pi<\theta<\pi,
\]
we have $u_r=1/r$, $u_\theta=0$, $v_r=0$, and $v_\theta=1$, so the polar
Cauchy--Riemann equations hold. Hence the principal logarithm is holomorphic
on the slit plane $\CC\setminus(-\infty,0]$.

The final sentence of the source is false as literally written: a holomorphic
function is continuous on its domain. The correct noncontinuity phenomenon is
that this branch cannot extend continuously to all of $\CC^\times$. Indeed,
approaching $-1$ from above gives imaginary part tending to $\pi$, while
approaching from below gives imaginary part tending to $-\pi$. Thus no
continuous extension across the negative real axis exists.
:::
