---
schema: qual/card@1
id: P-BKF04-7B
kind: problem
title: UC Berkeley Fall 2004 prelim 7B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $n \geq 1$ , and let $M _ { n } ( \mathbb { R } )$ be the ring of $n \times n$ matrices over the field of real numbers. What is the dimension of the subspace V of $M _ { n } ( \mathbb { R } )$ spanned by the matrices of the form $A B - B A$ where A, $B \in M _ { n } ( \mathbb { R } ) ?$
:::

::: {.solution}
Let $E _ { i j }$ be the matrix with 1 in the $( i , j )$ position and zeros elsewhere. Since $A B - B A$ is linear in each of A and $B ,$ the subspace V equals the span of $A B - B A$ where A is some $E _ { i j }$ and B is some $E _ { k \ell }$ . We have

$$
E _ { i j } E _ { k \ell } - E _ { k \ell } E _ { i j } = { \left\{ \begin{array} { l l } { 0 } & { { \mathrm { i f ~ } } j \neq k { \mathrm { ~ a n d ~ } } i \neq \ell } \\ { E _ { i \ell } } & { { \mathrm { i f ~ } } j = k { \mathrm { ~ a n d ~ } } i \neq \ell } \\ { - E _ { k j } } & { { \mathrm { i f ~ } } j \neq k { \mathrm { ~ a n d ~ } } i = \ell } \\ { E _ { i i } - E _ { j j } } & { { \mathrm { i f ~ } } j = k { \mathrm { ~ a n d ~ } } i = \ell . } \end{array} \right. }
$$

Varying $i , j , k , \ell ,$ , we find that V is spanned by the set of all $E _ { i j }$ with $i \neq j$ together with the set of $E _ { i i } - E _ { i + 1 , i + 1 }$ for $i = 1 , \ldots , n - 1$ These matrices are clearly independent, so dim $V = ( n ^ { 2 } - n ) + ( n - 1 ) = n ^ { 2 } - 1$ . (A more elegant way to describe V is as the space of trace-zero matrices.)
:::
