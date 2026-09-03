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

The definitions here split into two themes.  A bilinear or quadratic form adds geometry
to a vector space; its Gram matrix records the form in a basis, and nondegeneracy is the
invertibility condition that makes orthogonal-complement arguments behave as expected.
For operators, normality over \(\CC\) and semisimplicity describe diagonalization
behavior, while nilpotent and unipotent parts measure the failure of an operator to be
semisimple.  Over a perfect field, the Jordan--Chevalley decomposition separates the
semisimple and nilpotent pieces (or, multiplicatively for an invertible operator, the
semisimple and unipotent pieces).

[[D-5BR4D]]

[[D-SSGKC]]

[[D-RG5FO]]

[[D-BSUV4]]

[[D-B4VTH]]

[[D-HGMOW]]

[[D-23FX7]]

[[PR-24CPI]]

[[PR-WDPF7]]

Similarity and matrix equivalence are different relations.  Similarity changes the
basis of one endomorphism and therefore preserves characteristic/minimal polynomials and
Jordan data; row-column equivalence changes bases independently in domain and codomain
and instead records the rank-type data of a linear map.  Decide which relation the
problem is asking about before reaching for an invariant.

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

The named matrix groups are stabilizers of structure.  \(\GL_n\) consists of all
invertible changes of basis and \(\SL_n\) imposes determinant \(1\).  Orthogonal and
special orthogonal groups preserve a symmetric/quadratic form; unitary and special
unitary groups preserve a Hermitian form; the symplectic group preserves a
nondegenerate alternating form.  This viewpoint makes their defining equations and
their inclusions consequences of what structure is being preserved rather than a list
of unrelated matrix identities.

[[D-J5AAX]]

[[PR-UQ3XJ]]

[[D-P5D3T]]

[[D-3ZPR7]]

[[D-GY7ZN]]

[[D-QZ2LQ]]

[[D-MCUTE]]

[[D-3V3SP]]

## Counting over a finite field

To count \(\GL_n(\FF_q)\), choose an ordered basis one vector at a time: the first vector
is nonzero, and each subsequent vector must avoid the span of those already chosen.
The product \(\prod_{i=0}^{n-1}(q^n-q^i)\) is therefore a basis count, which is the
template for many finite classical-group counts.

[[PR-OYP6J]]

## Exercises

[[E-LJ7PF]]
[[E-D62SD]]
[[E-NUJ7W]]
[[E-GNYRR]]
