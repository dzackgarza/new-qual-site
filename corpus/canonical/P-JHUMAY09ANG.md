---
schema: qual/card@1
id: P-JHUMAY09ANG
kind: problem
title: "be a sequence of Lebesgue measurable functions . Suppose there exists such that"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Convergence Theorems
relations: []
review: draft
---

7. Fix $1 \leq p < \infty$ and let $\{ f _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence of Lebesgue measurable functions $f _ { n } : [ 0 , 1 ] \to \mathbb { C }$ . Suppose there exists $f \in L ^ { p } ( [ 0 , 1 ] )$ such that $f _ { n }  f$ in $L ^ { p }$ , that is,

$$
\int _ { [ 0 , 1 ] } | f _ { n } ( x ) - f ( x ) | ^ { p } d x \to 0 .
$$

a) Show that $f _ { n } \to f$ in measure, that is,

$$
\operatorname* { l i m } _ { n \to \infty } \mu ( \{ x \in [ 0 , 1 ] : | f _ { n } ( x ) - f ( x ) | \geq \varepsilon \} ) = 0
$$

for all $\varepsilon > 0$ . (Here $\mu = \mathrm { L e b e s g u e }$ measure.)

b) Show that there is a subsequence $f _ { n _ { k } }$ such that $f _ { n _ { k } } ( x )  f ( x )$ almost everywhere.
