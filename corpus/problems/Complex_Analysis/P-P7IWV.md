---
schema: qual/card@1
id: P-P7IWV
kind: problem
title: One root of $z^4+2z^3-2z+10$ in each open quadrant
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Prove that $f(z) = z^4 + 2z^3 -2z + 10$ has exactly one root in each open quadrant.
:::

::: {.solution}
For $R>0$ let $\Gamma_R$ be the positively oriented boundary of the quarter-disk $\theset{z : \abs{z}<R,\ 0<\arg z<\pi/2}$, and write $\Delta_\gamma\arg f$ for the change of argument of $f$ along a path $\gamma$.

::: pf

::: {.pf-step #axes}

$f$ has no zeros on the real or imaginary axis.

::: pf-proof

For real $x$,
$$
f(x)=(x^2+x-1)^2+x^2+9>0.
$$
For real $t$,
$$
f(it)=t^4+10-2i(t^3+t),
$$
whose real part is strictly positive.

:::

:::

::: {.pf-step #real-edge}

Along the segment $[0,R]$, $\Delta\arg f=0$.

::: pf-proof

By step [](#axes){.pf-ref}, $f$ is positive on this segment.

:::

:::

::: {.pf-step #arc}

Along the arc $z=Re^{it}$, $0\le t\le\pi/2$, $\Delta\arg f\to2\pi$ as $R\to\infty$.

::: pf-proof

On the arc,
$$
\frac{f(z)}{z^4}=1+\frac2z-\frac2{z^3}+\frac{10}{z^4}\longrightarrow1
$$
uniformly as $R\to\infty$, so the change of argument of $f$ tends to that of $z^4$, which is $4\cdot\frac\pi2=2\pi$.

:::

:::

::: {.pf-step #imag-edge}

Along the segment from $iR$ to $0$, $\Delta\arg f\to0$ as $R\to\infty$.

::: pf-proof

By step [](#axes){.pf-ref}, the image of this segment lies in the open right half-plane, so a continuous argument along it takes values in $(-\pi/2,\pi/2)$. Since $f(iR)/R^4\to1$, we have $\arg f(iR)\to0$, and $\arg f(0)=\arg10=0$.

:::

:::

::: {.pf-step #q1}

$f$ has exactly one zero in the open first quadrant.

::: pf-proof

Choose $R$ larger than the moduli of all roots. The number $N_1$ of zeros in the first quadrant is then independent of $R$, and by the argument principle and steps [](#real-edge){.pf-ref}, [](#arc){.pf-ref} and [](#imag-edge){.pf-ref},
$$
2\pi N_1=\Delta_{\Gamma_R}\arg f\longrightarrow2\pi.
$$
Hence $N_1=1$.

:::

:::

::: pf-step

$f$ has exactly one zero in each open quadrant.

::: pf-proof

The coefficients of $f$ are real, so nonreal roots occur in conjugate pairs, and step [](#q1){.pf-ref} gives exactly one root in the fourth quadrant. Since $f$ has degree $4$ and, by step [](#axes){.pf-ref}, no roots on the axes, the remaining two roots form a conjugate pair in the open left half-plane, one in each of the second and third quadrants.

:::

:::

:::

:::
