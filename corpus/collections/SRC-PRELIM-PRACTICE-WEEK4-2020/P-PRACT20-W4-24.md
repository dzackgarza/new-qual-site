---
schema: qual/card@1
id: P-PRACT20-W4-24
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 24"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Show that there are no polynomials $a , b , c , d : \mathbb { R } \to \mathbb { R }$ such that

$$
1 + x y + x ^ { 2 } y ^ { 2 } = a ( x ) b ( y ) + c ( x ) d ( y )
$$

for all $x , y \in \mathbb { R }$
:::

::: {.solution}
First, suppose that $\alpha , \beta , \gamma$ are such that

$$
\alpha \cdot ( 1 ) + \beta \cdot ( x ^ { 2 } + x + 1 ) + \gamma \cdot ( x ^ { 2 } - x + 1 ) = 0 .
$$

Then

$$
\alpha + \beta + \gamma = 0 , \quad \beta - \gamma = 0 , \quad \mathrm { a n d } \quad \beta + \gamma = 0 .
$$

Adding the second and third equation gives $\beta = 0$ . But then the second equation gives $\gamma = 0$ and then the first gives $\alpha = 0$ . This shows that $\left\{ 1 , x ^ { 2 } + x + 1 , x ^ { 2 } - x + 1 \right\}$ are linearly independent in the vector space of real polynomials.

Now supposing such polynomials $a , b , c ,$ d exist, we can plug in $y = 0 , 1$ , −1 and let $b ( 0 ) = b _ { 0 } , b ( 1 ) =$ $b _ { 1 } , b ( - 1 ) = b _ { 2 }$ (and similarly for d) to see that

$$
\begin{array} { r } { 1 = b _ { 0 } a ( x ) + d _ { 0 } c ( x ) , } \\ { x ^ { 2 } + x + 1 = b _ { 1 } a ( x ) + d _ { 1 } c ( x ) , } \\ { x ^ { 2 } - x + 1 = b _ { 2 } a ( x ) + d _ { 2 } c ( x ) . } \end{array}
$$

This is impossible because two vectors $a ( x )$ and $c ( x )$ cannot span a 3-dimensional space.
:::
