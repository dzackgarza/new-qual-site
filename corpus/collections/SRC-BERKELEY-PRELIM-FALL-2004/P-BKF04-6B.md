---
schema: qual/card@1
id: P-BKF04-6B
kind: problem
title: UC Berkeley Fall 2004 prelim 6B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose that $f ( z )$ is holomorphic on all of C except for a pole at $z = 0$ . Prove that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { n } } \sum _ { k = 1 } ^ { n } f \left( { \frac { 1 } { n } } e ^ { 2 \pi i k / n } \right)
$$

exists.
:::

::: {.solution}
If f were holomorphic at 0, then each term in the sum would be $f ( 0 ) + O ( 1 / n )$ where the implied constant is independent of k and n, so the average of these f-values would also be $f ( 0 ) + O ( 1 / n )$ , which tends to $f ( 0 )$ as $n \to \infty$

In general, using the Laurent series of f , we may write f as a finite linear combination of functions of the form $z ^ { - m }$ for $m > 0$ plus one function that is holomorphic at 0. By linearity, it remains to prove the statement for $f ( z ) = z ^ { - m }$ . In this case, the sum in the problem is a finite geometric series, and its value is 0 when $n > m$ .
:::
