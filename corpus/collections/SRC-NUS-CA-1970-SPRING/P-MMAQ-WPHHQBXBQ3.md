---
schema: qual/card@1
id: P-MMAQ-WPHHQBXBQ3
kind: problem
title: $\int_0^\infty\frac{x^2}{(x^2+1)(x^2+4)}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Integrals
  - Residues
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Evaluate the improper integral

$$
\int_0^\infty \frac{x^2\,dx}{(x^2+1)(x^2+4)}.
$$
:::

::: {.solution}
Let $f(z)\coloneqq\frac{z^2}{(z^2+1)(z^2+4)}$, and for $R>2$ let $C_R$ be the arc $\theset{Re^{i\theta}\st 0\le\theta\le\pi}$.

::: pf

::: {.pf-step #half-line}

$\displaystyle\int_0^\infty \frac{x^2\,dx}{(x^2+1)(x^2+4)}=\frac12\int_{-\infty}^\infty f(x)\,dx$.

::: pf-proof

The integrand is even, and it is $O(x^{-2})$ at $\pm\infty$, so both integrals converge absolutely.

:::

:::

::: {.pf-step #residues}

For $R>2$, $\displaystyle\int_{-R}^R f(x)\,dx+\int_{C_R}f(z)\,dz=\frac{\pi}{3}$.

::: pf-proof

The poles of $f$ are the simple poles $\pm i$ and $\pm 2i$, and the upper half-disc of radius $R$ contains $i$ and $2i$.
At a simple pole $z_0$, $\Res_{z=z_0}f=\lim_{z\to z_0}(z-z_0)f(z)$, so
$$
\Res_{z=i}f=\frac{i^2}{2i\,(i^2+4)}=\frac{-1}{6i}=\frac{i}{6},
\qquad
\Res_{z=2i}f=\frac{(2i)^2}{((2i)^2+1)\,4i}=\frac{-4}{-12i}=-\frac{i}{3}.
$$
By the residue theorem the contour integral is $2\pi i\qty(\frac i6-\frac i3)=2\pi i\cdot\qty(-\frac i6)=\frac\pi3$.

:::

:::

::: {.pf-step #arc}

$\displaystyle\lim_{R\to\infty}\int_{C_R}f(z)\,dz=0$.

::: pf-proof

For $\abs z=R>2$ the reverse triangle inequality gives $\abs{z^2+1}\ge R^2-1$ and $\abs{z^2+4}\ge R^2-4$, so $\abs{f(z)}\le\frac{R^2}{(R^2-1)(R^2-4)}$.
Since $C_R$ has length $\pi R$,
$$
\abs{\int_{C_R}f(z)\,dz}\le\frac{\pi R^3}{(R^2-1)(R^2-4)}\longrightarrow0\qquad(R\to\infty).
$$

:::

:::

::: pf-step

$\displaystyle\int_0^\infty \frac{x^2\,dx}{(x^2+1)(x^2+4)}=\boxed{\frac{\pi}{6}}$.

::: pf-proof

Letting $R\to\infty$ in step [](#residues){.pf-ref} and using step [](#arc){.pf-ref} gives $\int_{-\infty}^\infty f(x)\,dx=\frac\pi3$.
Step [](#half-line){.pf-ref} halves this.

:::

:::

:::

:::
