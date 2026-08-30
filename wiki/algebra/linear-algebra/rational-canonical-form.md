---
title: Rational canonical form
order: 40
problems:
  topics:
  - Rational Canonical Form
  - Structure Theorem
---

# Rational canonical form

The invariant factor decomposition, read as a matrix.
Unlike the [[Algebra/linear-algebra/jordan-canonical-form|Jordan form]] it exists over every field, because it never needs $\chi_A$ to split -- which is why a problem stated over $\QQ$ almost always wants this one.

[[D-HJR7M]]

[[FD-XT6HD]]

[[PR-4GQIZ]]

[[PR-GBL6P]]

:::{.proof}
$\not\Longleftarrow$:
In general $\min_A \divides \chi_A$, so suppose they differ.
Set $n\da \deg \chi_A$ and $n' \da \deg\min_A < n$; then $\min_A(A) = 0$ exhibits a linear dependence in $\ts{v, Av, \cdots, A^{n'}v}$ for every $v$, so no set $\ts{v, Av, \cdots, A^nv}$ is independent.

$\implies$:
By the structure theorem $V\cong \bigoplus_{i=1}^m k[x]/\gens{p_i}$, with $\chi_A = \prod p_i$ and $\min_A = p_m$.
Comparing degrees, $\deg\chi_A = \dim_k V$ and $\deg\min_A = \dim_k k[x]/\gens{p_m}$, so equality forces $\dim_k k[x]/\gens{p_i} = 0$ for $i<m$, making $V$ a cyclic $k[x]\dash$module.
Then $V = \ts{f(x)\actson v} = \spanof_k\ts{A^kv \st k\geq 0}$, and Cayley--Hamilton truncates the span at $k = n-1$.

:::

[[PR-TI6YA]]

:::{.remark}
The blocks of $\RCF(A)$ biject with the invariant factors, and a companion matrix is already in rational form.

:::

## Where the form comes from

:::{.proof title="Derivation"}
\envlist

- Let $k[x]$ act on $V$ by $p(x)\actson \vector v \da p(T)\vector v$, making $V$ a finitely generated torsion $k[x]\dash$module whose submodules are exactly the $T\dash$invariant subspaces.

- $k$ is a field so $k[x]$ is a PID, and the structure theorem gives the invariant factor decomposition
\[
V \cong \bigoplus_{i=1}^m k[x] / \gens{ p_i(x) }, \qquad p_1 \divides p_2 \divides \cdots \divides p_m
.\]

- Each factor is a $T\dash$invariant subspace $V_i$ on which $p_i$ is the minimal polynomial of $T$.
  The largest invariant factor $p_m$ is $\min_T$, and the product of them all is $\chi_T$: since $p_i \divides p_m$ for every $i$, we get $p_m \actson V = 0$ and minimality gives $\min_T \divides p_m$.

- So $T$ is block diagonal with one block per invariant factor, and it suffices to identify a single block, so assume $V = k[x]/\gens{p(x)}$ is cyclic with $\deg p = n$.

- Then $\ts{\vector v, T\vector v, \cdots, T^{n-1}\vector v}$ is a basis: a dependence among them would give a polynomial of degree below $n$ annihilating $T$, contradicting minimality of $p$.

- In that basis $T$ shifts each basis vector to the next, and the last one is expanded by $p(T) = 0$, giving the companion matrix
\[
M_1 =
\begin{bmatrix}
0 &  &  &  & -a_0 \\
1 & 0 &  &  & -a_1 \\
 &  1 &  0&  & -a_2 \\
 &  & \ddots &  0 & \vdots \\
 &  &  & 1 & -a_{n-1}
\end{bmatrix}
.\]

:::

## Cyclic vectors

[[PR-K6MMW]]
