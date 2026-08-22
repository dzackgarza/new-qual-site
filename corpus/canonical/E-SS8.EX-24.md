---
schema: qual/card@1
id: E-SS8.EX-24
kind: exercise
title: "SS 8.24: Identities among the elliptic integrals K and K-prime"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
solved: false
---

::: exercise
24. The elliptic integrals K and $K ^ { \prime }$ defined for $0 < k < 1$ by

$$

K (k) = \int_ {0} ^ {1} \frac {d x}{((1 - x ^ {2}) (1 - k ^ {2} x ^ {2})) ^ {1 / 2}} \quad \text {and} \quad K ^ {\prime} (k) = \int_ {1} ^ {1 / k} \frac {d x}{((x ^ {2} - 1) (1 - k ^ {2} x ^ {2})) ^ {1 / 2}}

$$

satisfy various interesting identities. For instance:

(a) Show that if $\tilde { k } ^ { 2 } = 1 - k ^ { 2 }$ and $0 < \tilde { k } < 1$ , then

$$

K ^ {\prime} (k) = K (\tilde {k}).

$$

[Hint: Change variables $x = ( 1 - \tilde { k } ^ { 2 } y ^ { 2 } ) ^ { - 1 / 2 }$ in the integral defining $K ^ { \prime } ( k ) . ]$

(b) Prove that if $\tilde { k } ^ { 2 } = 1 - k ^ { 2 }$ , and $0 < \tilde { k } < 1$ , then

$$

K (k) = \frac {2}{1 + \tilde {k}} K \left(\frac {1 - \tilde {k}}{1 + \tilde {k}}\right).

$$

[Hint: Change variables $x = 2 t / ( 1 + \tilde { k } + ( 1 - \tilde { k } ) t ^ { 2 } ) . ]$

(c) Show that for $0 < k < 1$ one has

$$

K (k) = \frac {\pi}{2} F (1 / 2, 1 / 2, 1; k ^ {2}),

$$

where $F$ the hypergeometric series. [Hint: This follows from the integral representation for $F$ given in Exercise 9, Chapter 6.]
:::
