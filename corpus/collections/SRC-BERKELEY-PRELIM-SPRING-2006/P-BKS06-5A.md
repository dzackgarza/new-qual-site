---
schema: qual/card@1
id: P-BKS06-5A
kind: problem
title: UC Berkeley Spring 2006 prelim 5A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Consider the following four commutative rings:

$$
\mathbb { Z } , \mathbb { Z } [ x ] , \mathbb { R } [ x ] , \mathbb { R } [ x , y ] .
$$

Which of these rings contains a nonzero prime ideal that is not a maximal ideal?
:::

::: {.solution}
In the ring of integers Z the nonzero prime ideals are $\langle p \rangle$ , where p is a prime number. Each of these ideals is maximal since $\mathbb { F } _ { p } = \mathbb { Z } / \langle p \rangle$ is a field. Hence every nonzero prime ideal in $\mathbb { Z }$ is maximal.

The polynomial ring $\mathbb { Z } [ x ]$ in one variable x over the ring of integers Z is not a principal ideal domain. For instance, $\langle 2 , x \rangle$ is not a principal ideal; it strictly contains the ideal $\langle 2 \rangle$ , which is therefore not a maximal ideal. The ideal h2i is a prime ideal, because $\mathbb { Z } [ x ] / \langle 2 \rangle = \mathbb { F } _ { 2 } [ x ]$ is a polynomial ring over a field, and hence an integral domain. Hence h2i is a nonzero prime ideal in $\mathbb { Z } [ x ]$ which is not maximal.

The polynomial ring $\mathbb { R } [ x ]$ in one variable x over the field R is a principal ideal domain. Hence every nonzero ideal has the form $\langle f ( x ) \rangle$ where $f ( x )$ is a nonzero polynomial with real coefficients. The ideal is prime if and only if $f ( x )$ is an irreducible polynomial, i.e., if $f ( x )$ is a linear polynomial or $f ( x )$ is a quadratic polynomial with no real roots. In either case, the quotient $\mathbb { R } [ x ] / \langle f \rangle$ is a field, namely, either R or C, which means that $\langle f \rangle$ is a maximal ideal. Hence every nonzero prime ideal in $\mathbb { R } [ x ]$ is a maximal ideal.

The polynomial ring $\mathbb { R } [ x , y ]$ in two variables $x , y$ over R has many nonzero prime ideals which are not maximal ideals. For instance, hxi is a prime ideal, but it is not maximal since it is contained in the ideal $\langle x , y \rangle$
:::
