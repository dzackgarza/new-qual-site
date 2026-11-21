---
schema: qual/card@1
id: E-SS2.EX-2
kind: problem
title: $\int_0^\infty\frac{\sin x}{x}\,dx=\frac\pi2$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the removable singularity, the contour identity, the
    semicircle estimate, and the passage to the improper integral with the odd and even parts split. No
    retained solution set covers this exercise (the collection retains the textbook, not a solutions manual),
    so the argument is the card's own; each estimate was re-read for this pass.
---

::: {.exercise}
Show that $\displaystyle\int_0^\infty \frac{\sin x}{x}\,dx = \frac{\pi}{2}$.

[Hint: The integral equals $\displaystyle\frac{1}{2i}\int_{-\infty}^{\infty} \frac{e^{ix}-1}{x}\,dx$. Use the indented semicircle.]
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. The device is the hint's: write the integral as $\frac{1}{2i}\int_{-\infty}^{\infty}\frac{e^{ix}-1}{x}dx$ and integrate over the indented semicircle.

::: pf

::: {.pf-step #removable}
$F(z)=\dfrac{e^{iz}-1}{z}$ has a removable singularity at $0$, with limit $i$ there.

::: pf-proof
$e^{iz}=1+iz+O(z^{2})$ near $0$, so $F(z)=i+O(z)$ and $F$ extends by $F(0)=i$ to an entire function. The extension is what is integrated below.
:::

:::

::: {.pf-step #contour}
For $R>0$ and $C_{R}$ the positively oriented upper semicircle, $\int_{-R}^{R}\frac{e^{ix}-1}{x}dx+\int_{C_{R}}F(z)\,dz=0$.

::: pf-proof
$F$ is entire, so by Cauchy's theorem its integral over the boundary of the upper half-disc of radius $R$, taken counterclockwise, vanishes; that boundary is the segment from $-R$ to $R$ followed by the semicircle from $R$ to $-R$. The segment contributes $\int_{-R}^{R}\frac{e^{ix}-1}{x}dx$ and the arc contributes the second term.
:::

:::

::: {.pf-step #arc}
$\int_{C_{R}}F(z)\,dz\to i\pi$ as $R\to\infty$.

::: pf-proof
On the arc $z=Re^{i\theta}$, $0\le\theta\le\pi$, one has $dz/z=i\,d\theta$, so $\int_{C_{R}}\frac{dz}{z}=i\pi$ exactly. For the other piece, $\abs{\int_{C_{R}}\frac{e^{iz}}{z}dz}\le\int_{0}^{\pi}\abs{e^{iRe^{i\theta}}}d\theta=\int_{0}^{\pi}e^{-R\sin\theta}d\theta$; using $\sin\theta\ge2\theta/\pi$ on $[0,\pi/2]$ and the symmetry of sine about $\pi/2$, this is at most $2\int_{0}^{\pi/2}e^{-2R\theta/\pi}d\theta=\frac{\pi}{R}(1-e^{-R})\le\frac{\pi}{R}$, which tends to $0$. Hence the arc integral tends to $i\pi$.
:::

:::

::: {.pf-step}
$\int_{0}^{\infty}\dfrac{\sin x}{x}dx=\dfrac{\pi}{2}$.

::: pf-proof
Steps [](#contour){.pf-ref} and [](#arc){.pf-ref} give $\lim_{R\to\infty}\int_{-R}^{R}\frac{e^{ix}-1}{x}dx=i\pi$. On the segment, $\frac{\cos x-1}{x}$ is odd and $\frac{\sin x}{x}$ is even, so
$$
\int_{-R}^{R}\frac{e^{ix}-1}{x}dx=\int_{-R}^{R}\frac{\cos x-1}{x}dx+i\int_{-R}^{R}\frac{\sin x}{x}dx=0+2i\int_{0}^{R}\frac{\sin x}{x}dx .
$$
Hence $2i\int_{0}^{\infty}\frac{\sin x}{x}dx=i\pi$ and dividing by $2i$ gives the value $\frac{\pi}{2}$.
:::

:::

:::
:::
