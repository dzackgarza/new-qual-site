---
schema: qual/card@1
id: P-BKS06-2B
kind: problem
title: Number of irreducible polynomials of prime degree over $\FF_2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\FF _ { 2 }$ be the field of 2 elements.
Let n be a prime.
Show that there are exactly $( 2 ^ { n } - 2 ) / n$ degree-n irreducible polynomials in $\FF _ { 2 } [ x ]$
:::

::: {.solution}
There is a unique field extension $\FF _ { 2 ^ { n } }$ of degree n over $\FF _ { 2 }$ . It is Galois over $\FF _ { 2 }$ (this is because it is a splitting field for the separable polynomial $x ^ { 2 ^ { n } } - x$). If $a \in \FF _ { 2 ^ { n } } - \FF _ { 2 }$ then $\FF _ { 2 } ( a )$ is a subfield of $\FF _ { 2 ^ { n } }$ of degree dividing n but not equal to 1, so $\FF _ { 2 } ( a ) = \FF _ { 2 ^ { n } }$ . Hence the minimal polynomial $f _ { a }$ of a over $\FF _ { 2 }$ is an irreducible polynomial of degree n over $\FF _ { 2 }$ Thus we have a map

$$
\begin{array} { l } { { ( \FF _ { 2 ^ { n } } - \FF _ { 2 } ) \longrightarrow \{ \mathrm { d e g r e e } { - } n \mathrm { ~ i r r e d u c i b l e ~ p o l y n o m i a l s ~ i n ~ } \FF _ { 2 } [ x ] \} } } \\ { { a \longmapsto f _ { a } . } } \end{array}
$$

On the other hand, if $f \in \FF _ { 2 } [ x ]$ is any degree-n irreducible polynomial, then f has a zero in $\FF _ { 2 ^ { n } }$ (since $\FF _ { 2 ^ { n } }$ is the unique degree-n extension of $\FF _ { 2 } )$ and it follows that f has n distinct zeros in $\FF _ { 2 ^ { n } }$ (since $\FF _ { 2 ^ { n } }$ is Galois over $\FF _ { 2 } )$ . Moreover, f is automatically monic (the only nonzero element of $\FF _ { 2 }$ is 1) so it is the minimal polynomial of each of its zeros.
Thus our map is n-to-1.

Its domain has size $2 ^ { n } - 2 .$ , so its range has size $( 2 ^ { n } - 2 ) / n$
:::
