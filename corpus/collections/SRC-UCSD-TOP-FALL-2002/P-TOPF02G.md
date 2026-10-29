---
schema: qual/card@1
id: P-TOPF02G
kind: problem
title: "Submanifold representatives of CP^n homology generators and cohomology ring"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Describe submanifold representatives of the generators of the homology groups of $\CP^n$, and explain how to use these to determine the cohomology ring structure.
:::

::: {.solution}

::: pf

::: {.pf-step #cp-k-generates-homology}
For each $0\le k\le n$, the standard linear subspace
$$
\CP^k=\{[z_0:\cdots:z_n]:z_{k+1}=\cdots=z_n=0\}\subset\CP^n
$$
represents a generator of
$$
H_{2k}(\CP^n;\ZZ)\cong\ZZ.
$$

::: pf-proof
The standard CW structure on $\CP^n$ has one cell in each even dimension $0,2,\dots,2n$ and no odd cells. The filtration
$$
\CP^0\subset\CP^1\subset\cdots\subset\CP^n
$$
is this CW filtration, and the fundamental class of $\CP^k$ generates $H_{2k}$.
:::

:::

::: pf-step
Let $x\in H^2(\CP^n;\ZZ)$ be the Poincare dual of the hyperplane
$$
\CP^{n-1}\subset\CP^n.
$$

::: pf-proof
The hyperplane has real codimension $2$, so its Poincare dual lies in degree $2$, where the cohomology group is infinite cyclic.
:::

:::

::: pf-step
For $1\le k\le n$, the class $x^k$ is Poincare dual to a linear subspace $\CP^{n-k}$.

::: pf-proof
Choose $k$ generic complex hyperplanes. They intersect transversely, and their intersection is a complex linear subspace of codimension $k$, hence a copy of $\CP^{n-k}$. Poincare duality identifies transverse intersection of oriented submanifolds with cup product of their dual classes, so the dual class is $x^k$.
:::

:::

::: {.pf-step #x-k-generates-cohomology}
Consequently $x^k$ generates $H^{2k}(\CP^n;\ZZ)$ for $0\le k\le n$.

::: pf-proof
By step [](#cp-k-generates-homology){.pf-ref}, $[\CP^{n-k}]$ is a generator of the corresponding homology group, so its Poincare dual is a generator of $H^{2k}$.
:::

:::

::: {.pf-step #truncation-relation}
Since there is no cohomology above degree $2n$, we have $x^{n+1}=0$.

::: pf-proof
The class $x^{n+1}$ would lie in $H^{2n+2}(\CP^n;\ZZ)=0$.
:::

:::

::: pf-step
Therefore
$$
H^*(\CP^n;\ZZ)\cong\ZZ[x]/(x^{n+1}),
\qquad |x|=2.
$$

::: pf-proof
Steps [](#x-k-generates-cohomology){.pf-ref} and [](#truncation-relation){.pf-ref} give one generator $x^k$ in each nonzero even degree and the single truncation relation.
:::

:::

:::

:::

