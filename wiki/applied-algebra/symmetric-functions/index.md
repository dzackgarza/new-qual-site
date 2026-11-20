---
title: Symmetric functions
order: 3
topics:
- Symmetric Functions
---

# Symmetric functions

A symmetric function of degree $d$ is a polynomial in $x_1,\ldots,x_n$ of degree $d$ that is fixed by the permutations of the variables; for $d\leq n$ the space $\Lambda^d$ of them does not depend on $n$, so a basis indexed by the partitions of $d$ is written without reference to $n$.

## Bases

Each of the following families, indexed by the partitions $\lambda$ of $d$, is a basis of $\Lambda^d$.

The monomial symmetric functions $m_\lambda$: the sum of the distinct monomials $x^\alpha$ whose exponent $\alpha$ is a rearrangement of $\lambda$.

The elementary symmetric functions $e_\lambda = \prod_i e_{\lambda_i}$, where $e_k$ is the coefficient of $t^k$ in $\prod_i(1+x_it)$ ([[D-FK47C|elementary symmetric functions]]).

The complete homogeneous symmetric functions $h_\lambda = \prod_i h_{\lambda_i}$, where $h_k$ is the coefficient of $t^k$ in $\prod_i(1-x_it)^{-1}$, so that $h_k = \sum_{\cardinality{\lambda} = k} m_\lambda$.

The power sums $p_\lambda = \prod_i p_{\lambda_i}$, where $p_k = \sum_i x_i^k$; they are related to the elementary symmetric functions by Newton's identities, and their values at a permutation are the characters of the symmetric group.

The Schur functions $s_\lambda$: the sum, over the semistandard tableaux of shape $\lambda$, of the monomial whose exponent counts the entries, equivalently the quotient $\det(x_i^{\lambda_j + n - j})/\det(x_i^{n-j})$ (the Weyl character formula for $\GL_n$).

By the fundamental theorem of symmetric polynomials, the ring of symmetric polynomials in $x_1,\ldots,x_n$ over $\ZZ$ is $\ZZ[e_1,\ldots,e_n]$, with $e_1,\ldots,e_n$ algebraically independent: the elementary symmetric functions generate, since the $x_i$ are the roots of $\prod_i(t+x_i) = \sum_k e_k t^{n-k}$ and hence each $x_i$ is integral over $\ZZ[e_1,\ldots,e_n]$; and they are independent, since a relation of least degree in $e_n$, specialized at $x_n = 0$, is a relation among $e_1,\ldots,e_{n-1}$ in $n-1$ variables, hence vanishes by induction, which makes the relation divisible by $e_n$ and leaves one of smaller degree.

## Change of basis

Newton's identities relate the power sums to the elementary symmetric functions:
$$
p_k - e_1p_{k-1} + \cdots + (-1)^{k-1}e_{k-1}p_1 + (-1)^k k e_k = 0,
$$
which is the expansion of $\sum_i \prod_{j\neq i}(t - x_j)$ evaluated at $t = x_i$ and summed over $i$; over a field in which $k$ is invertible, it expresses $e_k$ in terms of $p_1,\ldots,p_k$, so the two bases determine one another.

By the Jacobi--Trudi identity, $s_\lambda = \det(h_{\lambda_i - i + j})_{1\leq i,j\leq \ell(\lambda)}$: the determinant is the signed sum over the ways of choosing, for each row $i$, one entry $h_{\lambda_i - i + j_i}$ with the $j_i$ distinct, and the choices that do not weakly increase along the rows cancel in pairs, leaving the semistandard tableaux of shape $\lambda$ with coefficient $1$.

The coefficients of $s_\mu s_\nu = \sum_\lambda c^\lambda_{\mu\nu}s_\lambda$ are the Littlewood--Richardson coefficients, which [[P-APASP08I|one card computes for $s_{2,2}s_{2,1}$ by the Littlewood--Richardson rule]]: $c^\lambda_{\mu\nu}$ counts the semistandard skew tableaux of shape $\lambda/\mu$ and content $\nu$ whose word is a lattice word, read right to left along the rows from the top. These coefficients are the multiplicities in the tensor products of polynomial representations of $\GL_n$ and in the inductions from $S_k\times S_{n-k}$ to $S_n$.

## The characteristic map

The Frobenius characteristic map $\operatorname{ch}$ takes a class function $\chi$ on $S_n$ to the symmetric function
$$
\operatorname{ch}(\chi) \coloneqq \sum_{\lambda\vdash n} \frac{\chi(C_\lambda)}{z_\lambda}p_\lambda,
\qquad z_\lambda \coloneqq \prod_i i^{m_i}m_i!,
$$
with $m_i$ the number of parts of $\lambda$ equal to $i$; it is an isometry from the class functions with the inner product $\frac1{n!}\sum_g\chi(g)\overline{\psi(g)}$ to $\Lambda^n$ with the Hall inner product, in which the Schur functions are orthonormal, and it sends the irreducible character $\chi^\lambda$ to $s_\lambda$.

For partitions $\mu$ of $k$ and $\nu$ of $n-k$, it sends $\Indcat_{S_k\times S_{n-k}}^{S_n}(\chi^\mu\times\chi^\nu)$ to $s_\mu s_\nu$, so the multiplicity of $\chi^\lambda$ in that induced character is the Littlewood--Richardson coefficient $c^\lambda_{\mu\nu}$.

It also gives
$$
p_\rho = \sum_\lambda \chi^\lambda(\rho)\, s_\lambda,
$$
where $\chi^\lambda(\rho)$ is the value of $\chi^\lambda$ on the permutations of cycle type $\rho$; the Murnaghan--Nakayama rule computes these values by removing border strips from $\lambda$, one for each part of $\rho$, with the sign $(-1)^{\text{height}}$.
For $\rho = (1^n)$ the coefficient $\chi^\lambda(1) = \dim\chi^\lambda$ of $s_\lambda$ in $p_1^n$ is the number of standard Young tableaux of shape $\lambda$, which the hook length formula evaluates as $n!/\prod_{c\in\lambda}h(c)$, the product running over the cells $c$ of $\lambda$ with $h(c)$ the number of cells weakly to the right and weakly below $c$.
