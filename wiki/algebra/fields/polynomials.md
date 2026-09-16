---
title: Polynomials over a field
order: 0
topics:
- Polynomials
- Irreducibility Criteria
---

# Polynomials over a field

## Polynomial rings and Gauss's lemma

For a field $k$, $k[x]$ is a Euclidean domain with respect to degree, hence a PID and a UFD, and its prime elements are the irreducible polynomials.
A polynomial in $\ZZ[x]$ is primitive if the greatest common divisor of its coefficients is $1$, and by Gauss's lemma a product of primitive polynomials is primitive.

[[FD-CI4NB]] [[FD-SZKGS]]

[[FD-24RNF]] [[FD-QFRSI]]

[[D-BVMTZ]]

[[FD-KPW3H]] [[FD-GHY34]]

[[D-4VC6X]]

[[T-JEZZY]]

[[FT-OXN3Y]]

::: {.corollary}
A primitive polynomial $p\in \ZZ[x]$ of positive degree is irreducible in $\ZZ[x]$ if and only if it is irreducible in $\QQ[x]$.
:::

## Standard factorizations and root counts

::: {.remark}
The identities below factor $x^n\pm y^n$.
By Descartes' rule of signs, the number of positive real roots of a real polynomial, counted with multiplicity, is at most the number of sign changes in its sequence of nonzero coefficients, and differs from it by an even number.
:::

[[FF-UC7SQ]] [[FF-ED3CD]]

[[FF-2AKVH]] [[FF-HAMDC]]

[[FF-HK72Z]]

## Characteristic, automorphisms, and perfect fields

The [[D-JNCUB|characteristic]] of a field is $0$ or a prime $p$, and its [[D-EOCCU|prime subfield]] is $\QQ$ or $\FF_p$ respectively.
In characteristic $p$, $(a+b)^p = a^p+b^p$, so $a\mapsto a^p$ is a field homomorphism.
For a group $G$ of automorphisms of a field $L$, the [[D-5FG7E|fixed field]] $L^G$ is the subfield of elements fixed by every element of $G$.
A field $k$ is [[D-KQFIV|perfect]] if every irreducible polynomial over $k$ is separable; equivalently, $k$ has characteristic $0$, or characteristic $p$ and $a\mapsto a^p$ is surjective on $k$.

[[D-JNCUB]]

[[PR-3X3TO]]

[[D-5FG7E]]

[[D-EOCCU]]

[[T-U3EZL]]

[[D-MN47W]]

[[D-KGF4K]]

[[D-KQFIV]]

[[FD-YYLYR]]

[[FD-3GZPO]]

[[PR-IK6AM]]

## Cyclotomic polynomials

The $n$th [[D-BLV6F|cyclotomic polynomial]] $\Phi_n(x)=\prod(x-\zeta)$, the product over the primitive $n$th roots of unity $\zeta\in\CC$, has integer coefficients and satisfies
$$
x^n-1=\prod_{d\mid n}\Phi_d(x).
$$
Over $\QQ$, $\Phi_n$ is irreducible of degree $\phi(n)$, where $\phi$ is [[D-JX3YC|Euler's totient function]], so $[\QQ(\zeta_n):\QQ]=\phi(n)$ for a primitive $n$th root of unity $\zeta_n$.
By the Kronecker--Weber theorem, every finite abelian extension of $\QQ$ is contained in a [[D-IPR4B|cyclotomic field]].

[[D-BLV6F]]

[[D-IPR4B]]

[[PR-DCK6S]]

[[T-QX5QU]]

[[D-FK47C]]

## Exercises

[[E-LUR7G]] [[E-6OUJV]] [[E-OB3LO]] [[E-PHSV5]]
