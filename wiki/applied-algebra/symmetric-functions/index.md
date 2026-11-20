---
title: Symmetric functions
order: 3
topics:
- Symmetric Functions
---

# Symmetric functions

[[D-SYMFN]]

## Bases

Each of the following families, indexed by the partitions $\lambda$ of $d$, is a basis of $\Lambda^d$ [@FH91, Appendix A]: the monomial symmetric functions, the [[D-FK47C|elementary symmetric functions]] $e_\lambda$, the complete homogeneous symmetric functions, the power sums, and the Schur functions.

[[D-MSYMF]]

[[D-HSYMF]]

[[D-PSYMF]]

[[D-SCHUR]]

By the fundamental theorem of symmetric polynomials, the ring of symmetric polynomials in $x_1,\ldots,x_n$ over $\ZZ$ is $\ZZ[e_1,\ldots,e_n]$, with $e_1,\ldots,e_n$ algebraically independent: the elementary symmetric functions generate, since the $x_i$ are the roots of $\prod_i(t+x_i) = \sum_k e_k t^{n-k}$ and hence each $x_i$ is integral over $\ZZ[e_1,\ldots,e_n]$; and they are independent, since a relation of least degree in $e_n$, specialized at $x_n = 0$, is a relation among $e_1,\ldots,e_{n-1}$ in $n-1$ variables, hence vanishes by induction, which makes the relation divisible by $e_n$ and leaves one of smaller degree.

## Change of basis

Newton's identities relate the power sums to the elementary symmetric functions:
$$
p_k - e_1p_{k-1} + \cdots + (-1)^{k-1}e_{k-1}p_1 + (-1)^k k e_k = 0,
$$
which is the expansion of $\sum_i \prod_{j\neq i}(t - x_j)$ evaluated at $t = x_i$ and summed over $i$; over a field in which $k$ is invertible, it expresses $e_k$ in terms of $p_1,\ldots,p_k$, so the two bases determine one another.

By [[T-JTRUDI|the Jacobi--Trudi identity]], $s_\lambda$ is the determinant $\det(h_{\lambda_i - i + j})$ of complete homogeneous symmetric functions, of size $\ell(\lambda)$ and independent of the size of the determinant once that exceeds $\ell(\lambda)$.

The coefficients of $s_\mu s_\nu = \sum_\lambda c^\lambda_{\mu\nu}s_\lambda$ are the Littlewood--Richardson coefficients of [[T-LRULR|the Littlewood--Richardson rule]], which states that $c^\lambda_{\mu\nu}$ counts the semistandard tableaux of skew shape $\lambda/\mu$ and content $\nu$ whose word is a lattice word, read from right to left in each row from the top; [[P-APASP08I|one card computes $c^\lambda_{(2,2),(2,1)}$ by that rule]]. These coefficients are the multiplicities in the tensor products of polynomial representations of $\GL_n$ and in the inductions from $S_k\times S_{n-k}$ to $S_n$.

## The characteristic map

The [[T-FROBCH|Frobenius characteristic map]] $\operatorname{ch}$ takes a class function on $S_n$ to the symmetric function of degree $n$; it is an isometry from the class functions with the inner product $\frac1{n!}\sum_g\chi(g)\overline{\psi(g)}$ to $\Lambda^n$ with the Hall inner product, in which the Schur functions are orthonormal, and it sends the irreducible character $\chi^\lambda$ to $s_\lambda$.

For partitions $\mu$ of $k$ and $\nu$ of $n-k$, it sends $\Indcat_{S_k\times S_{n-k}}^{S_n}(\chi^\mu\times\chi^\nu)$ to $s_\mu s_\nu$, so the multiplicity of $\chi^\lambda$ in that induced character is the Littlewood--Richardson coefficient $c^\lambda_{\mu\nu}$.

It also gives
$$
p_\rho = \sum_\lambda \chi^\lambda(\rho)\, s_\lambda,
$$
where $\chi^\lambda(\rho)$ is the value of $\chi^\lambda$ on the permutations of cycle type $\rho$; the Murnaghan--Nakayama rule computes these values by removing border strips from $\lambda$, one for each part of $\rho$, with the sign $(-1)^{\text{height}}$.
For $\rho = (1^n)$ the coefficient $\chi^\lambda(1) = \dim\chi^\lambda$ of $s_\lambda$ in $p_1^n$ is the number of standard Young tableaux of shape $\lambda$, which [[T-HOOK|the hook length formula]] evaluates as the quotient of $n!$ by the product of the hook lengths.
