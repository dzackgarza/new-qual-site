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
Let $n > 1$ be in $\ZZ ,$ and let $R { : = } \ZZ [ { \sqrt { - n } } ]$

For $x = a + b { \sqrt { - n } } \in R \left( a , b \in \ZZ \right)$ , set ${ \bar { x } } = a - b { \sqrt { - n } } .$ , and define the norm

$$
N ( x ) = x \bar { x } = a ^ { 2 } + n b ^ { 2 } .
$$

(a) Assuming $x \neq 0$ , describe group isomorphisms $R / x R \cong R / \bar { x } R \cong x R / x \bar { x } R .$

[4]

(b) Deduce from (a) that $N ( x ) ^ { 2 } = [ R : x R ] [ x R : x \bar { x } R ] = [ R : x R ] ^ { 2 }$ . [3]

(c) Deduce from (b) that if N (x) is prime in $\ZZ$ then x is prime in R. [4]

(d) Deduce from (c) that if p is a prime in $\ZZ$ then there is at most one way to represent p in the form $p = a ^ { 2 } + n b ^ { 2 }$ where a and b are positive integers.
[4]
:::

::: {.solution}
(a) The automorphism of $R$ that takes any $y \in R$ to $\bar y$ induces the first isomorphism.
Multiplication by $x$ induces the second: it is surjective, and it is injective since if $xy = x\bar x z$ then, $R$ being an integral domain, $y = \bar x z$.

(b) Taking $(a,b) \in \ZZ \times \ZZ$ to $a + b\sqrt{-n} \in R$ gives a group isomorphism.
For an integer $m > 0$ there results an isomorphism $\ZZ/m \times \ZZ/m \cong R/mR$, so $\abs{R/mR} = [R : mR] = m^2$. In particular, for $m = x\bar x$ one gets $N(x)^2 = [R : x\bar x R] = [R : xR][xR : x\bar x R] = [R : xR]^2$, where the last equality holds by (a).

(c) If $N(x) = \abs{R/xR}$ (by (b)) is prime, so that $R/xR$ has no nontrivial proper subgroup, then the ideal $xR$ is maximal, hence prime, i.e., $x$ is prime in $R$.

(d) Suppose $p=a^2+nb^2=c^2+nd^2$ with $a,b,c,d>0$. Put $x=a+b\sqrt{-n}$ and $y=c+d\sqrt{-n}$. By (c), $x$ is prime in $R$, and $x\mid y\bar y=p$. Thus $x\mid y$ or $x\mid\bar y$.

In the first case, write $y=xu$. Taking norms gives $p=pN(u)$, so $N(u)=1$. If $u=r+s\sqrt{-n}$, then $r^2+ns^2=1$; since $n>1$, this forces $u=\pm1$. Positivity gives $y=x$, hence $a=c$ and $b=d$. In the second case the same norm argument gives $\bar y=\pm x$, which is impossible because $\bar y=c-d\sqrt{-n}$ and $a,b,c,d>0$. Therefore the representation is unique.
:::
