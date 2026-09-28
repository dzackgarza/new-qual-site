---
schema: qual/card@1
id: P-TOPS06C
kind: problem
title: 'Degree of a map from a $(2n+1)$-manifold with $\pi_1\cong\ZZ/k$ to $\RP^{2n+1}$ is even'
classification:
  areas:
  - topology
  topics:
  - Degree
  - Manifolds
  - Projective Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Let $M$ be a $2n+1$ dimensional compact oriented manifold with $\pi_1(M) = \mathbb{Z}/k$, where $k$ is an odd integer.
Show that the degree of any map from $M$ to $\mathbb{RP}^{2n+1}$ is an even integer.
:::

::: {.solution}
<1>1. The induced homomorphism
$$
f_*:\pi_1(M)\cong\mathbb Z/k\longrightarrow
\pi_1(\mathbb{RP}^{2n+1})\cong\mathbb Z/2
$$
is trivial.
::: {.proof}
The image of an element whose order divides the odd integer $k$ must have order dividing both $k$ and $2$, hence must be the identity.
:::

<1>2. Therefore $f$ lifts through the universal double cover
$$
p:S^{2n+1}\to\mathbb{RP}^{2n+1}:
$$
there is $\widetilde f:M\to S^{2n+1}$ with
$$
f=p\circ\widetilde f.
$$
::: {.proof}
The lifting criterion for coverings says that a map lifts precisely when the image of its fundamental group lies in the subgroup corresponding to the covering. For the universal cover that subgroup is trivial, and <1>1 gives the condition.
:::

<1>3. Because $2n+1$ is odd, $\mathbb{RP}^{2n+1}$ is orientable and the covering $p$ has degree $2$ after compatible choices of orientation.
::: {.proof}
Odd-dimensional real projective space is orientable, and an oriented two-sheeted covering has degree $2$.
:::

<1>4. Hence
$$
\deg f=\deg p\cdot\deg\widetilde f=2\deg\widetilde f.
$$
::: {.proof}
Degree is multiplicative under composition of maps between closed oriented manifolds of the same dimension.
:::

<1>5. Therefore
$$
\boxed{\deg f\text{ is even}.}
$$
::: {.proof}
The expression in <1>4 is divisible by $2$.
:::
:::
