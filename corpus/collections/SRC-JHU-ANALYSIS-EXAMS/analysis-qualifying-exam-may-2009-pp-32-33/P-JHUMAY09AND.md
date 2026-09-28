---
schema: qual/card@1
id: P-JHUMAY09AND
kind: problem
title: The Fourier transform of $1/(1+x^2)$ at frequency one
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the negative exponential convention and required semicircular contour with May 2009 problem 4 in the retained JHU extraction; replaced the truncated title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked absolute convergence, clockwise orientation of the lower semicircle, the residue at minus i and a uniform vanishing-arc estimate for the stated Fourier convention."
---

::: {.problem}
4. Let $f ( x ) = { \frac { 1 } { x ^ { 2 } + 1 } }$ . Use a contour integral consisting of the interval $[ - R , R ] \subset \mathbb { R }$ and a semicircle of radius R to compute the Fourier transform

$$
{ \widehat { f } } ( 1 ) = \int _ { \mathbb { R } } f ( x ) e ^ { - i x } d x ~ .
$$

Show that the contour integral converges to your answer as $R \to + \infty$
:::

::: {.solution}
The value is $\boxed{\widehat f(1)=\pi/e}$.

<1>1. The real integral exists absolutely.

::: {.proof}
For real $x$, $|e^{-ix}|=1$. The function
$(1+x^2)^{-1}$ is bounded on $[-1,1]$ and is at most
$x^{-2}$ for $|x|\geq1$. Since the latter is integrable
on both tails, the integral of $e^{-ix}/(1+x^2)$ is
absolutely convergent. Thus limits of its truncated
integrals determine its ordinary integral, not merely
a principal value.
:::

<1>2. The clockwise lower semicircle encloses one pole.

::: {.proof}
Set $F(z)=e^{-iz}/(1+z^2)$. For $R>1$, traverse
$[-R,R]$ from left to right, then return from $R$ to
$-R$ along the lower semicircle $\Gamma_R$.
This contour is clockwise. Its only enclosed pole is
$-i$, and that pole is simple, with residue
$$
\operatorname{Res}_{z=-i}F
=\frac{e^{-i(-i)}}{-2i}=\frac{i}{2e}.
$$
The residue theorem therefore gives [@SS03]
$$
\int_{-R}^R\frac{e^{-ix}}{1+x^2}\,dx
+\int_{\Gamma_R}F(z)\,dz
=-2\pi i\frac{i}{2e}=\frac\pi e.
$$
The minus sign is the contour orientation; the lower
half-plane is chosen because it gives exponential decay
for the prescribed sign $e^{-iz}$.
:::

<1>3. The semicircle contribution tends to zero.

::: {.proof}
On $\Gamma_R$, one has $\operatorname{Im}z\leq0$ and
$$
|e^{-iz}|=e^{\operatorname{Im}z}\leq1,
\qquad |1+z^2|\geq R^2-1.
$$
The arc length is $\pi R$, so
$$
\left|\int_{\Gamma_R}F(z)\,dz\right|
\leq\frac{\pi R}{R^2-1}\longrightarrow0.
$$
Letting $R\to\infty$ in the identity of step <1>2,
using this estimate and the absolute convergence in
step <1>1, gives $\widehat f(1)=\pi/e$ as asserted.
:::
:::
