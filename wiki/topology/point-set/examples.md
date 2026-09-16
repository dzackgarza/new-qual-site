---
order: 1
topics:
- Metric Spaces
- Euclidean Spaces
- Continuity
- Continuous Functions
- Homeomorphisms
- Function Spaces
- Density
- Topological Groups
---

# Examples

## Point-set

[[D-SN2OH]]

::: {.example title="Open and closed subsets of $\RR$"}
\envlist

- $\QQ \subseteq \RR$ is neither open nor closed.
  Every neighborhood of a rational number contains an irrational number, and every neighborhood of an irrational number contains a rational number, so neither $\QQ$ nor $\RR\sm\QQ$ has an interior point.
  $\QQ$ has no isolated points, and every $r\in \RR$ is a boundary point and an accumulation point of $\QQ$.
- $\ZZ \subseteq \RR$ is closed and not open.
  Its complement $\RR\sm\ZZ = \bigcup_{n\in \ZZ} (n, n+1)$ is open, and every neighborhood of $n\in \ZZ$ meets $\RR\sm \ZZ$, so $\ZZ$ has no interior points.
  Every point of $\ZZ$ is an isolated point and a boundary point, and $\ZZ$ has no accumulation points.
- Points are closed in $\RR$, since $\RR \sm \ts{ p } = (-\infty, p) \union (p, \infty)$ is open.
  An infinite intersection of open sets need not be open: $\bigcap_{n\geq 1} (p-1/n, p+1/n) = \ts{ p }$.
- An interval $(a, b)$ is open in $\RR$, and $(a,b)\cross\ts{0}$ is not open in $\RR^d$ for $d\geq 2$.
- $\ts{1/n \suchthat n\geq 1}$ has no interior points, each of its points is isolated, its boundary is $\ts{0}\union\ts{1/n \suchthat n\geq 1}$, and its only accumulation point is $0$.
- The Cantor set has no interior points and no isolated points; every point of it is a boundary point and an accumulation point.

:::

### Common spaces and operations

::: {.example title="Standard spaces"}
$$
S^n,\ \DD^n,\ T^n,\ \RP^n,\ \CP^n,\ \mathbb{M},\ \mathbb{K},\ \Sigma_{g},\ \RP^\infty,\ \CP^\infty,
$$
where $\mathbb M$ is the Möbius band, $\mathbb K$ the Klein bottle, and $\Sigma_g$ the closed orientable surface of genus $g$.

:::

::: {.example title="Spaces that serve as counterexamples"}
\envlist

- Finite sets with the discrete topology.
- Subspaces of $\RR$ such as $(a, b)$, $(a, b]$, $(a, \infty)$, and $\ts{0} \union \ts{1/n\suchthat n\geq 1}$.
- $\QQ$.
- The topologist's sine curve.
- One-point compactifications.
- $\RR^\omega$, the countable product of copies of $\RR$, with the product, box, and uniform topologies.
- The Hawaiian earring.
- The Cantor set.
- Quaternionic projective space $\HP^n$.
- The dunce cap.
- The Alexander horned sphere.

:::

[[FE-BGEZL]] [[FE-U5AQQ]]

::: {.example title="Non-Hausdorff spaces"}
\envlist

- An infinite set with the cofinite topology.
- The quotient group $\RR/\QQ$ with the quotient topology, which is indiscrete.
- The line with two origins.
- An algebraic set $V(J) \subseteq \AA^n_{k}$ with infinitely many points, for $k$ a field and $J\normal \kx{n}$, with the Zariski topology.

:::

::: {.example title="Constructions of spaces"}
\envlist

- Knot complements in $S^3$
- Covering spaces
- Lens spaces
- Matrix groups
- Prism manifolds
- The pair of pants
- Seifert surfaces
- Surgery on manifolds
- Simplicial complexes, such as the following:

![A small simplicial complex](../../../../assets/assets/figures/image_2020-05-22-18-58-03.png)

:::

::: {.example title="Operations on spaces"}
\envlist

- Cartesian product $A\cross B$
- Wedge sum $A \vee B$
- Connected sum $A \# B$
- Quotient $A/B$ by a subspace
- Puncturing, $A\sm \theset{a_{1},\ldots,a_k}$
- Smash product $A\wedge B$
- Join $A\ast B$
- Cone $CA$
- Suspension $\Sigma A$
- Loop space $\Omega A$
- Identifying finitely many points

:::

### Alternative topologies

::: {.example title="Topologies used for counterexamples"}
The discrete, indiscrete, cofinite, and uniform topologies.

:::

::: {.example title="The cofinite topology"}
Let $X$ be a set with the cofinite topology.
Then $X$ is compact, and if $X$ is infinite, then $X$ is not Hausdorff, since any two nonempty open sets have finite complements and therefore intersect.

:::

[[PR-NJTN5]]

::: {.proof}
If the topology is discrete, every singleton is open.
Conversely, if $\ts x$ is open for each $x \in X$, then every $U\subseteq X$ is the union $\bigcup_{x\in U}\ts x$ of open sets, so $U$ is open.

:::

::: {.example title="The discrete topology"}
In the discrete topology on $X$, every subset is open.

- $X$ is Hausdorff.
- $X$ is compact if and only if $X$ is finite.
- $X$ is totally disconnected.
- Every map $f\colon X\to Y$ to a space $Y$ is continuous, since every preimage $f^{-1}(V)$ is a subset of $X$ and hence open.

:::

::: {.example title="The indiscrete topology"}
In the indiscrete topology on $X$, the only open sets are $\emptyset$ and $X$.

- If $X$ has at least two points, then $X$ is not Hausdorff.
- Every map $f\colon Y\to X$ from a space $Y$ is continuous, since the preimages of $\emptyset$ and $X$ are $\emptyset$ and $Y$.
- $X$ is compact.

:::

### Connectedness

| Space                  | Connected    | Locally connected |
| ------                 | ---------    | ----------------- |
| $\RR$                  | $\checkmark$ | $\checkmark$      |
| $[0, 1] \union [2, 3]$ |              | $\checkmark$      |
| Topologist's sine curve | $\checkmark$ |                   |
| $\QQ$                  |              |                   |
