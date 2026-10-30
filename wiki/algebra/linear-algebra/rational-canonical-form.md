---
title: Rational canonical form
order: 40
topics:
- Rational Canonical Form
- Structure Theorem
---

# Rational canonical form

Let $A$ be an $n\times n$ matrix over a field $k$.
The rational canonical form of $A$ is the block diagonal matrix of the [[D-HJR7M|companion matrices]] of the invariant factors of the $k[x]$-module $k^n$, with $x$ acting by $A$.
It exists over every field; the [[algebra/linear-algebra/jordan-canonical-form|Jordan form]] exists if and only if $\chi_A$ splits over $k$.

[[D-HJR7M]]

[[FD-XT6HD]]

[[PR-4GQIZ]]

::: {.proof}
This proves that $\min_T = \det(xI-T)$ if and only if $V$ admits a cyclic vector. Write $A \coloneqq T$ and $n \coloneqq \dim_k V$.

$\impliedby$: Suppose $v$ is a cyclic vector, so that $v, Av, \ldots, A^{n-1}v$ is a basis of $V$.
If $n' \coloneqq \deg\min_A < n$, then $\min_A(A)v = 0$ is a linear dependence among $v, Av, \ldots, A^{n'}v$, a contradiction.
Hence $\deg\min_A = n = \deg\chi_A$, and since $\min_A$ divides $\chi_A$ and both are monic, $\min_A = \chi_A$.

$\implies$: By the structure theorem $V\cong \bigoplus_{i=1}^m k[x]/\generators{p_i}$ with nonconstant invariant factors $p_1\divides\cdots\divides p_m$, $\chi_A = \prod_i p_i$, and $\min_A = p_m$.
If $\min_A = \chi_A$, comparing degrees gives $m = 1$, so $V\cong k[x]/\generators{p_m}$ is a cyclic $k[x]$-module.
If $v$ generates $V$, then $V = \theset{f(A)v \st f\in k[x]}$ is spanned by $v, Av, A^2v, \ldots$, and by Cayley--Hamilton by $v, Av, \ldots, A^{n-1}v$.
:::

::: {.remark}
The blocks of the rational canonical form of $A$ are in bijection with the nonconstant invariant factors of $xI-A$, and a companion matrix is its own rational canonical form.
:::

## Cyclic vectors

[[PR-K6MMW]]
