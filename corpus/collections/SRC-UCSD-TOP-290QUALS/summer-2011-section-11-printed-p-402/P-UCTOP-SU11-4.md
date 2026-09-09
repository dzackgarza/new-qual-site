---
schema: qual/card@1
id: P-UCTOP-SU11-4
kind: problem
title: 'Manifold homotopy types of $\mathbb{CP}^n/\mathbb{CP}^k$'
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

For which $n$ and $k$ is $X = \mathbb{CP}^n / \mathbb{CP}^k$ homotopy-equivalent to a manifold?

::: {.solution}
<1>1. The quotient $X=\mathbb{CP}^n/\mathbb{CP}^k$ has integral cohomology
$$
H^r(X)\cong
\begin{cases}
\mathbb Z,&r=0,\\
\mathbb Z,&r=2i\text{ for }k+1\le i\le n,\\
0,&\text{otherwise}.
\end{cases}
$$
::: {.proof}
This is the relative cohomology computation for $(\mathbb{CP}^n,\mathbb{CP}^k)$, equivalently the cellular cohomology of the quotient after collapsing the $2k$-skeleton.
:::

<1>2. If $k=n-1$, then
$$
X=\mathbb{CP}^n/\mathbb{CP}^{n-1}\cong S^{2n}.
$$
::: {.proof}
The standard CW structure on $\mathbb{CP}^n$ is obtained from $\mathbb{CP}^{n-1}$ by attaching a single $2n$-cell. Collapsing $\mathbb{CP}^{n-1}$ to a point therefore gives $D^{2n}/S^{2n-1}\cong S^{2n}$.
:::

<1>3. Suppose $k<n-1$ and $X$ were homotopy-equivalent to a closed manifold $M$.
::: {.proof}
Since $H^{2n}(X;\mathbb Z)\cong\mathbb Z$ and $H^i(X)=0$ for $i>2n$, the manifold must have dimension $2n$ and be orientable.
:::

<1>4. Then Poincaré duality would force
$$
H^{2n-2}(M;\mathbb Z)\cong H^2(M;\mathbb Z).
$$
::: {.proof}
For a closed orientable $2n$-manifold, cap product with the fundamental class gives $H^{2n-2}(M)\cong H_2(M)$. Since the cohomology here is torsion-free, the universal coefficient theorem identifies $H_2(M)$ with $H^2(M)$.
:::

<1>5. But for $k<n-1$ one has
$$
H^{2n-2}(X;\mathbb Z)\cong\mathbb Z,
\qquad
H^2(X;\mathbb Z)=0,
$$
which is impossible under homotopy equivalence.
::: {.proof}
The first group is present because $n-1\ge k+1$, while the second vanishes because $k\ge1$.
:::

<1>6. Therefore
$$
\boxed{\mathbb{CP}^n/\mathbb{CP}^k\text{ is homotopy-equivalent to a manifold exactly when }k=n-1.}
$$
::: {.proof}
The case $k=n-1$ is realized by the sphere in <1>2, and <1>3--<1>5 exclude all other allowed values $0<k<n$.
:::
:::
