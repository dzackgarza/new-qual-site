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
a.
What is the degree of the antipodal map on the $n$-sphere? 

(No justification required)

b.  
Define a CW complex homeomorphic to the real projective $n\dash$space $\RP^n$.

c.
Let $\pi : \RP^n \to X$ be a covering map. Show that if $n$ is even, $\pi$ is a homeomorphism.
:::

::: {.solution}
<1>1. The degree of the antipodal map $a:S^n\to S^n$, $a(x)=-x$, is
$$\boxed{\deg a=(-1)^{n+1}.}$$
::: {.proof}
The antipodal map is the restriction of the linear map $-I$ on $\mathbb R^{n+1}$, whose determinant is $(-1)^{n+1}$.
:::

<1>2. A CW structure on $\mathbb{RP}^n$ has one cell $e^k$ in each dimension $0\le k\le n$.
::: {.proof}
Use the filtration
$$\mathbb{RP}^0\subset\mathbb{RP}^1\subset\cdots\subset\mathbb{RP}^n,$$
where $\mathbb{RP}^k$ is obtained from $\mathbb{RP}^{k-1}$ by attaching a $k$-cell; the attaching map is the antipodal quotient $S^{k-1}\to\mathbb{RP}^{k-1}$ on the boundary of the upper hemisphere.
:::

<1>3. Suppose now that $n$ is even and $\pi:\mathbb{RP}^n\to X$ is a covering map. Its number of sheets $d$ is finite.
::: {.proof}
The total space is compact. A fiber is a closed discrete subspace of the compact space $\mathbb{RP}^n$, hence finite. Since the base is connected, all fibers have the same finite cardinality $d$.
:::

<1>4. Euler characteristic multiplicativity gives
$$1=\chi(\mathbb{RP}^n)=d\,\chi(X).$$
::: {.proof}
For even $n$, the one-cell-per-dimension CW structure gives $\chi(\mathbb{RP}^n)=1$. Euler characteristic multiplies under finite coverings.
:::

<1>5. Hence $d=1$, so $\pi$ is a homeomorphism.
::: {.proof}
Both $d$ and $\chi(X)$ are integers and $d>0$, so $1=d\chi(X)$ forces $d=1$. A one-sheeted covering is a homeomorphism.
:::
:::
