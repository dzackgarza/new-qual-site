---
title: Quotients, products, and automorphisms
order: 30
topics:
- Isomorphism Theorems
- Direct Products
- Semidirect Products
---

# Quotients, products, and automorphisms

Quotients remove a normal subgroup; products rebuild a group from smaller pieces.
The isomorphism theorems say precisely when these operations undo one another, and the direct/semidirect product criteria turn that formalism into a classification method.

## The isomorphism theorems

For a homomorphism $\varphi:G\to H$, the first theorem replaces $G$ by $G/\ker\varphi$ without changing its image.
The remaining theorems control a subgroup against a normal subgroup, nested normal subgroups, and the subgroup lattice of a quotient.
On an exam they are usually used backwards: recognize a quotient already present in the problem and choose the theorem that identifies it with something easier.

[[T-I5N43]]

[[T-NFQBO]]

[[T-6CQEB]]

[[T-RLVA4]]

## Products

An internal direct product requires commuting normal factors with trivial intersection whose product is all of $G$.
Dropping normality for one factor gives an internal semidirect product and records the missing commutativity as an action on the normal factor.
This is why Sylow theory feeds directly into product decompositions: once a Sylow subgroup is forced to be normal, the remaining work is to determine a complement and its action.

[[PR-BEIVF]]

[[T-TTZ2Y]]

[[T-SVJUN]]

[[FT-7NMQR]]

[[E-DFUYC]]

[[E-R6I7G]]

[[T-YNKCZ]]

[[T-SB6AV]]

::: {.remark title="Recognizing a semidirect product"}
$G \cong N \semidirect H$ exactly when $N \normal G$, $H \leq G$, $N\intersect H = 1$ and $NH = G$.
When a Sylow argument produces a normal subgroup $N$, classification reduces to the possible complements and actions $H \to \Aut(N)$; this is the semidirect-product step in many small-order classifications.

For cyclic kernels, $\Aut(\ZZ/n) \cong (\ZZ/n)^\times$, so the possible actions are homomorphisms into this unit group, modulo the relevant equivalences.
:::

## Automorphism groups

Automorphism counts enter twice: as a classification invariant in their own right, and as the target for the action $H\to\operatorname{Aut}(N)$ defining a semidirect product.
For cyclic $N$, reduce immediately to $(\ZZ/n)^{\times}$.

[[PR-N6S6P]]

## Finitely generated abelian groups

Finite abelian groups are the case where the product decomposition is canonical enough to classify completely.
The invariant-factor and elementary-divisor forms encode the same module decomposition in different groupings; converting between them is a matter of regrouping prime powers.
Use whichever form makes the requested invariant—order, exponent, or quotient structure—visible fastest.

[[D-SS34F]]

[[D-JQNJQ]]

[[FD-JTWOB]] [[FD-H764S]]

[[PR-TLPVU]]

[[PR-2JG3F]]

[[PR-434DX]]
