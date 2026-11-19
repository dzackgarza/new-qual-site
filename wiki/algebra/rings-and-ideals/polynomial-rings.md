---
title: Polynomial rings
order: 30
topics:
- Polynomials
- Noetherian Rings
---

# Polynomial rings

Throughout, $R$ is a commutative ring with identity.

Over an integral domain the degree is additive, $\deg(fg)=\deg f+\deg g$, so $R[x]$ is an integral domain, its units are the constants that are units of $R$, and a nonzero polynomial has as many roots in $R$ as its degree allows.

## The ring $R[x]$

[[FD-CI4NB]]

[[D-GURUB]]

[[D-GXMDW]]

[[D-GOFWL]]

[[D-JNCUB]]

## Evaluation

For $a\in R$, evaluation at $a$ is the ring homomorphism $R[x]\to R$ that fixes $R$ and sends $x$ to $a$; the kernel is the ideal of polynomials vanishing at $a$, and the two computations a qualification problem asks for are the quotient $R[x]/\generators{x-a}\cong R$ and the description of a simple field extension as a quotient of $k[x]$.

[[P-CH10-55]]

[[P-LARQ14]]

## Properties inherited from $R$

Two of the three properties of $R$ tested here pass to $R[x]$: a unique factorization domain has a unique factorization domain of polynomials, and a Noetherian ring has a Noetherian polynomial ring by the Hilbert basis theorem.
The third does not: $R[x]$ is a principal ideal domain exactly when $R$ is a field, and the ideal $\generators{2,x}\subseteq\ZZ[x]$ is the standard principal-ideal failure, proved on [[algebra/rings-and-ideals/which-kind-of-ring|Which kind of ring is this?]].

[[PR-GEHJF]]

[[T-YYLPH]]

[[E-XH2QU]]

[[P-QELLQ]]

## Content and Gauss's lemma

A factorization over the field of fractions descends to $R[x]$ when the polynomial is primitive, which is what makes irreducibility in $\ZZ[x]$ and in $\QQ[x]$ the same question for monic polynomials.

[[D-4VC6X]]

[[T-JEZZY]]

[[P-RMVDW]]

## Irreducibility

[[D-BVMTZ]]

[[PR-I1T7M]]

[[T-CF6S3]]

[[P-NGAW5]]

[[PR-RRTST]]

Irreducibility over a field $k$, the field $k[x]/\generators f$ for an irreducible $f$, and the cyclotomic polynomials are on [[algebra/fields/polynomials|Polynomials over a field]].
