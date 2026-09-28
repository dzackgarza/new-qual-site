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

Three methods compute singular homology: cellular homology, the Mayer--Vietoris sequence, and the long exact sequence of a pair.

## Cellular homology

::: {.fact title="Cellular homology"}
For a [[D-ZOU5G|CW complex]] $X$, $H_*(X)$ is the homology of the [[D-A3PUW|cellular chain complex]], whose group $C_n$ is free abelian on the $n$-cells.
The coefficient of an $(n-1)$-cell $e^{n-1}_\beta$ in $\del e^n_\alpha$ is the [[D-XC53X|degree]] of the composite of the attaching map $S^{n-1}\to X^{(n-1)}$ with the quotient $X^{(n-1)}\to X^{(n-1)}/\qty{X^{(n-1)}\sm e^{n-1}_\beta}\cong S^{n-1}$.

:::

::: {.example}
\envlist

- If $X$ has no cells in any two adjacent dimensions, then every cellular boundary map is zero, so $H_n(X)$ is free on the $n$-cells; for $\CP^n$ this gives $\ZZ$ in each even degree $0,2,\ldots,2n$.
- If $X$ has no cells above dimension $d$, then $H_n(X) = 0$ for $n>d$.

:::

## The Mayer--Vietoris sequence

::: {.theorem title="Mayer--Vietoris"}
For subspaces $A,B\subseteq X$ whose interiors cover $X$, there is a long exact sequence
$$
\cdots \to H_n(A\intersect B) \to H_n(A)\oplus H_n(B)\to H_n(X)\to H_{n-1}(A\intersect B)\to\cdots.
$$

:::

::: {.example title="Standard decompositions"}
$S^n$ as the union of two open hemispherical caps meeting in a band $\homotopic S^{n-1}$; a connected sum $M\# N$ of $n$-manifolds as the union of $M$ and $N$ each minus an open ball, meeting in $S^{n-1}$; the torus as the union of two cylinders meeting in two disjoint circles.

:::

## Pairs and quotients

::: {.theorem}
For a pair $(X,A)$ there is a long exact sequence
$$
\cdots\to H_n(A)\to H_n(X)\to H_n(X,A)\to H_{n-1}(A)\to\cdots,
$$
and if $(X,A)$ is a good pair, the quotient map induces $H_n(X, A)\cong \tilde H_n(X/A)$ for all $n$.

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
