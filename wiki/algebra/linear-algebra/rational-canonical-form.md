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

[[PR-GBL6P]]

::: {.proof}
Let $V = k^n$ with $x$ acting by $A$.

$\impliedby$: Suppose $v$ is a cyclic vector, so that $v, Av, \ldots, A^{n-1}v$ is a basis of $V$.
If $n' \da \deg\min_A < n$, then $\min_A(A)v = 0$ is a linear dependence among $v, Av, \ldots, A^{n'}v$, a contradiction.
Hence $\deg\min_A = n = \deg\chi_A$, and since $\min_A$ divides $\chi_A$ and both are monic, $\min_A = \chi_A$.

$\implies$: By the structure theorem $V\cong \bigoplus_{i=1}^m k[x]/\gens{p_i}$ with nonconstant invariant factors $p_1\divides\cdots\divides p_m$, $\chi_A = \prod_i p_i$, and $\min_A = p_m$.
If $\min_A = \chi_A$, comparing degrees gives $m = 1$, so $V\cong k[x]/\gens{p_m}$ is a cyclic $k[x]$-module.
If $v$ generates $V$, then $V = \ts{f(A)v \st f\in k[x]}$ is spanned by $v, Av, A^2v, \ldots$, and by Cayley--Hamilton by $v, Av, \ldots, A^{n-1}v$.
:::

[[PR-TI6YA]]

::: {.remark}
The blocks of the rational canonical form of $A$ are in bijection with the nonconstant invariant factors of $xI-A$, and a companion matrix is its own rational canonical form.
:::

## Derivation

::: {.proof title="Derivation of the rational canonical form"}
\envlist

- Let $k[x]$ act on $V$ by $p(x)\actson \vector v \da p(T)\vector v$.
  This makes $V$ a finitely generated torsion $k[x]$-module whose submodules are the $T$-invariant subspaces.

- Since $k[x]$ is a PID, the structure theorem gives the invariant factor decomposition
$$
V \cong \bigoplus_{i=1}^m k[x] / \gens{ p_i(x) }, \qquad p_1 \divides p_2 \divides \cdots \divides p_m.
$$

- Each summand is a $T$-invariant subspace $V_i$ on which the minimal polynomial of $T$ is $p_i$.
  Since $p_i \divides p_m$ for every $i$, $p_m(T) = 0$ on $V$, so $\min_T \divides p_m$; since $\min_T(T)$ vanishes on $V_m\cong k[x]/\gens{p_m}$, $p_m\divides\min_T$.
  Hence $\min_T = p_m$.

- $T$ is block diagonal with one block for each $V_i$, so it suffices to treat a cyclic module $V = k[x]/\gens{p(x)}$ with $p(x) = x^n + a_{n-1}x^{n-1}+\cdots+a_0$ and generator $\vector v$.

- Then $\vector v, T\vector v, \ldots, T^{n-1}\vector v$ is a basis: a linear dependence among them would give a nonzero polynomial of degree less than $n$ annihilating the generator $\vector v$, hence annihilating $V$, contradicting that $p$ is the minimal polynomial of $T$.

- In this basis $T$ sends each basis vector to the next, and $T^n\vector v = -\sum_{i<n}a_iT^i\vector v$ because $p(T)=0$, so the matrix of $T$ is the companion matrix
$$
C(p) =
\begin{bmatrix}
0 &  &  &  & -a_0 \\
1 & 0 &  &  & -a_1 \\
 &  1 &  0&  & -a_2 \\
 &  & \ddots &  \ddots & \vdots \\
 &  &  & 1 & -a_{n-1}
\end{bmatrix},
$$
whose characteristic polynomial is $p$.
Hence $\chi_T = \prod_i p_i$.
:::

## Cyclic vectors

[[PR-K6MMW]]
