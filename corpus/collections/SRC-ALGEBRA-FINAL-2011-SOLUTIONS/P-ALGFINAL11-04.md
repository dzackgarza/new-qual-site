---
schema: qual/card@1
id: P-ALGFINAL11-04
kind: problem
title: Primitive roots of unity over finite fields
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let K be a finite field of cardinality $q ,$ let $n > 0$ be an integer relatively prime to $q ,$ and let $\zeta$ be a primitive n-th root of unity lying in some field $L \supset K$ with $[ L : K ] = m$

(a) Show that n divides $q ^ { m } - 1$

[4]

(b) Show that $[ K ( \zeta ) : K ]$ is the order of $q$ in the group $( \mathbb { Z } / n \mathbb { Z } ) ^ { * }$ (units in $\mathbb { Z } / n \mathbb { Z } )$ . [6]
:::

::: {.solution}
(a) $\mathrm { B y }$ the definition of “primitive n-th root of $\mathrm { { u n i t y } } , \mathrm { { \dot { \Omega } } }$ n is the order of $\zeta$ in the multiplicative group $L ^ { * } ;$ so $n | | L ^ { * } | = q ^ { m } - 1$

(b) By (a), the order $\mu$ of q divides $[ K ( \zeta ) : K ]$ . So $K ( \zeta )$ contains a subfield $L ^ { \prime } \supset K$ such that $[ L ^ { \prime } : K ] = \mu$ . The cyclic group $L ^ { \prime * }$ has order $q ^ { \mu } - 1$ divisible by $n ,$ so it contains a cyclic subgroup of order n, and therefore it contains all the n solutions of $X ^ { n } - 1$ , one of which is $\zeta ,$ , whence $L ^ { \prime } = K ( \zeta )$ and $[ K ( \zeta ) : K ] = [ L ^ { \prime } : K ] = \mu .$
:::
