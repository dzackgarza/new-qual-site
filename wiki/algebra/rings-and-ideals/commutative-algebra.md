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

Every nonzero ring has a maximal ideal and every proper ideal is contained in one; both are the same application of Zorn's lemma to the proper ideals containing a given ideal, in which the union of a chain is a proper ideal and bounds the chain.

[[D-P6XOT]]

[[FT-PUVIQ]]

[[PR-UTFSY]]

[[P-2E7UB]]

## Nakayama's lemma

[[FF-NREXC]]

[[FF-45SK3]]

[[FF-QILDV]]

[[FF-6K35J]]

[[FF-X6C7Z]]

## Noetherian rings and Krull dimension

Recall that a ring is [[D-TZXBO|Noetherian]] if every ascending chain of ideals stabilizes, equivalently if every ideal is finitely generated.
The three theorems on this shelf are the finiteness consequences a qualification problem uses: the principal ideal theorem bounds the height of a prime minimal over a principal ideal, Artin--Rees bounds the $I$-adic filtration of a finitely generated module, and Krull's intersection theorem is Artin--Rees followed by Nakayama's lemma applied to the finitely generated ideal $\Intersect_{n\geq1}I^n$.

[[PR-VARHT]]

[[FF-CSABG]]

[[FF-3K36R]]

[[FF-ESIOA]]

[[FF-HJGPV]]

## Integral extensions

[[PR-RJ3P7]]

## Localization

[[D-OXIVT]]

For a submonoid $S\leq(R,\cdot)$, the localization $R\localize{S}$ inverts the elements of $S$; its construction and universal property are [Tag 00CM](https://stacks.math.columbia.edu/tag/00CM) of the Stacks Project.

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

For an integral domain, the field of fractions is the localization at the nonzero elements, $\ff(R)\cong R\localize{(\nonzeroof{R})}$.

## Hilbert's basis theorem and primary ideals

[[T-YYLPH]]

[[D-JGYK4]]

By the Lasker--Noether theorem, every ideal of a Noetherian ring is a finite intersection of primary ideals [@AM18].

## Gorenstein rings

[[D-DU4UQ]]

::: {.example title="Finite-dimensional graded Gorenstein algebras"}
Let $k$ be a field and $R = R_0 \oplus R_1 \oplus \cdots \oplus R_n$ a graded commutative $k$-algebra with $R_0 = k$, $\dim_k R < \infty$, and $R_n\neq0$.
Then $R$ is Gorenstein if and only if $R$ satisfies Poincaré duality: $\dim_k R_n = 1$, and for each $i$ the multiplication pairing $R_i \times R_{n-i} \to R_n$ is perfect.
:::
