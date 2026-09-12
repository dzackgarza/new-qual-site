---
schema: qual/card@1
id: P-PSTM-04
kind: problem
title: Separating a compact set from an exterior point
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let X be a Hausdorff space.
Suppose A is a compact subspace, and $x \in X \setminus A$ Show that there exist disjoint open sets U and V containing A and x, respectively.
:::

::: {.solution}
Let $y \in A$ . Since $x \in X \setminus A$ , we see that $y \neq x .$ . Since X is Hausdorff, there are open, disjoint sets $U _ { y }$ and $V _ { y }$ containing y and x, respectively.

Now note that $\{ U _ { y } \} _ { y \in A }$ is an open cover of A. Since A is compact, this cover admits a finite subcover, say, $U _ { y _ { 1 } } , \ldots , U _ { y _ { n } }$ . Define:

$$
U : = \bigcup _ { i = 1 } ^ { n } U _ { y _ { i } } \quad { \mathrm { a n d } } \quad V : = \bigcap _ { i = 1 } ^ { n } V _ { y _ { i } } .
$$

It is readily seen that U and V are the desired open sets.
:::
