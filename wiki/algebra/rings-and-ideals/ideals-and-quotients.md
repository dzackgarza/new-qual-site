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

Throughout, rings are commutative with identity.
The kernel of a ring homomorphism is an [[D-GOFWL|ideal]], and for an ideal $I\subseteq R$ the quotient map $R\to R/I$ is initial among ring homomorphisms out of $R$ that vanish on $I$.

[[PR-PZZUO]]

[[PR-ZDWKC]]

[[D-A7MC4]]

## The isomorphism theorems

For a ring homomorphism $\varphi\colon R\to S$, the first isomorphism theorem gives $R/\ker\varphi\cong\im\varphi$.
By the correspondence theorem, $J\mapsto J/I$ is an inclusion-preserving bijection from the ideals of $R$ containing $I$ to the ideals of $R/I$, and it restricts to bijections on prime, maximal, and radical ideals.

[[PR-Z3YWJ]]

[[PR-GGCEU]]

[[PR-LJE4C]]

[[E-VFEWT]]

## Prime and maximal ideals

A proper ideal contains no unit.
An ideal $\mfp$ is [[D-5BM46|prime]] if and only if $R/\mfp$ is an integral domain, and $\mfm$ is [[D-7XH2R|maximal]] if and only if $R/\mfm$ is a field.
Hence every maximal ideal is prime, and $(0)\subset\ZZ$ is prime and not maximal.
The [[D-CXXCG|prime spectrum]] $\spec R$ is the set of prime ideals of $R$, and the [[D-NX4KW|max spectrum]] $\mspec R\subseteq\spec R$ is the set of maximal ideals.

[[PR-RHQZT]]

[[D-FJ53F]]

[[D-5BM46]]

[[FD-OSSYR]]

[[PR-LX7GH]]

[[D-CXXCG]]

[[D-7XH2R]]

[[FD-CD2FE]]

[[D-NX4KW]]

## Units and simple rings

A ring $R\neq 0$ is a field if and only if its only ideals are $0$ and $R$.

[[PR-DDDXH]]

::: {.proof}
$\implies$: If $0\neq x\in I\normal R$ and every nonzero element is a unit, then $1 = x\inv x \in I$, so $I = R$.

$\impliedby$: For $x\in R\nonzero$, the ideal $Rx$ is nonzero, so $Rx = R$, and $1 = rx$ for some $r\in R$; hence $x$ is a unit.
:::

## Radicals

The [[D-JLCOX|radical]] of an ideal $I$ is $\sqrt I = \ts{x\in R \st x^n\in I \text{ for some } n\geq 1}$.
The [[D-C2IM4|nilradical]] $\sqrt{(0)}$ is the set of nilpotent elements, it equals $\Intersect_{\mfp\in\spec R}\mfp$, and $R/\sqrt{(0)}$ is reduced.
The [[D-2IO6Q|Jacobson radical]] $J(R)$ is the intersection of the maximal ideals, and $x\in J(R)$ if and only if $1-rx$ is a unit for every $r\in R$.

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

The existence of maximal ideals by Zorn's lemma is on [[algebra/rings-and-ideals/commutative-algebra|Commutative algebra]].

## Exercises on nilradicals and Jacobson radicals

These exercises show that every element of a finite ring is a unit or a zero divisor, that an element nilpotent modulo the nilradical is nilpotent, that maximal ideals are prime, that the nilradical is contained in the Jacobson radical, and that the nilradical is the intersection of the prime ideals.

[[E-AMD-4SSSVQJY]]

[[E-AMD-564ETBH5]]

[[E-AMD-E3N4BHJH]]

[[E-AMD-MCTH4JE3]]

[[E-AMD-UEHZOJ3K]]
