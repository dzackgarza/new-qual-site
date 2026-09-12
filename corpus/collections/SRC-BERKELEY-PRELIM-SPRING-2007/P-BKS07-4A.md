---
schema: qual/card@1
id: P-BKS07-4A
kind: problem
title: UC Berkeley Spring 2007 prelim 4A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Define six fields as follows:

• Let $A = \mathbb { Q } ( \alpha )$ where Q is the field of rational numbers and α is the real cube root of 2.

• Let B be a splitting field of $x ^ { 3 } - 2$ over Q.

• Let C be an algebraic closure of the field $\mathbb { F } _ { 2 }$ of 2 elements.

• Let D be the subfield of C generated over $\mathbb { F } _ { 2 }$ by the set of $a \in C$ such that there exists $n \geq 1$ with $a ^ { n } = 1$

• Let E be the field R of real numbers.

• Let F be the field $\mathbb { Q } [ [ T ] ( T ^ { - 1 } )$ of formal Laurent series with rational coefficients.

For each pair of these, determine with proof whether or not they are isomorphic.
:::

::: {.solution}
We will show that the only isomorphic pair consists of $C$ and $D$

Let $S _ { 1 } = \{ A , B \} , S _ { 2 } = \{ C , D \}$ , and $S _ { 3 } = \{ E , F \}$ The fields in $S _ { 1 }$ are of finite dimension over Q, hence countable and of characteristic 0. The fields in $S _ { 2 }$ are of characteristic 2. The fields in $S _ { 3 }$ are uncountable and of characteristic 0. Hence no field in $S _ { i }$ is isomorphic to a field in $S _ { j }$ if $i \neq j$ .

By Eisenstein’s criterion, $x ^ { 3 } - 2$ is irreducible, so $\left[ A : \mathbb { Q } \right] = 3$ . The zeros of this polynomial are $\omega ^ { i } \alpha$ where ω is a primitive cube root of unity.
Thus $\omega \in B$ . Since $[ \mathbb { Q } ( \omega ) : \mathbb { Q } ] = 2$ , the degree $\left[ B : \mathbb { Q } \right]$ is even.
Hence $A \not \simeq B$

If $a \in C$ , then $\mathbb { F } _ { 2 } ( a )$ is a finite extension of $\mathbb { F } _ { 2 }$ , hence finite, say of order $q ;$ if moreover $a \neq 0$ , then $a ^ { q - 1 } = 1$ . Hence $C \subseteq D$ . But $D \subseteq C$ , so $C = D$

The square of a nonzero element of $\mathbb { Q } [ [ T ] ( T ^ { - 1 } )$ has a leading coefficient that is a rational square.
Thus 2 is not a square in $\mathbb { Q } [ [ T ] ] ( T ^ { - 1 } )$ . But 2 is a square in R. So $E \not \simeq F$
:::
