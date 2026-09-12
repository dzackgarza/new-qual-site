---
schema: qual/card@1
id: P-BKS06-1A
kind: problem
title: UC Berkeley Spring 2006 prelim 1A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let G be the subgroup of the free abelian group $\mathbb { Z } ^ { 4 }$ consisting of all integer vectors $( x , y , z , w )$ such that $2 x + 3 y + 5 z + 7 w = 0$

(a) Determine a linearly independent subset of G which generates $G$ as an abelian group.

(b) Show that $\mathbb { Z } ^ { 4 } / G$ is a free abelian group and determine its rank.
:::

::: {.solution}
(b) The linear map

$$
\mathbb { Z } ^ { 4 } \mapsto \mathbb { Z } , ( x , y , z , w ) \mapsto 2 x + 3 y + 5 z + 7 w
$$

has kernel G, and is onto because 2 and 3 are relatively prime.
Hence $\mathbb { Z } ^ { 4 } / G$ is isomorphic to the image $\mathbb { Z } ,$ which is a free abelian group of rank 1.

(a) There is a sequence of elementary column operations over $\mathbb { Z }$ (not involving divisions) that transforms the 1 × 4-matrix $( 2 ~ \mathrm { ~ 3 ~ ~ 5 ~ ~ 7 ~ } )$ into $\left( \begin{array} { c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right)$ . For instance, subtract 3 times the first column from the fourth to get $\left( 2 \ \ \textrm { 3 } \ 5 \ \textrm { 1 } \right)$ , and then subtract appropriate multiples of the fourth from each of the first three columns to make them zero.
The same sequence of operations applied to the $4 \times 4$ identity matrix eventually yields a matrix

$$
U = \left( \begin{array} { l l l l } { { 7 } } & { { 9 } } & { { 1 5 } } & { { - 3 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { - 2 } } & { { - 3 } } & { { - 5 } } & { { 1 } } \end{array} \right)
$$

such that

$$
\left( 2 \phantom { 0 } 3 \phantom { 0 } 5 \phantom { 0 } 7 \right) U = \left( 0 \phantom { 0 } 0 \phantom { 0 } 0 \phantom { 0 } 1 \right) .
$$

Because of the way U was constructed, it has an inverse $U ^ { - 1 }$ with integer entries.

The first three columns of U are in G, and we claim that they span $G$ as an abelian group.
Suppose $\mathbf { v } \in G$ . Then

$$
\begin{array} { r }  0 = \left( 2 \begin{array} { l l l } { 3 } & { 5 } & { 7 \right) \mathbf { v } = \left( 0 } & { 0 } & { 0 } & { 1 \right) U ^ { - 1 } \mathbf { v } , } \end{array} \end{array}
$$

so $U ^ { - 1 } \mathbf { v } = { \binom { \alpha } { \beta } }$ for some $\alpha , \beta , \gamma \in \mathbb { Z }$ . Thus

$$
\mathbf { v } = U \left( \begin{array} { l } { \alpha } \\ { \beta } \\ { \gamma } \\ { 0 } \end{array} \right) ,
$$

which is an integer combination of the first three columns of $U$ .

Finally these first three columns of U are linearly independent, since U is invertible.
:::
