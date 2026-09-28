---
schema: qual/card@1
id: P-TOPS13G
kind: problem
title: "Fundamental group of a 2-cell attached to S^1 by degree k and covering spaces of X_30"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Covering Spaces
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
(a) Let $k$ be a positive integer.
Compute the fundamental group of the space $X_k$ resulting from attaching a $2$-cell $e^2$ to a circle $S^1$ (identified with the unit circle in $\mathbb{C}$) by the map $\varphi : \partial e^2 = S^1 \to S^1$ defined by $\varphi(z) = z^k$.

(b) How many path-connected covering spaces of $X_{30}$ are there, up to equivalence (isomorphism)?
:::

::: {.solution}
<1>1. The space $X_k$ has one $0$-cell, one $1$-cell $a$, and one $2$-cell attached by the loop $a^k$.
::: {.proof}
The attaching map $z\mapsto z^k$ has degree $k$ on the circle.
:::

<1>2. Van Kampen gives
$$
\boxed{\pi_1(X_k)\cong\langle a\mid a^k=1\rangle\cong\mathbb Z/k.}
$$
::: {.proof}
The $2$-cell imposes precisely the relation that the generator of the circle has order dividing $k$.
:::

<1>3. Path-connected covering spaces of $X_{30}$ up to equivalence correspond to conjugacy classes of subgroups of $\mathbb Z/30$.
::: {.proof}
The CW complex is connected, locally path-connected, and semilocally simply connected, so the standard covering classification applies. The group is abelian, so conjugacy does nothing.
:::

<1>4. A cyclic group has exactly one subgroup for each divisor of its order. Since
$$
30=2\cdot3\cdot5,
$$
it has
$$
(1+1)^3=8
$$
positive divisors.
::: {.proof}
Subgroups of $\mathbb Z/n$ are uniquely determined by their order, and subgroup orders are exactly the divisors of $n$.
:::

<1>5. Therefore
$$
\boxed{X_{30}\text{ has }8\text{ path-connected covering spaces up to equivalence}.}
$$
::: {.proof}
Combine <1>3 and <1>4, including the identity and universal covers.
:::
:::
