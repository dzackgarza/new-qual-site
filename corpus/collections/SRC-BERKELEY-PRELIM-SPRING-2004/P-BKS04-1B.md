---
schema: qual/card@1
id: P-BKS04-1B
kind: problem
title: UC Berkeley Spring 2004 prelim 1B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let F be a field (of arbitrary characteristic). Suppose g is a nonnegative integer, and polynomials $a ( x ) , b ( x ) \in F [ x ]$ satisfy deg $a ( x ) \leq g$ and deg $b ( x ) = 2 g + 1$ . Prove that the polynomial $y ^ { 2 } + a ( x ) y + b ( x )$ is irreducible over $F ( x )$
:::

::: {.solution}
If instead it factors in $F ( x ) [ y ]$ into polynomials of $y { \mathrm { - d e g r e e } } \geq 1$ , then by Gauss’s Lemma, it factors in $F [ x ] [ y ] = F [ x , y ]$ into polynomials of $y \mathrm { - d e g r e e } \geq 1$ . Thus we would have

$$
y ^ { 2 } + a ( x ) y + b ( x ) = ( y + p ( x ) ) ( y + q ( x ) )
$$

for some $p ( x ) , q ( x ) \in F [ x ]$ . Since $p ( x ) q ( x ) = b ( x )$ has odd degree, $p ( x )$ and $q ( x )$ have distinct degrees, so

$$
\deg ( p ( x ) + q ( x ) ) = \operatorname* { m a x } ( \deg p ( x ) , \deg q ( x ) ) \geq ( \deg p ( x ) + \deg q ( x ) ) / 2 = ( 2 g + 1 ) / 2 > g .
$$

This contradictions deg $a ( x ) = g$
:::
