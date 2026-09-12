---
schema: qual/card@1
id: P-BKF09-8A
kind: problem
title: Berkeley Fall 2009 prelim problem 8A
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the number of elements a in the ring $R = \mathbb { Z } / 6 4 6 4 \mathbb { Z }$such that$a = x ^ { 5 }$for some$x \in R$
:::

::: {.solution}
By the Chinese Remainder Theorem, $R \cong ( \mathbb { Z } / 6 4 \mathbb { Z } ) \times ( \mathbb { Z } / 1 0 1 \mathbb { Z } )$.
Since 101 is prime, the multiplicative group$( \mathbb { Z } / 1 0 1 \mathbb { Z } ) ^ { \times }$is cyclic of order 100. Its subgroup of fifth powers has order 20. Including 0, this gives 21 fifth powers in$\mathbb { Z } / 1 0 1 \mathbb { Z }$.
The multiplicative group$( \mathbb { Z } / 6 4 \mathbb { Z } ) ^ { \times }$has order 32. Since 32 is coprime to 5, every element of$( \mathbb { Z } / 6 4 \mathbb { Z } ) ^ { \times }$is a fifth power.
The non-invertible elements of$\mathbb { Z } / 6 4 \mathbb { Z }$belong to the ideal (2), hence their fifth powers belong to$( 2 ^ { 5 } )$.
This shows that the only non-invertible fifth powers in$\mathbb { Z } / 6 4 \mathbb { Z }$are$\{ 0 , 3 2 \}$, giving a total of 34 fifth powers in$\mathbb { Z } / 6 4 \mathbb { Z }$.
Hence there are$2 1 \times 3 4 = 7 1 4$ fifth powers in R.
:::
