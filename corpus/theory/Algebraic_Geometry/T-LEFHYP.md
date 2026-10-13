---
schema: qual/card@1
id: T-LEFHYP
kind: theorem
title: The Lefschetz hyperplane theorem
slogan: 'A smooth hyperplane section inherits the ambient topology below middle degree; new cohomology and homotopy can first appear in the middle.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Lefschetz Theorems
  - Hyperplane Sections
  - Topology of Varieties
relations: []
review: draft
prompts:
- What is the Lefschetz hyperplane section theorem?
- What is the weak Lefschetz theorem?
---

::: {.theorem title="Lefschetz hyperplane theorem"}
Let $X \subseteq \PP^N_\CC$ be a smooth projective variety of dimension $n$, and let
$$
Y=X\cap H
$$
be a smooth hyperplane section.
Then the restriction maps
$$
H^i(X, \ZZ) \to H^i(Y, \ZZ)
$$
are isomorphisms for $i < n - 1$ and injective for $i = n - 1$, and the maps $\pi_i(Y) \to \pi_i(X)$ are isomorphisms for $i < n - 1$ and surjective for $i = n - 1$.
:::

::: {.example}
A smooth hypersurface $Y \subseteq \PP^{n}$ with $n \geq 3$ has $\pi_1(Y) \cong \pi_1(\PP^{n}) = 1$ and $H^2(Y, \ZZ) \cong H^2(\PP^{n}, \ZZ) \cong \ZZ$ when $n \geq 4$.
Iterating, a smooth complete intersection of dimension at least $2$ in projective space is simply connected.
A smooth plane curve of degree $d \geq 3$ is a hyperplane section of dimension $1$, and the theorem makes no claim about its fundamental group, which is nontrivial.
:::

::: {.remark}
If $D=X\cap V(F)$ is a smooth hypersurface section cut out by a homogeneous polynomial of degree $d$, then after the $d$-uple Veronese embedding it becomes a smooth hyperplane section, so the theorem applies to $D\hookrightarrow X$.

The topological proof studies the pair $(X,Y)$ by Morse theory on the affine complement $X\sm Y$. The resulting relative homotopy groups vanish below degree $n$, which gives the stated connectivity range.
:::
