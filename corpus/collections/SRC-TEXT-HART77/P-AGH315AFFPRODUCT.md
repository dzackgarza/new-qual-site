---
schema: qual/card@1
id: P-AGH315AFFPRODUCT
kind: problem
title: Products of affine varieties and the tensor product of coordinate rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Products
  - Coordinate Rings
  - Dimension
relations: []
review: draft
---

::: {.problem}
Let $X \subseteq \AA^n$ and $Y \subseteq \AA^m$ be affine varieties.

1. Show that $X \times Y \subseteq \AA^{n+m}$ with its induced topology is irreducible.
   The affine variety $X \times Y$ is called the **product** of $X$ and $Y$.
   Note that its topology is in general not the product topology.

2. Show that $A(X \times Y) \cong A(X) \tensor_k A(Y)$.

3. Show that $X \times Y$ is a product in the category of varieties, that is:

   - the projections $X \times Y \to X$ and $X \times Y \to Y$ are morphisms, and

   - given a variety $Z$ and morphisms $Z \to X$ and $Z \to Y$, there is a unique morphism $Z \to X \times Y$ commuting with the projections.

4. Show that $\dim (X \times Y) = \dim X + \dim Y$.

*Hint for the first part:* suppose $X \times Y = Z_1 \union Z_2$ with each $Z_i$ closed.
Let $X_i = \ts{ x \in X \st \ts{x} \times Y \subseteq Z_i }$.
Show that $X = X_1 \union X_2$ with $X_1, X_2$ closed, so $X = X_1$ or $X = X_2$, and hence $X \times Y = Z_1$ or $Z_2$.
:::
