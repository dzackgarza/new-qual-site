---
title: Ideals and quotients
order: 10
topics:
- Ideals
- Prime Ideals
- Maximal Ideals
- Nilpotence
- Algebras
---

# Ideals and quotients

Ideals are the subobjects seen by ring homomorphisms: every kernel is an ideal, and quotienting by an ideal is the universal way to force its elements to vanish.
Most qual problems in this chapter therefore alternate between intrinsic ideal conditions and the corresponding property of a quotient ring.

[[PR-PZZUO]]

[[PR-ZDWKC]]

[[D-A7MC4]]

## The isomorphism theorems

The first isomorphism theorem identifies $R/\ker\varphi$ with $\operatorname{im}\varphi$.
The second and correspondence theorems are the bookkeeping rules for nested ideals: ideals above $I$ are exactly ideals of $R/I$, and properties defined through quotients can be transported across that correspondence.
In particular this is the clean way to compare prime, maximal, and radical ideals before and after quotienting.

[[PR-Z3YWJ]]

[[PR-GGCEU]]

[[PR-LJE4C]]

[[E-VFEWT]]

## Ideals

A proper ideal contains no unit.
Prime and maximal ideals sharpen that condition in different ways: $\mathfrak p$ is prime exactly when $R/\mathfrak p$ is a domain, while $\mathfrak m$ is maximal exactly when $R/\mathfrak m$ is a field.
Thus every maximal ideal is prime in a commutative ring with identity, but the converse fails already for $(0)\subset\ZZ$.
The spectra below package these two families when one needs to range over all of them at once.

[[PR-RHQZT]]

[[D-FJ53F]]

[[D-5BM46]]

[[FD-OSSYR]]

[[PR-LX7GH]]

[[D-CXXCG]]

[[D-7XH2R]]

[[FD-CD2FE]]

[[D-NX4KW]]

## Units and simplicity

A commutative ring with identity is a field precisely when it has no nonzero proper ideals: if $0\ne x$, the ideal $(x)$ must be all of $R$, so $x$ is a unit.
This is the one-line conversion between an ideal-theoretic hypothesis and the usual elementwise definition of a field.

[[PR-DDDXH]]

::: {.proof}
$\implies$: If $0\neq x\in I\normal R$ and every nonzero element is a unit, then $x$ is a unit, so $xx\inv = 1 \in I$ and $I = R$.

$\impliedby$: For $x\in R\nonzero$, $Rx = R$ gives $1 = rx$ for some $r$, so $x = r\inv$.
:::

## Radicals

The radical $\sqrt I$ records the elements whose powers land in $I$.
At $I=(0)$ this is the nilradical, and the key structural identity is $\sqrt{(0)}=\bigcap_{\mathfrak p\in\operatorname{Spec}R}\mathfrak p$; quotienting by it removes every nilpotent and produces a reduced ring.
The Jacobson radical instead intersects the maximal ideals.
For calculations, use the unit criterion $x\in J(R)$ iff $1-rx$ is a unit for every $r\in R$.

[[D-JLCOX]]

[[D-GIGM2]]

[[E-P5BF6]]

[[D-C2IM4]]

[[E-JAPBK]]

[[E-2ZO7O]]

[[D-2IO6Q]]

[[FF-7U6UY]]

[[FF-QWCKR]]

[[E-G4KAC]]

Zorn's lemma, and the maximal ideal it produces, are on [[algebra/rings-and-ideals/commutative-algebra|Commutative algebra]].

## Nilradicals and Jacobson radicals, worked

These exercises are the standard conversions to be able to reproduce: pass between nilpotence and reduction modulo $\sqrt{(0)}$, prove maximal ideals are prime, compare the nilradical with the Jacobson radical, and recover the prime-intersection description from the definitions.

[[E-AMD-4SSSVQJY]]

[[E-AMD-564ETBH5]]

[[E-AMD-E3N4BHJH]]

[[E-AMD-MCTH4JE3]]

[[E-AMD-UEHZOJ3K]]
