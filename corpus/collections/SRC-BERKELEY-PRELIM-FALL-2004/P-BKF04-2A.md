---
schema: qual/card@1
id: P-BKF04-2A
kind: problem
title: UC Berkeley Fall 2004 prelim 2A
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
If $r \neq 0$ and $b = r ^ { 2 } a$ , then the ring automorphism $\mathbb { Q } [ x ]  \mathbb { Q } [ x ]$ sending x to rx maps $x ^ { 3 } - b x$ to $r ^ { 3 } x ^ { 3 } - b r x = r ^ { 3 } ( x ^ { 3 } - a x )$ , so it induces an isomorphism between the quotient rings

$$
{ \cal R } _ { b } = \frac { \mathbb { Q } [ x ] } { ( x ^ { 3 } - b x ) } \simeq \frac { \mathbb { Q } [ x ] } { ( r ^ { 3 } ( x ^ { 3 } - a x ) ) } = \frac { \mathbb { Q } [ x ] } { ( x ^ { 3 } - a x ) } = { \cal R } _ { a } .
$$

Conversely, suppose $R _ { a } \simeq R _ { b }$ . The maximal ideals of $R _ { a }$ correspond bijectively to maximal ideals of $\mathbb { Q } [ x ]$ containing $x ^ { 3 } - a x$ , which in turn correspond bijectively to distinct irreducible factors of $x ^ { 3 } - a x$ . Thus $R _ { a }$ has 1, 3, or 2 maximal ideals according as $a = 0$ , a is a nonzero square, or a is not a square. Since $R _ { b }$ must have the same number of maximal ideals, we immediately deduce that $b = r ^ { 2 } a$ for some r, except possibly in the case where neither a nor b is a square. We now assume we are in this remaining case. The quotient fields of $R _ { a }$ (the quotients of $R _ { a }$ by its two maximal ideals) are $\mathbb { Q }$ and $\mathbb { Q } [ x ] / ( x ^ { 2 } - a ) \simeq \mathbb { Q } [ { \sqrt { a } } ]$ . These must be the same as the quotient fields Q and $\mathbb { Q } [ { \sqrt { b } } ]$ of $R _ { b }$ , in some order. Since b is a square in $\mathbb { Q } [ { \sqrt { b } } ]$ but not in $\mathbb { Q } .$ , it must be a square in $\mathbb { Q } [ { \sqrt { a } } ]$ . Write

$$
( r { \sqrt { a } } + s ) ^ { 2 } = b .
$$

Expanding, we get $2 r s = 0$ . If $r = 0$ , we contradict the assumption that b is not a square. Thus $s = 0$ , and $b = r ^ { 2 } a$
:::
