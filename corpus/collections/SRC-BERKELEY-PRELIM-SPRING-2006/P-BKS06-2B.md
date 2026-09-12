---
schema: qual/card@1
id: P-BKS06-2B
kind: problem
title: UC Berkeley Spring 2006 prelim 2B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\mathbb { F } _ { 2 }$ be the field of 2 elements.
Let n be a prime.
Show that there are exactly $( 2 ^ { n } - 2 ) / n$ degree-n irreducible polynomials in $\mathbb { F } _ { 2 } [ x ]$
:::

::: {.solution}
There is a unique field extension $\mathbb { F } _ { 2 ^ { r } }$ n of degree n over $\mathbb { F } _ { 2 }$ . It is Galois over $\mathbb { F } _ { 2 }$ (this is because it is a splitting field for the separable polynomial $x ^ { 2 ^ { n } } - x )$ x). If $a \in \mathbb { F } _ { 2 ^ { n } } - \mathbb { F } _ { 2 }$ then $\mathbb { F } _ { 2 } ( a )$ is a subfield of $\mathbb { F } _ { 2 ^ { n } }$ of degree dividing n but not equal to 1, so $\mathbb { F } _ { 2 } ( a ) = \mathbb { F } _ { 2 ^ { n } }$ . Hence the minimal polynomial $f _ { a }$ of a over $\mathbb { F } _ { 2 }$ is an irreducible polynomial of degree n over $\mathbb { F } _ { 2 }$ Thus we have a map

$$
\begin{array} { l } { { ( \mathbb { F } _ { 2 ^ { n } } - \mathbb { F } _ { 2 } ) \longrightarrow \{ \mathrm { d e g r e e } { - } n \mathrm { ~ i r r e d u c i b l e ~ p o l y n o m i a l s ~ i n ~ } \mathbb { F } _ { 2 } [ x ] \} } } \\ { { a \longmapsto f _ { a } . } } \end{array}
$$

On the other hand, if $f \in \mathbb { F } _ { 2 } [ x ]$ is any degree-n irreducible polynomial, then f has a zero in $\mathbb { F } _ { 2 ^ { n } }$ (since $\mathbb { F } _ { 2 ^ { n } }$ is the unique degree-n extension of $\mathbb { F } _ { 2 } )$ and it follows that f has n distinct zeros in $\mathbb { F } _ { 2 ^ { n } }$ (since $\mathbb { F } _ { 2 ^ { n } }$ is Galois over $\mathbb { F } _ { 2 } )$ . Moreover, f is automatically monic (the only nonzero element of $\mathbb { F } _ { 2 }$ is 1) so it is the minimal polynomial of each of its zeros.
Thus our map is n-to-1.

Its domain has size $2 ^ { n } - 2 .$ , so its range has size $( 2 ^ { n } - 2 ) / n$
:::
