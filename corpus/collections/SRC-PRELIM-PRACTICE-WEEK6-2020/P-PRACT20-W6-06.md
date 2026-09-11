---
schema: qual/card@1
id: P-PRACT20-W6-06
kind: problem
title: "Week 6: Miscellaneous Topics, problem 6"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find examples of a function $f : ( - 1 , 1 ) \to \mathbb { R }$ which is

(A) continuous but not uniformly continuous,

(B) uniformly continuous but not Lipschitz continuous,

(C) Lipschitz continuous but not differentiable,

(D) differentiable but not continuously differentiable.
:::

::: {.solution}
For (A), let $\textstyle f ( x ) = { \frac { 1 } { 1 - x } }$ . Then f is continuous, but it is not uniformly continuous.
Indeed, the sequence $f ( 1 - 1 / n ) = n$ does not converge, which shows by Problem 4 (contrapositively) that f is not uniformly continuous.

For (B), consider $f ( x ) = { \sqrt { 1 - x } }$ . Then f is uniformly continuous because it is can be continuously extended to the compact set $[ - 1 , 1 ]$ However, f is not Lipschitz continuous.
Indeed, notice that f is differentiable on $( - 1 , 1 )$ with $\begin{array} { r } { f ^ { \prime } ( x ) = \frac { 1 } { 2 \sqrt { 1 - x } }  \infty \mathrm { ~ a s ~ } x  1 } \end{array}$ . Thus for any $K > 0$ , we can find $\delta > 0$ such that $f ^ { \prime } ( x ) > K$ when $x \in ( 1 - \delta , 1 ]$ . But then by the mean value theorem, for any $x , y \in \left( 1 - \delta , 1 \right] x \neq y .$ , we can find c between x and y such that

$$
| f ( x ) - f ( y ) | = \left| f ^ { \prime } ( c ) \right| | x - y | > K | x - y |
$$

which shows that K is not a Lipschitz constant for f . Since $K > 0$ was arbitrary, we conclude that f is not Lipschitz continuous.

For (C), consider $f ( x ) = \left| x \right|$ . Then f is Lipschitz continuous with Lipschitz constant 1 by the reverse triangle inequality, but f is not differentiable at $x = 0$

For (D) consider the function

$$
f ( x ) = \left\{ \begin{array} { c c } { x ^ { 2 } \sin \left( \frac { 1 } { x } \right) , } & { x \in ( - 1 , 0 ) \cup ( 0 , 1 ) , } \\ { 0 , } & { x = 0 . } \end{array} \right.
$$

Certainly f is differentiable for $x \neq 0$ since it is the product of smooth functions in that domain.
Indeed, we see that

$$
f ^ { \prime } ( x ) = 2 x \sin \left( { \frac { 1 } { x } } \right) - \cos \left( { \frac { 1 } { x } } \right) , x \in ( - 1 , 0 ) \cup ( 0 , 1 ) .
$$

Also at $x = 0$ , we see that

$$
\operatorname* { l i m } _ { x \to 0 } { \frac { f ( x ) - f ( 0 ) } { x - 0 } } = \operatorname* { l i m } _ { x \to 0 } x \sin \left( { \frac { 1 } { x } } \right) = 0
$$

which shows that $f ^ { \prime } ( 0 ) = 0$ . Thus f is differentiable for all $x \in ( - 1 , 1 )$ . However, the derivative is discontinuous because along the sequence $\begin{array} { r } { x _ { n } = \frac { 1 } { \sqrt { ( 2 n + 1 ) \pi } } } \end{array}$ , we have $f ^ { \prime } ( x _ { n } ) = 1 \not \to 0 = f ^ { \prime } ( 0 )$ even though $x _ { n } \to 0$
:::
