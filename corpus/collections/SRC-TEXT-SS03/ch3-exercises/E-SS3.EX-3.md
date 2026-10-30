---
schema: qual/card@1
id: E-SS3.EX-3
kind: problem
title: $\int_{-\infty}^\infty\frac{\cos x}{x^2+a^2}\,dx=\pi\frac{e^{-a}}{a}$
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
Show that

$$
\int_ {- \infty} ^ {\infty} \frac {\cos x}{x ^ {2} + a ^ {2}} d x = \pi \frac {e ^ {- a}}{a}, \quad \mathrm{for} a > 0.
$$
:::

::: {.solution}
Consider
$$
F(z)=\frac{e^{iz}}{z^2+a^2},\qquad a>0,
$$
and integrate over the upper semicircle of radius $R>a$. Since $\abs{e^{iz}}=e^{-\Im z}\le1$ there and $\abs{z^2+a^2}\ge R^2-a^2$, the arc integral tends to $0$ as $R\to\infty$.

The only pole in the upper half-plane is the simple pole $z=ia$, with residue
$$
\operatorname{Res}_{z=ia}F(z)
=\frac{e^{i(ia)}}{2ia}
=\frac{e^{-a}}{2ia}.
$$
Thus the residue theorem gives
$$
\int_{-\infty}^{\infty}\frac{e^{ix}}{x^2+a^2}\,dx
=2\pi i\frac{e^{-a}}{2ia}
=\frac{\pi e^{-a}}a.
$$
Taking real parts yields
$$
\boxed{\int_{-\infty}^{\infty}\frac{\cos x}{x^2+a^2}\,dx
=\pi\frac{e^{-a}}a}.
$$
:::

::: {.remark title="Variations"}
The integrand is even, so for $b>0$ the same computation gives
$$
\int_{0}^{\infty} \frac{\cos x}{x^{2}+b^{2}}\, dx=\frac{\pi e^{-b}}{2 b}.
$$
At $a=1$ the main statement gives $\int_\RR\frac{\cos x}{x^2+1}\,dx=\frac{\pi}{e}$.
:::
