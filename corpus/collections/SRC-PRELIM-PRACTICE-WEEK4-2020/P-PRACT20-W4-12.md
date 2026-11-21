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

The argument is the card's own: rank-nullity applied to a surjection from a six-dimensional space.

::: pf

::: {.pf-step #dim}

$\dim V=6$.

::: pf-proof

$V$ is the space of real $2\times3$ matrices, which has the $6$ matrix units $E_{ij}$, $1\le i\le2$, $1\le j\le3$, as a basis: every matrix is a unique combination of them. Hence $\dim_{\RR}V=6$.

:::

:::

::: {.pf-step #nullity}

$\dim\ker T=6-4=2$.

::: pf-proof

$T:V\to\RR^{4}$ is surjective, so $\operatorname{range}T=\RR^{4}$ and $\operatorname{rank}T=4$. The rank-nullity theorem for a linear map on a finite-dimensional space gives $\dim V=\operatorname{rank}T+\dim\ker T$, that is $6=4+\dim\ker T$.

:::

:::

::: {.pf-step #conclusion}

The null space of $T$ has dimension $2$.

::: pf-proof

By step [](#nullity){.pf-ref},
$$
\boxed{\dim N(T)=2.}
$$

:::

:::

:::

:::
