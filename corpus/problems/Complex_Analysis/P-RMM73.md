---
schema: qual/card@1
id: P-RMM73
kind: problem
title: Holomorphic functions in a neighborhood of $D_r(z_0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $f$ be holomorphic in a neighborhood of the closed disk $\overline{D}_r(z_0)$.
Prove Cauchy's estimate for derivatives:
$$|f^{(n)}(z_0)| \le \frac{n!}{r^n} \max_{|z-z_0| = r} |f(z)|$$
and the Mean Value Property:
$$f(z_0) = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + r e^{i\theta}) \, d\theta.$$
:::

::: solution
Cauchy's integral formula for derivatives gives
\[
f^{(n)}(z_0)
=
\frac{n!}{2\pi i}
\oint_{|z-z_0|=r}
\frac{f(z)}{(z-z_0)^{n+1}}\,dz.
\]
If
\[
M_r=\max_{|z-z_0|=r}|f(z)|,
\]
then the $ML$ estimate yields
\[
|f^{(n)}(z_0)|
\le
\frac{n!}{2\pi}
\frac{M_r}{r^{n+1}}(2\pi r)
=
\frac{n!}{r^n}M_r.
\]

For $n=0$, parameterize the circle by
\[
z=z_0+re^{i\theta},\qquad dz=ire^{i\theta}\,d\theta.
\]
Cauchy's formula becomes
\[
f(z_0)
=
\frac1{2\pi i}
\int_0^{2\pi}
\frac{f(z_0+re^{i\theta})}{re^{i\theta}}
ire^{i\theta}\,d\theta
=
\frac1{2\pi}
\int_0^{2\pi}f(z_0+re^{i\theta})\,d\theta.
\]
:::
