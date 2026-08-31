---
schema: qual/card@1
id: P-WAH54
kind: problem
title: A cyclic permutation of a basis is diagonalizable with minimal polynomial $x^n-1$
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Minimal and Characteristic Polynomials
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
- Show that if $\theset{\vector v_i}$ is a basis for $V$ where $\dim(V) = n$ and $T(\vector v_i) = \vector v_{i+1 \mod n}$ then $T$ is diagonalizable with minimal polynomial $x^n-1$.
:::

::: {.solution}
<1>1. Show that $x^n - 1$ annihilates $T$:
<2>1. For each basis vector $\mathbf{v}_i$ ($0 \le i \le n - 1$), the operator $T$ satisfies:
\[
T^n(\mathbf{v}_i) = \mathbf{v}_{i + n \pmod n} = \mathbf{v}_i = I(\mathbf{v}_i).
\]
::: {.proof}
applying the permutation $T$ $n$ times.
:::
<2>2. Since $T^n$ agrees with the identity operator $I$ on a basis, $T^n = I$, so $(T^n - I) = 0$.
Thus the minimal polynomial $m_T(x)$ divides $x^n - 1$.
::: {.proof}
definition of minimal polynomial.
:::

<1>2. Show that $\deg(m_T) = n$, so $m_T(x) = x^n - 1$:
<2>1. Consider the vector $\mathbf{v}_0$. Its images under powers of $T$ are:
\[
\mathbf{v}_0, \, T(\mathbf{v}_0) = \mathbf{v}_1, \, T^2(\mathbf{v}_0) = \mathbf{v}_2, \, \dots, \, T^{n-1}(\mathbf{v}_0) = \mathbf{v}_{n-1}.
\]
These $n$ vectors form the given basis of $V$, hence are linearly independent.
::: {.proof}
hypothesis on basis.
:::
<2>2. If $g(x) = \sum_{j=0}^d c_j x^j$ is a non-zero polynomial of degree $d < n$ with $g(T) = 0$, then:
\[
0 = g(T)(\mathbf{v}_0) = \sum_{j=0}^d c_j T^j(\mathbf{v}_0) = \sum_{j=0}^d c_j \mathbf{v}_j.
\]
By linear independence of $\{\mathbf{v}_0, \dots, \mathbf{v}_{n-1}\}$, $c_0 = c_1 = \cdots = c_d = 0$, a contradiction.
::: {.proof}
linear independence of basis vectors.
:::
<2>3. Thus no non-zero polynomial of degree $< n$ annihilates $T$, so $\deg(m_T) \ge n$.
Since $m_T(x) \mid (x^n - 1)$ and $\deg(x^n - 1) = n$, the monic minimal polynomial is:
\[
m_T(x) = x^n - 1.
\]
::: {.proof}
monic divisibility of equal degree polynomials.
:::

<1>3. Prove diagonalizability:
<2>1. Over $\mathbb{C}$, the polynomial $x^n - 1$ factors as:
\[
x^n - 1 = \prod_{k=0}^{n-1} (x - \omega^k), \quad \text{where } \omega = e^{2\pi i/n}.
\]
The $n$ roots $\omega^0, \omega^1, \dots, \omega^{n-1}$ are distinct.
::: {.proof}
distinct $n$-th roots of unity.
:::
<2>2. A linear operator is diagonalizable if and only if its minimal polynomial splits into distinct linear factors.
Since $m_T(x) = x^n - 1$ has $n$ distinct linear factors, $T$ is diagonalizable.
::: {.proof}
diagonalizability criterion via minimal polynomials.
:::
<2>3. Explicitly, for each $k \in \{0, \dots, n-1\}$, the discrete Fourier vector:
\[
\mathbf{w}_k = \sum_{j=0}^{n-1} \omega^{-jk} \mathbf{v}_j
\]
is a non-zero eigenvector satisfying $T(\mathbf{w}_k) = \omega^k \mathbf{w}_k$, providing an eigenbasis $\{\mathbf{w}_0, \dots, \mathbf{w}_{n-1}\}$ for $V$.
::: {.proof}
$T(\mathbf{w}_k) = \sum \omega^{-jk} \mathbf{v}_{j+1} = \omega^k \sum \omega^{-(j+1)k} \mathbf{v}_{j+1} = \omega^k \mathbf{w}_k$.
:::

<1>4. Conclusion:
$T$ is diagonalizable with minimal polynomial $m_T(x) = x^n - 1$. Q.E.D.
::: {.proof}
<1>2 and <1>3.
:::
:::
