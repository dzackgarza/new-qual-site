---
schema: qual/card@1
id: P-C53SG
kind: problem
title: Equality of the iterated integrals of $\frac{(x-y)\sin(xy)}{x^2+y^2}$ on $[0,1]^2$
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 4.2 in the preserved TAMU August 2015 source notes; the statement and polar-coordinate estimate agree with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
justify the statement that $\int_0^1\int_0^1 \frac{(x-y)\sin(xy)}{x^2+y^2}dxdy=\int_0^1\int_0^1\frac{(x-y)\sin(xy)}{x^2+y^2}dydx$
:::

::: {.solution}
Fubini's theorem applies once the integrand is shown to be absolutely integrable. Since $|\sin(xy)|\le1$,
\[
\left|\frac{(x-y)\sin(xy)}{x^2+y^2}\right|
\le \frac{|x-y|}{x^2+y^2}.
\]
The square $[0,1]^2$ is contained in the quarter disk
\[
D=\{(r\cos\theta,r\sin\theta):0\le r\le\sqrt2,\ 0\le\theta\le\pi/2\}.
\]
Hence, using polar coordinates,
\[
\begin{aligned}
\int_{[0,1]^2}\left|\frac{(x-y)\sin(xy)}{x^2+y^2}\right|\,dx\,dy
&\le \int_0^{\pi/2}\int_0^{\sqrt2}
\frac{r|\cos\theta-\sin\theta|}{r^2}\,r\,dr\,d\theta\\
&=\sqrt2\int_0^{\pi/2}|\cos\theta-\sin\theta|\,d\theta\\
&<\infty.
\end{aligned}
\]
(The value at $(0,0)$ is irrelevant.) Therefore the integrand belongs to $L^1([0,1]^2)$, and Fubini's theorem gives
\[
\int_0^1\int_0^1 \frac{(x-y)\sin(xy)}{x^2+y^2}\,dx\,dy
=
\int_0^1\int_0^1 \frac{(x-y)\sin(xy)}{x^2+y^2}\,dy\,dx.
\]
:::
