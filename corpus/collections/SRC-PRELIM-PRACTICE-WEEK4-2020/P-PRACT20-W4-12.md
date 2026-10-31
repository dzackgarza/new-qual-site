---
schema: qual/card@1
id: P-PRACT20-W4-12
kind: problem
title: Nullity of a linear map from $2\times3$ matrices onto $\RR^4$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
  - Rank and Nullity
relations: []
review: draft
---

::: {.problem}
Suppose that $V$ is the vector space of real $2 \times 3$ matrices.
If $T$ is a linear transformation from $V$ onto $\RR^{4}$, what is the dimension of the null space of $T$?
:::

::: {.solution}
$T$ maps a 6-dimensional vector space onto a 4-dimensional vector space.
By the rank-nullity theorem,

$$
\dim R(T)+\dim N(T)=6,
$$

and since $T$ is onto, $\dim R(T)=\dim\RR^4=4$, so $\boxed{\dim N(T)=2}$.
:::
