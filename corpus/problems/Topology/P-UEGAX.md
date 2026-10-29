---
schema: qual/card@1
id: P-UEGAX
kind: problem
title: Degree of the antipodal map, a CW structure on $\RP^n$, and even-dimensional
  coverings
classification:
  areas:
  - topology
  topics:
  - Degree
  - Cell Complexes
  - Covering Spaces
relations: []
review: draft
---

::: {.problem}
(a) What is the degree of the antipodal map on the $n$-sphere?

(No justification required)

(b) Define a CW complex homeomorphic to the real projective $n\dash$space $\RP^n$.

(c) Let $\pi : \RP^n \to X$ be a covering map. Show that if $n$ is even, $\pi$ is a homeomorphism.
:::

::: {.solution}

::: pf

::: pf-step

(a) The degree of the antipodal map $a:S^n\to S^n$, $a(x)=-x$, is
$$\boxed{\deg a=(-1)^{n+1}.}$$

::: pf-proof

The antipodal map is the restriction of the linear map $-I$ on $\RR^{n+1}$, whose determinant is $(-1)^{n+1}$.

:::

:::

::: pf-step

(b) A CW structure on $\RP^n$ has one cell $e^k$ in each dimension $0\le k\le n$.

::: pf-proof

Take the filtration
$$\RP^0\subset\RP^1\subset\cdots\subset\RP^n,$$
where $\RP^k$ is obtained from $\RP^{k-1}$ by attaching a $k$-cell; the attaching map is the antipodal quotient $S^{k-1}\to\RP^{k-1}$ on the boundary of the upper hemisphere.

:::

:::

::: pf-step

(c) Suppose now that $n$ is even and $\pi:\RP^n\to X$ is a covering map. Its number of sheets $d$ is finite.

::: pf-proof

The total space is compact. A fiber is a closed discrete subspace of the compact space $\RP^n$, hence finite. Since the base is connected, all fibers have the same finite cardinality $d$.

:::

:::

::: pf-step

Euler characteristic multiplicativity gives
$$1=\chi(\RP^n)=d\,\chi(X).$$

::: pf-proof

For even $n$, the CW structure of part (b) gives $\chi(\RP^n)=\sum_{k=0}^n(-1)^k=1$.
The base $X$ is a compact manifold, being the continuous image of $\RP^n$ and locally homeomorphic to it, and it is Hausdorff because disjoint neighbourhoods of two finite fibres in $\RP^n$ can be chosen to be unions of sheets; so $X$ has the homotopy type of a finite CW complex.
Lifting a CW structure along a $d$-sheeted covering multiplies the number of cells in each dimension by $d$, so $\chi(\RP^n)=d\,\chi(X)$.

:::

:::

::: pf-step

Hence $d=1$, so $\pi$ is a homeomorphism.

::: pf-proof

Both $d$ and $\chi(X)$ are integers and $d>0$, so $1=d\chi(X)$ forces $d=1$. A one-sheeted covering is a homeomorphism.

:::

:::

:::

:::
