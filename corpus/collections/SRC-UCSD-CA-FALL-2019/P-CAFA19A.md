---
schema: qual/card@1
id: P-CAFA19A
kind: problem
title: '$\int_0^\infty x^2/(x^4+5x^2+4)\,dx$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Compute the integral $\int_0^{\infty} \frac{x^2}{x^4 + 5x^2 + 4}\,dx$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own computation follows, with the estimates, the two residues and the doubling as separate steps.

::: pf

::: {.pf-step #estimates}
For $F(z)=\dfrac{z^{2}}{(z^{2}+1)(z^{2}+4)}$ the integral of $F$ over the semicircular arc of radius $R$ tends to $0$ as $R\to\infty$.

::: pf-proof
For $\abs{z}=R\ge2$ one has $\abs{z^{2}+1}\ge R^{2}-1$ and $\abs{z^{2}+4}\ge R^{2}-4\ge R^{2}/2$, so $\abs{F(z)}\le\dfrac{R^{2}}{(R^{2}-1)R^{2}/2}\to0$; the arc has length $\pi R$, hence the arc integral is at most $\pi R\cdot\abs{F}$ on the arc, which tends to $0$.
:::

:::

::: {.pf-step #residues}
The poles in the upper half-plane are $i$ and $2i$, with residues $\dfrac{i}{6}$ and $-\dfrac{i}{3}$.

::: pf-proof
$z^{4}+5z^{2}+4=(z^{2}+1)(z^{2}+4)=(z-i)(z+i)(z-2i)(z+2i)$, so the poles are simple and exactly $i,2i$ have positive imaginary part. At $z=i$, $\operatorname{Res}F=\dfrac{i^{2}}{(i+i)(i^{2}+4)}=\dfrac{-1}{(2i)(3)}$; since $\dfrac{1}{i}=-i$ this is $\dfrac{i}{6}$. At $z=2i$, $\operatorname{Res}F=\dfrac{(2i)^{2}}{((2i)^{2}+1)(2i+2i)}=\dfrac{-4}{(-3)(4i)}=\dfrac{1}{3i}=-\dfrac{i}{3}$.
:::

:::

::: {.pf-step #whole-line}
$\displaystyle\int_{-\infty}^{\infty}\frac{x^{2}}{x^{4}+5x^{2}+4}\,dx=\frac{\pi}{3}$.

::: pf-proof
The residue theorem applied to the closed contour (segment $[-R,R]$ followed by the upper semicircle) gives $\int F=2\pi i\sum\operatorname{Res}=2\pi i\Big(\dfrac{i}{6}-\dfrac{i}{3}\Big)=2\pi i\cdot\Big(-\dfrac{i}{6}\Big)=\dfrac{\pi}{3}$ for every $R>2$; the arc contributes nothing in the limit by step [](#estimates){.pf-ref}, and $F$ is real on the real axis.
:::

:::

::: {.pf-qed}
The integrand is even, so $\displaystyle\int_{0}^{\infty}\frac{x^{2}}{x^{4}+5x^{2}+4}\,dx=\frac12\cdot\frac{\pi}{3}=\frac{\pi}{6}$.
:::

:::

:::
