---
title: Symmetric functions
order: 3
topics:
- Symmetric Functions
---

# Symmetric functions

## Bases

Each of the following families is indexed by partitions $\lambda$ of $n$ and is a basis of the space of symmetric functions of degree $n$.

| Basis | Notation | Description |
| --- | --- | --- |
| monomial | $m_\lambda$ | the sum of the distinct monomials $x^\alpha$ with $\alpha$ a rearrangement of $\lambda$ |
| elementary | $e_\lambda$ | $e_\lambda=\prod_i e_{\lambda_i}$, where $e_k$ is the coefficient of $t^k$ in $\prod_i(1+x_it)$ |
| complete homogeneous | $h_\lambda$ | $h_\lambda=\prod_i h_{\lambda_i}$, where $h_k$ is the coefficient of $t^k$ in $\prod_i(1-x_it)\inv$ |
| power sum | $p_\lambda$ | $p_\lambda=\prod_i p_{\lambda_i}$ with $p_k = \sum_i x_i^k$; related to $e$ by Newton's identities, and to the characters of $S_n$ |
| Schur | $s_\lambda$ | the sum over semistandard Young tableaux of shape $\lambda$; the characters of the polynomial irreducible representations of $\GL_n$ |

By the fundamental theorem of symmetric polynomials, the ring of symmetric polynomials in $x_1,\ldots,x_n$ over $\ZZ$ is $\ZZ[e_1,\ldots,e_n]$, and $e_1,\ldots,e_n$ are algebraically independent.

## Computations

- **Change of basis.** Newton's identities relate the power sums and the elementary symmetric functions:
  $$
  p_k - e_1p_{k-1} + \cdots + (-1)^{k-1}e_{k-1}p_1 + (-1)^k k e_k = 0.
  $$
- **Expansion of Schur functions.** $s_\lambda$ is the sum over semistandard tableaux of shape $\lambda$ of the corresponding monomials, and by the Jacobi--Trudi identity $s_\lambda = \det(h_{\lambda_i - i + j})$.
- **Products of Schur functions.** The coefficients of $s_\mu s_\nu = \sum_\lambda c^\lambda_{\mu\nu}s_\lambda$ are given by the Littlewood--Richardson rule; they are also the multiplicities in tensor products of polynomial representations of $\GL_n$ and in induction products of representations of symmetric groups.

## The characteristic map

The Frobenius characteristic map is an isometry from the class functions on $S_n$ to the symmetric functions of degree $n$, sending the irreducible character $\chi^\lambda$ to $s_\lambda$.
Under it, the Littlewood--Richardson rule, the Murnaghan--Nakayama rule, and the hook length formula each correspond to a statement about characters of symmetric groups.
