---
title: Determinants and eigenvalues
order: 10
problems:
  topics:
  - Determinants
  - Eigenvalues and Eigenvectors
  - Trace
  - Vector Spaces
  - Linear Transformations
---

# Determinants and eigenvalues

## Definitions

[[D-5BR4D]]

[[D-SSGKC]]

[[D-RG5FO]]

[[D-BSUV4]]

[[D-B4VTH]]

[[D-HGMOW]]

[[D-23FX7]]

[[PR-24CPI]]

[[PR-WDPF7]]

[[D-JIGMN]]

[[D-JRPTK]]

## Determinants

:::{.fact title="The formula, and the three ways to use it"}
\[
\det M = \sum_{\sigma \in S_n} \eps(\sigma) \prod_{i=1}^n a_{i, \sigma(i)}
,\]
which for $3\times 3$ reads
\[
\operatorname{det}\left(\begin{array}{ccc}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right)=\begin{gathered}
a_{11} a_{22} a_{33}+a_{12} a_{23} a_{31}+a_{13} a_{21} a_{32} \\
-a_{13} a_{22} a_{31}-a_{12} a_{21} a_{33}-a_{11} a_{23} a_{32}
\end{gathered}
.\]

Writing $\minor_A(i, j)$ for $A$ with row $i$ and column $j$ deleted, expansion along a row is
\[
\det(A) = \sum_{j=1}^n (-1)^{i+j} a_{ij} \det \minor_A(i, j)
,\]
and the adjugate inverts:
\[
A\inv = {1\over \det A} \operatorname{adj}(A), \qquad \adj(A)_{ij} \da (-1)^{i+j} \det \minor_A(j, i)
.\]

:::

:::{.fact title="Block multiplication"}
Compatible blocks multiply as entries:
\[
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
\begin{bmatrix}
E & F \\
G & H
\end{bmatrix}
= \matt{AE + BG}{AF + BH}{CE + DG}{ CF + DH}
.\]
If any of those products is not defined, the identity is not valid.

:::

## Eigenvalues from the coefficients

:::{.fact title="Trace and determinant are the outer coefficients"}
The determinant is the product of the eigenvalues and the trace is their sum:
\[
\tr(A) = \sum \lambda_i, \qquad \det(A) = \prod \lambda_i
.\]
More completely, the coefficients of $\chi_A$ are the elementary symmetric functions of the eigenvalues:
\[
\chi_A(t) = t^n - \qty{\sum_i \lambda_i }t^{n-1} + \qty{\sum_{i < j} \lambda_i \lambda_j }t^{n-2} + \cdots \pm \qty{\prod_i \lambda_i}
.\]
For a triangular matrix the diagonal *is* the spectrum, so the determinant is the product of the diagonal entries.

:::

:::{.fact title="Trace is conjugation invariant"}
$\trace(AB) = \trace(BA)$, so similar matrices have the same trace:
$\trace(PJP\inv) = \trace(P\inv P J) = \trace J$.
Determinant, characteristic polynomial, and minimal polynomial are also similarity invariants; if any of these differ, the matrices are not similar.

:::

:::{.fact title="Powers of a triangular matrix"}
\[
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
\end{array}\right)
.\]

:::

## Matrix groups

[[D-J5AAX]]

[[PR-UQ3XJ]]

[[D-P5D3T]]

[[D-3ZPR7]]

[[D-GY7ZN]]

[[D-QZ2LQ]]

[[D-MCUTE]]

[[D-3V3SP]]

## Counting over a finite field

[[PR-OYP6J]]

## Exercises

[[E-LJ7PF]]
[[E-D62SD]]
[[E-NUJ7W]]
[[E-GNYRR]]
