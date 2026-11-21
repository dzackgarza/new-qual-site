---
schema: qual/card@1
id: E-SS2.EX-3
kind: problem
title: Laplace transforms of $\cos bx$ and $\sin bx$ by a sector contour
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
    Structured the contour computation into numbered steps and supplied the estimates it used: that
    the sector is a closed contour on which e^{-Az} is entire so the integral vanishes, that on the
    arc Re(Az) = AR cos t >= AR cos omega = aR, which gives the bound R omega e^{-aR} -> 0, and
    that the radial integrals convert to the half-line integrals by the substitution z = e^{-i
    omega} x. Also recorded why both integrals converge absolutely for a > 0, which is what lets the
    limit R -> infinity be taken. Not checked this session: the printed statement page.

---

::: {.exercise}
Evaluate the integrals
$$
\int_0^{\infty} e^{-ax} \cos bx\, dx \quad \text{and} \quad \int_0^{\infty} e^{-ax} \sin bx\, dx, \quad a > 0
$$
by integrating $e^{-Az}$, $A = \sqrt{a^2 + b^2}$, over an appropriate sector with angle $\omega$, with $\cos\omega = a/A$.
:::

::: {.solution}

The computation is the card's own; the statement is the exercise stored on the card, and no source text or solution set is retained for it.

Let $A=\sqrt{a^{2}+b^{2}}>0$ and choose $\omega$ with $\cos\omega=a/A$ and $\sin\omega=b/A$, so $\abs{\omega}<\pi/2$ because $a>0$.

::: pf

::: {.pf-step #geometry}
$Ae^{-i\omega}=a-ib$, and the rays $\arg z=0$ and $\arg z=-\omega$ together with the circle $\abs{z}=R$ bound a closed sector.

::: pf-proof
$Ae^{-i\omega}=A\cos\omega-iA\sin\omega=a-ib$ by the choice of $\omega$. The sector with vertices at the origin, sides along the two rays and outer arc of radius $R$ is a closed contour: it is the image of the rectangle $\{0\leq r\leq R,\ -\omega\leq t\leq0\}$ under the continuous map $(r,t)\mapsto re^{it}$ restricted so that the radial sides are described once each.
:::

:::

::: {.pf-step #convergence}
Both integrals converge absolutely.

::: pf-proof
$\abs{e^{-(a-ib)x}}=e^{-ax}\abs{e^{ibx}}=e^{-ax}$ and $\int_{0}^{\infty}e^{-ax}dx=1/a<\infty$ for $a>0$, so $\int_{0}^{\infty}e^{-(a-ib)x}dx$ converges absolutely, as do its real and imaginary parts.
:::

:::

::: {.pf-step #contour}
$\int_{0}^{R}e^{-Ax}\,dx+\int_{\text{arc}}e^{-Az}\,dz-\int_{0}^{R}e^{-Ae^{-i\omega}x}e^{-i\omega}\,dx=0$.

::: pf-proof
$e^{-Az}$ is entire, so its integral over the closed contour of step [](#geometry){.pf-ref} vanishes by Cauchy's theorem. On the side along the positive axis $z=x$ and $dz=dx$; on the side along the ray $\arg z=-\omega$ we have $z=e^{-i\omega}x$ and $dz=e^{-i\omega}dx$; the third piece is the arc, and the contour is traversed so that the two radial pieces enter with the signs shown.
:::

:::

::: {.pf-step #arc}
$\abs{\int_{\text{arc}}e^{-Az}dz}\leq R\abs{\omega}e^{-aR}\to0$.

::: pf-proof
On the arc $z=Re^{it}$ with $t$ between $0$ and $-\omega$, so $\Re(Az)=AR\cos t\geq AR\cos\omega=aR$ because $\abs{t}\leq\abs{\omega}<\pi/2$ and $\cos$ is even and decreasing on $[0,\pi]$. Hence $\abs{e^{-Az}}\leq e^{-aR}$ there, and the arc has length $R\abs{\omega}$, so the integral is bounded by $R\abs{\omega}e^{-aR}$, which tends to $0$ as $R\to\infty$.
:::

:::

::: {.pf-step #limit}
Letting $R\to\infty$ gives $\frac1A=e^{-i\omega}\int_{0}^{\infty}e^{-(a-ib)x}dx$, hence $\int_{0}^{\infty}e^{-(a-ib)x}dx=\frac{a+ib}{a^{2}+b^{2}}$.

::: pf-proof
$\int_{0}^{R}e^{-Ax}dx=(1-e^{-AR})/A\to1/A$. The arc term tends to $0$ by step [](#arc){.pf-ref} and the remaining integral tends to $\int_{0}^{\infty}e^{-Ae^{-i\omega}x}dx$ by step [](#convergence){.pf-ref} with $Ae^{-i\omega}=a-ib$. Passing to the limit in step [](#contour){.pf-ref} gives $1/A=e^{-i\omega}\int_{0}^{\infty}e^{-(a-ib)x}dx$; multiplying by $e^{i\omega}$ and using $e^{i\omega}=(a+ib)/A$ with $A^{2}=a^{2}+b^{2}$ gives the stated value.
:::

:::

::: {.pf-step #real-imaginary}
The two integrals are $\frac{a}{a^{2}+b^{2}}$ and $\frac{b}{a^{2}+b^{2}}$.

::: pf-proof
$e^{-(a-ib)x}=e^{-ax}(\cos bx+i\sin bx)$, so taking real and imaginary parts of step [](#limit){.pf-ref} gives $\int_{0}^{\infty}e^{-ax}\cos bx\,dx=\frac{a}{a^{2}+b^{2}}$ and $\int_{0}^{\infty}e^{-ax}\sin bx\,dx=\frac{b}{a^{2}+b^{2}}$.
:::

:::

:::

:::
