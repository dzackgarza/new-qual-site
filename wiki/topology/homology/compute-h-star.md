---
title: Compute $H_*$
order: 0
topics:
- Homology
- Mayer-Vietoris
- Simplicial Homology
- Relative Homology

---

# Compute $H_*$

## Cellular homology

[[D-A3PUW]]

::: {.example}
\envlist

- If $X$ has no cells in any two adjacent dimensions, then every cellular boundary map is zero, so $H_n(X)$ is free on the $n$-cells; for $\CP^n$ this gives $\ZZ$ in each even degree $0,2,\ldots,2n$.
- If $X$ has no cells above dimension $d$, then $H_n(X) = 0$ for $n>d$.

:::

## The Mayer--Vietoris sequence

[[D-FAIJX]]

::: {.example title="Standard decompositions"}
$S^n$ as the union of two open hemispherical caps meeting in a band $\homotopic S^{n-1}$; a connected sum $M\# N$ of $n$-manifolds as the union of $M$ and $N$ each minus an open ball, meeting in $S^{n-1}$; the torus as the union of two cylinders meeting in two disjoint circles.

:::

## Pairs and quotients

A pair $(X,A)$ has the [[D-UEWPN|long exact sequence of the pair]].

[[PR-P222G]]

The reduced homology of a quotient $X/A$ of a good pair is therefore computed from the long exact sequence of $(X,A)$.

## Choosing a method

| The space is given as | Method |
| --- | --- |
| a cell complex, or a polygon with identifications | cellular homology |
| a union of two subspaces with known homology | Mayer--Vietoris |
| a quotient $X/A$ of a good pair, or a pair | the long exact sequence of the pair |
| a product | the Künneth theorem |

## Consistency checks

[[T-GL7E6]]

[[D-QK5BM]]

[[PR-LR35S]]
