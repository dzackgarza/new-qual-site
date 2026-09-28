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

| $\size G$ | Conclusion |
| --- | --- |
| $p$ | cyclic, hence abelian |
| $p^2$ | abelian |
| $pq$ with $p \notdivides q-1$ | cyclic, hence abelian |
| $pq$ with $p \divides q-1$ | there is exactly one nonabelian group of this order up to isomorphism, $\ZZ/q\semidirect\ZZ/p$ |
| $p^3$ | not necessarily abelian: $D_4$ and $Q_8$ have order $8$ |

[[PR-LFGHA]]

[[PR-IGLFV]]

[[PR-SLWTB]]

For $\size G = p^2$, the [[D-NK7G7|center]] $Z(G)$ is nontrivial by the class equation; if $\size{Z(G)} = p$, then $G/Z(G)$ has order $p$ and is cyclic, and a group whose quotient by its center is cyclic is abelian, so $Z(G)=G$, a contradiction.
Hence $Z(G)=G$.

## From a quotient

::: {.proposition}
If $G/Z(G)$ is cyclic, then $G$ is abelian.
:::

::: {.proof}
Let $gZ(G)$ generate $G/Z(G)$.
Every element of $G$ has the form $g^iz$ with $i\in\ZZ$ and $z\in Z(G)$, and $g^iz\cdot g^jw = g^{i+j}zw = g^jw\cdot g^iz$ for $z,w\in Z(G)$.
:::

[[E-O73XQ]]

::: {.remark}
If $G$ is nonabelian, then $G/Z(G)$ is not cyclic, so $[G:Z(G)]$ is not prime.
In particular $\size{Z(G)} \neq \size G/p$ for every prime $p$.
:::

## From the structure theorem

A finite abelian group is a direct product of cyclic groups of prime-power order, and the isomorphism classes of abelian groups of order $\prod_i p_i^{e_i}$ correspond to tuples of partitions of the exponents $e_i$.
For example, there are $2\cdot 1 = 2$ abelian groups of order $p^2 q$, namely $\ZZ/p^2\times\ZZ/q$ and $\ZZ/p\times\ZZ/p\times\ZZ/q$.
This is the classification of finitely generated modules over the principal ideal domain $\ZZ$; see [[algebra/modules/classify-this-module|Classify this module]].

[[PR-2JG3F]]

## Distinguishing nonabelian groups

Isomorphism invariants that separate nonabelian groups of the same order:

- A normal Sylow subgroup $N$ with a complement $H$ exhibits $G \cong N \semidirect H$; see [[algebra/group-actions/show-g-is-not-simple|Show $G$ is not simple]] and [[algebra/groups/quotients-and-products|Quotients, products, and automorphisms]].

- The number of elements of each order: $D_4$ has five elements of order $2$ and $Q_8$ has one.

- The abelianization $G/[G,G]$, computable from a presentation by adjoining the relations $[x,y]=1$ for all generators $x,y$.

- The center, the sizes of the conjugacy classes, and the automorphism group.
