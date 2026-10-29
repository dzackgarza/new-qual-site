---
schema: qual/card@1
id: P-TOPS10D
kind: problem
title: 'Manifold homotopy types of $\CP^n/\CP^k$'
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Projective Spaces
  - Quotient Spaces
relations: []
review: draft
---

::: {.problem}
For which $n$ and $k$ (with $0 < k < n$) is $X = \CP^n / \CP^k$ homotopy equivalent to a manifold?
:::

::: {.solution}

::: pf

::: {.pf-step #codimension-one-quotient-is-sphere}
If $k=n-1$, then
$$
\CP^n/\CP^{n-1}\cong S^{2n}.
$$

::: pf-proof
The standard CW decomposition of $\CP^n$ is obtained from $\CP^{n-1}$ by attaching a single $2n$-cell. Collapsing the entire $(2n-2)$-skeleton therefore gives $D^{2n}/S^{2n-1}\cong S^{2n}$.
:::

:::

::: {.pf-step #degree-2-and-top-minus-2-cohomology}
Suppose $k\le n-2$. Then
$$
H^{2n-2}(X;\ZZ)\cong\ZZ,
\qquad
H^2(X;\ZZ)=0.
$$

::: pf-proof
By the relative-cohomology computation for $X=\CP^n/\CP^k$, the positive cohomology groups occur exactly in degrees $2j$ for $j=k+1,\ldots,n$. Since $k\le n-2$, the exponent $j=n-1$ occurs; since $k>0$, exponent $j=1$ does not.
:::

:::

::: {.pf-step #manifold-would-be-closed-oriented}
If $X$ were homotopy equivalent to a compact boundaryless manifold $M$, then $M$ would be a closed oriented $2n$-manifold.

::: pf-proof
The top nonzero integral cohomology of $X$ is $H^{2n}(X)\cong\ZZ$, so the manifold must have dimension $2n$ and nonzero integral top cohomology, hence be orientable.
:::

:::

::: {.pf-step #poincare-duality-contradiction}
Poincaré duality would give a perfect pairing
$$
H^2(M;\ZZ)\times H^{2n-2}(M;\ZZ)\to\ZZ,
$$
contradicting step [](#degree-2-and-top-minus-2-cohomology){.pf-ref}.

::: pf-proof
Homotopy equivalence transfers the cohomology groups in step [](#degree-2-and-top-minus-2-cohomology){.pf-ref} to $M$, but a nonzero class in $H^{2n-2}$ of a closed oriented $2n$-manifold must pair nontrivially with some class in $H^2$.
:::

:::

::: pf-step
Consequently
$$
\boxed{\CP^n/\CP^k\text{ has the homotopy type of a closed manifold exactly when }k=n-1,}
$$
in which case that manifold is $S^{2n}$.

::: pf-proof
Combine step [](#codimension-one-quotient-is-sphere){.pf-ref} and steps [](#degree-2-and-top-minus-2-cohomology){.pf-ref}, [](#manifold-would-be-closed-oriented){.pf-ref} and [](#poincare-duality-contradiction){.pf-ref}.
:::

:::

:::

:::
