---
order: 120
---

# Rational Canonical Form

Corresponds to the **Invariant Factor Decomposition** of $T$.

[[D-HJR7M]]

[[FD-XT6HD]]

[[PR-4GQIZ]]

[[PR-GBL6P]]

:::{.proof}
$\not\implies$:
In general, $\min_A \divides \chi_A$, so suppose they're not equal.
Set $n\da \deg \chi_A$, then if $n' \da \deg \min_A < n$, using that $\min_A(A) = 0$ this exhibits a linear dependence in $\ts{v, Av, \cdots, A^{n'} v}$ for any $v$.
In particular, since $n>n'$, any set $\ts{v, Av,\cdots,A^nv}$ has a linear dependence.

$\implies$:
Apply the structure theorem to write $V\cong \bigoplus_{i=1}^m k[x]/\gens{p_i}$.
Since $\chi_A(x) = \prod p_i(x)$ and $\min_A(x) = p_m(x)$, this forces $m=1$ -- one way to see this is that $\dim_k V = \sum_{i=1}^m \dim_k k[x]/\gens{p_i}$,
where $\deg \chi_A = \dim_k V$ and $\deg \min_A = \dim k[x]/\gens{p_m}$.
For these to be equal, this forces $\dim_k k[x]/\gens{p_i} = 0$ for $1\leq i \leq m-1$, making $V$ a cyclic $k[x]\dash$module.
So $V = k[x]\actson \vector v$ for some $\vector v\in V$, which is the desired cyclic vector, and 
\[
V = \ts{f(x).v \st f\in k[x]} = \spanof_k\ts{A^k v \st k\geq 0}
.\]
By Cayley-Hamilton, $\chi_A(A) = 0$ and so $A^n$ is a linear combinations of $A^k$ for $0\leq k \leq n-1$, so $V= \spanof_k \ts{A^k v \st 0\leq k \leq n-1}$.

:::

[[PR-TI6YA]]

:::{.remark}
Thus the blocks of $\RCF(A)$ biject with invariant factors of $A$.
Note that any companion matrix is already in $\RCF$.

:::

:::{.proof title="Derivation of RCF"}
\envlist

- Let $k[x] \actson V$ by $p(x) \actson \vector v \da p(T)(\vector v)$, making $V$ into a finitely generated torsion $k[x]\dash$module. 
  - Note that $k[x]\dash$submodules are exactly $T\dash$invariant subspaces.

- $k$ a field implies $k[x]$ a PID, so apply structure theorem to obtain an invariant factor decomposition 
\[
V \cong k[x] / \gens{\chi_T(x)} \cong \bigoplus_{i=1}^m k[x] / \gens{ p_i(x) }
&& p_1(x) \divides p_2(x) \divides \cdots p_m(x)
.\]
  
- Since each factor is submodule, each corresponds to a $T\dash$invariant subspace $V_i$ where $p_i$ is the minimal polynomial of $T$ restricted to $V_i$.

  - The largest invariant factor $p_m$ is the minimal polynomial of $T$, their product is the characteristic polynomial.
  This follows because $p_m(x)\actson V = 0$, since $p_i\divides p_m$ for all $i$, forcing $\min_A \divides p_m$ by minimality.

- Write $V \cong \bigoplus_{i=1}^m V_i$ as a $k[x]\dash$module, where $V_i \da k[x] / \gens{ p_i(x) }$, then $T$ is a block matrix $\bigoplus_{i=1}^m T_i$ where $T_i$ is the restriction of $T$ to $V_i$:
\[
\left(\begin{array}{ccccc}T_{1} & 0 & 0 & \cdots & 0 \\ 0 & T_{2} & 0 & \cdots & 0 \\ \vdots & & \ddots & & \vdots \\ 0 & \cdots & & & T_{n}\end{array}\right)
.\]

- It suffices to determine the form of a single $M_i$, so without loss of generality suppose $m=1$ so $V = V_1 = k[x] / \gens{ p(x) }$ is a cyclic $k[x]\dash$module with $\deg p(x) = n$.

- $\chi_M(x) = \min_M(x) \iff$ there exists a cyclic vector $\vector v$, so the set \( \ts{\vector v_i}_{i=0}^{n-1} \da \ts{ \vector v, T\vector v, T^2\vector v, \cdots, T^{n-1}\vector v } \) is a basis for $V_1$.
  - If there is any linear independence, this gives a polynomial relation $\sum_{i=1}^{n'} a_iT^i\vector v = 0$ for some $n'<n$, but then $q(x) \da \sum_{i=1}^{n'} a_i x^i$ is a polynomial annihilating $T$, contradicting the minimality of $p(x)$.
  - So this yields $n$ linearly independent vectors in $k^n$, so it's a basis.
- What is $M_i$ in this basis?
  Check where basis elements are mapped to by $T$, noting that 
  \[
p(T) = \sum_{i=1}^{n}a_i T^i\vector v = T^n + a_{n-1} T^{n-1}\vector v + a_{n-2} T^{n-2} + \cdots + a_1 T\vector v + a_0 \vector v = 0
  ,\]
  using the minimal polynomial we can write
  - $T\vector v_0 = \vector v_1$
  - $T\vector v_2 = T^2 \vector v_0$
  - $T\vector v_3 = T^3 \vector v_0$
  - $\cdots$
  - $T\vector v_{n-2} = T^{n-1}\vector v$
  - $T\vector v_{n-1} = T^n\vector v = -a_{n-1}T^{n-1}\vector v - \cdots - a_1 T\vector v - a_0 \vector v$ 

- So we have
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

## Cyclic Vectors

[[PR-K6MMW]]
