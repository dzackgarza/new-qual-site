---
schema: qual/card@1
id: P-CZVX6
kind: problem
title: Irreducible characteristic polynomial iff no proper invariant subspaces, and
  diagonalizability over $\overline{F}$ in characteristic $0$
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Diagonalization
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.problem}
Let $V$ be a finite-dimensional vector space over a field $F$ and let $T: V \to V$ be a linear operator with characteristic polynomial $f(x) = \det(x I - T) \in F[x]$.

(a) Show that $f(x)$ is irreducible in $F[x]$ if and only if there are no proper non-zero $T$-invariant subspaces of $V$ (i.e. $W \le V$ with $T(W) \subseteq W$ implies $W = \{0\}$ or $W = V$).

(b) If $f(x)$ is irreducible in $F[x]$ and $\operatorname{char}(F) = 0$, show that $T$ is diagonalizable over the algebraic closure $\overline{F}$.
:::

::: {.solution}
**Goal:** Prove the equivalence between irreducibility of the characteristic polynomial and simplicity of the $F[x]$-module $V$ in (a), and deduce diagonalizability over $\overline{F}$ in characteristic zero in (b).

::: pf

::: pf-step
Part (a) ($\implies$): If $f(x)$ is irreducible, $V$ has no proper non-zero $T$-invariant subspaces.

::: pf-proof

::: pf-step
We prove the contrapositive: suppose there exists a $T$-invariant subspace $W \le V$ such that $0 < \dim W < \dim V$.
:::

::: pf-step
Let $k = \dim W$ and $n = \dim V$, so $1 \le k \le n - 1$.
:::

::: pf-step
Choose a basis $\{w_1, \dots, w_k\}$ for $W$, and extend it to an ordered basis $\mathcal{B} = \{w_1, \dots, w_k, v_1, \dots, v_{n-k}\}$ of $V$.
:::

::: pf-step
Since $T(W) \subseteq W$, the matrix representation of $T$ with respect to $\mathcal{B}$ is block upper-triangular:
$$[T]_\mathcal{B} = \begin{pmatrix} A & B \\ 0 & C \end{pmatrix},$$
where $A \in M_{k \times k}(F)$ is the matrix of the restriction $T|_W$, and $C \in M_{(n-k) \times (n-k)}(F)$ is the matrix of the induced operator on the quotient space $V/W$.
:::

::: pf-step
Compute the characteristic polynomial of $T$:
$$f(x) = \det(x I_n - [T]_\mathcal{B}) = \det \begin{pmatrix} x I_k - A & -B \\ 0 & x I_{n-k} - C \end{pmatrix} = \det(x I_k - A) \cdot \det(x I_{n-k} - C).$$
:::

::: pf-step
Let $g(x) = \det(x I_k - A) \in F[x]$ and $h(x) = \det(x I_{n-k} - C) \in F[x]$.
:::

::: pf-step
Since $\deg g = k \ge 1$ and $\deg h = n - k \ge 1$, $f(x) = g(x) h(x)$ is a factorization into polynomials of strictly smaller positive degrees.
:::

::: pf-step
Thus $f(x)$ is reducible in $F[x]$.
:::

::: pf-step
By contraposition, if $f(x)$ is irreducible, $V$ has no proper non-zero $T$-invariant subspaces.
:::

:::

:::

::: pf-step
Part (a) ($\impliedby$): If $V$ has no proper non-zero $T$-invariant subspaces, $f(x)$ is irreducible.

::: pf-proof

::: pf-step
Choose any non-zero vector $v \in V \setminus \{0\}$.
:::

::: pf-step
The cyclic subspace $W_v = \operatorname{span}_F\{T^j v : j \ge 0\} = F[T] v$ is a non-zero $T$-invariant subspace of $V$.
:::

::: pf-step
By hypothesis, $V$ contains no proper non-zero $T$-invariant subspaces, so $W_v = V$.
:::

::: pf-step
Thus $v$ is a cyclic vector for $V$, and the minimal polynomial $m_T(x)$ of $T$ has degree equal to $\dim W_v = \dim V = n$.
:::

::: pf-step
By the Cayley–Hamilton Theorem, $m_T(x) \mid f(x)$. Since both $m_T(x)$ and $f(x)$ are monic of degree $n$, we have $f(x) = m_T(x)$.
:::

::: pf-step
Now suppose for contradiction that $f(x)$ is reducible in $F[x]$, so $f(x) = g(x) h(x)$ with $\deg g \ge 1$, $\deg h \ge 1$, and $\deg g + \deg h = n$.
:::

::: pf-step
Since $m_T(x) = f(x)$ and $\deg g < n$, $g(T) \ne 0$ as a linear operator on $V$.
:::

::: pf-step
Thus there exists some vector $u \in V$ such that $w = g(T) u \ne 0$.
:::

::: pf-step
Consider the cyclic subspace $U = F[T] w$. Since $w \ne 0$, $U \ne \{0\}$.
:::

::: pf-step
Evaluate $h(T)$ on $w$:
$$h(T) w = h(T)(g(T) u) = (h(T) g(T)) u = f(T) u = 0.$$
:::

::: pf-step
Thus $h(T)$ annihilates $w$, which implies that the minimal polynomial of $w$ divides $h(x)$.
:::

::: pf-step
Therefore $\dim U \le \deg h < n$, so $U$ is a non-zero $T$-invariant subspace strictly contained in $V$ ($0 < \dim U < n$).
:::

::: pf-step
This contradicts the hypothesis that $V$ has no proper non-zero $T$-invariant subspaces.
:::

::: pf-step
Hence $f(x)$ must be irreducible in $F[x]$.
:::

:::

:::

::: pf-step
Part (b): Diagonalizability over $\overline{F}$ in characteristic 0.

::: pf-proof

::: pf-step
By Part (a), since $f(x)$ is irreducible in $F[x]$, the minimal polynomial of $T$ is $m_T(x) = f(x)$.
:::

::: pf-step
Since $\operatorname{char}(F) = 0$ and $f(x)$ is irreducible, $f(x)$ is a separable polynomial: its derivative $f'(x)$ is a non-zero polynomial with $\deg f' = n - 1 < n = \deg f$, so $\gcd(f(x), f'(x)) = 1$.
:::

::: pf-step
Over the algebraic closure $\overline{F}$, $f(x)$ splits completely into distinct linear factors:
$$f(x) = (x - \lambda_1)(x - \lambda_2) \cdots (x - \lambda_n), \quad \text{where } \lambda_i \ne \lambda_j \text{ for all } i \ne j.$$
:::

::: pf-step
Since the minimal polynomial $m_T(x) = f(x)$ splits over $\overline{F}$ into distinct linear factors (is square-free), $T$ is diagonalizable over $\overline{F}$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
The characteristic polynomial $f(x)$ is irreducible in $F[x]$ if and only if $V$ is a simple $F[T]$-module, and in characteristic zero this guarantees that $T$ has $n$ distinct eigenvalues in $\overline{F}$, hence is diagonalizable over $\overline{F}$.
:::

:::

:::
:::
