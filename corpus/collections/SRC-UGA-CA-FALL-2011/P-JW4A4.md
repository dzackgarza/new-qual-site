---
schema: qual/card@1
id: P-JW4A4
kind: problem
title: $\int_0^\infty\frac{\sqrt{x}}{(x+1)^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, and the vanishing of the two circular integrals supplied. The prose said "the circular arcs vanish" without a bound; the card now gives both ML estimates (R^{1/2}/(R-1)^2 on the large circle and r^{1/2}/(1-r)^2 on the small one, multiplied by 2 pi times the radius). It also states the branch of the square root, checks that -1 lies in the cut plane, computes the residue as the derivative of z^{1/2} at -1 with (-1)^{1/2} = i on that branch, and adds an independent check of the value by the substitution x = t^2 (which gives 2 · pi/4 = pi/2). The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; I = pi/2 is correct.
---

::: {.problem}
Calculate
$$
\int_0^\infty {\sqrt x \over (x+1)^2} \,dx
.$$

:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Write $I=\int_0^\infty\frac{\sqrt x}{(1+x)^2}dx$.

::: pf

::: {.pf-step #branch}
$F(z)=\dfrac{z^{1/2}}{(1+z)^2}$ is holomorphic off $[0,\infty)\cup\{-1\}$ for the branch $z^{1/2}=e^{\frac12(\log\abs{z}+i\arg z)}$ with $0<\arg z<2\pi$.

::: pf-proof
On the plane cut along the positive real axis the argument $\arg z\in(0,2\pi)$ is a continuous branch, so $z^{1/2}$ is holomorphic there; $(1+z)^{-2}$ is holomorphic off $-1$, which lies on the negative axis and hence in the cut plane. So $F$ is holomorphic off $[0,\infty)\cup\{-1\}$, and $-1$ is a pole of order $2$.
:::

:::

::: {.pf-step #banks}
On the upper bank $z^{1/2}=\sqrt x$ and on the lower bank $z^{1/2}=-\sqrt x$, so the two banks contribute $2I$ in the limit.

::: pf-proof
For $x>0$ approached from above, $\arg z\to0^+$ and $z^{1/2}\to\sqrt x$. Approached from below, $\arg z\to2\pi^-$ and $z^{1/2}\to e^{i\pi}\sqrt x=-\sqrt x$. The keyhole contour traverses the upper bank from $0$ to $\infty$ and the lower bank from $\infty$ to $0$; reversing the latter,
$$
\int_{\text{upper}}+\int_{\text{lower}}\longrightarrow\int_0^\infty\frac{\sqrt x}{(1+x)^2}dx-\int_0^\infty\frac{-\sqrt x}{(1+x)^2}dx=2I .
$$
:::

:::

::: {.pf-step #arcs}
The integrals over the large and small circles tend to $0$.

::: pf-proof
On $\abs{z}=R$ with $R>2$, $\abs{F(z)}\le R^{1/2}/(R-1)^2$, so the integral over the circle is at most $2\pi R\cdot R^{1/2}/(R-1)^2\to0$ as $R\to\infty$. On $\abs{z}=r$ with $r<\frac12$, $\abs{F(z)}\le r^{1/2}/(1-r)^2$, so the integral is at most $2\pi r\cdot r^{1/2}/(1-r)^2\to0$ as $r\to0$.
:::

:::

::: {.pf-step #residue}
$\operatorname{Res}_{z=-1}F=-\dfrac i2$.

::: pf-proof
With $\arg(-1)=\pi$ on the branch, $(-1)^{1/2}=e^{i\pi/2}=i$. Since $-1$ is a double pole and $z\mapsto z^{1/2}$ is holomorphic near $-1$,
$$
\operatorname{Res}_{z=-1}\frac{z^{1/2}}{(1+z)^2}=\evaluated{\frac{d}{dz}z^{1/2}}_{z=-1}=\frac12(-1)^{-1/2}=\frac{1}{2i}=-\frac i2 .
$$
:::

:::

::: {.pf-step}
$I=\dfrac\pi2$.

::: pf-proof
The contour encloses only the pole at $-1$, so by the residue theorem the contour integral equals $2\pi i\cdot(-\frac i2)=\pi$. By steps [](#banks){.pf-ref} and [](#arcs){.pf-ref} it also tends to $2I$. Hence $2I=\pi$ and $I=\frac\pi2$. As a check, the substitution $x=t^2$ gives $I=2\int_0^\infty\frac{t^2}{(1+t^2)^2}dt$, and $\int_0^\infty\frac{t^2}{(1+t^2)^2}dt=\frac{\pi}{4}$, so $I=\frac{\pi}{2}$.
:::

:::

:::
:::
