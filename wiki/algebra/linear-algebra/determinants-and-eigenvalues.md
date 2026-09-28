---
title: Determinants and eigenvalues
order: 10
topics:
- Determinants
- Eigenvalues and Eigenvectors
- Trace
- Vector Spaces
- Linear Transformations
---

# Determinants and eigenvalues

## Definitions

A bilinear form $b$ on a finite-dimensional vector space $V$ has a [[D-RG5FO|Gram matrix]] $G=(b(e_i,e_j))_{i,j}$ in each basis $(e_i)$ of $V$, and $b$ is [[D-5BR4D|nondegenerate]] if and only if $G$ is invertible; for a nondegenerate symmetric form and a subspace $W\subseteq V$, $\dim W+\dim W^\perp=\dim V$.
A complex matrix is [[D-BSUV4|normal]] if it commutes with its conjugate transpose, and normal matrices are exactly the unitarily diagonalizable ones.
Over a perfect field, every linear operator $T$ has a unique Jordan--Chevalley decomposition $T=T_s+T_n$ with $T_s$ [[D-B4VTH|semisimple]], $T_n$ [[D-HGMOW|nilpotent]], and $T_sT_n=T_nT_s$; for invertible $T$, the multiplicative form is $T=T_sT_u$ with $T_u=I+T_s\inv T_n$ [[D-23FX7|unipotent]].

[[D-5BR4D]]

[[D-SSGKC]]

[[D-RG5FO]]

[[D-BSUV4]]

[[D-B4VTH]]

[[D-HGMOW]]

[[D-23FX7]]

[[PR-24CPI]]

[[PR-WDPF7]]

Square matrices $A$ and $B$ are [[D-JIGMN|similar]] if $B=PAP\inv$ for an invertible $P$, and $m\times n$ matrices are [[D-JRPTK|equivalent]] if $B=PAQ$ for invertible $P$ and $Q$.
Similar matrices have the same characteristic polynomial, minimal polynomial, and Jordan form; two matrices over a field are equivalent if and only if they have the same size and rank.

[[D-JIGMN]]

[[D-JRPTK]]

## Determinants

::: {.fact title="Determinant formulas"}
For $A=(a_{ij})\in\Mat(n\times n;R)$,
$$
\det A = \sum_{\sigma \in S_n} \sgn(\sigma) \prod_{i=1}^n a_{i, \sigma(i)},
$$
which for $n=3$ reads
$$
\det\left(\begin{array}{ccc}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right)=\begin{gathered}
a_{11} a_{22} a_{33}+a_{12} a_{23} a_{31}+a_{13} a_{21} a_{32} \\
-a_{13} a_{22} a_{31}-a_{12} a_{21} a_{33}-a_{11} a_{23} a_{32}
\end{gathered}.
$$

Writing $\minor_A(i, j)$ for the matrix obtained from $A$ by deleting row $i$ and column $j$, expansion along row $i$ is
$$
\det(A) = \sum_{j=1}^n (-1)^{i+j} a_{ij} \det \minor_A(i, j),
$$
and if $\det A$ is invertible, the adjugate gives the inverse:
$$
A\inv = {1\over \det A} \adj(A), \qquad \adj(A)_{ij} \da (-1)^{i+j} \det \minor_A(j, i).
$$
:::

::: {.fact title="Block multiplication"}
For block matrices whose block sizes make the products $AE$, $BG$, $AF$, $BH$, $CE$, $DG$, $CF$, $DH$ defined,
$$
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
\begin{bmatrix}
E & F \\
G & H
\end{bmatrix}
= \matt{AE + BG}{AF + BH}{CE + DG}{ CF + DH}.
$$
:::

## Eigenvalues and the characteristic polynomial

::: {.fact title="Trace and determinant from the eigenvalues"}
Let $A$ be an $n\times n$ matrix over a field whose characteristic polynomial $\chi_A$ splits, with eigenvalues $\lambda_1,\ldots,\lambda_n$ listed with algebraic multiplicity.
The coefficients of $\chi_A$ are, up to sign, the [[D-FK47C|elementary symmetric functions]] of the eigenvalues:
$$
\chi_A(t) = t^n - \qty{\sum_i \lambda_i }t^{n-1} + \qty{\sum_{i < j} \lambda_i \lambda_j }t^{n-2} - \cdots + (-1)^n\qty{\prod_i \lambda_i}.
$$
In particular
$$
\tr(A) = \sum_i \lambda_i, \qquad \det(A) = \prod_i \lambda_i.
$$
The eigenvalues of a triangular matrix are its diagonal entries, so its determinant is the product of its diagonal entries.
:::

::: {.fact title="Similarity invariants"}
$\tr(AB) = \tr(BA)$, so similar matrices have the same trace: $\tr(PJP\inv) = \tr(P\inv P J) = \tr J$.
The determinant, characteristic polynomial, and minimal polynomial are also similarity invariants.
:::

::: {.fact title="Powers of a triangular matrix"}
$$
A\da\left(\begin{array}{ccc}
a_1 & & * \\
& \ddots & \\
0 & & a_n
\end{array}\right)
\implies
A^k = \left(\begin{array}{ccc}
a_1^k & & * \\
& \ddots & \\
0 & & a_n^k
\end{array}\right).
$$
:::

## Matrix groups

The [[D-J5AAX|general linear group]] $\GL_n(F)$ is the group of invertible $n\times n$ matrices over $F$, and the [[D-P5D3T|special linear group]] $\SL_n(F)$ is its subgroup of matrices of determinant $1$.
The [[D-3ZPR7|orthogonal group]] $\ts{A \st A^tA=I}$ is the group of matrices preserving the standard symmetric bilinear form, the [[D-QZ2LQ|unitary group]] $\ts{A\st A^\dagger A=I}$ preserves the standard Hermitian form, and the [[D-3V3SP|symplectic group]] $\ts{A\st A^tJA=J}$ preserves the standard alternating form with Gram matrix $J=\matt{0}{I_n}{-I_n}{0}$.
The [[D-GY7ZN|special orthogonal]] and [[D-MCUTE|special unitary]] groups are the subgroups of matrices of determinant $1$.

[[D-J5AAX]]

[[D-P5D3T]]

[[D-3ZPR7]]

[[D-GY7ZN]]

[[D-QZ2LQ]]

[[D-MCUTE]]

[[D-3V3SP]]

## Counting over a finite field

An element of $\GL_n(\FF_q)$ is determined by its columns, which form an ordered basis of $\FF_q^n$.
The first column is any of the $q^n-1$ nonzero vectors, and the $(i+1)$st column is any of the $q^n-q^i$ vectors outside the span of the first $i$ columns, so
$$
\size{\GL_n(\FF_q)} = \prod_{i=0}^{n-1}(q^n-q^i).
$$
Since $\det\colon\GL_n(\FF_q)\to\FF_q^\times$ is surjective with kernel $\SL_n(\FF_q)$, $\size{\SL_n(\FF_q)} = \size{\GL_n(\FF_q)}/(q-1)$.

[[PR-UQ3XJ]]

## Exercises

[[E-LJ7PF]]

[[E-D62SD]]

[[E-NUJ7W]]

[[E-GNYRR]]
