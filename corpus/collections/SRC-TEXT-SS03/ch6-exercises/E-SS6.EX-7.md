---
schema: qual/card@1
id: E-SS6.EX-7
kind: problem
title: "SS 6.7: The Beta function and its relation to Gamma"
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

::: {.exercise}
7. The Beta function is defined for $\mathrm { R e } ( \alpha ) > 0$ and $\operatorname { R e } ( \beta ) > 0$ by

$$
B (\alpha , \beta) = \int_ {0} ^ {1} (1 - t) ^ {\alpha - 1} t ^ {\beta - 1} d t.
$$

(a) Prove that $B ( \alpha , \beta ) = \frac { \Gamma ( \alpha ) \Gamma ( \beta ) } { \Gamma ( \alpha + \beta ) }$

(b) Show that $B ( \alpha , \beta ) = \int _ { 0 } ^ { \infty } { \frac { u ^ { \alpha - 1 } } { ( 1 + u ) ^ { \alpha + \beta } } } d u .$

[Hint: For part (a), note that

$$
\Gamma (\alpha) \Gamma (\beta) = \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} t ^ {\alpha - 1} s ^ {\beta - 1} e ^ {- t - s} d t d s,
$$

and make the change of variables $s = u r , t = u ( 1 - r ) . ]$
:::

::: {.solution}
For $\Re\alpha,\Re\beta>0$,
\[
\Gamma(\alpha)\Gamma(\beta)
=\int_0^\infty\int_0^\infty
 t^{\alpha-1}s^{\beta-1}e^{-t-s}\,dt\,ds.
\]
Set
\[
t=u(1-r),\qquad s=ur,
\]
with $u>0$ and $0<r<1$. The Jacobian has absolute value $u$, so
\[
\Gamma(\alpha)\Gamma(\beta)
=\int_0^\infty e^{-u}u^{\alpha+\beta-1}\,du
\int_0^1(1-r)^{\alpha-1}r^{\beta-1}\,dr.
\]
Thus
\[
\Gamma(\alpha)\Gamma(\beta)
=\Gamma(\alpha+\beta)B(\alpha,\beta),
\]
and therefore
\[
\boxed{B(\alpha,\beta)=
\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}}.
\]

For part (b), put
\[
u=\frac{1-t}{t},\qquad t=\frac1{1+u},\qquad dt=-\frac{du}{(1+u)^2}.
\]
As $t$ runs from $0$ to $1$, $u$ runs from $\infty$ to $0$. Therefore
\[
B(\alpha,\beta)
=\int_0^\infty
\frac{u^{\alpha-1}}{(1+u)^{\alpha+\beta}}\,du.
\]
:::
