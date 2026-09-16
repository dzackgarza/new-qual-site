---
schema: qual/card@1
id: E-SS3.EX-2
kind: problem
title: "SS 3.2: The integral of 1/(1+x^4)"
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
2. Evaluate the integral

$$
\int_ {- \infty} ^ {\infty} \frac {d x}{1 + x ^ {4}}.
$$

Where are the poles of $1 / ( 1 + z ^ { 4 } ) \ ?$
:::

::: {.solution}
The poles of
\[
\frac1{1+z^4}
\]
are the four roots of $z^4=-1=e^{i\pi}$, namely
\[
e^{i\pi/4},\quad e^{3i\pi/4},\quad e^{5i\pi/4},\quad e^{7i\pi/4}.
\]
Integrate over the upper semicircle. The arc contribution tends to $0$ because the integrand is $O(R^{-4})$ while the arc length is $O(R)$. The poles in the upper half-plane are
\[
z_1=e^{i\pi/4},\qquad z_2=e^{3i\pi/4}.
\]
They are simple, and
\[
\operatorname{Res}_{z=z_j}\frac1{1+z^4}=\frac1{4z_j^3}.
\]
Hence
\[
\int_{-\infty}^{\infty}\frac{dx}{1+x^4}
=2\pi i\left(\frac1{4z_1^3}+\frac1{4z_2^3}\right).
\]
Since
\[
z_1^{-3}=e^{-3i\pi/4}=\frac{-1-i}{\sqrt2},
\qquad
z_2^{-3}=e^{-9i\pi/4}=\frac{1-i}{\sqrt2},
\]
the sum is $-\sqrt2\,i$. Therefore
\[
\int_{-\infty}^{\infty}\frac{dx}{1+x^4}
=2\pi i\left(-\frac{\sqrt2\,i}{4}\right)
=\frac{\pi}{\sqrt2}.
\]
:::
