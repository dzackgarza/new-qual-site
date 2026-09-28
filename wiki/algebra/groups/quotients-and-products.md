---
title: Quotients, products, and automorphisms
order: 30
topics:
- Isomorphism Theorems
- Direct Products
- Semidirect Products
---

# Quotients, products, and automorphisms

## The isomorphism theorems

For a homomorphism $\varphi\colon G\to H$, the first isomorphism theorem gives $G/\ker\varphi\cong\im\varphi$.
The second theorem compares a subgroup $H\le G$ with a normal subgroup $N\normal G$: $HN/N\cong H/(H\intersect N)$.
The third theorem compares nested normal subgroups $K\le N$ of $G$: $(G/K)/(N/K)\cong G/N$.
The correspondence theorem identifies the subgroups of $G/N$ with the subgroups of $G$ containing $N$.

[[T-I5N43]]

[[T-NFQBO]]

[[T-6CQEB]]

[[T-RLVA4]]

## Products

A group $G$ is the internal direct product of subgroups $H$ and $K$ if $H,K\normal G$, $H\intersect K=1$, and $HK=G$; then $hk=kh$ for all $h\in H$, $k\in K$, and $G\cong H\times K$.
If only $N\normal G$ is normal, $H\le G$, $N\intersect H=1$, and $NH=G$, then conjugation defines a homomorphism $\psi\colon H\to\Aut(N)$, $\psi(h)(n)=hnh\inv$, and $G\cong N\semidirect_\psi H$.
In particular, when a Sylow subgroup $N$ of $G$ is normal and has a complement $H$, the isomorphism type of $G$ is determined by $N$, $H$, and $\psi$.

[[PR-BEIVF]]

[[T-TTZ2Y]]

[[T-SVJUN]]

[[FT-7NMQR]]

[[E-DFUYC]]

[[E-R6I7G]]

[[T-YNKCZ]]

[[T-SB6AV]]

::: {.remark title="Semidirect products with a given kernel and complement"}
For groups $N$ and $H$, if $\varphi,\psi\colon H\to\Aut(N)$ satisfy $\psi=\varphi\circ\alpha$ for some $\alpha\in\Aut(H)$, then $N\semidirect_\varphi H\cong N\semidirect_\psi H$.
For $N=\ZZ/n$, $\Aut(\ZZ/n)\cong(\ZZ/n)^\times$, so every semidirect product $\ZZ/n\semidirect_\psi H$ is given by a homomorphism $\psi\colon H\to(\ZZ/n)^\times$.
:::

## Automorphism groups

For cyclic $N\cong\ZZ/n$, $\Aut(N)\cong(\ZZ/n)^\times$, whose order is the number of integers in $\ts{1,\ldots,n}$ coprime to $n$, the value at $n$ of [[D-JX3YC|Euler's totient function]].

[[PR-N6S6P]]

## Finitely generated abelian groups

A finite abelian group has an [[D-SS34F|invariant factor decomposition]] $\ZZ/d_1\times\cdots\times\ZZ/d_k$ with $d_1\divides d_2\divides\cdots\divides d_k$, and an [[D-JQNJQ|elementary divisor decomposition]] as a product of cyclic groups of prime-power order; each is unique up to the order of the factors.
The elementary divisors are the prime-power factors of the $d_i$, and $d_k$ is the product, over the primes $p$, of the largest elementary divisor that is a power of $p$.
The order of the group is $d_1\cdots d_k$ and its exponent is $d_k$.

[[D-SS34F]]

[[D-JQNJQ]]

[[FD-JTWOB]] [[FD-H764S]]

[[PR-TLPVU]]

[[PR-2JG3F]]

[[PR-434DX]]
