---
schema: qual/card@1
id: E-SS2.EX-7
kind: exercise
title: "The image diameter bounds twice the derivative at the center"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
---

::: exercise
7. Suppose $f : \mathbb { D } \to \mathbb { C }$ is holomorphic.
   Show that the diameter $d =$ $\begin{array} { r } { \operatorname* { s u p } _ { z , w \in \mathbb { D } } | f ( z ) - f ( w ) | } \end{array}$ of the image of f satisfies

$$
2 | f ^ {\prime} (0) | \leq d.
$$

Moreover, it can be shown that equality holds precisely when f is linear, $f ( z ) =$ $a _ { 0 } + a _ { 1 } z$

Note.
In connection with this result, see the relationship between the diameter of a curve and Fourier series described in Problem 1, Chapter 4, Book I.

[Hint: $\begin{array} { r } { 2 f ^ { \prime } ( 0 ) = \frac { 1 } { 2 \pi i } \int _ { | \zeta | = r } \frac { f ( \zeta ) - f ( - \zeta ) } { \zeta ^ { 2 } } d \zeta } \end{array}$ whenever $0 < r < 1 . ]$
:::
