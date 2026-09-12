---
schema: qual/card@1
id: P-BKS07-5A
kind: problem
title: UC Berkeley Spring 2007 prelim 5A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $a _ { 0 } ( x ) , a _ { 1 } ( x ) , \dots , a _ { r - 1 } ( x )$ and $b ( x )$ be $C ^ { m }$ functions on R. Prove that if $y ( x )$ is a solution of the differential equation

$$
y ^ { ( r ) } + a _ { r - 1 } ( x ) y ^ { ( r - 1 ) } + \cdot \cdot \cdot + a _ { 1 } ( x ) y ^ { \prime } + a _ { 0 } ( x ) y = b ( x )
$$

(in particular, assuming that the derivatives $y ^ { \prime } , y ^ { \prime \prime } , \ldots , y ^ { ( r ) }$ exist), then $y ( x )$ is $C ^ { m + r }$
:::

::: {.solution}
Rewrite the differential equation as

$$
y ^ { ( r ) } = b - \left( a _ { r - 1 } y ^ { ( r - 1 ) } + \cdot \cdot \cdot + a _ { 1 } y ^ { \prime } + a _ { 0 } y \right) ,\tag{1}
$$

and proceed by induction on m. For $m = 0$ , the derivatives of $y$ on the right-hand side of (1) are differentiable and hence continuous.
The functions $a _ { i }$ and b are continuous by assumption, so $y ^ { ( r ) }$ is continuous, $i . e . , y$ is $C ^ { r }$

For $m > 0$ , assume by induction that y is $C ^ { m + r - 1 }$ Then the derivatives of y on the right-hand side of (1) are $C ^ { m }$ . The functions $a _ { i }$ and b are $C ^ { m }$ by assumption, so $y ^ { ( r ) }$ is $C ^ { m }$ hence y is $C ^ { m + r }$
:::
