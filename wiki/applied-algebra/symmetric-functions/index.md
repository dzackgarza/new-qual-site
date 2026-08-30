---
title: Symmetric functions
order: 3
problems:
  topics:
  - Symmetric Functions
---

# Symmetric functions

## The five bases

Each is indexed by partitions of $n$, and each has a use:

| Basis | Notation | Where it appears |
| --- | --- | --- |
| monomial | $m_\lambda$ | the definition |
| elementary | $e_\lambda$ | generating the ring; $e_k$ are the coefficients of $\prod(1+x_it)$ |
| complete homogeneous | $h_\lambda$ | dual to $e$; the coefficients of $\prod(1-x_it)\inv$ |
| power sum | $p_\lambda$ | Newton's identities, and characters of $S_n$ |
| Schur | $s_\lambda$ | the characters of $\GL_n$, and the bridge to representations |

The fundamental theorem is that $\ZZ[e_1,\dots,e_n]$ is the whole ring of symmetric polynomials, and that the $e_i$ are algebraically independent.

## The three things to be able to do

- **Change basis**, especially $p$ to $e$ and back, by Newton's identities
  \[
  p_k - e_1p_{k-1} + \cdots + (-1)^{k-1}e_{k-1}p_1 + (-1)^k k e_k = 0
  .\]
- **Expand a Schur function** by the combinatorial definition as a sum over semistandard tableaux, or by the Jacobi--Trudi determinant $s_\lambda = \det(h_{\lambda_i - i + j})$.
- **Multiply Schur functions** by the Littlewood--Richardson rule, which is also the decomposition of a tensor product of $\GL_n$ representations and the induction of $S_n$ representations.

## Why this sits next to representation theory

The characteristic map sends the class functions on $S_n$ to symmetric functions of degree $n$, carrying the irreducible character $\chi^\lambda$ to $s_\lambda$.
So the Littlewood--Richardson rule, the Murnaghan--Nakayama rule and the hook length formula are all statements about symmetric functions and about representations at the same time, and this paper may ask for either side.
