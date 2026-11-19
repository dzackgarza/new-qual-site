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

The two cards below give the decomposition in general and in the structured case: existence over any Noetherian ring, and the explicit intersection over a principal ideal domain, where the prime powers of a generator name the components.

[[T-LSNTH]]

[[T-PRMDC]]

## Gorenstein rings

[[D-DU4UQ]]

In the graded case the Gorenstein condition already fixes the top degree: a finite-dimensional graded Gorenstein algebra with $R_0=k$ and $R_n\neq0$ has $\dim_k R_n=1$, since its top piece lies in the one-dimensional socle.

[[T-GRDSOC]]

For a zero-dimensional Gorenstein algebra the dualizing module is the algebra itself, and the socle against a specified augmentation is one-dimensional; that computation is on the second card.

[[P-HCAO21]]
