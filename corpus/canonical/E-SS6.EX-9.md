---
schema: qual/card@1
id: E-SS6.EX-9
kind: exercise
title: "The hypergeometric series  was defined in Exercise 16 of Chapter 1"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
---

::: exercise
9. The hypergeometric series $F ( \alpha , \beta , \gamma ; z )$ was defined in Exercise 16 of Chapter 1. Show that

$$

F (\alpha , \beta , \gamma ; z) = \frac {\Gamma (\gamma)}{\Gamma (\beta) \Gamma (\gamma - \beta)} \int_ {0} ^ {1} t ^ {\beta - 1} (1 - t) ^ {\gamma - \beta - 1} (1 - z t) ^ {- \alpha} d t.

$$

Here $\alpha > 0 , \beta > 0 , \gamma > \beta$ , and $| z | < 1$

Show as a result that the hypergeometric function, initially defined by a power series convergent in the unit disc, can be continued analytically to the complex plane slit along the half-line $\lbrack 1 , \infty )$

Note that

$$

\log (1 - z) = - z F (1, 1, 2; z),

$$

$$

e ^ {z} = \lim _ {\beta \rightarrow \infty} F (1, \beta , 1; z / \beta),

$$

$$

(1 - z) ^ {- \alpha} = F (\alpha , 1, 1; z).

$$

[Hint: To prove the integral identity, expand $( 1 - z t ) ^ { - \alpha }$ as a power series.]
:::
