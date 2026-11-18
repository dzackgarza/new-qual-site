---
schema: qual/card@1
id: P-CAF13B
kind: problem
title: '$\int_{-\infty}^\infty \cos x/(1+x^2)\,dx$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same computation. The two estimates that make the arc vanish are
    separated --- |e^{iz}| = e^{-Im z} <= 1 on the upper semicircle, and |1+z^2| >= R^2 - 1 --- and the arc
    integral is bounded by pi R / (R^2 - 1). The residue is computed from the simple-pole formula at z = i,
    and the last step explains why taking real parts is legitimate: the imaginary part is the integral of
    an odd function. No published solution located; the card keeps its own computation and says so.
---

::: {.problem}
Use residues to calculate $\int_{-\infty}^{\infty} \frac{\cos x}{1 + x^2}\,dx$.
:::

::: {.solution}

No published solution was located for this examination problem; the computation is the card's own and is the standard semicircle with a residue at $z=i$.

The statement was checked against the Fall 2013 complex-analysis examination collection holding this card. Throughout $F(z)\coloneqq e^{iz}/(1+z^{2})$, and for $R>1$ the contour $\gamma_{R}$ is the interval $[-R,R]$ followed by the upper semicircle $\abs{z}=R$, $\operatorname{Im}z\geq0$; the poles of $F$ are $\pm i$, and only $i$ lies inside $\gamma_{R}$.

::: pf

::: {.pf-step #arc}

$\abs{\int_{\text{arc}}F(z)\,dz}\leq\frac{\pi R}{R^{2}-1}\to0$.

::: pf-proof

On the upper semicircle, $z=Re^{i\theta}$ with $\theta\in[0,\pi]$, so $\operatorname{Im}z=R\sin\theta\geq0$ and $\abs{e^{iz}}=e^{-\operatorname{Im}z}\leq1$; and $\abs{1+z^{2}}\geq\abs{z}^{2}-1=R^{2}-1$. Hence $\abs{F}\leq1/(R^{2}-1)$ on the arc, and the arc has length $\pi R$, so the estimate follows; it tends to $0$ as $R\to\infty$.

:::

:::

::: {.pf-step #residue}

$\operatorname{Res}(F,i)=\frac{e^{-1}}{2i}$.

::: pf-proof

$F=e^{iz}/\big((z-i)(z+i)\big)$ has a simple pole at $z=i$, and the residue there is $\lim_{z\to i}(z-i)F(z)=e^{i\cdot i}/(2i)=e^{-1}/(2i)$, using $i^{2}=-1$.

:::

:::

::: {.pf-step #value}

$\int_{-\infty}^{\infty}\frac{e^{ix}}{1+x^{2}}\,dx=\frac{\pi}{e}$.

::: pf-proof

For $R>1$ the only pole of $F$ inside $\gamma_{R}$ is $i$, so the residue theorem gives $\int_{\gamma_{R}}F=2\pi i\operatorname{Res}(F,i)=2\pi i\cdot\frac{e^{-1}}{2i}=\frac{\pi}{e}$. The arc contributes $\int_{\text{arc}}F$, which tends to $0$ by step [](#arc){.pf-ref}; hence
$$
\int_{-R}^{R}\frac{e^{ix}}{1+x^{2}}\,dx=\frac{\pi}{e}-\int_{\text{arc}}F\longrightarrow\frac{\pi}{e}\qquad(R\to\infty).
$$

:::

:::

::: pf-step

$\int_{-\infty}^{\infty}\frac{\cos x}{1+x^{2}}\,dx=\frac{\pi}{e}$.

::: pf-proof

The function $x\mapsto e^{ix}/(1+x^{2})$ has real part $\cos x/(1+x^{2})$ and imaginary part $\sin x/(1+x^{2})$; the second is odd and continuous, so its integral over $\RR$ is $0$, and the improper integral of the first converges absolutely because $\abs{\cos x/(1+x^{2})}\leq1/(1+x^{2})$. Since the integral of $e^{ix}/(1+x^{2})$ is the real number $\pi/e$ by step [](#value){.pf-ref}, its real part, which is the integral of $\cos x/(1+x^{2})$, is $\pi/e$.

:::

:::

:::

:::
