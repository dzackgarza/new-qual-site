---
schema: qual/card@1
id: P-RAF16C
kind: problem
title: "Evaluation of integral via Fubini-Tonelli"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Use the fact that
$$
\frac{1}{x} = \int_0^\infty e^{-xt}\,dt \quad (x > 0)
$$
and the Fubini-Tonelli Theorem to evaluate the integral
$$
\int_0^\infty e^{-\alpha x} \frac{\sin(\beta x)}{x}\,dx,
$$
where $\alpha$ and $\beta$ are positive numbers.
Be sure to verify the assumption in the Fubini-Tonelli Theorem.

You may find the following formula useful:
$$
\int e^{ax}\sin bx\,dx = \frac{e^{ax}}{a^2 + b^2}(a\sin bx - b\cos bx) + C.
$$
:::

::: solution
<1>1. Verify absolute integrability of the double integral.
::: proof
Using
\[
\frac1x=\int_0^\infty e^{-tx}\,dt,
\]
the desired integral is formally
\[
\int_0^\infty\int_0^\infty
e^{-(\alpha+t)x}\sin(\beta x)\,dt\,dx.
\]
Its absolute integral equals, by Tonelli's theorem,
\[
\int_0^\infty e^{-\alpha x}\frac{|\sin(\beta x)|}{x}\,dx.
\]
For $0<x\le1$,
\[
\frac{|\sin(\beta x)|}{x}\le\beta,
\]
so the integral is finite near $0$. For $x\ge1$,
\[
e^{-\alpha x}\frac{|\sin(\beta x)|}{x}
\le e^{-\alpha x},
\]
which is integrable. Hence the double integral is absolutely integrable, and Fubini's theorem applies.
:::

<1>2. Interchange the integrals and compute the inner integral.
::: proof
By Fubini,
\[
\begin{aligned}
I
&:=\int_0^\infty e^{-\alpha x}\frac{\sin(\beta x)}x\,dx\\
&=\int_0^\infty
\left(\int_0^\infty e^{-(\alpha+t)x}\sin(\beta x)\,dx\right)dt.
\end{aligned}
\]
For $u>0$, the standard Laplace integral gives
\[
\int_0^\infty e^{-ux}\sin(\beta x)\,dx
=\frac{\beta}{u^2+\beta^2}.
\]
Taking $u=\alpha+t$,
\[
I=\int_0^\infty\frac{\beta}{(\alpha+t)^2+\beta^2}\,dt.
\]
:::

<1>3. Evaluate the remaining elementary integral.
::: proof
With $u=\alpha+t$,
\[
I=\int_\alpha^\infty\frac{\beta}{u^2+\beta^2}\,du
=\left[\arctan\frac{u}{\beta}\right]_{u=\alpha}^{\infty}.
\]
Therefore
\[
I=\frac\pi2-\arctan\frac\alpha\beta
=\boxed{\arctan\frac\beta\alpha},
\]
because $\alpha,\beta>0$.
:::
:::
