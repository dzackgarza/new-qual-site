---
schema: qual/card@1
id: P-CAF05E
kind: problem
title: "Evaluation of the sinc integral via residue calculus"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Use the method of residues to compute the integral $\int_0^{\infty} \frac{\sin x}{x}\,dx$.
Justify all your steps.

Hint: Integrate the function $\frac{e^{iz}}{z}$ on an appropriate closed curve.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own indented-contour computation follows, with the two circular estimates and the two real intervals as separate steps.

::: pf

::: {.pf-step #contour}
For $0<\varepsilon<R$ let $\Gamma$ be the positively oriented boundary of the upper half-disc of radius $R$ with the upper half-disc of radius $\varepsilon$ about $0$ removed. Then $\oint_{\Gamma}\frac{e^{iz}}{z}dz=0$.

::: pf-proof
$F(z)=e^{iz}/z$ is holomorphic on the region enclosed by $\Gamma$, which does not contain $z=0$; by Cauchy's theorem the integral over its boundary vanishes.
:::

:::

::: {.pf-step #real-axis}
The two real intervals contribute $2i\displaystyle\int_{\varepsilon}^{R}\frac{\sin t}{t}dt$.

::: pf-proof
$\int_{\varepsilon}^{R}\frac{e^{ix}}{x}dx+\int_{-R}^{-\varepsilon}\frac{e^{ix}}{x}dx$; substituting $x=-t$ in the second gives $-\int_{\varepsilon}^{R}\frac{e^{-it}}{t}dt$, so the sum is $\int_{\varepsilon}^{R}\frac{e^{it}-e^{-it}}{t}dt=2i\int_{\varepsilon}^{R}\frac{\sin t}{t}dt$.
:::

:::

::: {.pf-step #large-arc}
The integral over the large semicircle tends to $0$ as $R\to\infty$.

::: pf-proof
On $\abs{z}=R$ the modulus of the integrand is $e^{-R\sin\theta}/R\le1/R$ away from the axis, and Jordan's lemma or the direct estimate $\abs{\int}\le\int_{0}^{\pi}e^{-R\sin\theta}d\theta\le\int_{0}^{\pi}e^{-2R\theta/\pi}d\theta=\frac{\pi}{2R}(1-e^{-2R})$ gives the result.
:::

:::

::: {.pf-step #small-arc}
The integral over the small semicircle, traversed clockwise, tends to $-i\pi$ as $\varepsilon\to0$.

::: pf-proof
Parametrise $z=\varepsilon e^{i\theta}$ with $\theta$ decreasing from $\pi$ to $0$. Then $\int=i\int_{\pi}^{0}e^{i\varepsilon e^{i\theta}}d\theta$, and $e^{i\varepsilon e^{i\theta}}\to1$ uniformly in $\theta$, so the integral tends to $i(0-\pi)=-i\pi$ — half the residue $2\pi i\cdot1$, with the sign from the clockwise orientation.
:::

:::

::: {.pf-qed}
Taking $R\to\infty$ and $\varepsilon\to0$ in step [](#contour){.pf-ref}: $0=2i\int_{0}^{\infty}\frac{\sin t}{t}dt-i\pi$, so $\int_{0}^{\infty}\frac{\sin x}{x}dx=\frac{\pi}{2}$, using steps [](#real-axis){.pf-ref}, [](#large-arc){.pf-ref} and [](#small-arc){.pf-ref}.
:::

:::

:::
