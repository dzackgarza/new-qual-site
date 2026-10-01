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
Let $A$ be a commutative ring and let $M$, $N$, and $L$ be $A$-modules.
An $A$-bilinear \dfn{pairing} is a map
$$
\beta\colon M\tensor_A N\to L.
$$
By the tensor-hom adjunction it induces the two adjoint maps
$$
\beta_M\colon M\to\Hom_A(N,L),
\qquad
m\mapsto\bigl(n\mapsto\beta(m\tensor_A n)\bigr),
$$
and
$$
\beta_N\colon N\to\Hom_A(M,L),
\qquad
n\mapsto\bigl(m\mapsto\beta(m\tensor_A n)\bigr).
$$
The pairing is **perfect** if both $\beta_M$ and $\beta_N$ are isomorphisms.
:::

::: {.remark}
Perfection is a strictly stronger demand than non-degeneracy, which asks that both adjoint maps be injective; over a field with finite-dimensional modules the two agree, and over a general ring they do not.

Perfect pairings are the natural form of duality statements.
Serre duality on a projective $n$-dimensional scheme asserts that the cup product
$$
H^i(X;\mcf)
\tensor_k
H^{n-i}(X; \mcf\dual \tensor_{\OO_X} \omega_X)
\to H^n(X;\omega_X) \cong k
$$
is a perfect pairing of finite-dimensional $k$-vector spaces, which is what converts it into the usable statement $h^i(\mcf) = h^{n-i}(\mcf\dual \tensor_{\OO_X} \omega_X)$.
:::
