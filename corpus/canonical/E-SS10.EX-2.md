---
schema: qual/card@1
id: E-SS10.EX-2
kind: exercise
title: "SS 10.2: The generating function of the Fibonacci numbers"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
---

::: exercise
2. Consider the Fibonacci numbers $\{ F _ { n } \} _ { n = 0 } ^ { \infty }$ , defined by the two initial values $F _ { 0 } = 0 , F _ { 1 } = 1$ and the recursion relation

$$

F _ {n} = F _ {n - 1} + F _ {n - 2} \quad \mathrm{for} n \geq 2.

$$

(a) Consider the generating function $\textstyle F ( x ) = \sum _ { n = 0 } ^ { \infty } F _ { n } x ^ { n }$ associated to $\{ F _ { n } \}$ , and prove that

$$

F (x) = x ^ {2} F (x) + x F (x) + x

$$

for all x in a neighborhood of 0.

(b) Show that the polynomial $q ( x ) = 1 - x - x ^ { 2 }$ can be factored as

$$

q (x) = (1 - \alpha x) (1 - \beta x),

$$

where α and $\beta$ are the roots of the polynomial $p ( x ) = x ^ { 2 } - x - 1$

(c) Expand the expression for F in partial fractions and obtain

$$

F (x) = \frac {x}{1 - x - x ^ {2}} = \frac {x}{(1 - \alpha x) (1 - \beta x)} = \frac {A}{1 - \alpha x} + \frac {B}{1 - \beta x},

$$

where $A = 1 / ( \alpha - \beta )$ and $B = 1 / ( \beta - \alpha )$

(d) Conclude that $F _ { n } = A \alpha ^ { n } + B \beta ^ { n }$ for $n \geq 0$ . The two roots of $p$ are actually

$$

\alpha = \frac {1 + \sqrt {5}}{2} \quad \mathrm{and} \quad \beta = \frac {1 - \sqrt {5}}{2},

$$

so that $A = 1 / \sqrt { 5 }$ and $B = - 1 / \sqrt { 5 } .$

The number $1 / \alpha = ( \sqrt { 5 } - 1 ) / 2$ , which is known as the golden mean, satisfies the following property: given a line segment $\left[ A C \right]$ of unit length (Figure 2), there exists a unique point B on this segment so that the following proportion holds
:::
