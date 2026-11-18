---
schema: qual/card@1
id: E-SS8.EX-20
kind: problem
title: Elliptic integrals mapping the upper half-plane onto rectangles
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Schwarz-Christoffel
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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Each step re-read: the three finite prevertices carry exponent
    -1/2 and hence right angles; infinity is a fourth prevertex with the same exponent, computed
    from d/dw F(1/w) = -w^{-2} F'(1/w); four right angles give a rectangle; the symmetries z -> -z
    and z -> 1/z make adjacent sides equal when lambda = -1; and the side length is the Beta
    integral B(1/4,1/2)/2, evaluated with Euler's reflection formula. The card keeps the recorded
    defect of the printed statement: as printed lambda may be 0 or 1, where two branch points
    coincide, and the intended hypothesis lambda not in {0,1} is what the argument uses. Not
    claimed: the rectangle's side ratio for general lambda.
---

::: {.exercise}
Other examples of elliptic integrals providing conformal maps from the upper half-plane to rectangles are given below.

(a) The function
$$
\int_0^z \frac{d\zeta}{\sqrt{\zeta(\zeta - 1)(\zeta - \lambda)}}, \quad \text{with } \lambda \in \RR \text{ and } \lambda \neq 1
$$
maps the upper half-plane conformally to a rectangle, one of whose vertices is the image of the point at infinity.

(b) In the case $\lambda = -1$, the image of
$$
\int_0^z \frac{d\zeta}{\sqrt{\zeta(\zeta^2 - 1)}}
$$
is a square whose side lengths are $\frac{\Gamma^2(1/4)}{2\sqrt{2\pi}}$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 8 Exercise 20. The card records a defect in the printed statement of part (a): as printed it allows $\lambda=0$ or $\lambda=1$, at which two of the three branch points coincide; the intended hypothesis is $\lambda\in\RR\setminus\{0,1\}$, and that is what is used.

::: pf

::: {.pf-step #prevertices}
In part (a) the finite branch points $0,1,\lambda$ are distinct, and each contributes the exponent $-\tfrac12$ in Schwarz--Christoffel.

::: pf-proof
$F'(z)=z^{-1/2}(z-1)^{-1/2}(z-\lambda)^{-1/2}$; the singularities are the three listed points, each with exponent $-\tfrac12$ in the sense of a factor $(z-a)^{-\beta}$ with $\beta=\tfrac12$.
:::

:::

::: {.pf-step #angles}
Each of the three finite prevertices gives interior angle $\pi/2$.

::: pf-proof
The Schwarz--Christoffel formula assigns interior angle $(1-\beta)\pi$ to a prevertex carrying the factor $(z-a)^{-\beta}$; here $\beta=\tfrac12$, so the angle is $\pi/2$.
:::

:::

::: {.pf-step #infinity}
Infinity is a fourth prevertex, also with angle $\pi/2$.

::: pf-proof
With $w=1/z$ one has $F'(z)=O(z^{-3/2})$ near $z=\infty$, so
$\frac{d}{dw}F(1/w)=-w^{-2}F'(1/w)=O(w^{-1/2})$, the exponent $-\tfrac12$ of a prevertex at $w=0$. Hence the angle there is also $\pi/2$, and the image of the point at infinity is a vertex of the image.
:::

:::

::: {.pf-step #rectangle}
The image is a rectangle.

::: pf-proof
$F$ is a conformal map of the upper half-plane onto a polygon-like region whose boundary consists of four arcs meeting at right angles, by steps [](#angles){.pf-ref} and [](#infinity){.pf-ref}; a quadrilateral with four right angles is a rectangle.
:::

:::

::: {.pf-step #square}
If $\lambda=-1$ the rectangle is a square.

::: pf-proof
Then $F'(z)=1/\sqrt{z(z^{2}-1)}$, and the reflection $z\mapsto-z$ interchanges the two finite intervals adjacent to $0$, while $z\mapsto1/z$ interchanges the corresponding opposite sides of the image; both symmetries preserve the integral's modulus, so adjacent sides have equal length and the rectangle is a square.
:::

:::

::: {.pf-step #length}
A side of the square has length $L=\dfrac{\Gamma(1/4)^{2}}{2\sqrt{2\pi}}$.

::: pf-proof
One side is the image of the interval $(0,1)$, so $L=\int_{0}^{1}\frac{dx}{\sqrt{x(1-x^{2})}}$. Substituting $x=t^{1/2}$, $dx=\tfrac12t^{-1/2}dt$ and $\sqrt{x(1-x^{2})}=t^{1/4}(1-t)^{1/2}$, so
$L=\tfrac12\int_{0}^{1}t^{-3/4}(1-t)^{-1/2}dt=\tfrac12B\bigl(\tfrac14,\tfrac12\bigr)=\dfrac{\Gamma(1/4)\sqrt\pi}{2\Gamma(3/4)}$.
Euler's reflection formula at $\tfrac14$ gives $\Gamma(\tfrac14)\Gamma(\tfrac34)=\pi\sqrt2$; substituting $\Gamma(\tfrac34)=\pi\sqrt2/\Gamma(\tfrac14)$ gives $L=\dfrac{\Gamma(1/4)^{2}}{2\sqrt{2\pi}}$.
:::

:::

::: {.pf-step}
Parts (a) and (b) hold.

::: pf-proof
Steps [](#rectangle){.pf-ref} and [](#square){.pf-ref} give the two assertions, and step [](#length){.pf-ref} gives the side length of the square in the case $\lambda=-1$:
$$
\boxed{\text{the elliptic integral maps }\halfplane\text{ to a rectangle (a square for }\lambda=-1),\text{ with }L=\frac{\Gamma(1/4)^{2}}{2\sqrt{2\pi}}.}
$$
:::

:::

:::
:::
