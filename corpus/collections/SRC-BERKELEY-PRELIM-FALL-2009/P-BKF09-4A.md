---
schema: qual/card@1
id: P-BKF09-4A
kind: problem
title: Berkeley Fall 2009 prelim problem 4A
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let p, n be positive integers with p prime. Let $G = G L _ { n } ( F _ { p } )$be the group of invertible$n \times n$matrices over the field with p elements. Let$U \subset G$ be the subgroup consisting of upper triangular matrices with all diagonal entries equal to 1. Prove that every p-subgroup of G is conjugate to a subgroup of U .
:::

::: {.solution}
By Sylow’s theorems it suffices to show that U is a Sylow p-subgroup of G. The above-diagonal entries of a matrix $X \in U$may be chosen arbitrarily in$F _ { p } ,$so$U$has order$p ^ { { \binom { n } { 2 } } }$. The order of G is$$( p ^ { n } - 1 ) ( p ^ { n } - p ) \cdot \cdot \cdot ( p ^ { n } - p ^ { n - 1 } ) = p ^ { \binom { n } { 2 } } ( p ^ { n } - 1 ) ( p ^ { n - 1 } - 1 ) \cdot \cdot \cdot ( p - 1 ) ,$$whose p-power factor is clearly$p ^ { { \binom { n } { 2 } } }$, as desired. The formula for the order of$G$can be derived as follows. We may choose the rows of a matrix$Y \in G$in succession, where the k-th row is arbitrary, provided it does not belong to the$( k - 1 )$-dimensional subspace spanned by the previously chosen rows (note that this procedure preserves the inductive hypothesis that the chosen rows are linearly independent). This gives$p ^ { n } - p ^ { k - 1 }$ choices for the k-th row. Now take the product over k from 1 to n.
:::
