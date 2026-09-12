---
schema: qual/card@1
id: P-BKS07-9B
kind: problem
title: UC Berkeley Spring 2007 prelim 9B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let k and n be integers with $n \geq k \geq 0$ Let A and B be $n \times k$ matrices with real coefficients.
Let $A ^ { t }$ be the transpose of A. For each size-k subset $I \subseteq \{ 1 , \ldots , n \}$ , let $A _ { I }$ be the $k \times k$ matrix obtained by discarding all rows of A except those whose index belongs to I. Define $B _ { I }$ similarly.
Prove that

$$
\operatorname* { d e t } ( A ^ { t } B ) = \sum _ { I } \operatorname* { d e t } ( A _ { I } ) \operatorname* { d e t } ( B _ { I } ) ,
$$

where the sum is over all size-k subsets $I \subseteq \{ 1 , \ldots , n \}$ . (Suggestion: use linearity to reduce to the case where the columns of A and B are particularly simple.)
:::

::: {.solution}
Let $a _ { i }$ be the i-th column vector of A. Let $b _ { j }$ be the j-th column vector of B. Let $e _ { 1 } , \ldots , e _ { n }$ be the standard basis of $\mathbb { R } ^ { n }$ . Both sides of the identity are linear in each $a _ { i }$ and $b _ { j }$ , so we may assume that each column is a standard basis vector, say $\boldsymbol a _ { i } = \boldsymbol e _ { f ( i ) }$ and $b _ { j } = e _ { g ( j ) }$ Then $A ^ { t } B$ is the matrix whose ij-entry is $a _ { i } ^ { t } b _ { j }$ , which is 1 if $f ( i ) = g ( j )$ and 0 otherwise.

If $f ( 1 ) , \ldots , f ( k )$ are not all different, then $A ^ { t } B$ has a repeated row, and every $A _ { I }$ has a repeated column, so both sides of the desired identity are 0. So assume that the $f ( i )$ are all different.

Similarly, if $g ( 1 ) , \ldots , g ( k )$ are not all different, then $A ^ { t } B$ has a repeated column, and every $B _ { I }$ has a repeated column, so both sides of the desired identity are $0 .$ . So assume that the $g ( j )$ are all different.

If $I \ne \{ f ( 1 ) , \ldots , f ( k ) \}$ , then $A _ { I }$ has fewer than k nonzero entries, so det $A _ { I } \ = \ 0$ . If $I \neq \{ g ( 1 ) , \ldots , g ( k ) \}$ , then $B _ { I }$ has fewer than k nonzero entries, so det $B _ { I } = 0$

Suppose that $\{ f ( 1 ) , \ldots , f ( k ) \} \neq \{ g ( 1 ) , \ldots , g ( k ) \}$ . Then $A ^ { t } B$ has fewer than k nonzero entries.
But also, by the previous paragraph, for every I, either det $A _ { I }$ or det $B _ { I }$ is 0. Thus the desired identity holds.

Finally, suppose that $\{ f ( 1 ) , \ldots , f ( k ) \} \ = \ \{ g ( 1 ) , \ldots , g ( k ) \}$ Let $S$ be this common $k -$ element subset of $\{ 1 , \ldots , n \}$ Then $A ^ { t } B = ( A _ { S } ) ^ { t } ( B _ { S } )$ , so the left hand side of the identity equals det $( A _ { S } )$ det(BS). If $I \neq S$ , then det $\left( A _ { I } \right) \operatorname* { d e t } ( B _ { I } ) = 0$ , so the right hand side of the identity equals det $( A _ { S } )$ det(BS) too.
:::
