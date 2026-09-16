---
schema: qual/card@1
id: D-DEFPERF
kind: definition
title: Perfect pairings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Modules
  - Duality
relations:
- kind: uses
  target: D-DEFTENS
review: draft
prompts:
- What is a bilinear pairing of modules, and when is it perfect?
- Where does a perfect pairing appear in the statement of Serre duality?
---

::: {.definition title="perfect pairing"}
A bilinear \dfn{pairing} is a map $M \tensor_A N \to L$.
By the tensor-hom adjunction this is the same data as a canonical map
\[
M \to \Hom_A(N, L) .
\]
The pairing is **perfect** if this canonical map is an isomorphism.
:::

::: {.remark}
Perfection is a strictly stronger demand than non-degeneracy, which asks only that the canonical map be injective; over a field with finite-dimensional modules the two agree, and over a general ring they do not.

This is the form in which every duality statement on the exam is phrased.
Serre duality on a projective $n$-dimensional scheme asserts that the cup product
\[
H^i(X;\mcf) \tensor H^{n-i}(X; \mcf\dual \tensor \omega_X) \to H^n(X;\omega_X) \cong k
\]
is a perfect pairing of finite-dimensional $k$-vector spaces, which is what converts it into the usable statement $h^i(\mcf) = h^{n-i}(\mcf\dual \tensor \omega_X)$.
:::
