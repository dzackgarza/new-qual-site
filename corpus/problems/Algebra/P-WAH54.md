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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "if $\theset{\vector v_i}$ is a basis for $V$ where $\dim(V) = n$" with no field. Over a field whose characteristic divides n, or that lacks the n-th roots of unity, T is not diagonalizable; the statement now takes V to be a complex vector space and indexes the basis by i = 0, ..., n-1.'
---

::: {.problem}
Show that if $\theset{\vector v_0, \ldots, \vector v_{n-1}}$ is a basis for a complex vector space $V$ where $\dim(V) = n \geq 1$ and $T(\vector v_i) = \vector v_{i+1 \mod n}$, then $T$ is diagonalizable with minimal polynomial $x^n-1$.
:::

::: {.solution}

Let $m_T$ be the minimal polynomial of $T$ and $\omega = e^{2\pi i/n}$.

::: pf

::: {.pf-step #divides}

$m_T(x)$ divides $x^n - 1$.

::: pf-proof

Applying $T$ $n$ times sends $\vector v_i$ to $\vector v_{i+n \bmod n} = \vector v_i$, so $T^n$ agrees with the identity on a basis and $T^n - I = 0$.

:::

:::

::: {.pf-step #degree}

$m_T(x) = x^n - 1$.

::: pf-proof

Let $g(x) = \sum_{j=0}^{d} c_j x^j$ with $d < n$ and $g(T) = 0$. Since $T^j(\vector v_0) = \vector v_j$ for $0 \le j \le n-1$,
$$
0 = g(T)(\vector v_0) = \sum_{j=0}^{d} c_j \vector v_j,
$$
and linear independence of the basis gives $c_0 = \cdots = c_d = 0$. Hence $\deg m_T \ge n$. By step [](#divides){.pf-ref}, the monic polynomial $m_T$ divides the monic polynomial $x^n-1$ of degree $n$, so they are equal.

:::

:::

::: pf-step

$T$ is diagonalizable, with eigenbasis $\vector w_k = \sum_{j=0}^{n-1} \omega^{-jk} \vector v_j$ and $T\vector w_k = \omega^k \vector w_k$ for $0 \le k \le n-1$.

::: pf-proof

Over $\CC$, $x^n - 1 = \prod_{k=0}^{n-1}(x - \omega^k)$ with the $n$ roots $\omega^k$ distinct. By step [](#degree){.pf-ref}, $m_T$ is a product of distinct linear factors, so $T$ is diagonalizable. Explicitly, since $\omega^{-nk} = 1$,
$$
T\vector w_k = \sum_{j=0}^{n-1} \omega^{-jk} \vector v_{j+1 \bmod n} = \omega^{k} \sum_{j=0}^{n-1} \omega^{-(j+1)k} \vector v_{j+1 \bmod n} = \omega^k \vector w_k,
$$
and each $\vector w_k \neq 0$ because its coefficient on $\vector v_0$ is $1$. Eigenvectors for the $n$ distinct eigenvalues $\omega^k$ are linearly independent, so they form a basis of $V$.

:::

:::

:::

:::
