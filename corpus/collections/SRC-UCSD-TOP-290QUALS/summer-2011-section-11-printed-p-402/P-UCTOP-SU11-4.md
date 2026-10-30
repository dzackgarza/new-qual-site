---
schema: qual/card@1
id: P-UCTOP-SU11-4
kind: problem
title: 'Manifold homotopy types of $\CP^n/\CP^k$'
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

::: {.problem}
For which $n \geq 2$ and $0 < k < n$ is $X = \CP^n / \CP^k$ homotopy-equivalent to a manifold?
:::

::: {.solution}

::: pf

::: pf-step
The quotient $X=\CP^n/\CP^k$ has integral cohomology
$$
H^r(X)\cong
\begin{cases}
\ZZ,&r=0,\\
\ZZ,&r=2i\text{ for }k+1\le i\le n,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof
This is the relative cohomology computation for $(\CP^n,\CP^k)$, equivalently the cellular cohomology of the quotient after collapsing the $2k$-skeleton.
:::

:::

::: {.pf-step #k-equals-n-minus-1-gives-sphere}
If $k=n-1$, then
$$
X=\CP^n/\CP^{n-1}\cong S^{2n}.
$$

::: pf-proof
The standard CW structure on $\CP^n$ is obtained from $\CP^{n-1}$ by attaching a single $2n$-cell. Collapsing $\CP^{n-1}$ to a point therefore gives $D^{2n}/S^{2n-1}\cong S^{2n}$.
:::

:::

::: {.pf-step #suppose-manifold-exists}
Suppose $k<n-1$ and $X$ were homotopy-equivalent to a closed manifold $M$.

::: pf-proof
A closed $m$-manifold $M$ has $H_m(M;\ZZ_2)\cong\ZZ_2$ and $H_i(M;\ZZ_2)=0$ for $i>m$, so $m=2n$, the top degree of the mod-2 homology of $X$; then $H_{2n}(M;\ZZ)\cong\ZZ$ makes $M$ orientable. The question concerns closed manifolds: every finite CW complex is homotopy equivalent to an open manifold, a regular neighbourhood of an embedding in some $\RR^N$.
:::

:::

::: {.pf-step #duality-forces-iso}
Then Poincaré duality would force
$$
H^{2n-2}(M;\ZZ)\cong H^2(M;\ZZ).
$$

::: pf-proof
For a closed orientable $2n$-manifold, cap product with the fundamental class gives $H^{2n-2}(M)\cong H_2(M)$. Since the cohomology here is torsion-free, the universal coefficient theorem identifies $H_2(M)$ with $H^2(M)$.
:::

:::

::: {.pf-step #contradiction-groups-differ}
But for $k<n-1$ one has
$$
H^{2n-2}(X;\ZZ)\cong\ZZ,
\qquad
H^2(X;\ZZ)=0,
$$
which is impossible under homotopy equivalence.

::: pf-proof
The first group is present because $n-1\ge k+1$, while the second vanishes because $k\ge1$.
:::

:::

::: pf-step
Therefore
$$
\boxed{\CP^n/\CP^k\text{ is homotopy-equivalent to a manifold exactly when }k=n-1.}
$$

::: pf-proof
The case $k=n-1$ is realized by the sphere in step [](#k-equals-n-minus-1-gives-sphere){.pf-ref}, and steps [](#suppose-manifold-exists){.pf-ref}, [](#duality-forces-iso){.pf-ref} and [](#contradiction-groups-differ){.pf-ref} exclude all other allowed values $0<k<n$.
:::

:::

:::

:::
