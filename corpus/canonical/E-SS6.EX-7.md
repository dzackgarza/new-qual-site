---
schema: qual/card@1
id: E-SS6.EX-7
kind: exercise
title: "SS 6.7: The Beta function and its relation to Gamma"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
solved: false
---

::: exercise
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
