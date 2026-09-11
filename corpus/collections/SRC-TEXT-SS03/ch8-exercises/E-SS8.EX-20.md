---
schema: qual/card@1
id: E-SS8.EX-20
kind: problem
title: "Other examples of elliptic integrals providing conformal maps from the upper hal"
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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired the missing exclusion lambda=0, where the branch points coalesce and the rectangle statement fails.
---

::: exercise
20. Other examples of elliptic integrals providing conformal maps from the upper half-plane to rectangles are given below.

(a) The function

$$
\int_ {0} ^ {z} \frac {d \zeta}{\sqrt {\zeta (\zeta - 1) (\zeta - \lambda)}}, \quad \mathrm{with} \lambda \in \mathbb {R} \mathrm{and} \lambda \neq 1
$$

maps the upper half-plane conformally to a rectangle, one of whose vertices is the image of the point at infinity.

(b) In the case $\lambda = - 1$ , the image of

$$
\int_ {0} ^ {z} \frac {d \zeta}{\sqrt {\zeta (\zeta^ {2} - 1)}}
$$

is a square whose side lengths are $\textstyle { \frac { \Gamma ^ { 2 } ( 1 / 4 ) } { 2 { \sqrt { 2 \pi } } } }$
:::

::: solution
For part (a), the finite branch points must be distinct, so the intended hypothesis is $\lambda\in\mathbb R\setminus\{0,1\}$. Choose the branch of
\[
F'(z)=\frac1{\sqrt{z(z-1)(z-\lambda)}}
\]
that is holomorphic on $\mathbb H$. The Schwarz--Christoffel formula says that a factor $(z-a)^{-\beta}$ at a real prevertex produces interior angle $(1-\beta)\pi$. At each of $0,1,\lambda$ the exponent is $-1/2$, so each corresponding angle is $\pi/2$.

At infinity put $w=1/z$. Since $F'(z)=O(z^{-3/2})$,
\[
\frac{d}{dw}F(1/w)=-w^{-2}F'(1/w)=O(w^{-1/2}),
\]
so infinity is a fourth prevertex with angle $\pi/2$. Hence the image is a quadrilateral with four right angles, therefore a rectangle.

For $\lambda=-1$,
\[
F'(z)=\frac1{\sqrt{z(z^2-1)}}.
\]
The symmetry $z\mapsto -z$ interchanges the two finite intervals adjacent to $0$, and $z\mapsto1/z$ interchanges the corresponding opposite sides; hence the rectangle has equal adjacent side lengths and is a square.

One side has length
\[
L=\int_0^1\frac{dx}{\sqrt{x(1-x^2)}}.
\]
With $t=x^2$,
\[
L=\frac12\int_0^1 t^{-3/4}(1-t)^{-1/2}\,dt
=\frac12 B\left(\frac14,\frac12\right)
=\frac{\Gamma(1/4)\sqrt\pi}{2\Gamma(3/4)}.
\]
Euler's reflection formula at $1/4$ gives
\[
\Gamma(1/4)\Gamma(3/4)=\pi\sqrt2,
\]
and therefore
\[
L=\frac{\Gamma(1/4)^2}{2\sqrt{2\pi}}.
\]
:::
