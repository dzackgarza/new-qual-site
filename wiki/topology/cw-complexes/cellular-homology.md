---
title: Cellular homology
order: 226
topics:
- CW Complexes
- Cellular Homology
- Euler Characteristic
---

# Cellular homology

The cellular chain complex of a [[D-ZOU5G|CW complex]] $X$ has differentials lowering degree:
$$
C_*(X) = \qty{0 \leftarrow C_0 \xleftarrow{\ \del_1\ } C_1 \xleftarrow{\ \del_2\ } C_2 \leftarrow \cdots }.
$$

## The cellular chain complex

::: {.fact title="Computing cellular homology"}
Let $X$ be a CW complex with finitely many cells in each dimension.

1. The cellular chain group $C_n$ is free abelian on the $n$-cells $e^n_\alpha$.

2. The differential is
$$
\del_n(e_{\alpha}^n) = \sum_{\beta} d_{\alpha\beta}\, e_{\beta}^{n-1},
$$
where $d_{\alpha\beta}$ is the degree of the composite $S^{n-1} \to X^{(n-1)} \to X^{(n-1)}/\qty{X^{(n-1)}\sm e^{n-1}_\beta}\cong S^{n-1}$ of the attaching map of $e^n_\alpha$ with the map collapsing the complement of $e^{n-1}_\beta$.
For a smooth map $S^{n-1}\to S^{n-1}$ and a regular value $y$, the degree is the number of points of the preimage of $y$ counted with sign $+1$ where the map preserves orientation and $-1$ where it reverses it.

3. If $X$ has a single $0$-cell, then $\del_1 = 0$.
If $X$ has no $n$-cells, then $H_n(X) = 0$.

4. With bases of cells, $\del_n\colon \ZZ^{m} \to \ZZ^{k}$ is a $k\times m$ integer matrix, and $H_n(X) = \ker\del_n/\im\del_{n+1}$.

5. If the Smith normal form of $\del_{n+1}$ has nonzero diagonal entries $d_1,\ldots,d_r$, and $\ker\del_n$ has rank $s$, then
$$
H_n(X)\cong \ZZ^{s-r}\oplus\bigoplus_{i=1}^r \ZZ/d_i.
$$

:::

::: {.example title="A kernel from reduced row echelon form"}
The integer matrix with reduced row echelon form
$$
\begin{pmatrix}
1&2&0&2\\0&0&1&-1\\0&0&0&0
\end{pmatrix},
$$
viewed as a map $\ZZ^4\to\ZZ^3$ on coordinates $(x_1,x_2,x_3,x_4)$, has kernel given by $x_1=-2x_2-2x_4$ and $x_3=x_4$, with basis
$$
\ker = \generators{(2,-1,0,0),\ (2,0,-1,-1)}.
$$
The kernel is the same over $\QQ$ and over $\ZZ$ here, because $\ker_\ZZ = \ker_\QQ\intersect\ZZ^4$ and row reduction does not change $\ker_\QQ$.
The image of the transpose is different: over $\QQ$ it is spanned by the nonzero rows $(1,2,0,2)$ and $(0,0,1,-1)$, but over $\ZZ$ the row lattice of the original matrix can be a proper sublattice of their span, for example when $(2,4,0,4)$ is a row of the original matrix.
The integer row lattice is read off from the Hermite normal form, which uses only invertible integer row operations, and $H_n$ from the Smith normal form of $\del_{n+1}$: if its nonzero diagonal entries are $d_1,\ldots,d_r$ and $\ker\del_n$ has rank $s$, then $H_n(X)\cong\ZZ^{s-r}\oplus\bigoplus_{i=1}^r\ZZ/d_i$.

:::

## Constructing a CW complex with prescribed homology

::: {.proposition}
For finitely generated abelian groups $G_1, G_2, \ldots$, there is a connected CW complex $X$ with $H_n(X)\cong G_n$ for all $n\geq 1$.
The space is the wedge of the [[D-KC4BS|Moore spaces]] $M(G_n,n)$, whose reduced homology is additive over the wedge [[PR-B6BB2]].

:::


## Exercises

[[P-EJKY7]]

