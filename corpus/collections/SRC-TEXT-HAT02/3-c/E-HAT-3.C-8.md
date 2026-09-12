---
schema: qual/card@1
id: E-HAT-3.C-8
kind: problem
title: "Tensor product of Hopf algebras"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that the tensor product of two Hopf algebras is a Hopf algebra.

::: {.solution}
Let $A$ and $B$ be graded Hopf algebras over the same commutative coefficient ring. Give $A\otimes B$ the usual graded tensor-product algebra structure
\[
(a\otimes b)(a'\otimes b')
=(-1)^{|b||a'|}aa'\otimes bb'.
\]

Write the coproducts in Sweedler notation as
\[
\Delta_A(a)=\sum a_{(1)}\otimes a_{(2)},
\qquad
\Delta_B(b)=\sum b_{(1)}\otimes b_{(2)}.
\]
Define
\[
\Delta_{A\otimes B}(a\otimes b)
=
\sum (-1)^{|a_{(2)}||b_{(1)}|}
(a_{(1)}\otimes b_{(1)})
\otimes
(a_{(2)}\otimes b_{(2)}).
\]
Equivalently, this is the composite
\[
A\otimes B
\xrightarrow{\Delta_A\otimes\Delta_B}
(A\otimes A)\otimes(B\otimes B)
\longrightarrow
(A\otimes B)\otimes(A\otimes B),
\]
where the second map interchanges the middle two factors with the Koszul sign.

Coassociativity follows immediately from coassociativity of $\Delta_A$ and $\Delta_B$ together with associativity of the graded symmetry. The counit is
\[
\varepsilon_A\otimes\varepsilon_B,
\]
and the two counit identities follow factorwise. Finally, $\Delta_{A\otimes B}$ is an algebra homomorphism because $\Delta_A$ and $\Delta_B$ are algebra homomorphisms and the Koszul sign in the middle interchange is exactly the sign required by the graded tensor-product multiplication.

Thus $A\otimes B$ satisfies the Hopf-algebra axioms.
:::
