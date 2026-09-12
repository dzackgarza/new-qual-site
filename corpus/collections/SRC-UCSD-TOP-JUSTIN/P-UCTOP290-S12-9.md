---
schema: qual/card@1
id: P-UCTOP290-S12-9
kind: problem
title: "Compactly-supported cohomology of X x R is a suspension isomorphism"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Compact Support
relations: []
review: draft
---

::: problem
Show that (working with cellular chain complexes)
\[
H_c^*(X \times \mathbb{R}) \cong H_c^{*-1}(X)
\]
for any space $X$.
This is the analogue for compactly-supported cohomology of the suspension isomorphism $\widetilde{H}^*(\Sigma X) \cong \widetilde{H}^{*-1}(X)$.
:::

::: {.solution}
<1>1. Give $\mathbb R$ the locally finite CW structure with vertices $v_i=i$ and oriented edges $e_i=[i,i+1]$, $i\in\mathbb Z$. Its compactly-supported cellular cochain complex is
$$
0\to \bigoplus_{i\in\mathbb Z}\mathbb Z\,v_i^*
\xrightarrow{\delta}
\bigoplus_{i\in\mathbb Z}\mathbb Z\,e_i^*\to0,
$$
where
$$
(\delta\phi)(e_i)=\phi(v_{i+1})-\phi(v_i).
$$
::: {.proof}
A compactly-supported cellular cochain is nonzero on only finitely many cells in this locally finite CW structure. The coboundary formula is dual to $\partial e_i=v_{i+1}-v_i$.
:::

<1>2. This complex has
$$
H_c^0(\mathbb R)=0,
\qquad
H_c^1(\mathbb R)\cong\mathbb Z.
$$
::: {.proof}
A finitely supported $0$-cochain with zero coboundary is constant on all vertices, hence zero. For degree $1$, the homomorphism
$$
\sum_i a_i e_i^*\longmapsto\sum_i a_i
$$
vanishes on coboundaries and induces an isomorphism from the cokernel of $\delta$ to $\mathbb Z$: every finite-support sequence of total sum zero is a finite difference sequence.
:::

<1>3. As a cochain complex of free abelian groups, $C_c^*(\mathbb R)$ is chain-homotopy equivalent to $\mathbb Z[-1]$, the complex with one copy of $\mathbb Z$ in cohomological degree $1$.
::: {.proof}
By <1>2 the complex has a single free cohomology group $\mathbb Z$ in degree $1$. Since all terms are free abelian, the short exact sequences defining cycles and boundaries split, so the acyclic summand is contractible and the complex splits up to chain homotopy as its cohomology placed in degree $1$.
:::

<1>4. For a locally finite CW complex $X$, the product CW structure gives
$$
C_c^*(X\times\mathbb R)
\cong C_c^*(X)\otimes C_c^*(\mathbb R)
$$
with the usual total differential.
::: {.proof}
Product cells are pairs $e^p\times e_i^q$. A compactly-supported cellular cochain has finite support on such pairs, so the cellular cochain group is the algebraic tensor product of the finite-support cochain groups. The cellular boundary of a product has the standard signed product formula, yielding the tensor-product differential.
:::

<1>5. Therefore
$$
\boxed{H_c^k(X\times\mathbb R)\cong H_c^{k-1}(X)}.
$$
::: {.proof}
Tensor the chain-homotopy equivalence in <1>3 with the free cochain complex $C_c^*(X)$. By <1>4,
$$
C_c^*(X\times\mathbb R)\simeq C_c^*(X)\otimes\mathbb Z[-1]
=C_c^*(X)[-1].
$$
Taking cohomology yields the stated degree shift.
:::
:::
