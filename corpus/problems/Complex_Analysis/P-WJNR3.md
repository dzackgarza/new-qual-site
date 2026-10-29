---
schema: qual/card@1
id: P-WJNR3
kind: problem
title: $\int_0^\infty\frac{\sin^3 x}{x^3}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
---

::: {.problem}
Calculate
$$
\int_0^\infty {\sin^3(x) \over x^3} \, dx.
$$
:::

::: {.solution}
Let $I=\int_0^\infty\frac{\sin^3x}{x^3}\,dx$.

::: pf

::: {.pf-step #parts}

$I=\dfrac38\displaystyle\int_0^\infty\frac{\cos x-\cos3x}{x^2}\,dx$.

::: pf-proof

Integrating by parts with $dv=x^{-3}\,dx$,
$$
I=\qty[-\frac{\sin^3 x}{2x^2}]_0^\infty + \frac32\int_0^\infty\frac{\sin^2x\cos x}{x^2}\,dx,
$$
and the boundary term vanishes at both ends since $\sin^3 x/x^2 \to 0$ as $x \to 0$ and as $x \to \infty$. The identity $4\sin^2x\cos x = 2(1-\cos 2x)\cos x = \cos x-\cos3x$ finishes the step.

:::

:::

::: {.pf-step #frullani}

For $0<a<b$, $\displaystyle\int_0^\infty\frac{\cos(ax)-\cos(bx)}{x^2}\,dx = \frac\pi2(b-a)$.

::: pf-proof

Integrating by parts, the boundary term $\qty[-\frac{\cos(ax)-\cos(bx)}{x}]_0^\infty$ vanishes because $\cos(ax)-\cos(bx) = \bigo(x^2)$ at $0$, and
$$
\int_0^\infty\frac{\cos(ax)-\cos(bx)}{x^2}\,dx
=\int_0^\infty\frac{b\sin(bx)-a\sin(ax)}x\,dx
=\frac\pi2(b-a)
$$
by the Dirichlet integral $\int_0^\infty \frac{\sin(cx)}{x}\,dx = \frac{\pi}{2}$ for $c > 0$.

:::

:::

::: pf-step

$I=\boxed{\dfrac{3\pi}{8}}$.

::: pf-proof

Step [](#frullani){.pf-ref} with $a=1$ and $b=3$ gives $\int_0^\infty\frac{\cos x-\cos3x}{x^2}\,dx=\pi$; substitute into step [](#parts){.pf-ref}.

:::

:::

:::

:::
