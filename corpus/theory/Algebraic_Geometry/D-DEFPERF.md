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
$$
M \to \Hom_A(N, L) .
$$
The pairing is \dfn{perfect} if this canonical map is an isomorphism.
It is \dfn{nondegenerate} if the canonical maps $M\to\Hom_A(N,L)$ and $N\to\Hom_A(M,L)$ are injective.
:::

::: {.remark}
Over a field, with $M$ and $N$ finite-dimensional and $L$ the field, nondegenerate and perfect agree.
Over $\ZZ$, the pairing $\ZZ\tensor_\ZZ\ZZ\to\ZZ$, $a\tensor b\mapsto 2ab$, is nondegenerate and not perfect: the canonical map $\ZZ\to\Hom_\ZZ(\ZZ,\ZZ)\cong\ZZ$ is multiplication by $2$.

Let $X$ be a nonsingular projective variety of dimension $n$ over an algebraically closed field $k$, and let $\mcf$ be a locally free sheaf of finite rank.
Serre duality asserts that the cup product
$$
H^i(X;\mcf) \tensor H^{n-i}(X; \dualof{\mcf} \tensor \omega_X) \to H^n(X;\omega_X) \cong k
$$
is a perfect pairing of finite-dimensional $k$-vector spaces [@Har10a, Corollary III.7.7]; so $h^i(\mcf) = h^{n-i}(\dualof{\mcf} \tensor \omega_X)$.
:::
