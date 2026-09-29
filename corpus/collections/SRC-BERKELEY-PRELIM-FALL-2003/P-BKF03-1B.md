---
schema: qual/card@1
id: P-BKF03-1B
kind: problem
title: Evaluation of $\int_{-\infty}^{\infty} x^2/(x^n+1)\,dx$ for even $n\ge4$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the sector-contour residue computation, ray rotation factor, arc decay, and final evenness factor.
---

::: {.problem}
Evaluate $\int _ { - \infty } ^ { \infty } { \frac { x ^ { 2 } } { x ^ { n } + 1 } } d x$ , where $n \geq 4$ is an even integer.
:::

::: {.solution}

Because $n$ is even, the integrand is even.
Thus it suffices to compute
\[
I:=\int_0^\infty \frac{x^2}{1+x^n}\,dx,
\]
and then double the result.

Let
\[
F(z)=\frac{z^2}{1+z^n},
\qquad
\rho=e^{\pi i/n},
\qquad
\omega=e^{2\pi i/n}=\rho^2.
\]

::: pf

::: {.pf-step #pole-and-residue}
In the sector $0<\arg z<2\pi/n$, the function $F$ has exactly one pole, at $z=\rho$, and
\[
\operatorname{Res}_{z=\rho}F(z)=-\frac{\rho^3}{n}.
\]

::: pf-proof
The poles satisfy $z^n=-1$, so they are
\[
e^{(2k+1)\pi i/n}.
\]
Exactly one has argument strictly between $0$ and $2\pi/n$, namely $\rho=e^{\pi i/n}$.
It is simple because $(1+z^n)'=nz^{n-1}$ does not vanish there.
Therefore
\[
\operatorname{Res}_{z=\rho}F(z)
=\frac{\rho^2}{n\rho^{n-1}}
=\frac{\rho^{3-n}}n.
\]
Since $\rho^n=-1$, one has $\rho^{3-n}=-\rho^3$, giving the formula.
:::

:::

::: {.pf-step #arc-integral-vanishes}
The integral over the circular arc of radius $R$ in this sector tends to $0$ as $R\to\infty$.

::: pf-proof
On the arc, $|z|=R$.
For $R$ large,
\[
|1+z^n|\ge R^n-1,
\]
so
\[
|F(z)|\le \frac{R^2}{R^n-1}=O(R^{2-n}).
\]
The arc length is $2\pi R/n$, hence its integral is $O(R^{3-n})$.
Since $n\ge4$, this tends to $0$.
:::

:::

::: {.pf-step #radial-sides-contribution}
The two radial sides of the sector contribute $(1-\rho^6)I$ in the limit.

::: pf-proof
The lower radial side contributes
\[
\int_0^R \frac{x^2}{1+x^n}\,dx.
\]
On the upper radial side, traversed back toward the origin, set $z=\omega t$ with $t$ decreasing from $R$ to $0$.
Since $\omega^n=e^{2\pi i}=1$,
\[
F(\omega t)\,\omega\,dt
=\frac{\omega^3t^2}{1+t^n}\,dt
=\rho^6\frac{t^2}{1+t^n}\,dt.
\]
Therefore the upper side contributes
\[
-\rho^6\int_0^R\frac{t^2}{1+t^n}\,dt.
\]
Letting $R\to\infty$ gives $(1-\rho^6)I$.
:::

:::

::: {.pf-step #I-value}
The residue theorem gives
\[
I=\frac{\pi}{n\sin(3\pi/n)}.
\]

::: pf-proof
By steps [](#pole-and-residue){.pf-ref}, [](#arc-integral-vanishes){.pf-ref} and [](#radial-sides-contribution){.pf-ref}, the residue theorem yields
\[
(1-\rho^6)I
=2\pi i\left(-\frac{\rho^3}{n}\right)
=-\frac{2\pi i}{n}\rho^3.
\]
Now
\[
\rho^3-\rho^{-3}=2i\sin\frac{3\pi}{n},
\]
so, after multiplying by $\rho^3$,
\[
\rho^6-1=2i\rho^3\sin\frac{3\pi}{n}.
\]
Hence
\[
1-\rho^6=-2i\rho^3\sin\frac{3\pi}{n}.
\]
Substituting into the contour identity and cancelling the nonzero factor $-2i\rho^3$ gives
\[
I=\frac{\pi}{n\sin(3\pi/n)}.
\]
:::

:::

::: {.pf-step #final-integral-value}
Therefore
\[
\boxed{\int_{-\infty}^{\infty}\frac{x^2}{x^n+1}\,dx
=\frac{2\pi}{n\sin(3\pi/n)}}.
\]

::: pf-proof
Since $n$ is even, $x^n$ and $x^2$ are both even functions, so the integrand is even.
Thus the integral over the whole real line is $2I$, and step [](#I-value){.pf-ref} gives the displayed value.
:::

:::

:::

:::
