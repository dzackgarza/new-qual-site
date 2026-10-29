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

::: {.theorem}
If $(X,A)$ is a [[D-IGUUS|good pair]], the quotient map induces $H_n(X, A)\cong \tilde H_n(X/A)$ for all $n$.

:::

The reduced homology of a quotient $X/A$ of a good pair is therefore computed from the long exact sequence of $(X,A)$.

## Choosing a method

| The space is given as | Method |
| --- | --- |
| a cell complex, or a polygon with identifications | cellular homology |
| a union of two subspaces with known homology | Mayer--Vietoris |
| a quotient $X/A$ of a good pair, or a pair | the long exact sequence of the pair |
| a product | the Künneth theorem |

## Consistency checks

::: {.fact}
\envlist

- If $X$ has finitely many path components, $H_0(X) \cong \ZZ^{\abs{\pi_0(X)}}$.
- For path-connected $X$, $H_1(X)$ is the abelianization of $\pi_1(X)$, which can be compared with [[topology/fundamental-group/compute-pi-1|a fundamental group computation]].
- For a finite CW complex $X$ with $c_n$ cells of dimension $n$, $\chi(X)=\sum_n (-1)^n \operatorname{rank} H_n(X) = \sum_n (-1)^n c_n$.
- For a connected closed $n$-manifold $M$: if $M$ is orientable, $H_n(M) \cong \ZZ$ and $H_{n-1}(M)$ is free; if $M$ is non-orientable, $H_n(M) = 0$ and the torsion subgroup of $H_{n-1}(M)$ is $\ZZ/2$.
  The torus and the Klein bottle have $H_1\cong\ZZ^2$ and $H_1\cong\ZZ\oplus\ZZ/2$.

:::
