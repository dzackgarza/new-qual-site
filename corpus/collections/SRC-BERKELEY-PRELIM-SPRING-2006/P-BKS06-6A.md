---
schema: qual/card@1
id: P-BKS06-6A
kind: problem
title: Bounded quadratic variation implies at most countably many discontinuities
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $u \colon \RR \to \RR$ be a function for which there exists $B > 0$ such that
$$
\sum_{k=1}^{N-1} \abs{u(x_{k+1}) - u(x_{k})}^{2} \leq B
$$
for all finite increasing sequences $x_{1} < x_{2} < \cdots < x_{N}$. Show that $u$ has at most countably many discontinuities.
:::

::: {.solution}
Let A be the set of points of discontinuity for u. Then

$$
A = \bigcup _ { n \geq 1 } A _ { n }
$$

where

$$
A _ { n } = \{ x \in \RR : \abs{ \operatorname* { l i m } _ { y \to x } \operatorname* { s u p } u ( y ) - \operatorname* { l i m } _ { y \to x } \operatorname* { i n f } u ( y ) } > \frac { 1 } { n } \}
$$

To prove that A is countable, we will prove that

$$
\cardinality{ A _ { n } } \leq 4 n ^ { 2 } B .
$$

If $y _ { 1 } < y _ { 2 } < \dots < y _ { N }$ are in $A _ { n }$ then we can choose a strictly increasing sequence $( x _ { k } ) _ { k = 1 } ^ { 2 N }$ such that

$$
x _ { 2 k - 1 } < y _ { k } < x _ { 2 k }
$$

and

$$
\abs{ u ( x _ { 2 k } ) - u ( x _ { 2 k - 1 } ) } > \frac { 1 } { 2 n }
$$

for $k = 1 , \ldots , N$ . Summing over k gives the inequality on the right in

$$
B \geq \sum _ { k = 1 } ^ { 2 N - 1 } \abs{ u ( x _ { k + 1 } ) - u ( x _ { k } ) } ^ { 2 } \geq \sum _ { k = 1 } ^ { N } \abs{ u ( x _ { 2 k } ) - u ( x _ { 2 k - 1 } ) } ^ { 2 } \geq N \left( \frac { 1 } { 2 n } \right) ^ { 2 } .
$$

Hence $N \leq 4 n ^ { 2 } B .$ , which concludes the proof.
:::
