---
schema: qual/card@1
id: E-SS3.EX-4
kind: problem
title: 'SS 3.4: $\int_{-\infty}^\infty\frac{x\sin x}{x^2+a^2}\,dx$'
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

::: exercise
4. Show that

$$
\int_ {- \infty} ^ {\infty} \frac {x \sin x}{x ^ {2} + a ^ {2}} d x = \pi e ^ {- a}, \quad \text { for   all } a > 0.
$$
:::

::: solution
Consider
\[
F(z)=\frac{z e^{iz}}{z^2+a^2},\qquad a>0,
\]
and integrate over the upper semicircle. By Jordan's lemma the semicircular contribution tends to $0$ as the radius tends to infinity. The only pole in the upper half-plane is the simple pole $z=ia$, and
\[
\operatorname{Res}_{z=ia}F(z)
=\frac{ia\,e^{-a}}{2ia}
=\frac{e^{-a}}2.
\]
Hence
\[
\int_{-\infty}^{\infty}\frac{x e^{ix}}{x^2+a^2}\,dx
=2\pi i\cdot\frac{e^{-a}}2
=\pi i e^{-a}.
\]
Taking imaginary parts gives
\[
\boxed{\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+a^2}\,dx=\pi e^{-a}}.
\]
:::
