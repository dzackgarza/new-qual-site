---
schema: qual/card@1
id: E-SS1.EX-16
kind: problem
title: "Radii of convergence for (log n)-squared and factorial coefficients"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
---

::: exercise
16. Determine the radius of convergence of the series $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n } z ^ { n }$ when:

(a) $a _ { n } = ( \log n ) ^ { 2 }$

(b) $a _ { n } = n !$

(c) $\textstyle a _ { n } = { \frac { n ^ { 2 } } { 4 ^ { n } + 3 n } }$

(d) $a _ { n } = ( n ! ) ^ { 3 } / ( 3 n ) !$ [Hint: Use Stirling’s formula, which says that $n ! \sim c n ^ { n + \frac { 1 } { 2 } } e ^ { - n }$ for some $c > 0 . . ]$

(e) Find the radius of convergence of the hypergeometric series

$$
F (\alpha , \beta , \gamma ; z) = 1 + \sum_ {n = 1} ^ {\infty} \frac {\alpha (\alpha + 1) \cdots (\alpha + n - 1) \beta (\beta + 1) \cdots (\beta + n - 1)}{n ! \gamma (\gamma + 1) \cdots (\gamma + n - 1)} z ^ {n}.
$$

Here $\alpha , \beta \in \mathbb { C }$ and $\gamma \neq 0 , - 1 , - 2 , . . .$

4. Exercises

(f) Find the radius of convergence of the Bessel function of order r:

$$
J _ {r} (z) = \left(\frac {z}{2}\right) ^ {r} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{n ! (n + r) !} \left(\frac {z}{2}\right) ^ {2 n},
$$

where r is a positive integer.
:::
