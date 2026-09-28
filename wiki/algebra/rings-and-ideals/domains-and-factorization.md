---
title: Domains and factorization
order: 20
topics:
- Integral Domains
- Factorization
- Euclidean Domains
---

# Domains and factorization

The implications among the classes of rings, with a ring separating each class from the next, are on [[algebra/rings-and-ideals/which-kind-of-ring|Which kind of ring is this?]].

## Elements

Let $R$ be an integral domain.
Elements $a,b\in R$ are [[D-R4H6F|associates]] if $a=ub$ for a [[D-QQIQZ|unit]] $u$, so factorizations are compared up to units and associates.
A nonzero nonunit $p$ is [[D-TO3IY|irreducible]] if $p=ab$ implies that $a$ or $b$ is a unit, and [[D-AWSKI|prime]] if $p\divides ab$ implies $p\divides a$ or $p\divides b$.

[[D-AVBIP]]

[[D-QQIQZ]]

[[D-TO3IY]]

[[FD-6LLJF]] [[FD-R4K7Z]]

[[D-AWSKI]]

[[FD-S52W7]]

[[D-R4H6F]]

::: {.remark title="Prime and irreducible elements"}
In an integral domain every prime element is irreducible.
In a [[D-INULL|unique factorization domain]] every irreducible element is prime.
In $\ZZ[\sqrt{-5}]$ the element $3$ is irreducible and not prime, since $3$ divides $9=(2+\sqrt{-5})(2-\sqrt{-5})$ and divides neither factor.
:::

## Classes of rings

A commutative ring $R\neq 0$ is an [[D-QJ3QL|integral domain]] if it has no nonzero [[D-4I3SL|zero divisors]], equivalently if $ab=ac$ and $a\neq0$ imply $b=c$.
It is a [[D-UI6CU|field]] if every nonzero element is a unit.

[[D-7O2CH]]

[[D-4I3SL]]

[[FD-S62UB]]

[[D-QJ3QL]]

[[FD-2A5XH]]

[[D-UI6CU]]

[[FD-SNOTW]]

[[E-HOJKE]]

### Euclidean domains, principal ideal domains, and unique factorization domains

For integral domains,
$$
\text{Euclidean domain}\implies\text{PID}\implies\text{UFD}\implies\text{integral domain},
$$
and none of these implications reverses.
In a [[D-NKRGN|Euclidean domain]] the division algorithm computes greatest common divisors; in a [[D-HTIL5|principal ideal domain]] $\gens{a,b}=\gens{d}$ for a greatest common divisor $d$ of $a$ and $b$; and in a [[D-INULL|unique factorization domain]] every nonzero nonunit is a product of irreducible elements, unique up to order and associates.

[[D-D7VK2]]

[[D-HTIL5]]

[[E-KB4GA]]

[[D-INULL]]

[[FD-25SUQ]]

[[D-NKRGN]]

[[FD-GXXBV]]

### Other classes of rings

- A ring is [[D-TZXBO|Noetherian]] if every ascending chain of ideals stabilizes.

- A ring is [[D-PQHHJ|reduced]] if its only nilpotent element is $0$.

- A ring is [[D-TGB4R|local]] if it has a unique maximal ideal.

- A [[D-HWLVG|valuation ring]] is an integral domain $R$ with fraction field $K$ such that $x\in R$ or $x\inv\in R$ for every $x\in K^\times$; a [[D-VK2KZ|discrete valuation ring]] is a valuation ring whose valuation has value group $\ZZ$.

- In a [[D-WUGPG|Dedekind domain]] every nonzero proper ideal is a product of prime ideals, uniquely up to order.

- A Noetherian local ring $(R,\mfm)$ is [[D-DEFREGLR|regular]] if $\dim_{R/\mfm}\mfm/\mfm^2=\dim R$.

[[D-TZXBO]]

[[D-PQHHJ]]

[[FF-U4FHF]]

[[D-TGB4R]]

[[E-YYL5U]]

[[E-K4SU4]]

[[E-PQ3FR]]

[[D-WUGPG]]

[[E-M6J67]]

[[D-HWLVG]]

[[D-VK2KZ]]

[[D-DEFREGLR]]

[[FF-CQSNC]]

## Structure theorems

An $R$-module is [[D-4KM4P|simple]] if it is nonzero and has no submodules other than $0$ and itself, and [[D-CYAJI|semisimple]] if it is a direct sum of simple modules.
By the Artin--Wedderburn theorem, a ring that is semisimple as a left module over itself is isomorphic to a finite product $\prod_i M_{n_i}(D_i)$ of matrix rings over division rings $D_i$.
By Wedderburn's little theorem, every finite division ring is a field.

[[D-4KM4P]]

[[D-CYAJI]]

[[T-ZOTWN]]

[[T-GYVNQ]]
