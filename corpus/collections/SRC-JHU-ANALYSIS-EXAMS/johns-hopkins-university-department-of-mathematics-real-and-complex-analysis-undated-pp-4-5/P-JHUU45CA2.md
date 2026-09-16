---
schema: qual/card@1
id: P-JHUU45CA2
kind: problem
title: Evaluating the sinc integral by contour integration
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both the direct improper-convergence request and contour-evaluation request with Problem 5 of the undated JHU exam on pages 4–5."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked separate convergence of the two infinite tails, the clockwise indentation sign, cancellation on the real segments, and an explicit large-semicircle estimate."
---

::: {.problem}
This problem is about the integral

$$I = \int_{-\infty}^{\infty} \frac{\sin x}{x} \, dx.$$

- Show directly that $I$ is a convergent improper Riemann integral.

- Use a contour integral to evaluate $I$.
:::

::: solution
The improper integral exists and equals $\boxed{\pi}$.

<1>1. The integral converges as an ordinary improper Riemann integral.

::: proof
The quotient $\sin x/x$ extends continuously across zero
with value one. For $B>A>0$, integration by parts gives
$$
\int_A^B\frac{\sin x}{x}\,dx
=\left[-\frac{\cos x}{x}\right]_A^B
-\int_A^B\frac{\cos x}{x^2}\,dx.
$$
Consequently the absolute value of this tail is at most
$$
\frac1A+\frac1B+\int_A^B\frac{dx}{x^2}=\frac2A.
$$
The Cauchy criterion proves convergence at positive infinity.
Evenness gives convergence at negative infinity separately.
Thus $I=2\int_0^\infty\sin x/x\,dx$ is an improper
integral, not merely a symmetric principal value.
:::

<1>2. An indented upper semicircle evaluates the half-line integral.

::: proof
For $0<\varepsilon<R$, integrate $F(z)=e^{iz}/z$ over
$[-R,-\varepsilon]$, the clockwise upper semicircle
$\gamma_\varepsilon$ from $-\varepsilon$ to $\varepsilon$,
$[\varepsilon,R]$, and the counterclockwise upper semicircle
$\Gamma_R$ from $R$ to $-R$. The enclosed upper half-annulus
contains no pole, so Cauchy's theorem gives total integral
zero [@SS03]. The real-segment contribution is
$$
\int_{-R}^{-\varepsilon}\frac{e^{ix}}x\,dx
+\int_\varepsilon^R\frac{e^{ix}}x\,dx
=2i\int_\varepsilon^R\frac{\sin x}x\,dx.
$$
Parametrizing the small arc by $z=\varepsilon e^{it}$,
with $t$ decreasing from $\pi$ to zero, gives
$$
\int_{\gamma_\varepsilon}F(z)\,dz
=i\int_\pi^0e^{i\varepsilon e^{it}}\,dt
\longrightarrow-i\pi,
$$
since the integrand tends uniformly to one.

For the large arc, the same parametrization with $R$
gives
$$
\left|\int_{\Gamma_R}F(z)\,dz\right|
\leq\int_0^\pi e^{-R\sin t}\,dt
\leq2\int_0^{\pi/2}e^{-2Rt/\pi}\,dt
\leq\frac\pi R\longrightarrow0.
$$
Here symmetry reduces the estimate to $[0,\pi/2]$, and
concavity of sine on that interval gives $\sin t\geq2t/\pi$.
Passing to the limits in the contour identity, using
step <1>1 for the real integral, yields
$$
2i\int_0^\infty\frac{\sin x}x\,dx-i\pi=0.
$$
The half-line value is $\pi/2$, and evenness gives $I=\pi$.
:::
:::
