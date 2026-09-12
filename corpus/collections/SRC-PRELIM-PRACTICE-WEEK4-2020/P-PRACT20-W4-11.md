---
schema: qual/card@1
id: P-PRACT20-W4-11
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 11"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
If V, W are 2-dimensional subspaces of $\mathbb { R } ^ { 4 }$ , what are the possible dimensions of $V \cap W ?$ What if $V , W$ are 4-dimensional subspaces of $\mathbb { R } ^ { 7 } ?$
:::

::: {.solution}
Suppose that $V , W$ are subspaces of $\mathbb { R } ^ { n }$ . We have $V \cap W \subseteq V , W$ so the dimension of the intersection can no higher than that of $V$ or $W$ . But we also have the dimension formula

$$
\dim \left( V \cap W \right) = \dim \left( V \right) + \dim \left( W \right) - \dim \left( \operatorname { s p a n } \left( V \cup W \right) \right)
$$

and span $( V \cup W ) \subset \mathbb { R } ^ { n }$ . Thus

$$
\dim \left( V \cap W \right) \geq \dim \left( V \right) + \dim \left( W \right) - n .
$$

Applying both these results, we see in the first case

$$
0 \leq \dim \left( V \cap W \right) \leq 2
$$

and in the latter case

$$
1 \leq \dim \left( V \cap W \right) \leq 4 .
$$

It’s easy to achieve any value in between the bounds just using the coordinate vectors.
For example, in the first case,

 if $V = { \mathrm { s p a n } } \left( e _ { 1 } , e _ { 2 } \right)$ and $W = \operatorname { s p a n } \left( e _ { 3 } , e _ { 4 } \right)$ , then dim $( V \cap W ) = 0$

 if $V = { \mathrm { s p a n } } \left( e _ { 1 } , e _ { 2 } \right)$ and $W = \mathrm { s p a n } \left( e _ { 1 } , e _ { 4 } \right)$ , then dim $( V \cap W ) = 1$

 if $V = { \mathrm { s p a n } } \left( e _ { 1 } , e _ { 2 } \right)$ and $W = \mathrm { s p a n } \left( e _ { 1 } , e _ { 2 } \right)$ , then dim $( V \cap W ) = 2$
:::
