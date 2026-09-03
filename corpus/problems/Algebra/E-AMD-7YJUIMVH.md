---
schema: qual/card@1
id: E-AMD-7YJUIMVH
kind: problem
title: A linear operator cycling a basis has minimal polynomial $x^n-1$ and is diagonalizable
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
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that if $\theset{\vector v_i}$ is a basis for $V$ where $\dim(V) = n$ and $T(\vector v_i) = \vector v_{i+1 \mod n}$ then $T$ is diagonalizable with minimal polynomial $x^n-1$.
:::

::: {.solution}
**Goal:** Let $V$ be an $n$-dimensional vector space over $\mathbb{C}$ (or an algebraically closed field of characteristic not dividing $n$), with basis $\mathcal{B} = \{v_0, v_1, \dots, v_{n-1}\}$.
Let $T: V \to V$ be the linear operator defined by $T(v_i) = v_{i+1 \pmod n}$ for $0 \le i \le n-1$.
Prove that the minimal polynomial of $T$ is $m_T(x) = x^n - 1$ and that $T$ is diagonalizable.

<1>1. Computation of powers of $T$: <2>1. For any integer $k \ge 0$ and any basis vector $v_i$, $T^k(v_i) = v_{i+k \pmod n}$.
::: {.proof}
By induction on $k$: Base case $k=0$ gives $T^0(v_i) = v_i = v_{i+0 \pmod n}$.
:::
If $T^k(v_i) = v_{i+k \pmod n}$, then $T^{k+1}(v_i) = T(T^k(v_i)) = T(v_{i+k \pmod n}) = v_{i+k+1 \pmod n}$.
<2>2. In particular, $T^n(v_i) = v_{i+n \pmod n} = v_i$ for all $i \in \{0, \dots, n-1\}$.
::: {.proof}
Since $n \equiv 0 \pmod n$.
:::
<2>3. Since $T^n(v_i) = I(v_i)$ on all basis vectors $v_i$, $T^n = I$ (the identity operator on $V$).
::: {.proof}
Two linear operators agreeing on a basis are identical.
:::
<2>4. Therefore, $T$ satisfies the polynomial $p(x) = x^n - 1$, i.e., $p(T) = T^n - I = 0$.
::: {.proof}
Direct evaluation.
:::

<1>2. The minimal polynomial $m_T(x)$ equals $x^n - 1$: <2>1. By definition of the minimal polynomial, $m_T(x)$ divides any polynomial $q(x)$ such that $q(T) = 0$.
Hence $m_T(x) \mid (x^n - 1)$.
::: {.proof}
Property of minimal polynomials.
:::
<2>2. $\deg(m_T(x)) \ge n$.
<3>1. Consider the vector $v_0 \in V$.
The vectors $\{v_0, T(v_0), T^2(v_0), \dots, T^{n-1}(v_0)\}$ equal $\{v_0, v_1, v_2, \dots, v_{n-1}\}$.
::: {.proof}
By <1>1.<2>1, $T^k(v_0) = v_k$.
:::
<3>2. The set $\{v_0, v_1, \dots, v_{n-1}\}$ is the basis $\mathcal{B}$, hence linearly independent.
::: {.proof}
Hypothesis that $\mathcal{B}$ is a basis.
:::
<3>3. If there existed a non-zero polynomial $g(x) = \sum_{k=0}^{m} c_k x^k$ with $m < n$ such that $g(T) = 0$, then $g(T)(v_0) = \sum_{k=0}^m c_k v_k = 0$.
::: {.proof}
Action of $g(T)$ on $v_0$.
:::
<3>4. By linear independence of $\{v_0, \dots, v_{n-1}\}$, all coefficients $c_k = 0$, so no non-zero polynomial of degree $< n$ annihilates $T$.
::: {.proof}
Linear independence of basis elements.
:::
<3>5. Q.E.D.
::: {.proof}
$\deg(m_T) \ge n$.
:::
<2>3. Since $m_T(x) \mid (x^n - 1)$, $\deg(m_T(x)) \ge n$, and both $m_T(x)$ and $x^n - 1$ are monic, we have $m_T(x) = x^n - 1$.
::: {.proof}
A monic polynomial of degree $n$ dividing a monic polynomial of degree $n$ must equal it.
:::

<1>3. $T$ is diagonalizable: <2>1. Over $\mathbb{C}$, the polynomial $x^n - 1$ factors as the product of $n$ distinct linear factors: $$x^n - 1 = \prod_{k=0}^{n-1} (x - \omega^k),$$ where $\omega = e^{2\pi i / n}$ is a primitive $n$-th root of unity.
::: {.proof}
Standard factorization of $x^n - 1$ over $\mathbb{C}$.
:::
The roots $\omega^k$ for $k = 0, \dots, n-1$ are pairwise distinct.
<2>2. A linear operator on a finite-dimensional vector space is diagonalizable if and only if its minimal polynomial splits into distinct linear factors over the base field.
::: {.proof}
Fundamental theorem of linear algebra on diagonalizability.
:::
<2>3. Explicit eigenbasis construction: For each $k \in \{0, 1, \dots, n-1\}$, define $w_k = \sum_{j=0}^{n-1} \omega^{-j k} v_j \in V$.
<3>1. Action of $T$ on $w_k$: $$T(w_k) = \sum_{j=0}^{n-1} \omega^{-j k} T(v_j) = \sum_{j=0}^{n-1} \omega^{-j k} v_{j+1 \pmod n} = \sum_{\ell=0}^{n-1} \omega^{-(\ell-1) k} v_\ell = \omega^k \sum_{\ell=0}^{n-1} \omega^{-\ell k} v_\ell = \omega^k w_k.$$ Proof: Discrete Fourier transform shifting property.
<3>2. Since $w_k \neq 0$ (coefficients not all zero), each $w_k$ is an eigenvector with distinct eigenvalue $\lambda_k = \omega^k$.
::: {.proof}
Eigenvectors for distinct eigenvalues are linearly independent, so $\{w_0, \dots, w_{n-1}\}$ forms a basis of eigenvectors for $V$.
:::
<3>3. Q.E.D.
::: {.proof}
Explicit verification of diagonalizability.
:::

<1>4. Conclusion: $T$ has minimal polynomial $m_T(x) = x^n - 1$ and is diagonalizable.
::: {.proof}
By <1>2 and <1>3.
:::
:::
