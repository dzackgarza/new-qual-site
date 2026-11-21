---
schema: qual/card@1
id: P-W23PS
kind: problem
title: The integral $\int_0^\infty\frac{1}{1+x^n}\,dx$ by a wedge of angle $\frac{2\pi}{n}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained exam assets/attachments/UGA_Complex_Analysis_Fall_2021.pdf,
    problem 3: for n at least 2, to use a wedge of angle 2 pi/n to evaluate the
    integral of 1/(1+x^n). The card agrees, and its closing remark records that
    the paper prints the integral over the whole line, which for odd n is
    improper at x = -1 and for even n is twice the half-line value.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The computation is correct. The poles of 1/(1+z^n) are the n-th roots of -1,
    of argument (2k+1)pi/n, so exactly one, omega = e^{i pi/n}, lies in the open
    sector, and none on the boundary for R > 1; the residue there is
    1/(n omega^{n-1}) = -omega/n because omega^n = -1. Along the return ray,
    z = zeta t with zeta = omega^2, the integrand is 1/(1+t^n) because
    zeta^n = 1, and the reversed orientation produces the factor -zeta. On the
    arc the bound |1+z^n| >= R^n - 1 and the length 2 pi R/n give O(R^{1-n}),
    which vanishes for n at least 2. The residue theorem then gives
    (1 - zeta) I = -2 pi i omega/n, and (1 - zeta)/omega = omega^{-1} - omega =
    -2i sin(pi/n), so I = pi/(n sin(pi/n)). Nothing was changed.
---

::: {.problem}
Suppose $n \geq 2$.
Use a wedge of angle $\frac{2 \pi}{n}$ to evaluate the integral
$$
    I=\int_{0}^{\infty} \frac{1}{1+x^{n}} d x
$$
:::

::: {.solution}
Let $f(z) \coloneqq 1/(1+z^n)$, $\omega \coloneqq e^{i\pi/n}$ and $\zeta \coloneqq \omega^2 = e^{2\pi i/n}$.
For $R>1$, let $\Gamma_R$ be the boundary of the sector $\theset{re^{it} \st 0\leq r\leq R,\ 0\leq t\leq 2\pi/n}$, oriented positively: the segment $\gamma_1 = [0,R]$, the arc $C_R = \theset{Re^{it} \st 0\leq t\leq 2\pi/n}$, and the segment $\gamma_3$ from $R\zeta$ to $0$.

::: pf

::: {.pf-step #pole}
The only pole of $f$ inside $\Gamma_R$ is the simple pole $\omega$, and $\Res_{z=\omega} f = -\omega/n$.

::: pf-proof
The poles of $f$ are the roots $e^{(2k+1)i\pi/n}$, $0\leq k\leq n-1$, of $z^n=-1$, and they are simple.
Their arguments are $(2k+1)\pi/n$, so only $k=0$ lies in the open sector of angle $2\pi/n$, and none lies on $\Gamma_R$ when $R>1$.
At a simple zero $\omega$ of $1+z^n$, $\Res_{z=\omega} f = 1/(n\omega^{n-1}) = \omega/(n\omega^n) = -\omega/n$, since $\omega^n=-1$.
:::

:::

::: {.pf-step #ray}
$\int_{\gamma_3} f = -\zeta\int_0^R \frac{dt}{1+t^n}$.

::: pf-proof
Parametrize $\gamma_3$ in reverse by $z=\zeta t$, $t\in[0,R]$, with $dz = \zeta\,dt$.
Since $\zeta^n=1$, $f(\zeta t) = 1/(1+t^n)$, and reversing the orientation gives the sign.
:::

:::

::: {.pf-step #arc}
$\int_{C_R} f \to 0$ as $R\to\infty$.

::: pf-proof
On $C_R$, $\abs{1+z^n}\geq R^n-1$, and $C_R$ has length $2\pi R/n$.
By the ML estimate, $\abs{\int_{C_R} f}\leq \frac{2\pi R}{n(R^n-1)} = O(R^{1-n})$, which tends to $0$ because $n\geq 2$.
:::

:::

::: pf-step
$I = \boxed{\dfrac{\pi}{n\sin(\pi/n)}}$.

::: pf-proof
By the residue theorem and steps [](#pole){.pf-ref} and [](#ray){.pf-ref},
$$
(1-\zeta)\int_0^R \frac{dt}{1+t^n} + \int_{C_R} f = 2\pi i\Res_{z=\omega} f = -\frac{2\pi i\,\omega}{n}.
$$
Letting $R\to\infty$ and using step [](#arc){.pf-ref}, $(1-\zeta) I = -2\pi i\omega/n$.
Since $(1-\zeta)/\omega = \omega^{-1}-\omega = -2i\sin(\pi/n)$,
$$
I = \frac{-2\pi i}{n(\omega^{-1}-\omega)} = \frac{-2\pi i}{-2in\sin(\pi/n)} = \frac{\pi}{n\sin(\pi/n)}.
$$
:::

:::

:::

:::

::: remark
The exam paper prints the integral over $(-\infty,\infty)$. For odd $n$ that integral is not defined, because $1+x^n$ vanishes at $x=-1$. For even $n$ the integrand is even, and the integral over $(-\infty,\infty)$ is $2I=\dfrac{2\pi}{n\sin(\pi/n)}$.
:::
