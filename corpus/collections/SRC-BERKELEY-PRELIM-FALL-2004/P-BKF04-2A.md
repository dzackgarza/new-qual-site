---
schema: qual/card@1
id: P-BKF04-2A
kind: problem
title: Isomorphism classes of the rings $\QQ[x]/(x^3-cx)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
For $c \in \mathbb { Q }$ , define $R _ { c } : = \mathbb { Q } [ x ] / ( x ^ { 3 } - c x )$ . Let $a , b \in \mathbb { Q }$ . Show that the rings $R _ { a }$ and $R _ { b }$ are isomorphic if and only if there exists a nonzero $r \in \mathbb { Q }$ such that $b = r ^ { 2 } a$
:::

::: {.solution}
If $r\neq0$ and $b=r^2a$, then the ring automorphism $\QQ[x]\to\QQ[x]$ sending $x$ to $rx$ maps $x^3-bx$ to $r^3x^3-brx=r^3(x^3-ax)$, so it induces an isomorphism between the quotient rings

$$
{ \cal R } _ { b } = \frac { \mathbb { Q } [ x ] } { ( x ^ { 3 } - b x ) } \simeq \frac { \mathbb { Q } [ x ] } { ( r ^ { 3 } ( x ^ { 3 } - a x ) ) } = \frac { \mathbb { Q } [ x ] } { ( x ^ { 3 } - a x ) } = { \cal R } _ { a } .
$$

Conversely, suppose $R_a\simeq R_b$. The maximal ideals of $R_a$ correspond bijectively to maximal ideals of $\QQ[x]$ containing $x^3-ax$, which in turn correspond bijectively to distinct monic irreducible factors of $x^3-ax$. Thus $R_a$ has $1$, $3$, or $2$ maximal ideals according as $a=0$, $a$ is a nonzero square, or $a$ is not a square. Since $R_b$ has the same number of maximal ideals, $b=r^2a$ for some nonzero $r\in\QQ$, except possibly in the case where neither $a$ nor $b$ is a square. Assume now that neither is a square. The quotients of $R_a$ by its two maximal ideals are $\QQ$ and $\QQ[x]/(x^2-a)\simeq\QQ[\sqrt a]$. These are the same as the quotients $\QQ$ and $\QQ[\sqrt b]$ of $R_b$, in some order. Since $b$ is a square in $\QQ[\sqrt b]$ but not in $\QQ$, it is a square in $\QQ[\sqrt a]$. Write

$$
( r { \sqrt { a } } + s ) ^ { 2 } = b .
$$

with $r,s\in\QQ$. Expanding and comparing the coefficients of $\sqrt a$ gives $2rs=0$. If $r=0$, then $b=s^2$ is a square, contrary to assumption. Thus $s=0$, and $b=r^2a$ with $r\neq0$.
:::
