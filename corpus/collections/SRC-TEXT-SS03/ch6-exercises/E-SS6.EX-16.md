---
schema: qual/card@1
id: E-SS6.EX-16
kind: exercise
title: "Another proof of the analytic continuation of the zeta function"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
---

::: exercise
16. Use the previous exercise to give another proof that $\zeta ( s )$ is continuable in the complex plane with only singularity a simple pole at $s = 1$

[Hint: Write

$$
\zeta (s) = \frac {1}{\Gamma (s)} \int_ {0} ^ {1} \frac {x ^ {s - 1}}{e ^ {x} - 1} d x + \frac {1}{\Gamma (s)} \int_ {1} ^ {\infty} \frac {x ^ {s - 1}}{e ^ {x} - 1} d x.
$$

The second integral defines an entire function, while

$$
\int_ {0} ^ {1} \frac {x ^ {s - 1}}{e ^ {x} - 1} d x = \sum_ {m = 0} ^ {\infty} \frac {B _ {m}}{m ! (s + m - 1)},
$$

where $B _ { m }$ denotes the $m ^ { \mathrm { t h } }$ Bernoulli number defined by

$$
{\frac {x}{e ^ {x} - 1}} = \sum_ {m = 0} ^ {\infty} {\frac {B _ {m}}{m !}} x ^ {m}.
$$

Then $B _ { 0 } = 1$ , and since $z / ( e ^ { z } - 1 )$ is holomorphic for $| z | < 2 \pi$ , we must have lim s $\begin{array} { r } { \operatorname * { l p } _ { m  \infty } | B _ { m } / m ! | ^ { 1 / m } = 1 / 2 \pi . ] } \end{array}$
:::
