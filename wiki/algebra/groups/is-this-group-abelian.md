---
title: Is this group abelian?
order: 0
topics:
- Abelian Groups
- Classification
---

# Is this group abelian?

Throughout, $G$ is a finite group and $p<q$ are primes.

## From the order alone

::: {.fact title="Which orders force an abelian group"}
| $\size{G}$ | Conclusion |
| --- | --- |
| $p$ | cyclic, hence abelian |
| $p^2$ | abelian |
| $pq$ with $p \notdivides q-1$ | cyclic, hence abelian |
| $pq$ with $p \divides q-1$ | abelian, or the unique nonabelian group of this order, $\ZZ/q\semidirect\ZZ/p$ |
| $p^3$ | not necessarily abelian: $D_4$ and $Q_8$ have order $8$ |
:::

[[PR-LFGHA]]

[[PR-IGLFV]]

[[PR-SLWTB]]

[[P-BL7XW]]

[[FF-TDXQT]]

## From a quotient

::: {.fact title="A nonabelian group of order $p^3$ has center of order $p$"}
The center cannot have order $p^2$: the quotient by a center of order $p^2$ would be cyclic of order $p$, and a group whose quotient by its center is cyclic is abelian.
:::

[[E-O73XQ]]

[[T-4CDTT]]

## From the structure theorem

For $p^2q$ the count is $P(2)P(1)=2$, namely $\ZZ/p^2\times\ZZ/q$ and $\ZZ/p\times\ZZ/p\times\ZZ/q$.

This is the classification of finitely generated modules over the principal ideal domain $\ZZ$; see [[algebra/modules/classify-this-module|Classify this module]].

[[PR-2JG3F]]

[[PR-434DX]]

## Distinguishing nonabelian groups

::: {.fact title="Invariants that separate nonabelian groups of one order"}
- A normal Sylow subgroup $N$ with a complement $H$ exhibits $G \cong N \semidirect H$; see [[algebra/group-actions/show-g-is-not-simple|Show $G$ is not simple]] and [[algebra/groups/quotients-and-products|Quotients, products, and automorphisms]].

- The number of elements of each order: $D_4$ has five elements of order $2$ and $Q_8$ has one.

- The abelianization $G/[G,G]$, computable from a presentation by adjoining the relations $[x,y]=1$ for all generators $x,y$.

- The center, the sizes of the conjugacy classes, and the automorphism group.
:::

[[P-7VKFN]]

[[D-BQ4BQ]]
