---
schema: qual/card@1
id: P-CAFA15D
kind: problem
title: '$\int_0^\infty \cos x/(x^6+1)\,dx$ by residues'
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
    Restructured the prose solution into a Lamport proof and filled the step it skipped:
    the prose went from 2 pi i times the residue sum straight to the boxed real expression.
    The three residues are now computed (zeta_1^5 = e^{5 pi i/6}, zeta_3^5 = e^{25 pi i/6} =
    e^{pi i/6}, i zeta_2 = -1), the imaginary part of the residue sum is reduced with the
    angle-sum formulae to -(e^{-1/2}(cos A + sqrt3 sin A) + e^{-1})/6 for A = sqrt3/2, and
    the real part then gives the boxed value. Also corrected: the prose invoked Jordan's
    lemma, which is not needed and does not apply to a rational decay; the arc integral
    vanishes by the ML estimate with |F| <= 1/(R^6 - 1). The value was checked numerically
    (0.81738313 against a Simpson quadrature giving 0.81738314). The collection's provenance
    is the examination paper only, so no retained solution set covers the exercise and the
    argument is the card's own.
---

::: {.problem}
Evaluate $\int_0^{\infty} \frac{\cos x}{x^6 + 1}\,dx$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Write $F(z)\coloneqq\frac{e^{iz}}{z^6+1}$ and $A\coloneqq\frac{\sqrt3}{2}$.

::: pf

::: {.pf-step #poles}
The poles of $F$ are the six roots of $z^6=-1$, namely $e^{i(2k+1)\pi/6}$; those in the upper half-plane are
$$
\zeta_1=e^{i\pi/6},\qquad \zeta_2=i,\qquad \zeta_3=e^{5i\pi/6},
$$
and each is a simple pole.

::: pf-proof
$z^6+1=0$ means $z^6=-1=e^{i\pi}$, so $z=e^{i(\pi+2\pi k)/6}=e^{i(2k+1)\pi/6}$ for $k=0,\ldots,5$, of which $k=0,1,2$ have imaginary part positive. If $\zeta$ is such a root then $(z^6+1)'=6z^5$ does not vanish at $\zeta$, since $\zeta\ne0$, so the zero is simple and the pole is simple.
:::

:::

::: {.pf-step #residues}
$$
\operatorname{Res}(F,\zeta_j)=\frac{e^{i\zeta_j}}{6\zeta_j^5},
$$
and explicitly
$$
\operatorname{Res}(F,\zeta_1)=\frac{e^{-1/2}}{6}e^{i\left(A-\frac{5\pi}{6}\right)},\qquad
\operatorname{Res}(F,\zeta_2)=-\frac{i}{6e},\qquad
\operatorname{Res}(F,\zeta_3)=\frac{e^{-1/2}}{6}e^{-i\left(A+\frac{\pi}{6}\right)} .
$$

::: pf-proof
At a simple pole $\zeta$ of $e^{iz}/q(z)$ the residue is $e^{i\zeta}/q'(\zeta)=e^{i\zeta}/(6\zeta^5)$. Now $\zeta_1^5=e^{5i\pi/6}$ and $i\zeta_1=i\left(\frac{\sqrt3}{2}+\frac{i}{2}\right)=A-\frac{i}{2}$, so $e^{i\zeta_1}=e^{-1/2}e^{iA}$ and $\operatorname{Res}(F,\zeta_1)=\frac{1}{6}e^{-1/2}e^{iA}e^{-5i\pi/6}$. Next $\zeta_2^5=i^5=i$ and $i\zeta_2=i\cdot i=-1$, so $\operatorname{Res}(F,\zeta_2)=\frac{e^{-1}}{6i}=-\frac{ie^{-1}}{6}$. Finally $\zeta_3^5=e^{25i\pi/6}=e^{i\pi/6}$ because $25\pi/6-4\pi=\pi/6$, and $i\zeta_3=i\left(-\frac{\sqrt3}{2}+\frac{i}{2}\right)=-A-\frac{i}{2}$, so $e^{i\zeta_3}=e^{-1/2}e^{-iA}$ and $\operatorname{Res}(F,\zeta_3)=\frac{1}{6}e^{-1/2}e^{-iA}e^{-i\pi/6}$.
:::

:::

::: {.pf-step #contour}
$\displaystyle\int_{-\infty}^{\infty}\frac{e^{ix}}{x^6+1}\,dx=2\pi i\sum_{j=1}^{3}\operatorname{Res}(F,\zeta_j)$.

::: pf-proof
Integrate $F$ over the boundary of the upper half-disc of radius $R$. The residue theorem gives $2\pi i$ times the sum of the residues of the three enclosed poles. On the semicircular arc $\abs{F(z)}\le1/(\abs{z}^6-1)$ and the arc has length $\pi R$, so the arc integral is at most $\pi R/(R^6-1)\to0$; no Jordan estimate is needed, the decay of $1/(z^6+1)$ alone sufficing. Letting $R\to\infty$ leaves the integral over the real axis.
:::

:::

::: {.pf-step #real-part}
$\displaystyle\int_0^{\infty}\frac{\cos x}{x^6+1}\,dx=-\pi\operatorname{Im}\left(\sum_{j=1}^{3}\operatorname{Res}(F,\zeta_j)\right)$.

::: pf-proof
The integrand $1/(x^6+1)$ is even and real, so the real part of the integral of step [](#contour){.pf-ref} is $2\int_0^\infty\frac{\cos x}{x^6+1}dx$. Writing $2\pi iS$ for the right side of step [](#contour){.pf-ref} with $S$ the residue sum, $\operatorname{Re}(2\pi iS)=-2\pi\operatorname{Im}S$; halving gives the claim.
:::

:::

::: {.pf-step #imaginary-part}
$$
\operatorname{Im}S=-\frac16\left[e^{-1/2}\left(\cos A+\sqrt3\sin A\right)+e^{-1}\right].
$$

::: pf-proof
Steps [](#residues){.pf-ref} give
$$
S=\frac{e^{-1/2}}{6}\left(e^{i\left(A-\frac{5\pi}{6}\right)}+e^{-i\left(A+\frac{\pi}{6}\right)}\right)-\frac{i}{6e},
$$
whose imaginary part is $\frac{e^{-1/2}}{6}\left(\sin\left(A-\frac{5\pi}{6}\right)-\sin\left(A+\frac{\pi}{6}\right)\right)-\frac{1}{6e}$. The angle-sum formulae give
$$
\sin\left(A-\frac{5\pi}{6}\right)=-\frac{\sqrt3}{2}\sin A-\frac12\cos A,\qquad
\sin\left(A+\frac{\pi}{6}\right)=\frac{\sqrt3}{2}\sin A+\frac12\cos A,
$$
so their difference is $-\sqrt3\sin A-\cos A$, and the claim follows.
:::

:::

::: {.pf-step}
$\displaystyle\int_0^{\infty}\frac{\cos x}{x^6+1}\,dx=\frac{\pi}{6e}+\frac{\pi}{6\sqrt e}\left(\cos\frac{\sqrt3}{2}+\sqrt3\sin\frac{\sqrt3}{2}\right)$.

::: pf-proof
Combining steps [](#real-part){.pf-ref} and [](#imaginary-part){.pf-ref},
$$
\int_0^{\infty}\frac{\cos x}{x^6+1}\,dx=\frac{\pi}{6}\left[e^{-1/2}\left(\cos A+\sqrt3\sin A\right)+e^{-1}\right],
$$
which is the displayed value since $A=\frac{\sqrt3}{2}$, $e^{-1/2}=\frac{1}{\sqrt e}$ and $e^{-1}=\frac1e$. The value is $\boxed{0.8173831\ldots}$, as a numerical quadrature of the integral confirms.
:::

:::

:::
:::
