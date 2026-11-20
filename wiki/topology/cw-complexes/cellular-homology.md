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

[[D-CELLHM]]

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

[[PR-CWPRH]]


## Exercises

[[P-EJKY7]]

