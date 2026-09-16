---
schema: qual/card@1
id: P-BKF09-1A
kind: problem
title: Generating function $\sum p(k)z^k$ of a polynomial sequence is rational
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $p ( k )$be a degree n polynomial with complex coefficients defined by$$p ( k ) = p _ { 0 } + { \binom { k } { 1 } } p _ { 1 } + { \binom { k } { 2 } } p _ { 2 } + \cdot \cdot \cdot + { \binom { k } { n } } p _ { n } .$$Define$$f ( z ) = \sum _ { k = 0 } ^ { \infty } p ( k ) z ^ { k } .$$Find the radius of convergence of the power series, prove that$f ( z )$is a rational function restricted to the disk of convergence, and give a formula for$f ( z )$
:::

::: {.solution}
We have

$$\left( \frac { d } { d z } \right) ^ { n } \frac { 1 } { 1 - z } = \frac { n ! } { ( 1 - z ) ^ { n + 1 } } .$$Since$\begin{array} { r } { \frac { 1 } { 1 - z } = \sum _ { k = 0 } ^ { \infty } z ^ { k } } \end{array}$for$| z | < 1$, we also have for$| z | < 1$$${ \frac { n ! } { ( 1 - z ) ^ { n + 1 } } } = \left( { \frac { d } { d z } } \right) ^ { n } \sum _ { k = 0 } ^ { \infty } z ^ { k } = \sum _ { k = 0 } ^ { \infty } k ( k - 1 ) \cdot \cdot \cdot ( k - n + 1 ) z ^ { k - n } = { \frac { n ! } { ( 1 - z ) ^ { n + 1 } } } .$$We may rewrite this as$${ \frac { z ^ { n } } { ( 1 - z ) ^ { n + 1 } } } = \sum _ { k = 0 } ^ { \infty } { \binom { k } { n } } z ^ { k } .$$Thus,$$f ( z ) = \sum _ { k = 0 } ^ { \infty } \sum _ { j = 0 } ^ { n } p _ { j } { \binom { k } { n } } z ^ { k } = \sum _ { j = 0 } ^ { n } p _ { j } \sum _ { k = 0 } ^ { \infty } { \binom { k } { n } } z ^ { k } = \sum _ { j = 0 } ^ { n } p _ { j } { \frac { z ^ { j } } { ( 1 - z ) ^ { j + 1 } } } ,$$which is a sum of rational functions, and is therefore rational.
The series converges to this rational function in the disk$| z | < 1$, and the rational function has a pole on its boundary at$z = 1$(unless all$p _ { j } = 0 )$.
Thus the convergence radius$R = 1$if not all$p _ { j } = 0$(and$R = \infty$ otherwise).
:::
