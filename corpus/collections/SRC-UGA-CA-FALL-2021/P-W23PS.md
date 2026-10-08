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
---

::: {.problem}
Suppose $n \geq 2$. Use a wedge of angle $\frac{2 \pi}{n}$ to evaluate the integral
\[
    I=\int_{0}^{\infty} \frac{1}{1+x^{n}} d x
\]
:::

::: {.remark}
The current Quals `.docx` writes the OMML limits as $-\infty$ to $\infty$ (Word’s default nary limits). That integral has a pole on the real axis when $n$ is odd, and the same sentence asks for a wedge of angle $2\pi/n$, which evaluates the integral from $0$ to $\infty$. The exam as transcribed in `2021_Fall.md.source`, and the existing solutions, are $\int_0^\infty$.
:::

::: {.solution}
Set $f(z)=1/(1+z^n)$, $\zeta=e^{2\pi i/n}$, and $\omega=e^{\pi i/n}$. For $R>1$, let $\Gamma_R$ be the positively oriented boundary of the sector $0\leq\arg z\leq2\pi/n$, $|z|\leq R$: the segments $[0,R]$ and $[R\zeta,0]$, joined by the counterclockwise arc $Re^{it}$, $0\leq t\leq2\pi/n$.

<1>1. The only pole of $f$ inside $\Gamma_R$ is $\omega$, and
\[
\operatorname{Res}_{z=\omega}f(z)=-\frac{\omega}{n}.
\]

::: {.proof}
The roots of $1+z^n$ are $e^{(2k+1)\pi i/n}$ for $0\leq k<n$, all simple. Exactly one has argument strictly between $0$ and $2\pi/n$, namely $\omega$. Because $\omega^n=-1$, the simple-pole formula gives
\[
\operatorname{Res}_{z=\omega}f(z)
=\frac1{n\omega^{n-1}}=-\frac{\omega}{n}.
\]
:::

<1>2. The integral over the circular arc of $\Gamma_R$ tends to zero as $R\to\infty$.

::: {.proof}
On the arc, $|1+z^n|\geq R^n-1$, while the arc length is $2\pi R/n$. Thus
\[
\left|\int_{\mathrm{arc}}f(z)\,dz\right|
\leq\frac{2\pi R}{n(R^n-1)}\longrightarrow0
\]
because $n\geq2$.
:::

<1>3. The integral is
\[
\boxed{I=\frac{\pi}{n\sin(\pi/n)}}.
\]

::: {.proof}
Write $I_R=\int_0^R(1+x^n)^{-1}\,dx$. The outgoing radial segment contributes $I_R$. Parameterizing the return segment by $z=\zeta t$ with $t$ decreasing from $R$ to $0$, and using $\zeta^n=1$, shows that its contribution is $-\zeta I_R$. The residue theorem and step <1>1 therefore give
\[
(1-\zeta)I_R+\int_{\mathrm{arc}}f(z)\,dz
=-\frac{2\pi i\omega}{n}.
\]
The improper integral converges, since $0<(1+x^n)^{-1}\leq x^{-n}$ for $x\geq1$. Letting $R\to\infty$ and applying step <1>2 yields
\[
I=-\frac{2\pi i\omega}{n(1-\zeta)}.
\]
Finally,
\[
1-\zeta
=e^{\pi i/n}\bigl(e^{-\pi i/n}-e^{\pi i/n}\bigr)
=-2i\omega\sin(\pi/n),
\]
which gives the claimed value.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 evaluates the requested integral.
:::
:::
