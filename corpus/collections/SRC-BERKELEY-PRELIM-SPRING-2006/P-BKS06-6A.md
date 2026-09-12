---
schema: qual/card@1
id: P-BKS06-6A
kind: problem
title: UC Berkeley Spring 2006 prelim 6A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $u \colon  { \mathbb { R } } \to  { \mathbb { R } }$ be a function for which there exists $B > 0$ such that

$$
\sum _ { k = 1 } ^ { N - 1 } | u ( x _ { k + 1 } ) - u ( x _ { k } ) | ^ { 2 } \leq B
$$

for all finite increasing sequences $x _ { 1 } < x _ { 2 } < \dots < x _ { N }$ . Show that u has at most countably many discontinuities.
:::

::: {.solution}
Let A be the set of points of discontinuity for u. Then

$$
A = \bigcup _ { n \geq 1 } A _ { n }
$$

where

$$
A _ { n } = \{ x \in \mathbb { R } : | \operatorname* { l i m } _ { y \to x } \operatorname* { s u p } u ( y ) - \operatorname* { l i m } _ { y \to x } \operatorname* { i n f } u ( y ) | > \frac { 1 } { n } \}
$$

To prove that A is countable, we will prove that

$$
\left| A _ { n } \right| \leq 4 n ^ { 2 } B .
$$

If $y _ { 1 } < y _ { 2 } < \dots < y _ { N }$ are in $A _ { n }$ then we can choose a strictly increasing sequence $( x _ { k } ) _ { k = 1 } ^ { 2 N }$ such that

$$
x _ { 2 k - 1 } < y _ { k } < x _ { 2 k }
$$

and

$$
| u ( x _ { 2 k } ) - u ( x _ { 2 k - 1 } ) | > \frac { 1 } { 2 n }
$$

for $k = 1 , \ldots , N$ . Summing over k gives the inequality on the right in

$$
B \geq \sum _ { k = 1 } ^ { 2 N - 1 } | u ( x _ { k + 1 } ) - u ( x _ { k } ) | ^ { 2 } \geq \sum _ { k = 1 } ^ { N } | u ( x _ { 2 k } ) - u ( x _ { 2 k - 1 } ) | ^ { 2 } \geq N \left( \frac { 1 } { 2 n } \right) ^ { 2 } .
$$

Hence $N \leq 4 n ^ { 2 } B .$ , which concludes the proof.
:::
