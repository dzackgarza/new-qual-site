---
schema: qual/card@1
id: E-SS8.EX-23
kind: problem
title: "SS 8.23: A conformal map onto a regular polygon"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
23. If

$$
F (z) = \int_ {1} ^ {z} \frac {d \zeta}{(1 - \zeta^ {n}) ^ {2 / n}},
$$

then $F$ maps the unit disc conformally onto the interior of a regular polygon with n sides and perimeter

$$
2 ^ {\frac {n - 2}{n}} \int_ {0} ^ {\pi} (\sin \theta) ^ {- 2 / n} d \theta .
$$
:::

::: solution
Factor
\[
1-z^n=\prod_{k=0}^{n-1}(1-\omega^k z),
\qquad \omega=e^{2\pi i/n}.
\]
Thus
\[
F'(z)=(1-z^n)^{-2/n}
\]
has Schwarz--Christoffel exponent $-2/n$ at each of the $n$ equally spaced boundary points $\omega^k$. Hence every image vertex has interior angle
\[
\left(1-\frac2n\right)\pi=\frac{n-2}{n}\pi.
\]
Moreover $F'(\omega z)=F'(z)$, and therefore
\[
F(\omega z)-F(0)=\omega\bigl(F(z)-F(0)\bigr).
\]
So the image polygon is invariant under rotation by $2\pi/n$. A polygon with $n$ equal angles and this rotational symmetry is a regular $n$-gon.

It remains to compute its perimeter. On the boundary arc from $1$ to $e^{2\pi i/n}$, write $z=e^{i\theta}$, $0\le\theta\le2\pi/n$. Its image is one side, of length
\[
\begin{aligned}
L
&=\int_0^{2\pi/n}|1-e^{in\theta}|^{-2/n}\,d\theta\\
&=2^{-2/n}\int_0^{2\pi/n}\sin(n\theta/2)^{-2/n}\,d\theta\\
&=\frac{2^{1-2/n}}{n}\int_0^\pi(\sin u)^{-2/n}\,du.
\end{aligned}
\]
Multiplying by $n$ gives the perimeter
\[
2^{1-2/n}\int_0^\pi(\sin u)^{-2/n}\,du
=2^{(n-2)/n}\int_0^\pi(\sin u)^{-2/n}\,du.
\]
:::
