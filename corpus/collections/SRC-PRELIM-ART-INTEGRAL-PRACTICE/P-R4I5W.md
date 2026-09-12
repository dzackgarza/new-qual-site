---
schema: qual/card@1
id: P-R4I5W
kind: problem
title: Evaluate $\int\sqrt{1+\cos(2ax)}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate
\[
\int \sqrt{1+\cos(2ax)}\,dx.
\]
:::

::: solution
Using $1+\cos(2u)=2\cos^2u$,
\[
\sqrt{1+\cos(2ax)}=\sqrt2\,|\cos(ax)|.
\]
Thus the stored simplification to $\sqrt2\cos(ax)$ is valid only on intervals where $\cos(ax)\ge0$.

If $a\ne0$, on any interval on which $\cos(ax)$ has constant sign,
\[
\int \sqrt{1+\cos(2ax)}\,dx
=\begin{cases}
\dfrac{\sqrt2}{a}\sin(ax)+C,&\cos(ax)\ge0,\\[6pt]
-\dfrac{\sqrt2}{a}\sin(ax)+C,&\cos(ax)\le0.
\end{cases}
\]
These local primitives glue continuously across the zeros of $\cos(ax)$ after adjusting the constants. Equivalently, a global primitive is
\[
\frac{\sqrt2}{a}H(ax)+C,
\]
where, for
\[
k=\left\lfloor\frac{u+\pi/2}{\pi}\right\rfloor,
\qquad
H(u)=2k+\sin(u-k\pi).
\]
Then $H'(u)=|\cos u|$ wherever differentiated, including across the joining points by continuity of the derivative. If $a=0$, the integrand is the constant $\sqrt2$ and the primitive is $\sqrt2 x+C$.
:::
