---
schema: qual/card@1
id: P-TRIV-CA32
kind: problem
title: Integral representation and functional equation of the Riemann zeta function
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 32, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The analytic-continuation step explicitly asks for the contour in Figure 5. Flash preserves only the image placeholder/caption, so that figure-dependent contour data remain unresolved.
---

::: problem
ORiemann's zeta function is defined as $\begin{array} { r } { \zeta ( z ) = \sum _ { n = 1 } ^ { \infty } n ^ { - z } } \end{array}$

•For which values of z does this converge?

Show that the zeta function admits the integral representation

$$
\zeta ( z ) = \frac { 1 } { \Gamma ( z ) } \int _ { 0 } ^ { \infty } \frac { t ^ { z - 1 } } { e ^ { t } - 1 } \mathrm { d } t
$$

hint: the relation $\textstyle \sum _ { m = 1 } ^ { \infty } e ^ { - m t } = { \frac { e ^ { - t } } { 1 - e ^ { - t } } }$ might prove useful.

• Now we take the contour of figure 5. Since we want to allow non integer values of z, there is a branch cut along the positive real axis.
What is $\begin{array} { r } { { \frac { 1 } { \Gamma ( z ) } } \int _ { 0 } ^ { \infty } { \frac { t ^ { z - 1 } } { e ^ { t } - 1 } } \mathrm { d } t } \end{array}$ along this contour?

For $z < 0$ we can deform the contour by sending the radius of the circle D to infinity; the price to pay is that, to compute I, we have to evaluate an infinite number of poles, but this can be done.
By comparing this result to what you did in the previous step, you should find that

$$
\zeta ( z ) = \zeta ( 1 - z ) \frac { e ^ { 3 \pi i z / 2 } - e ^ { \pi i z / 2 } } { e ^ { 2 \pi i z } - 1 } \frac { ( 2 \pi ) ^ { z } } { \Gamma ( z ) } .
$$

At this point the source supplies Figure 5 as the contour for the analytic-continuation argument; its graphical content is not present in the deterministic extraction.

•Using the formula you just found, show that $\zeta ( - 1 ) = - { \frac { 1 } { 1 2 } }$ . Notice that this doesn't mean that $1 + 2 + 3 + 4 + \ldots = - { \frac { 1 } { 1 2 } }$ , since that $\textstyle \zeta ( z ) = \sum _ { n = 1 } ^ { \infty } n ^ { - z }$ is valid only for $z > 1$ . On a side note, this is the reason why string theory (without supersymmetry) needs 26 spacetime dimensions.
:::
