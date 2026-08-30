---
title: Invariant theory
order: 5
problems:
  topics:
  - Invariant Theory
  - Group Theory
---

# Invariant theory

Given a group acting linearly on a polynomial ring, describe the subring it fixes.

## The two finiteness theorems

- **Noether:** for $G$ finite with $\characteristic k \nmid \size G$, the invariant ring $k[V]^G$ is finitely generated, in degrees at most $\size G$.
  The proof is the Reynolds operator, averaging over $G$, which is Maschke's argument again.
- **Hilbert:** finite generation for reductive $G$ in general, proved from the ascending chain condition rather than by averaging.

## The standard computations

- **$S_n$ permuting variables:** the invariants are the symmetric polynomials, generated freely by $e_1, \dots, e_n$.
  This is the fundamental theorem of [[applied-algebra/symmetric-functions/index|symmetric functions]] read as an invariant theory statement.
- **$\ZZ/n$ acting by a root of unity:** the invariants are spanned by monomials whose exponent sum is divisible by $n$.
- **A finite group acting on $k[x,y]$:** compute by Molien's series
  \[
  \sum_d \dim(k[V]^G_d)\, t^d = {1\over \size G}\sum_{g\in G} {1\over \det(1 - tg)}
  ,\]
  which gives the Hilbert series of the invariant ring before any generator is found, and is usually the fastest way to see how many generators of each degree to expect.

## Why the Reynolds operator is the mechanism

Averaging over $G$ projects the polynomial ring onto its invariants and commutes with multiplication by invariants, which is what makes $k[V]^G$ a direct summand and gives finite generation.
It needs $\size G$ invertible, so modular invariant theory is a separate and much harder subject -- the same hypothesis, and the same failure, as in [[algebra/representations/maschke-and-schur|Maschke's theorem]].
