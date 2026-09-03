---
title: Commutative algebra
order: 40
topics:
- Local Rings
- Noetherian Rings
- Localization
---

# Commutative algebra

The layer past the qual's core that the qual still asks about: Zorn, Nakayama, Noetherian conditions, localization.

## Zorn's lemma

[[D-P6XOT]]

[[T-V7JRG]]

[[FT-PUVIQ]]

[[T-QSTRJ]]

[[FF-QELG7]]

[[PR-UTFSY]]

[[E-NXHG6]]

:::{.remark title="What Zorn is for here"}
Three existence statements, all proved the same way: every nonzero ring has a maximal ideal, every proper ideal is contained in a maximal one, and every vector space has a basis.
The pattern is a chain argument on a poset of partial objects, and the only step with content is that the union of a chain is an upper bound.

:::

## Nakayama

Nakayama is the local test for whether a finite set really generates.  Over a local
ring $(R,\mathfrak m)$ and for $M$ finitely generated, the extreme form is
$\mathfrak mM=M\Rightarrow M=0$; equivalently, generators of the vector space
$M/\mathfrak mM$ lift to generators of $M$.  This is why reduction modulo the maximal
ideal detects finite generation phenomena and why the lemma appears in geometric
statements about fibers and differentials.

[[FF-NREXC]]

[[FF-45SK3]]

[[FF-QILDV]]

[[FF-6K35J]]

[[FF-X6C7Z]]

## Noetherian rings and Krull dimension

Noetherianity is the finiteness condition that makes ideal-theoretic induction work:
ascending chains stabilize and every ideal is finitely generated.  The results below
control what happens to powers and chains of ideals—Krull's principal-ideal and
intersection theorems, together with Artin--Rees—and are the standard tools for turning
that finiteness into dimension and separation statements.

[[FF-ESIOA]]

[[FF-3K36R]]

[[FF-HJGPV]]

[[FF-CSABG]]

## Integral extensions

Integral extensions preserve enough prime-ideal structure to compare spectra.  The
going-up theorem is the chain-lifting statement: once a prime upstairs lies over the
bottom of a chain downstairs, the rest of the chain can be lifted through the integral
extension.  This is the prime-ideal analogue of the algebraicity constraints familiar
from field extensions.

[[FF-IBDAT]]

## Localization

[[D-OXIVT]]

Use the [Stacks Project localization section](https://stacks.math.columbia.edu/tag/00CM)
for the canonical construction and universal property.

For a submonoid $S\leq (R,\cdot)$, write $S^{-1}R$ for the localization of $R$
obtained by inverting the image of $S$.

:::{.warnings}
The canonical map
\[
R &\to R\localize{S} \\
x &\mapsto {x\over 1}
\]
need not be injective.

:::

:::{.remark}
For an integral domain $R$,
\[
\ff(R) \cong R\localize{ (R\nonzero) }
.\]

:::

[[T-YYLPH]]

[[D-JGYK4]]

Hilbert's basis theorem is the permanence result to remember: adjoining finitely many
polynomial variables to a Noetherian ring keeps it Noetherian.  Primary ideals refine
prime ideals by allowing nilpotence in the quotient, and are the language in which
Noetherian ideals are decomposed when a problem asks for more than their radical.

:::{.fact}
The division algorithm for Euclidean domains.

:::
