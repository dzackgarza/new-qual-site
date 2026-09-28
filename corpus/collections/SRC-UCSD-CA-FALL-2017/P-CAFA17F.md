---
schema: qual/card@1
id: P-CAFA17F
kind: problem
title: "Mean value formula for log|z - a| and subharmonicity of a series"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
(a) Prove that for any $r>0$ and real $\rho$, $$\frac{1}{2\pi}\int_0^{2\pi} \log|re^{it} - \rho|\,dt = \max(\log r, \log|\rho|).$$

(b) Show that the series $$u(z) = \sum_{n=0}^{\infty} \frac{1}{2^n} \log\left|z - \frac{1}{2^n}\right|$$ defines a subharmonic function.
:::

::: {.remark}
The official Fall 2017 exam calls $r$ an arbitrary real number while writing $\log r$. The intended hypothesis must be $r>0$.
:::

::: {.solution}
For (a), first suppose $r>|\rho|$. Then
\[
\log|re^{it}-\rho|
=\log r+\operatorname{Re}\log\left(1-\frac{\rho}{r}e^{-it}\right),
\]
where the logarithm on the right is represented by its convergent power series because $|\rho|/r<1$. Averaging over $t$ kills every nonconstant Fourier term, so the mean is $\log r$.

If $r<|\rho|$, factor instead
\[
\log|re^{it}-\rho|
=\log|\rho|+\operatorname{Re}\log\left(1-\frac r\rho e^{it}\right),
\]
and the same argument gives mean $\log|\rho|$. The equality case follows by continuity, or directly from the standard integral of $\log|e^{it}-1|$. Thus the displayed formula holds.

For (b), each function
\[
u_n(z)=2^{-n}\log\left|z-2^{-n}\right|
\]
is subharmonic and locally integrable, with distributional Laplacian
\[
\Delta u_n=2\pi\,2^{-n}\delta_{2^{-n}}.
\]
On every compact set $K$, the quantities
\[
\int_K\left|\log|z-a|\right|\,dA(z)
\]
are uniformly bounded for $a$ in a fixed bounded set. Since $\sum2^{-n}<\infty$, the series $\sum u_n$ therefore converges in $L^1_{\mathrm{loc}}$ to the pointwise-defined extended-real function $u$. Passing to distributions gives
\[
\Delta u
=2\pi\sum_{n=0}^\infty2^{-n}\delta_{2^{-n}}\ge0.
\]
Hence $u$ is subharmonic.
:::
