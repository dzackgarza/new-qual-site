---
schema: qual/card@1
id: E-SS2.EX-10
kind: problem
title: "Weierstrass’s theorem states that a continuous function on [0, 1] can be uni for"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
10. Weierstrass’s theorem states that a continuous function on [0, 1] can be uni formly approximated by polynomials.
    Can every continuous function on the closed unit disc be approximated uniformly by polynomials in the variable $z ?$
:::

::: solution
No. Consider the continuous function
\[
f(z)=\overline z
\]
on the closed unit disc.

Suppose there were polynomials $p_n(z)$ converging uniformly to $\overline z$ on the closed unit disc. On the positively oriented unit circle $C$, every polynomial is entire, so Cauchy's theorem gives
\[
\int_C p_n(z)\,dz=0.
\]
Uniform convergence on $C$ allows passage to the limit in the contour integral:
\[
\int_C \overline z\,dz
=\lim_{n\to\infty}\int_C p_n(z)\,dz
=0.
\tag{1}
\]
But parametrizing $C$ by $z=e^{it}$, $0\le t\le2\pi$, gives
\[
\overline z=e^{-it},
\qquad
dz=i e^{it}\,dt,
\]
and therefore
\[
\int_C \overline z\,dz
=\int_0^{2\pi} i\,dt
=2\pi i\ne0,
\]
contradicting (1).

Hence not every continuous function on the closed unit disc can be uniformly approximated by polynomials in $z$.
:::
