---
schema: qual/card@1
id: E-SS9.EX-5
kind: exercise
title: "SS 9.5: The Weierstrass sigma function"
classification:
  areas:
  - complex-analysis
  topics: ['Elliptic Functions', 'Weierstrass P', 'Lattices']
relations: []
review: draft
---

::: exercise
5. Let $\sigma ( z )$ be the canonical product

$$
\sigma (z) = z \prod_ {j = 1} ^ {\infty} E _ {2} (z / \tau_ {j}),
$$

where $\tau _ { j }$ is an enumeration of the periods $\{ n + m \tau \}$ with $( n , m ) \neq ( 0 , 0 )$ , and $E _ { 2 } ( z ) = ( 1 - z ) e ^ { z + z ^ { 2 } / 2 }$

(a) Show that $\sigma ( z )$ is an entire function of order 2 that has simple zeros at all the periods $n + m \tau$ , and vanishes nowhere else.

(b) Show that

$$
\frac {\sigma^ {\prime} (z)}{\sigma (z)} = \frac {1}{z} + \sum_ {(n, m) \neq (0, 0)} \left[ \frac {1}{z - n - m \tau} + \frac {1}{n + m \tau} + \frac {z}{(n + m \tau) ^ {2}} \right],
$$

and that this series converges whenever z is not a lattice point.

(c) Let $L ( z ) = - \sigma ^ { \prime } ( z ) / \sigma ( z )$ . Then

$$
L ^ {\prime} (z) = \frac {(\sigma^ {\prime} (z)) ^ {2} - \sigma (z) \sigma^ {\prime \prime} (z)}{(\sigma (z)) ^ {2}} = \wp (z).
$$
:::
