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
Prove that $f(z) = z^4 + 2z^3 -2z + 10$ has exactly one root in each open
quadrant.
:::

::: {.solution}
First exclude roots on the coordinate axes. For real $x$,
\[
f(x)=(x^2+x-1)^2+x^2+9>0.
\]
For real $t$,
\[
f(it)=t^4+10-2i(t^3+t),
\]
whose real part is strictly positive. Thus $f$ has no zeros on either axis.

Now count zeros in the first quadrant. Let $\Gamma_R$ be the positively oriented boundary of the quarter-disk
\[
\{z:|z|<R,\ 0<\arg z<\pi/2\}.
\]
Along the positive real edge, $f$ is positive, so the change of argument is $0$.

On the circular edge $z=Re^{it}$, $0\le t\le\pi/2$,
\[
\frac{f(z)}{z^4}
=1+\frac2z-\frac2{z^3}+\frac{10}{z^4}
\longrightarrow1
\]
uniformly as $R\to\infty$. Hence the change of argument of $f$ along this arc tends to the change of argument of $z^4$, namely
\[
4\cdot\frac\pi2=2\pi.
\]

On the imaginary edge, traversed from $iR$ down to $0$, the image stays in the open right half-plane. Moreover
\[
\arg f(iR)\longrightarrow0,
\qquad
\arg f(0)=0,
\]
so the change of argument along this edge tends to $0$.

Choose $R$ larger than the moduli of all roots. The number $N_1$ of zeros in the first quadrant is then independent of $R$, while the argument principle gives
\[
2\pi N_1=\Delta_{\Gamma_R}\arg f\longrightarrow2\pi.
\]
Therefore $N_1=1$.

The coefficients of $f$ are real, so nonreal roots occur in conjugate pairs. Hence there is also exactly one root in the fourth quadrant. Since $f$ has degree $4$ and no roots on the axes, the remaining two roots form a conjugate pair in the left half-plane, giving exactly one root in each of the second and third quadrants.
:::
