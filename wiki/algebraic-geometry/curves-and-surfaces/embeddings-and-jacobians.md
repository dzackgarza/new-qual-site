---
title: Embeddings and Jacobians
order: 9
topics:
- Jacobian
- Abel-Jacobi
- Canonical Embedding
---

# Embeddings and Jacobians

Two constructions attach a projective space or an abelian variety to a smooth projective curve: a very ample class gives a closed embedding into $\PP^N$ ([[T-DIVMAPPN]]), and the degree-zero part of the Picard group gives the Jacobian, an abelian variety of dimension $g$ whose tangent space at the identity is $H^1(C,\OO_C)$ ([[D-MODPIC]]).

[[T-D8TUX]]

## The Jacobian

[[T-U5QSY]]

[[T-CRVJACFUN]]

For a smooth projective curve $C$ of genus $g$ the functor of degree-zero line bundles is represented by an abelian variety $\Jac(C)$ of dimension $g$, so $\Pic^0(C)$ is the group of points of $\Jac(C)$ ([[T-U5QSY]], [[T-CRVJACFUN]], [[D-MODPIC]]).
A point $P_0\in C(k)$ gives the morphism $C\to\Jac(C)$, $P\mapsto\OO_C(P-P_0)$, and for $g\ge1$ it is a closed immersion; the resulting subvariety is the curve embedded in its Jacobian, and its class is the principal polarization.

## What this chapter still needs

The construction of $\Jac(C)$ as an abelian variety and the Abel--Jacobi theorem that identifies its divisor classes with integrals of holomorphic differentials are taken from Miranda, *Algebraic Curves and Riemann Surfaces* (bibliography key `Mir95`), which is not retained in `tmp/sources`.
The statements to transcribe are the construction of the Jacobian variety and the Abel--Jacobi theorem in Miranda's treatment of the Jacobian; their chapter and statement numbers are to be read from the book when it is supplied, not guessed, and the two paragraphs above then cite those numbers in place of the cards.

## Properness and the valuative criterion

Properness of the Jacobian also follows from the valuative criterion: for a discrete valuation ring $R$, $X\times\Spec R$ is regular, so a line bundle on the generic fibre extends by taking the closure of a divisor.
