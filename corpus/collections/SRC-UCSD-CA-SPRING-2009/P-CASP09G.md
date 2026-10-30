---
schema: qual/card@1
id: P-CASP09G
kind: problem
title: 'The Fourier transform of $(\sin x/x)^2$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Evaluate $\int_{-\infty}^{\infty} \left(\frac{\sin x}{x}\right)^2 e^{itx}\,dx$ for all real $t \ge 0$.
:::

::: {.solution}
Let
$$
s(x)=\frac{\sin x}{x},
$$
with the removable value $s(0)=1$. A standard contour integral gives
$$
\widehat s(t):=
\int_{-\infty}^{\infty}s(x)e^{itx}\,dx
=\begin{cases}
\pi,&\abs{t}<1,\\
\pi/2,&\abs{t}=1,\\
0,&\abs{t}>1.
\end{cases}
$$
The endpoint values are irrelevant for convolution.

With the convention
$$
\widehat f(t)=\int_{\RR}f(x)e^{itx}\,dx,
$$
the product-convolution formula is
$$
\widehat{fg}(t)=\frac1{2\pi}(\widehat f*\widehat g)(t).
$$
Therefore
$$
\widehat{s^2}(t)
=\frac1{2\pi}
\int_{\RR}\widehat s(u)\widehat s(t-u)\,du.
$$
The integrand equals $\pi^2$ exactly where
$$
u\in[-1,1]\cap[t-1,t+1].
$$
That intersection has length $2-\abs{t}$ for $\abs{t}\le2$ and length $0$ for
$\abs{t}\ge2$. Hence
$$
\boxed{
\int_{-\infty}^{\infty}
\left(\frac{\sin x}{x}\right)^2e^{itx}\,dx
=
\begin{cases}
\pi\left(1-\dfrac{\abs{t}}{2}\right),&\abs{t}\le2,\\[4pt]
0,&\abs{t}\ge2.
\end{cases}}
$$
At $\abs{t}=2$ both formulas give $0$.
:::
