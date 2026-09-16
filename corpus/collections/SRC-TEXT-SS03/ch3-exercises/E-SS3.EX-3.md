---
schema: qual/card@1
id: E-SS3.EX-3
kind: problem
title: 'SS 3.3: $\int_{-\infty}^\infty\frac{\cos x}{x^2+a^2}\,dx$'
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
3. Show that

$$
\int_ {- \infty} ^ {\infty} \frac {\cos x}{x ^ {2} + a ^ {2}} d x = \pi \frac {e ^ {- a}}{a}, \quad \mathrm{for} a > 0.
$$
:::

::: {.solution}
Consider
\[
F(z)=\frac{e^{iz}}{z^2+a^2},\qquad a>0,
\]
and integrate over the upper semicircle of radius $R>a$. Since $|e^{iz}|=e^{-\Im z}\le1$ there and $|z^2+a^2|\ge R^2-a^2$, the arc integral tends to $0$ as $R\to\infty$.

The only pole in the upper half-plane is the simple pole $z=ia$, with residue
\[
\operatorname{Res}_{z=ia}F(z)
=\frac{e^{i(ia)}}{2ia}
=\frac{e^{-a}}{2ia}.
\]
Thus the residue theorem gives
\[
\int_{-\infty}^{\infty}\frac{e^{ix}}{x^2+a^2}\,dx
=2\pi i\frac{e^{-a}}{2ia}
=\frac{\pi e^{-a}}a.
\]
Taking real parts yields
\[
\boxed{\int_{-\infty}^{\infty}\frac{\cos x}{x^2+a^2}\,dx
=\pi\frac{e^{-a}}a}.
\]
:::
