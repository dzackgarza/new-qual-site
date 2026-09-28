---
schema: qual/card@1
id: P-BKF99-9
kind: problem
title: Three-dimensional differentiation-invariant spaces of smooth functions
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Applied Jordan normal form to differentiation restricted to V and solved
    each Jordan-chain differential equation. This gives exactly the
    exponential-polynomial spaces indexed by partitions of dimension three.
---

::: {.problem}
Describe all three-dimensional vector spaces $V$ of complex-valued $C^\infty$ functions on $\mathbb R$ that are invariant under differentiation.
:::

::: {.solution}
Let $D:V\to V$ denote differentiation.

<1>1. For every Jordan block of $D$ of size $m$ and eigenvalue $\lambda$,
the corresponding invariant subspace is
$$
e^{\lambda x}\operatorname{span}_{\CC}\{1,x,\ldots,x^{m-1}\}.
$$

::: {.proof}
Choose a Jordan chain $f_0,\ldots,f_{m-1}$ satisfying
$$
(D-\lambda)f_0=0,
\qquad
(D-\lambda)f_j=f_{j-1}\quad(1\leq j<m).
$$
Write $f_j=e^{\lambda x}g_j$. Then
$$
(D-\lambda)f_j=e^{\lambda x}g_j',
$$
so $g_0'=0$ and $g_j'=g_{j-1}$. Inductively, $g_j$ is a polynomial of
degree at most $j$, with nonzero coefficient of $x^j$ because the Jordan
chain is linearly independent. Hence
$$
\operatorname{span}\{f_0,\ldots,f_{m-1}\}
=
e^{\lambda x}\operatorname{span}\{1,x,\ldots,x^{m-1}\}.
$$
:::

<1>2. Every finite-dimensional differentiation-invariant space of
complex-valued smooth functions is a direct sum
$$
\bigoplus_{j=1}^r
e^{\lambda_j x}
\operatorname{span}_{\CC}\{1,x,\ldots,x^{m_j-1}\},
$$
where the $\lambda_j$ are distinct and $m_j\geq1$.

::: {.proof}
Over $\CC$, the linear operator $D$ has a Jordan decomposition. Group its
Jordan blocks by eigenvalue. For a fixed eigenvalue $\lambda$, there cannot
be two Jordan blocks: each block contains a nonzero eigenvector, while every
smooth solution of
$$
f'=\lambda f
$$
is a scalar multiple of $e^{\lambda x}$, so the $\lambda$-eigenspace of
$D$ on the ambient function space is one-dimensional. Thus there is at most
one block for each eigenvalue. Step <1>1 identifies the subspace belonging to
each block, and the Jordan decomposition gives their direct sum.
:::

<1>3. If $\dim V=3$, then $V$ is exactly one of the following forms:
$$
\boxed{
\begin{aligned}
&\operatorname{span}_{\CC}\{e^{\lambda x},e^{\mu x},e^{\nu x}\},
&&\lambda,\mu,\nu\text{ pairwise distinct};\\
&\operatorname{span}_{\CC}\{e^{\lambda x},xe^{\lambda x},e^{\mu x}\},
&&\lambda\neq\mu;\\
&\operatorname{span}_{\CC}\{e^{\lambda x},xe^{\lambda x},x^2e^{\lambda x}\},
&&\lambda\in\CC.
\end{aligned}}
$$

::: {.proof}
By step <1>2, the positive integers $m_j$ sum to $3$. The only partitions of
$3$ are $1+1+1$, $2+1$, and $3$. Substituting these three possibilities into
the decomposition of step <1>2 gives exactly the displayed list.
:::

<1>4. Every space in step <1>3 is three-dimensional and invariant under
differentiation.

::: {.proof}
For each $\lambda$ and $m$,
$$
D\left(e^{\lambda x}x^k\right)
=
\lambda e^{\lambda x}x^k
+k e^{\lambda x}x^{k-1},
$$
so each listed span is invariant. The displayed generators are linearly
independent: within one exponential block this follows from independence of
$1,x,\ldots$, and blocks with distinct exponents are generalized
eigenspaces of $D$ for distinct eigenvalues. Their dimensions therefore sum
to $3$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 shows that every possible $V$ is on the list, and step <1>4 verifies
that every space on the list has the required properties.
:::
:::
