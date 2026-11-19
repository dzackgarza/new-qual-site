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

## Forms and normal matrices

A bilinear form is read in a basis by its Gram matrix, which decides nondegeneracy, and a complex matrix is normal exactly when it is unitarily diagonalizable; over a perfect field every operator splits uniquely into commuting semisimple and nilpotent parts.

[[D-5BR4D]]

[[D-SSGKC]]

[[D-H4TDM]]

[[PR-WDPF7]]

[[D-BSUV4]]

[[E-LJ7PF]]

[[D-B4VTH]]

[[D-GIGM2]]

[[D-23FX7]]

[[PR-24CPI]]

Similar matrices have the same characteristic polynomial, minimal polynomial, and Jordan form, and two matrices over a field are equivalent exactly when they have the same size and rank.

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
\inverseof{A} = {1\over \det A} \operatorname{adj}(A), \qquad \operatorname{adj}(A)_{ij} \coloneqq (-1)^{i+j} \det \minor_A(j, i).
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
\trace(A) = \sum_i \lambda_i, \qquad \det(A) = \prod_i \lambda_i.
$$
The eigenvalues of a triangular matrix are its diagonal entries, so its determinant is the product of its diagonal entries.
:::

::: {.fact title="Similarity invariants"}
$\trace(AB) = \trace(BA)$, so similar matrices have the same trace: $\trace(PJ\inverseof{P}) = \trace(\inverseof{P} P J) = \trace J$.
The determinant, characteristic polynomial, and minimal polynomial are also similarity invariants.
:::

::: {.fact title="Powers of a triangular matrix"}
$$
A\coloneqq\left(\begin{array}{ccc}
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
A product of upper-triangular matrices is upper triangular, and its $i$th diagonal entry is the product of the $i$th diagonal entries of the factors, which gives the statement by induction on $k$.
:::

## Matrix groups

The classical groups are the invertible matrices preserving one form: the orthogonal group preserves the standard symmetric form, the unitary group the standard Hermitian one, and the symplectic group the standard alternating one, with the special linear, special orthogonal and special unitary groups cut out by determinant $1$.

[[D-J5AAX]]

[[D-P5D3T]]

[[D-3ZPR7]]

[[D-GY7ZN]]

[[D-QZ2LQ]]

[[D-MCUTE]]

[[D-3V3SP]]

::: {.example title="A basis of $\mathfrak{su}(2)$ from the Pauli matrices"}
The Lie algebra $\mathfrak{su}(2) = \theset{X \in \Mat_{2\times 2}(\CC) \suchthat X^\dagger = -X,\ \trace X = 0}$ is a real vector space of dimension $3$ with basis
$$
\sigma_1 \coloneqq \frac{1}{\sqrt 2}\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix},\qquad
\sigma_2 \coloneqq \frac{1}{\sqrt 2}\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix},\qquad
\sigma_3 \coloneqq \frac{1}{\sqrt 2}\begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}.
$$
With the Pauli matrices $\tau_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $\tau_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$, $\tau_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, these are $\sigma_1 = \frac{1}{\sqrt 2}\, i\tau_y$, $\sigma_2 = \frac{1}{\sqrt 2}\, i\tau_x$, and $\sigma_3 = \frac{1}{\sqrt 2}\, i\tau_z$.
Each Pauli matrix is Hermitian and traceless, so $i$ times it is skew-Hermitian and traceless, and lies in $\mathfrak{su}(2)$.
:::

## Counting over a finite field

[[PR-UQ3XJ]]

Since $\det\colon \GL_n(\FF_q)\to \FF_q^\times$ is surjective with kernel $\SL_n(\FF_q)$, the order of $\SL_n(\FF_q)$ is that of $\GL_n(\FF_q)$ divided by $q-1$.

## Problems

[[E-LJ7PF]]

[[E-D62SD]]

[[E-NUJ7W]]

[[E-GNYRR]]
