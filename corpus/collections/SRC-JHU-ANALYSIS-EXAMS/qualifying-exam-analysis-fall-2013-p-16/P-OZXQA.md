---
schema: qual/card@1
id: P-OZXQA
kind: problem
title: Fourier transform of the sinc function
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Spring 2014 problem 6 on PDF page 15; the requested limit uses symmetric endpoints and the positive exponential convention."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the sinc integral by an indented contour, cancellation at finite symmetric endpoints, and both half-height transition values without interchanging the frequency and endpoint limits."
---

For $t \in \mathbb{R}$, compute

$$\lim_{A \to \infty} \int_{-A}^{A} \frac{\sin x}{x} e^{ixt} \, dx.$$

::: solution
The requested limit is
$$
\boxed{\begin{cases}
\pi,& |t|<1,\\
\pi/2,& |t|=1,\\
0,& |t|>1.
\end{cases}}
$$
We give $\sin x/x$ its continuous value one at zero.

<1>1. The basic half-line integral is $\int_0^\infty\sin x/x\,dx=\pi/2$.

::: proof
For $B>A>0$, integration by parts gives
$$
\int_A^B\frac{\sin x}{x}\,dx
=\left[-\frac{\cos x}{x}\right]_A^B
-\int_A^B\frac{\cos x}{x^2}\,dx,
$$
so the absolute value is at most $2/A$. This proves
convergence at infinity by the Cauchy criterion; continuity
settles the origin.

For $0<\varepsilon<R$, integrate $F(z)=e^{iz}/z$ along $[-R,-\varepsilon]$, a
clockwise upper semicircle of radius $\varepsilon$, then
$[\varepsilon,R]$ and the counterclockwise upper semicircle
of radius $R$. There is no pole in the enclosed half-annulus,
so Cauchy's theorem gives total integral zero [@SS03].
The real segments contribute $2i\int_\varepsilon^R\sin x/x\,dx$.
The small arc, parametrized with angle decreasing from
$\pi$ to zero, contributes
$i\int_\pi^0e^{i\varepsilon e^{i\theta}}\,d\theta\to-i\pi$.
The large arc has integral of modulus at most
$$
\int_0^\pi e^{-R\sin\theta}\,d\theta
\leq2\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta
\leq\frac\pi R\longrightarrow0.
$$
The middle inequality uses symmetry and concavity of sine:
$\sin\theta\geq2\theta/\pi$ on $[0,\pi/2]$.
Passing to the limits yields $2i\int_0^\infty\sin x/x\,dx-i\pi=0$,
which gives the stated value.
:::

<1>2. A real frequency contributes its sign, with frequency zero treated separately.

::: proof
For $s>0$, substituting $u=sx$ gives
$$
\lim_{A\to\infty}\int_0^A\frac{\sin(sx)}x\,dx
=\frac\pi2.
$$
For $s<0$, oddness of sine makes the value $-\pi/2$.
For $s=0$, the integrand vanishes identically, so the
value is zero. Thus the value is $(\pi/2)\operatorname{sgn}(s)$,
where $\operatorname{sgn}(0)=0$.
:::

<1>3. The symmetric transform reduces to the two frequencies $1+t$ and $1-t$.

::: proof
At each finite $A$, the imaginary part of the integrand
is odd, so its integral over $[-A,A]$ is zero. Evenness
of the real part and the product-to-sum identity give
$$
\int_{-A}^A\frac{\sin x}{x}e^{ixt}\,dx
=\int_0^A\frac{\sin((1+t)x)+\sin((1-t)x)}x\,dx.
$$
By step <1>2 the limit is
$$
\frac\pi2\bigl(\operatorname{sgn}(1+t)
+\operatorname{sgn}(1-t)\bigr).
$$
Both signs are positive for $|t|<1$, exactly one is zero
at $t=\pm1$, and the signs cancel for $|t|>1$.
These are the three displayed values. All cancellations
were made at the prescribed finite symmetric endpoints;
no separate convergence of the two complex tails is assumed.
:::
:::
