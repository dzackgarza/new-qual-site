---
schema: qual/card@1
id: P-BKS07-2A
kind: problem
title: UC Berkeley Spring 2007 prelim 2A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Find a matrix U such that $U ^ { - 1 } A U = J$ is in Jordan canonical form, where

$$
A = \left( { \begin{array} { r r r } { 0 } & { - 3 } & { 5 } \\ { - 1 } & { - 6 } & { 1 1 } \\ { 0 } & { - 4 } & { 7 } \end{array} } \right) .
$$
:::

::: {.solution}
Expanding by minors along the first column shows that the characteristic determinant is given by

$$
\operatorname* { d e t } ( A - \lambda I ) = - \lambda ^ { 3 } + \lambda ^ { 2 } + \lambda - 1 = - ( \lambda - 1 ) ^ { 2 } ( \lambda + 1 ) .
$$

Thus $\lambda _ { 1 } = - 1$ is an eigenvalue of algebraic (and hence geometric) multiplicity 1 while $\lambda _ { 2 } = 1$ is an eigenvalue of algebraic multiplicity 2. The eigenvectors of A belong to the kernels of the matrices

$$
A - \lambda _ { 1 } I = \left( { \begin{array} { r r r } { 1 } & { - 3 } & { 5 } \\ { - 1 } & { - 5 } & { 1 1 } \\ { 0 } & { - 4 } & { 8 } \end{array} } \right) , \qquad A - \lambda _ { 2 } I = \left( { \begin{array} { r r r } { - 1 } & { - 3 } & { 5 } \\ { - 1 } & { - 7 } & { 1 1 } \\ { 0 } & { - 4 } & { 6 } \end{array} } \right) ,
$$

which can be row-reduced to

$$
P _ { 1 } ( A - \lambda _ { 1 } I ) = \left( { \begin{array} { r r r } { 1 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { - 2 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) , \qquad P _ { 2 } ( A - \lambda _ { 2 } I ) = \left( { \begin{array} { r r r } { 1 } & { 0 } & { - 1 / 2 } \\ { 0 } & { 1 } & { - 3 / 2 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) ,
$$

where $P _ { 1 }$ and $P _ { 2 }$ are products of elementary row operations.
We see that $u _ { 1 } = ( 1 , 2 , 1 ) ^ { T }$ and $u _ { 2 , 0 } = ( 1 , 3 , 2 ) ^ { T }$ are the eigenvectors of A and the geometric multiplicity of $\lambda _ { 2 }$ is 1. To put A in Jordan canonical form, we want $A ( u _ { 1 } , u _ { 2 , 0 } , u _ { 2 , 1 } ) = A U = U J = ( \lambda _ { 1 } u _ { 1 } , \lambda _ { 2 } u _ { 2 , 0 } , \lambda _ { 2 } u _ { 2 , 1 } + u _ { 2 , 0 } )$ so we need to find a vector $u _ { 2 , 1 }$ satisfying $A u _ { 2 , 1 } = \lambda _ { 2 } u _ { 2 , 1 } + u _ { 2 , 0 }$ . This can be done by solving $P _ { 2 } ( A - \lambda _ { 2 } I ) u _ { 2 , 1 } = P _ { 2 } u _ { 2 , 0 } .$

$$
\begin{array} { r l r } { ( \begin{array} { c c c } { - 1 } & { - 3 } & { 5 } \\ { - 1 } & { - 7 } & { 1 1 } \\ { 0 } & { - 4 } & { 6 } \end{array} ) \xrightarrow { 1 } ) \quad } & { \mathrm { r o w ~ r e d u c e ~ } } & { ( \begin{array} { c c c } { 1 } & { 0 } & { - 1 / 2 } \\ { 0 } & { 1 } & { - 3 / 2 } \\ { 0 } & { 0 } & { 0 } \end{array} | \begin{array} { c } { 1 / 2 } \\ { - 1 / 2 } \\ { 0 } \end{array} ) . } \end{array}
$$

Thus $u _ { 2 , 1 } = ( 1 , 1 , 1 ) ^ { T }$ works (as does $( 1 , 1 , 1 ) ^ { T } + \alpha ( 1 , 3 , 2 ) ^ { T }$ for any $\alpha \in \mathbb { C } )$ and we have

$$
\begin{array}{c} U = { \binom { 1 } { 2 } } \ 3 \ 1  \\ { 1 \ 2 \ 1 } \end{array}  \qquad U ^ { - 1 } A U = J = { ( \begin{array} { l l l } { - 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } \end{array} ) } \ .
$$
:::
