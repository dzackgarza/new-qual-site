---
schema: qual/card@1
id: P-BKS06-9B
kind: problem
title: UC Berkeley Spring 2006 prelim 9B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Find a bounded non-convergent sequence of real numbers $( a _ { n } ) _ { n \geq 1 }$ such that

$$
| 2 a _ { n } - a _ { n - 1 } - a _ { n + 1 } | \leq n ^ { - 2 }
$$

for all $n \geq 2 .$
:::

::: {.solution}
We will let $a _ { n } = f ( n )$ , where $f ( x )$ is a function similar to the sine function but with oscillations that slow down as $x \longrightarrow \infty .$ , so that $f ^ { \prime \prime } ( x )  0$ . To be precise, we take

$$
f ( x ) : = { \frac { 1 } { 2 } } \sin ( \ln ( x + 1 ) ) .
$$

This sequence is bounded. It also does not converge, since the spacing between values of ln n tends to zero, which means that the values of (ln n) mod (2π) are dense in [0, 2π].

By Taylor’s theorem with remainder (centered at n),

$$
f ( n + 1 ) = f ( n ) + f ^ { \prime } ( n ) + { \frac { 1 } { 2 } } f ^ { \prime \prime } ( \xi _ { + } ) \quad { \mathrm { f o r ~ s o m e ~ } } \xi _ { + } \in ( n , n + 1 ) , { \mathrm { ~ a n d ~ } }
$$

$$
f ( n - 1 ) = f ( n ) - f ^ { \prime } ( n ) + { \frac { 1 } { 2 } } f ^ { \prime \prime } ( \xi _ { - } ) \quad \mathrm { f o r ~ s o m e ~ } \xi _ { - } \in ( n - 1 , n ) , \mathrm { ~ s o } ,
$$

$$
| 2 f ( n ) - f ( n - 1 ) - f ( n + 1 ) | = { \frac { 1 } { 2 } } | f ^ { \prime \prime } ( \xi _ { + } ) + f _ { \cdot } ^ { \prime \prime } ( \xi _ { - } ) | = | f ^ { \prime \prime } ( \xi ) | \quad { \mathrm { f o r ~ s o m e ~ } } \xi \in ( \xi _ { - } , \xi ^ { + } ) \subseteq ( n - 1 , n + 1 )
$$

by the intermediate value theorem. We compute

$$
f ^ { \prime } ( x ) = { \frac { 1 } { 2 ( x + 1 ) } } \cos ( \ln ( x + 1 ) )
$$

$$
f ^ { \prime \prime } ( x ) = - \frac { 1 } { 2 ( x + 1 ) ^ { 2 } } \left( \cos ( \ln ( x + 1 ) ) + \sin ( \ln ( x + 1 ) ) \right) ,
$$

$$
| f ^ { \prime \prime } ( x ) | \leq { \frac { 1 } { ( x + 1 ) ^ { 2 } } }
$$

$$
| f ^ { \prime \prime } ( \xi ) | \leq \frac { 1 } { ( \xi + 1 ) ^ { 2 } } \leq \frac { 1 } { n ^ { 2 } } .
$$

so

$$
| 2 a _ { n } - a _ { n - 1 } - a _ { n + 1 } | = | f ^ { \prime \prime } ( \xi ) | \leq n ^ { - 2 } .
$$
:::
