---
schema: qual/card@1
id: P-ALGFINAL11-02
kind: problem
title: Norms and prime elements in quadratic integer rings
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $n > 1$ be in $\mathbb { Z } ,$ and let $R { : = } \mathbb { Z } [ { \sqrt { - n } } ]$

For $x = a + b { \sqrt { - n } } \in R \left( a , b \in \mathbb { Z } \right)$ , set ${ \bar { x } } = a - b { \sqrt { - n } } .$ , and define the norm

$$
N ( x ) = x \bar { x } = a ^ { 2 } + n b ^ { 2 } .
$$

(a) Assuming $x \neq 0$ , describe group isomorphisms $R / x R \cong R / \bar { x } R \cong x R / x \bar { x } R .$

[4]

$$
( \mathrm { b } ) \mathrm { \ D e d u c e \ f r o m \ ( a ) \ t h a t \ } N ( x ) ^ { 2 } = [ R : x R ] [ x R : x \bar { x } R ] = [ R : x R ] ^ { 2 } .\tag{[3]}
$$

(c) Deduce from (b) that if N (x) is prime in $\mathbb { Z }$ then x is prime in R. [4]

(d) Deduce from (c) that if p is a prime in $\mathbb { Z }$ then there is at most one way to represent p in the form $p = a ^ { 2 } + n b ^ { 2 }$ where a and b are positive integers.
[4]
:::

::: {.solution}
(a) The automorphism of R that takes any $y \in R$ to $\bar { y }$ induces the first isomorphism.
Multiplication by x induces the second (which is clearly surjective, and also injective since if $x y = x { \bar { x } } z$ then, R being an integral domain, $y = { \bar { x } } z )$ .

(b) Taking $( a , b ) \in \mathbb { Z } \times \mathbb { Z }$ to $a + b { \sqrt { - n } } \in R$ gives a group isomorphism.
For $n > 0 \in \mathbb { Z } .$ there results an isomorphism $\mathbb { Z } _ { n } \times \mathbb { Z } _ { n } \cong R / n R \mathrm { : }$ ; so the cardinality $| R / n R | = [ R : n R ] = n ^ { 2 }$ In particular, for $n = x { \bar { x } }$ one gets $N ( x ) ^ { 2 } = [ R : x { \bar { x } } R ] = [ R : x R ] [ x R : x { \bar { x } } R ] = [ R : x R ] ^ { 2 }$ where the last equality holds by (a).

(c) If $N ( x ) \stackrel { ( \mathrm { b } ) } { = } | R / x R |$ is prime, so that $R / x R$ has no nontrivial proper subgroup, then the ideal $x R$ is maximal, hence prime, i.e., x is prime in R.

(d) By (c), if $p \ = \ a ^ { 2 } + n b ^ { 2 } \ = \ x \bar { x } \ ( x : = \ a + b \sqrt { - n } )$ is a Z-prime then $p = x { \bar { x } }$ is a factorization of p into R-primes.
By (b), any unit $u + v { \sqrt { - n } }$ in R has norm $\pm 1$ , i.e., $u ^ { 2 } + n v ^ { 2 } = \pm 1$ , whence $u = \pm 1$ and $v = 0$ . Since factorization into primes is unique up to multiplying by units and permuting the factors, it follows that if $p = a ^ { 2 } + n b ^ { 2 } = c ^ { 2 } + n d ^ { 2 }$ with $a , b ,$ c and d all positive then $a = c$ and $b = d .$
:::
