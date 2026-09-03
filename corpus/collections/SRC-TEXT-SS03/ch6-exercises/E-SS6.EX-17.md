---
schema: qual/card@1
id: E-SS6.EX-17
kind: problem
title: "The Mellin transform of a Schwartz function"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
---

::: exercise
17. Let f be an indefinitely diferentiable function on R that has compact support, or more generally, let $f$ belong to the Schwartz space.<sup>4</sup> Consider

$$
I (s) = \frac {1}{\Gamma (s)} \int_ {0} ^ {\infty} f (x) x ^ {- 1 + s} d x.
$$

(a) Observe that $I ( s )$ is holomorphic for $\operatorname { R e } ( s ) > 0$ . Prove that I has an analytic continuation as an entire function in the complex plane.

(b) Prove that $I ( 0 ) = 0$ , and more generally

$$
I (- n) = (- 1) ^ {n} f ^ {(n + 1)} (0) \quad \text {   for   all   } n \geq 0.
$$

[Hint: To prove the analytic continuation, as well as the formulas in the second part, integrate by parts to show that $\begin{array} { r } { I ( s ) = \frac { ( - 1 ) ^ { k } } { \Gamma ( s + k ) } \int _ { 0 } ^ { \infty } f ^ { ( k ) } ( x ) x ^ { s + k - 1 } d x . } \end{array}$
:::
