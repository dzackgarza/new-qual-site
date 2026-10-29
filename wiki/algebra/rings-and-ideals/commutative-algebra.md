---
title: Commutative algebra
order: 40
topics:
- Local Rings
- Noetherian Rings
- Localization
---

# Commutative algebra

Throughout, rings are commutative with identity.

## Zorn's lemma

[[D-P6XOT]]

[[FT-PUVIQ]]

[[PR-UTFSY]]

[[E-NXHG6]]

::: {.remark title="Existence statements proved by Zorn's lemma"}
Every nonzero ring has a maximal ideal, every proper ideal is contained in a maximal ideal, and every vector space has a basis.
Each proof applies Zorn's lemma to a poset of partial objects ordered by inclusion -- proper ideals containing a given ideal, or linearly independent subsets -- in which the union of a chain is again an element of the poset and is an upper bound for the chain.
:::

## Nakayama's lemma

[[FF-NREXC]]

[[FF-45SK3]]

[[FF-QILDV]]

[[FF-6K35J]]

[[FF-X6C7Z]]

## Noetherian rings and Krull dimension

Recall that a ring is [[D-TZXBO|Noetherian]] if every ascending chain of ideals stabilizes, equivalently if every ideal is finitely generated.
Let $R$ be a Noetherian ring and $I\subseteq R$ an ideal.

- By Krull's principal ideal theorem, a prime ideal minimal over a principal ideal has height at most $1$.

- By the Artin--Rees lemma, for a finitely generated $R$-module $M$ and a submodule $N\subseteq M$ there is $c\geq 0$ with $I^nM\intersect N = I^{n-c}(I^cM\intersect N)$ for all $n\geq c$.

- By Krull's intersection theorem, if $R$ is local and $I$ is proper, then $\Intersect_{n\geq 1}I^nM=0$ for every finitely generated $R$-module $M$.

[[FF-ESIOA]]

[[FF-3K36R]]

[[FF-HJGPV]]

[[FF-CSABG]]

## Integral extensions

[[PR-RJ3P7]]

## Localization

[[D-OXIVT]]

For a submonoid $S\leq (R,\cdot)$, write $S^{-1}R$ for the localization of $R$ at $S$; its construction and universal property are in the [Stacks Project, Tag 00CM](https://stacks.math.columbia.edu/tag/00CM).

::: {.warnings}
The canonical map
$$
\begin{aligned}
R &\to R\localize{S} \\
x &\mapsto {x\over 1}
\end{aligned}
$$
need not be injective: its kernel is $\theset{x\in R \st sx=0 \text{ for some } s\in S}$.
:::

::: {.remark}
For an integral domain $R$,
$$
\ff(R) \cong R\localize{ (\nonzeroof{R}) }.
$$
:::

## Hilbert's basis theorem and primary ideals

[[T-YYLPH]]

[[D-JGYK4]]

By the Lasker--Noether theorem, every ideal of a Noetherian ring is a finite intersection of [[D-JGYK4|primary ideals]].
