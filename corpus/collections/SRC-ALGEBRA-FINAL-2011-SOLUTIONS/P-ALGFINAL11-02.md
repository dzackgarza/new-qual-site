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
(a) The automorphism of $R$ that takes any $y \in R$ to $\bar y$ induces the first isomorphism.
Multiplication by $x$ induces the second: it is surjective, and it is injective since if $xy = x\bar x z$ then, $R$ being an integral domain, $y = \bar x z$.

(b) Taking $(a,b) \in \mathbb Z \times \mathbb Z$ to $a + b\sqrt{-n} \in R$ gives a group isomorphism.
For an integer $m > 0$ there results an isomorphism $\mathbb Z/m \times \mathbb Z/m \cong R/mR$, so $\abs{R/mR} = [R : mR] = m^2$. In particular, for $m = x\bar x$ one gets $N(x)^2 = [R : x\bar x R] = [R : xR][xR : x\bar x R] = [R : xR]^2$, where the last equality holds by (a).

(c) If $N(x) = \abs{R/xR}$ (by (b)) is prime, so that $R/xR$ has no nontrivial proper subgroup, then the ideal $xR$ is maximal, hence prime, i.e., $x$ is prime in $R$.

(d) By (c), if $p = a^2 + nb^2 = x\bar x$ with $x \coloneqq a + b\sqrt{-n}$ is a prime of $\mathbb Z$, then $p = x\bar x$ is a factorization of $p$ into primes of $R$.
By (b), any unit $u + v\sqrt{-n}$ of $R$ has norm $1$, i.e., $u^2 + nv^2 = 1$, whence $u = \pm 1$ and $v = 0$. Since factorization into primes in an integral domain is unique up to multiplying by units and permuting the factors, it follows that if $p = a^2 + nb^2 = c^2 + nd^2$ with $a$, $b$, $c$ and $d$ all positive then $a = c$ and $b = d$.
:::
