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

::: problem
Describe submanifold representatives of the generators of the homology groups of $\mathbb{CP}^n$, and explain how to use these to determine the cohomology ring structure.
:::

::: {.solution}
<1>1. For each $0\le k\le n$, the standard linear subspace
$$
\mathbb{CP}^k=\{[z_0:\cdots:z_n]:z_{k+1}=\cdots=z_n=0\}\subset\mathbb{CP}^n
$$
represents a generator of
$$
H_{2k}(\mathbb{CP}^n;\mathbb Z)\cong\mathbb Z.
$$
::: {.proof}
The standard CW structure on $\mathbb{CP}^n$ has one cell in each even dimension $0,2,\dots,2n$ and no odd cells. The filtration
$$
\mathbb{CP}^0\subset\mathbb{CP}^1\subset\cdots\subset\mathbb{CP}^n
$$
is this CW filtration, and the fundamental class of $\mathbb{CP}^k$ generates $H_{2k}$.
:::

<1>2. Let $x\in H^2(\mathbb{CP}^n;\mathbb Z)$ be the Poincare dual of the hyperplane
$$
\mathbb{CP}^{n-1}\subset\mathbb{CP}^n.
$$
::: {.proof}
The hyperplane has real codimension $2$, so its Poincare dual lies in degree $2$, where the cohomology group is infinite cyclic.
:::

<1>3. For $1\le k\le n$, the class $x^k$ is Poincare dual to a linear subspace $\mathbb{CP}^{n-k}$.
::: {.proof}
Choose $k$ generic complex hyperplanes. They intersect transversely, and their intersection is a complex linear subspace of codimension $k$, hence a copy of $\mathbb{CP}^{n-k}$. Poincare duality identifies transverse intersection of oriented submanifolds with cup product of their dual classes, so the dual class is $x^k$.
:::

<1>4. Consequently $x^k$ generates $H^{2k}(\mathbb{CP}^n;\mathbb Z)$ for $0\le k\le n$.
::: {.proof}
By <1>1, $[\mathbb{CP}^{n-k}]$ is a generator of the corresponding homology group, so its Poincare dual is a generator of $H^{2k}$.
:::

<1>5. Since there is no cohomology above degree $2n$, we have $x^{n+1}=0$.
::: {.proof}
The class $x^{n+1}$ would lie in $H^{2n+2}(\mathbb{CP}^n;\mathbb Z)=0$.
:::

<1>6. Therefore
$$
H^*(\mathbb{CP}^n;\mathbb Z)\cong\mathbb Z[x]/(x^{n+1}),
\qquad |x|=2.
$$
::: {.proof}
Steps <1>4--<1>5 give one generator $x^k$ in each nonzero even degree and the single truncation relation.
:::
:::

