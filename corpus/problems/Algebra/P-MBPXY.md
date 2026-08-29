---
schema: qual/card@1
id: P-MBPXY
kind: problem
title: Hom–tensor adjunction
classification:
  areas:
  - algebra
  topics:
  - Tensor Products
  - Representation Theory
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Which is the connection between Hom and tensor product?
What is this called in representation theory?
:::

::: {.solution}
<1>1. The connection is the Hom–tensor adjunction:
$$\operatorname{Hom}_R(M \otimes_R N, P) \cong \operatorname{Hom}_R(M, \operatorname{Hom}_R(N, P)).$$
Proof: statement of the adjunction.

<1>2. This is a natural isomorphism of $R$-modules (and of abelian groups), for $R$-modules $M, N, P$.
Proof: the adjunction is natural in all three variables.

<1>3. In representation theory, this is called **Frobenius reciprocity** (in the form relating induction and restriction).
Proof: the name in representation theory.

<1>4. Specifically, for a subgroup $H \le G$, Frobenius reciprocity states
$$\operatorname{Hom}_G(\operatorname{Ind}_H^G V, W) \cong \operatorname{Hom}_H(V, \operatorname{Res}_H^G W),$$
which is the Hom–tensor adjunction with $M = \mathbb{C}[G]$ (as a $(\mathbb{C}[G], \mathbb{C}[H])$-bimodule), $N = V$, and the tensor product $\mathbb{C}[G] \otimes_{\mathbb{C}[H]} V = \operatorname{Ind}_H^G V$.
Proof: <1>1 specialized to group algebras.

<1>5. Q.E.D.
Proof: <1>2 and <1>4.
:::
