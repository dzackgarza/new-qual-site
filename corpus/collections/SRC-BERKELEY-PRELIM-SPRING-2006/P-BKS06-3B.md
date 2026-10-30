---
schema: qual/card@1
id: P-BKS06-3B
kind: problem
title: Evaluate $\int_{-\infty}^{\infty}\frac{e^{itx}}{e^x+e^{-x}}\,dx$ by a rectangular contour
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Evaluate the integral
$$
\int_{-\infty}^{\infty} \frac{e^{itx}}{e^{x} + e^{-x}}\, dx
$$
for $t > 0$.
:::

::: {.solution}

The answer is $\dfrac{\pi}{e^{\pi t/2}+e^{-\pi t/2}}$.

::: pf

::: {.pf-step #s1}

Let $g(z)=\dfrac{e^{itz}}{e^z+e^{-z}}$ and $I=\int_{-\infty}^\infty g(x)\,dx$. The integral converges absolutely.

::: pf-proof

For real $x$, $\abs{g(x)}=1/(e^x+e^{-x})\le e^{-\abs{x}}$.

:::

:::

::: {.pf-step #s2}

Let $C_R$ be the boundary of the rectangle with vertices $\pm R$ and $\pm R+\pi i$, oriented counterclockwise. Then $\oint_{C_R}g(z)\,dz=\pi e^{-\pi t/2}$.

::: pf-proof

The zeros of $e^z+e^{-z}=e^{-z}(e^{2z}+1)$ are the points $z=\frac{\pi i}2+k\pi i$, $k\in\ZZ$. Only $\frac{\pi i}2$ lies inside the rectangle. The zero is simple, and
$$
\operatorname{Res}_{z=\pi i/2}g=\frac{e^{it\cdot\pi i/2}}{e^{\pi i/2}-e^{-\pi i/2}}=\frac{e^{-\pi t/2}}{2i}.
$$
The residue theorem gives $2\pi i\cdot\frac{e^{-\pi t/2}}{2i}=\pi e^{-\pi t/2}$.

:::

:::

::: {.pf-step #s3}

The integrals over the vertical sides of $C_R$ tend to $0$ as $R\to\infty$.

::: pf-proof

For $z=\pm R+iy$ with $0\le y\le\pi$, $\abs{e^{itz}}=e^{-ty}\le1$ and $\abs{e^z+e^{-z}}\ge e^R-e^{-R}$. So each vertical integral is at most $\pi/(e^R-e^{-R})$.

:::

:::

::: {.pf-step #s4}

The integral over the top side, from $R+\pi i$ to $-R+\pi i$, equals $e^{-\pi t}\int_{-R}^Rg(x)\,dx$.

::: pf-proof

For $z=x+\pi i$, $e^{itz}=e^{-\pi t}e^{itx}$ and $e^z+e^{-z}=-(e^x+e^{-x})$. So the integral is $\int_R^{-R}\frac{e^{-\pi t}e^{itx}}{-(e^x+e^{-x})}\,dx=e^{-\pi t}\int_{-R}^Rg(x)\,dx$.

:::

:::

::: pf-qed

Letting $R\to\infty$ and using steps [](#s1){.pf-ref} to [](#s4){.pf-ref}, $(1+e^{-\pi t})I=\pi e^{-\pi t/2}$. Hence
$$
I=\frac{\pi e^{-\pi t/2}}{1+e^{-\pi t}}=\frac{\pi}{e^{\pi t/2}+e^{-\pi t/2}}.
$$

:::

:::

:::
