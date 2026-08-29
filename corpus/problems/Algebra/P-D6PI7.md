---
schema: qual/card@1
id: P-D6PI7
kind: problem
title: Diagonalizable matrices have squarefree minimal polynomials
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Minimal and Characteristic Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
- Show that if a matrix is diagonalizable, its minimal polynomial is squarefree.
:::

::: solution
**Goal:** Prove that if a matrix $A \in M_n(F)$ is diagonalizable over a field $F$, then its minimal polynomial $m_A(x)$ is squarefree (a product of distinct linear factors).

<1>1. Diagonalization and distinct eigenvalues: *Proof:* <2>1. Because $A$ is diagonalizable, there exists an invertible matrix $P \in \operatorname{GL}_n(F)$ such that: $$P^{-1} A P = D = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n),$$ where each $\lambda_i \in F$ is an eigenvalue of $A$.
<2>2. Let $\{\mu_1, \mu_2, \dots, \mu_k\}$ be the set of pairwise distinct eigenvalues of $A$ (so $k \le n$). <2>3. Define the monic polynomial with distinct roots: $$p(x) = \prod_{j=1}^k (x - \mu_j) \in F[x].$$ <2>4. By construction, $p(x)$ is squarefree.

<1>2. Proof that $p(A) = 0$: *Proof:* <2>1. For the diagonal matrix $D$, applying $p$ yields: $$p(D) = \operatorname{diag}(p(\lambda_1), p(\lambda_2), \dots, p(\lambda_n)).$$ <2>2. For every $i \in \{1, \dots, n\}$, $\lambda_i \in \{\mu_1, \dots, \mu_k\}$, so $p(\lambda_i) = 0$.
<2>3. Therefore $p(D) = 0$ is the zero matrix.
<2>4. For $A = P D P^{-1}$: $$p(A) = p(P D P^{-1}) = P p(D) P^{-1} = P \cdot 0 \cdot P^{-1} = 0.$$

<1>3. Minimal polynomial equality: *Proof:* <2>1. By definition of the minimal polynomial $m_A(x)$, $p(A) = 0 \implies m_A(x) \mid p(x)$.
<2>2. Every eigenvalue $\mu_j$ of $A$ is a root of $m_A(x)$ (if $A v = \mu_j v$ with $v \neq 0$, then $0 = m_A(A) v = m_A(\mu_j) v$, so $m_A(\mu_j) = 0$). <2>3. Thus each $(x - \mu_j)$ divides $m_A(x)$.
<2>4. Since the linear factors $(x - \mu_j)$ are coprime and both $m_A(x)$ and $p(x)$ are monic, we have: $$m_A(x) = p(x) = \prod_{j=1}^k (x - \mu_j).$$

<1>4. Conclusion: $m_A(x)$ factors into pairwise distinct linear factors, so $m_A(x)$ is squarefree.
Q.E.D.
:::
