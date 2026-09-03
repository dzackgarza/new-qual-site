---
title: Polynomials over a field
order: 0
problems:
  topics:
  - Polynomials
  - Irreducibility Criteria
---

# Polynomials over a field

The layer beneath field theory: what $k[x]$ looks like, and how to tell whether something factors.

## Basics

Over a field, $k[x]$ is Euclidean by degree, hence a PID and a UFD.  That makes irreducible polynomials the prime elements and turns gcd computations into the basic tool for factorization and extension theory.
Over $\ZZ[x]$, Gauss's lemma is the bridge back to $\QQ[x]$: strip off the content, work with a primitive polynomial, and test irreducibility over the field of fractions.

[[FD-CI4NB]] [[FD-SZKGS]]

[[FD-24RNF]] [[FD-QFRSI]]

[[D-BVMTZ]]

[[FD-KPW3H]] [[FD-GHY34]]

[[D-4VC6X]]

[[T-JEZZY]]

[[FT-OXN3Y]]

::: {.corollary}
A primitive $p\in \QQ[x]$ is irreducible exactly when it is irreducible in $\ZZ[x]$.
:::

## Standard factorizations and root counts

::: {.remark}
Irreducibility arguments usually begin with an attempt to factor by hand, so the identities below are worth having ready.
Descartes' rule bounds how many real roots such a factorization can account for, which is often enough to finish a problem over $\QQ$ or $\RR$.
:::

[[FF-UC7SQ]] [[FF-ED3CD]]

[[FF-2AKVH]] [[FF-HAMDC]]

[[FF-HK72Z]]

## Field-theoretic prerequisites

Polynomial behavior depends on the base field.
Characteristic determines the prime subfield and controls derivatives; automorphisms and fixed fields are what later turn roots into Galois data; perfectness is the condition that removes inseparability.
Keep these notions adjacent to the polynomial criteria because changing the base field can change factorization and which roots lie in the base field.

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

The $n$th cyclotomic polynomial $\Phi_n$ packages the primitive $n$th roots of unity, with
\[
x^n-1=\prod_{d\mid n}\Phi_d(x).
\]
Over $\QQ$, $\Phi_n$ is irreducible and has degree $\varphi(n)$, so adjoining one primitive $n$th root produces the cyclotomic field of that degree.
This is the standard place where polynomial factorization, Euler's totient, and Galois theory meet.

[[D-BLV6F]]

[[D-IPR4B]]

[[PR-DCK6S]]

[[T-QX5QU]]

[[D-FK47C]]

## Exercises

[[E-LUR7G]] [[E-6OUJV]] [[E-OB3LO]] [[E-PHSV5]]
