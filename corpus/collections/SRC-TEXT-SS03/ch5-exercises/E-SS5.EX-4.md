---
schema: qual/card@1
id: E-SS5.EX-4
kind: exercise
title: "SS 5.4: Growth and zeros of a product with geometrically spaced zeros"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
---

::: exercise
4. Let $t > 0$ be given and fixed, and define $F ( z )$ by

$$

F (z) = \prod_ {n = 1} ^ {\infty} (1 - e ^ {- 2 \pi n t} e ^ {2 \pi i z}).

$$

Note that the product defines an entire function of $z ,$

(a) Show that $| F ( z ) | \leq A e ^ { a | z | ^ { 2 } }$ , hence F is of order 2.

(b) $F$ vanishes exactly when $z = - i n t + m$ for $n \geq 1$ and $n ,$ m integers. Thus, if $z _ { n }$ is an enumeration of these zeros we have

$$

\sum \frac {1}{| z _ {n} | ^ {2}} = \infty \quad \text { but } \quad \sum \frac {1}{| z _ {n} | ^ {2 + \epsilon}} <   \infty .

$$

[Hint: To prove (a), write $F ( z ) = F _ { 1 } ( z ) F _ { 2 } ( z )$ where

$$

F _ {1} (z) = \prod_ {n = 1} ^ {N} (1 - e ^ {- 2 \pi n t} e ^ {2 \pi i z}) \quad \text { and } \quad F _ {2} (z) = \prod_ {n = N + 1} ^ {\infty} (1 - e ^ {- 2 \pi n t} e ^ {2 \pi i z}).

$$

Choose $N \approx c | z |$ with c appropriately large. Then, since

$$

\left(\sum_ {N + 1} ^ {\infty} e ^ {- 2 \pi n t}\right) e ^ {2 \pi | z |} \leq 1,

$$

one has $| F _ { 2 } ( z ) | \le A$ . However,

$$

| 1 - e ^ {- 2 \pi n t} e ^ {2 \pi i z} | \leq 1 + e ^ {2 \pi | z |} \leq 2 e ^ {2 \pi | z |}.

$$

Thus $| F _ { 1 } ( z ) | \le 2 ^ { N } e ^ { 2 \pi N | z | } \le e ^ { c ^ { \prime } | z | ^ { 2 } }$ . Note that a simple variant of the function $F$ arises as a factor in the triple product formula for the Jacobi theta function $\Theta _ { i }$ taken up in Chapter 10.]
:::
