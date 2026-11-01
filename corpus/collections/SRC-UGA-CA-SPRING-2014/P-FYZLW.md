---
schema: qual/card@1
id: P-FYZLW
kind: problem
title: The Dirichlet integral $\int_{-\infty}^{\infty}\frac{\sin x}{x}\,dx$ by complex methods
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UGA-CA-SPRING-2014`; it is the standard
    evaluation and no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved by integrating $e^{iz}/z$ over the upper half-disc with an indentation at the origin: the
    contour integral vanishes, the large arc contributes $O(1/R)$ since
    $\int_0^\pi e^{-R\sin\theta}d\theta\le\pi/R$, and the indentation contributes $-i\pi$. Taking
    imaginary parts gives $\int_\RR \sin x/x\,dx=\pi$. Nothing is left in outline.
---

::: {.problem}
Use methods of complex variables to evaluate the integral
$$
\int_{-\infty}^{\infty}\frac{\sin x}{x}\,dx.
$$
:::

::: {.solution}

We show that the principal value $\mathrm{PV}\int_{\RR}\frac{e^{ix}}{x}\,dx=i\pi$, and then take imaginary parts; since $\frac{\sin x}{x}$ is continuous at the origin and its improper integral converges, the principal value of $\int_\RR\frac{\sin x}{x}dx$ is that improper integral.

::: pf

::: {.pf-step #s1}

For $0<\varepsilon<R$ let $C_{\varepsilon,R}$ be the closed contour consisting of $[-R,-\varepsilon]$, the clockwise semicircle $\gamma_\varepsilon$ in the upper half-plane from $-\varepsilon$ to $\varepsilon$, the segment $[\varepsilon,R]$, and the counterclockwise semicircle $\Gamma_R$ of radius $R$ from $R$ to $-R$. Then $\int_{C_{\varepsilon,R}}\frac{e^{iz}}{z}\,dz=0$.

::: pf-proof

The function $z\mapsto e^{iz}/z$ is holomorphic on the simply connected open set obtained by deleting the origin, and $C_{\varepsilon,R}$ bounds a region not containing $0$; by Cauchy's theorem the integral over the closed contour vanishes.

:::

:::

::: {.pf-step #s2}

$\displaystyle\Bigl|\int_{\Gamma_R}\frac{e^{iz}}{z}\,dz\Bigr|\le\frac{\pi}{R}\bigl(1-e^{-R}\bigr)\to0$ as $R\to\infty$.

::: pf-proof

On $\Gamma_R$ write $z=Re^{i\theta}$, $0\le\theta\le\pi$, so $dz/z=i\,d\theta$ and $\abs{e^{iz}}=e^{-R\sin\theta}$. Hence
$$
\Bigl|\int_{\Gamma_R}\frac{e^{iz}}{z}dz\Bigr|\le\int_0^{\pi}e^{-R\sin\theta}d\theta=2\int_0^{\pi/2}e^{-R\sin\theta}d\theta\le2\int_0^{\pi/2}e^{-2R\theta/\pi}d\theta=\frac{\pi}{R}\bigl(1-e^{-R}\bigr),
$$
using $\sin\theta\ge2\theta/\pi$ on $[0,\pi/2]$ and the symmetry $\sin(\pi-\theta)=\sin\theta$.

:::

:::

::: {.pf-step #s3}

$\displaystyle\int_{\gamma_\varepsilon}\frac{e^{iz}}{z}\,dz\to-i\pi$ as $\varepsilon\to0$.

::: pf-proof

On $\gamma_\varepsilon$ the function $e^{iz}$ is bounded and $e^{iz}=1+O(\varepsilon)$. Hence
$$
\int_{\gamma_\varepsilon}\frac{e^{iz}}{z}dz=\int_{\gamma_\varepsilon}\frac{dz}{z}+O(\varepsilon).
$$
The first integral is the change of $\log z$ along the clockwise semicircle from $-\varepsilon$ to $\varepsilon$ through the upper half-plane, that is $-\pi i$ (the argument drops by $\pi$); the second is $O(\varepsilon)$ since the length of $\gamma_\varepsilon$ is $\pi\varepsilon$ and the integrand of the remainder is $O(1)$. So the limit is $-\pi i$.

:::

:::

::: {.pf-step #s4}

$\displaystyle\mathrm{PV}\int_{\RR}\frac{e^{ix}}{x}\,dx=i\pi$, and consequently $\displaystyle\int_{\RR}\frac{\sin x}{x}\,dx=\pi$.

::: pf-proof

Combining steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} and letting $\varepsilon\to0$, $R\to\infty$,
$$
0=\mathrm{PV}\int_{\RR}\frac{e^{ix}}{x}dx-i\pi,
\qquad\text{so}\qquad
\mathrm{PV}\int_{\RR}\frac{e^{ix}}{x}dx=i\pi .
$$
Equating real and imaginary parts,
$$
\mathrm{PV}\int_{\RR}\frac{\cos x}{x}dx=0,\qquad
\mathrm{PV}\int_{\RR}\frac{\sin x}{x}dx=\pi .
$$
The function $x\mapsto\sin x/x$ extends continuously to $x=0$ with value $1$, and $\int_0^\infty\frac{\sin x}{x}dx$ converges (Dirichlet's test, since $\int_0^X\sin x\,dx$ is bounded and $1/x$ decreases to $0$); hence the principal value coincides with the improper integral, and the integrand is even, so
$$
\int_{-\infty}^{\infty}\frac{\sin x}{x}dx=\pi .
$$

:::

:::

:::

:::
