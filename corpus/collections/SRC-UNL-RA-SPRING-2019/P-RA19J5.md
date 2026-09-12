---
schema: qual/card@1
id: P-RA19J5
kind: problem
title: Riemann-Stieltjes integrability of $e^{2x}$ against a broken-step integrator on $[0,4]$
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 5 in the preserved UNL January 2019 qualifying-exam PDF/extraction. The source has alpha(2)=3 but right limit 4, so alpha has a jump of size 1 at 2.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

:::{.problem}
Use the Riemann condition to show that $f\in\mathcal R_\alpha[0,4]$ where $f(x)=e^{2x}$ and
$$\alpha(x)=\begin{cases}
x+1,&0\le x\le2,\\
3x-2,&2<x\le4.
\end{cases}$$
Compute the value of the Riemann--Stieltjes integral
$$\int_0^4 f(x)\,d\alpha.$$
:::

:::: {.solution}
The key point is that the integrator is not continuous at $2$:
\[
\alpha(2)=3,
\qquad
\alpha(2+)=4.
\]
Thus there is a jump of size $1$ immediately to the right of $2$.

<1>1. Verify the Riemann--Stieltjes condition.
::: {.proof}
The function $\alpha$ is increasing on $[0,4]$. Let $P$ be a partition containing $2$. On intervals not adjacent to $2$, the increment of $\alpha$ is either $\Delta x$ or $3\Delta x$. On the interval $[2,x_i]$ immediately to the right of $2$,
\[
\alpha(x_i)-\alpha(2)=1+3(x_i-2).
\]
Hence
\[
U(P,f,\alpha)-L(P,f,\alpha)
\le 3\sum_i (M_i-m_i)\Delta x_i +(M_*-m_*),
\]
where $M_*-m_*$ is the oscillation of $f$ on the interval immediately to the right of $2$.

Since $f(x)=e^{2x}$ is uniformly continuous on $[0,4]$, both terms can be made arbitrarily small by taking the mesh of $P$ sufficiently small. Therefore the Riemann condition holds and
\[
f\in\mathcal R_\alpha[0,4].
\]
:::

<1>2. Separate the jump from the absolutely continuous pieces.
::: {.proof}
Define
\[
\beta(x)=
\begin{cases}
x+1,&0\le x\le2,\\
3x-3,&2<x\le4,
\end{cases}
\qquad
H(x)=\mathbf1_{(2,4]}(x).
\]
Then $\beta$ is continuous, piecewise $C^1$, with
\[
\beta'(x)=1\quad(0<x<2),
\qquad
\beta'(x)=3\quad(2<x<4),
\]
and
\[
\alpha=\beta+H.
\]
The Riemann--Stieltjes integral against $H$ is the jump contribution
\[
\int_0^4 f\,dH=f(2).
\]
Therefore
\[
\int_0^4 f\,d\alpha
=\int_0^2 f(x)\,dx+f(2)+3\int_2^4 f(x)\,dx.
\]
:::

<1>3. Compute the value.
::: {.proof}
With $f(x)=e^{2x}$,
\[
\begin{aligned}
\int_0^4 e^{2x}\,d\alpha
&=\frac{e^4-1}{2}+e^4+\frac{3(e^8-e^4)}2\\
&=\boxed{\frac{3e^8-1}{2}}.
\end{aligned}
\]
:::
::::
