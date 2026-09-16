---
schema: qual/card@1
id: T-LEFHYP
kind: theorem
title: The Lefschetz hyperplane theorem
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
---

::: {.theorem title="Lefschetz hyperplane theorem"}
Let $X \subseteq \PP^N$ be a projective variety of dimension $n$ over $\CC$, and let $Y = X \cap H$ be a hyperplane section such that $X \setminus Y$ is smooth.
Then the restriction maps
\[
H^i(X, \ZZ) \to H^i(Y, \ZZ)
\]
are isomorphisms for $i < n - 1$ and injective for $i = n - 1$, and the maps $\pi_i(Y) \to \pi_i(X)$ are isomorphisms for $i < n - 1$ and surjective for $i = n - 1$.
:::

::: {.example}
A smooth hypersurface $Y \subseteq \PP^{n}$ with $n \geq 3$ has $\pi_1(Y) \cong \pi_1(\PP^{n}) = 1$ and $H^2(Y, \ZZ) \cong H^2(\PP^{n}, \ZZ) \cong \ZZ$ when $n \geq 4$.
Iterating, a smooth complete intersection of dimension at least $2$ in projective space is simply connected.
A smooth plane curve of degree $d \geq 3$ is a hyperplane section of dimension $1$, and the theorem makes no claim about its fundamental group, which is nontrivial.
:::

::: {.remark}
Every hypersurface section is a hyperplane section after a Veronese embedding, so the theorem applies to $Y = X \cap V(F)$ for any homogeneous $F$ with $X \setminus Y$ smooth.
The proof uses that $X \setminus Y$ is an affine variety of dimension $n$, which has the homotopy type of a CW complex of dimension at most $n$.
:::
