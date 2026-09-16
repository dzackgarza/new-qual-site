---
schema: qual/card@1
id: P-QNJ6C
kind: problem
title: Non-integrability of $\frac{xy}{(x^2+y^2)^2}$ on $[-1,1]^2$
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Integrals
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2017 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2017.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: {.problem}
Let $f$ on $[-1,1]^2$ be defined by
\[
f(x,y)=
\begin{cases}
\dfrac{xy}{(x^2+y^2)^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
\]
Determine whether $f$ is Lebesgue integrable.
:::

::: {.solution}
The function is measurable. To test Lebesgue integrability, consider its absolute value on the sector
\[
S:=\{(r\cos\theta,r\sin\theta):0<r<1,\ \pi/6\le\theta\le\pi/3\}.
\]
This sector lies inside $[-1,1]^2$. In polar coordinates,
\[
|f(r\cos\theta,r\sin\theta)|
=\frac{|\cos\theta\sin\theta|}{r^2}.
\]
On $[\pi/6,\pi/3]$, the factor $|\cos\theta\sin\theta|$ is bounded below by a positive constant. Therefore
\[
\begin{aligned}
\int_{[-1,1]^2}|f(x,y)|\,dx\,dy
&\ge \int_S|f|\\
&=\int_{\pi/6}^{\pi/3}\int_0^1
\frac{\cos\theta\sin\theta}{r^2}\,r\,dr\,d\theta\\
&=\left(\int_{\pi/6}^{\pi/3}\cos\theta\sin\theta\,d\theta\right)
\left(\int_0^1\frac{dr}{r}\right)\\
&=\infty.
\end{aligned}
\]
Hence
\[
\boxed{f\notin L^1([-1,1]^2).}
\]
So $f$ is not Lebesgue integrable.
:::
