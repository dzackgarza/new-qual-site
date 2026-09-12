---
schema: qual/card@1
id: E-SS6.EX-15
kind: problem
title: "SS 6.15: An integral representation of the zeta function"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
15. Prove that for $\operatorname { R e } ( s ) > 1$ ，

$$
\zeta (s) = \frac {1}{\Gamma (s)} \int_ {0} ^ {\infty} \frac {x ^ {s - 1}}{e ^ {x} - 1} d x.
$$

[Hint: Write $\textstyle 1 / ( e ^ { x } - 1 ) = \sum _ { n = 1 } ^ { \infty } e ^ { - n x } . ]$
:::

::: solution
Let $s=\sigma+i\tau$ with $\sigma>1$. Since
\[
\frac1{e^x-1}=\sum_{n=1}^\infty e^{-nx},\qquad x>0,
\]
and
\[
\sum_{n=1}^\infty\int_0^\infty e^{-nx}x^{\sigma-1}\,dx
=\Gamma(\sigma)\sum_{n=1}^\infty n^{-\sigma}<\infty,
\]
Fubini's theorem permits termwise integration. Hence
\[
\int_0^\infty \frac{x^{s-1}}{e^x-1}\,dx
=\sum_{n=1}^\infty\int_0^\infty e^{-nx}x^{s-1}\,dx.
\]
With $u=nx$,
\[
\int_0^\infty e^{-nx}x^{s-1}\,dx
=n^{-s}\int_0^\infty e^{-u}u^{s-1}\,du
=n^{-s}\Gamma(s).
\]
Therefore
\[
\int_0^\infty \frac{x^{s-1}}{e^x-1}\,dx
=\Gamma(s)\sum_{n=1}^\infty n^{-s}
=\Gamma(s)\zeta(s),
\]
which gives
\[
\boxed{\zeta(s)=\frac1{\Gamma(s)}\int_0^\infty\frac{x^{s-1}}{e^x-1}\,dx},
\qquad \Re s>1.
\]
:::
