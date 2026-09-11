---
schema: qual/card@1
id: P-BKF81-1
kind: problem
title: Evaluate $\int_{-\infty}^{\infty}\cos x/(1+x^4)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Closed the malformed math delimiter in the title and evaluated the integral by residues of e^{iz}/(1+z^4) in the upper half-plane."
---

::: problem
Evaluate
\[
\int_{-\infty}^{\infty}\frac{\cos x}{1+x^4}\,dx.
\]
:::

::: solution
Consider
$$
F(z)=\frac{e^{iz}}{1+z^4}
$$
and integrate over the upper semicircle of radius $R>1$.

<1>1. The semicircular contribution tends to zero.
::: proof
On the upper half-plane,
$$
|e^{iz}|=e^{-\operatorname{Im}z}\le1.
$$
On $|z|=R$,
$$
|1+z^4|\ge R^4-1.
$$
Since the semicircle has length $\pi R$, its integral has absolute value at
most
$$
\frac{\pi R}{R^4-1},
$$
which tends to $0$ as $R\to\infty$.
:::

<1>2. Compute the residues in the upper half-plane.
::: proof
The poles there are
$$
\zeta_1=e^{i\pi/4},
\qquad
\zeta_2=e^{3i\pi/4}.
$$
They are simple, with
$$
\operatorname{Res}(F;\zeta_j)
=\frac{e^{i\zeta_j}}{4\zeta_j^3}.
$$
Put
$$
a=\frac1{\sqrt2}.
$$
Then
$$
\zeta_1=a(1+i),
\qquad
\zeta_2=a(-1+i),
$$
so
$$
e^{i\zeta_1}=e^{-a}e^{ia},
\qquad
e^{i\zeta_2}=e^{-a}e^{-ia}.
$$
Also
$$
\zeta_1^3=e^{3i\pi/4},
\qquad
\zeta_2^3=e^{i\pi/4}.
$$
Writing $c=\cos a$ and $s=\sin a$, a direct simplification gives
$$
\begin{aligned}
\operatorname{Res}(F;\zeta_1)+\operatorname{Res}(F;\zeta_2)
&=\frac{e^{-a}}{4\sqrt2}
\left((-1-i)e^{ia}+(1-i)e^{-ia}\right)\\
&=-\frac{i e^{-a}}{2\sqrt2}(c+s).
\end{aligned}
$$
:::

<1>3. Apply the residue theorem and take real parts.
::: proof
Letting $R\to\infty$, step <1>1 and the residue theorem yield
$$
\int_{-\infty}^{\infty}\frac{e^{ix}}{1+x^4}\,dx
=2\pi i\left(-\frac{i e^{-a}}{2\sqrt2}(c+s)\right)
=\frac{\pi}{\sqrt2}e^{-a}(c+s).
$$
The right-hand side is real. Equivalently, the imaginary part of the
integrand is odd. Taking real parts therefore gives
$$
\boxed{
\int_{-\infty}^{\infty}\frac{\cos x}{1+x^4}\,dx
=\frac{\pi}{\sqrt2}e^{-1/\sqrt2}
\left(
\cos\frac1{\sqrt2}+\sin\frac1{\sqrt2}
\right).}
$$
:::
:::
