---
schema: qual/card@1
id: P-DRL6B
kind: problem
title: Diagonalizable iff the space is a direct sum of eigenspaces
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $V$ be a finite-dimensional vector space over a field $K$, and let $T: V \to V$ be a linear operator.
Show that $T$ is diagonalizable if and only if $V$ is the direct sum of its eigenspaces:
$$V = \bigoplus_{i=1}^k E_{\lambda_i}(T) = \bigoplus_{i=1}^k \ker(T - \lambda_i I)$$
where $\lambda_1, \dots, \lambda_k \in K$ are the distinct eigenvalues of $T$.
:::

::: solution
**Goal:** Prove that a linear operator $T: V \to V$ on a finite-dimensional vector space is diagonalizable iff $V$ decomposes into a direct sum of eigenspaces.

<1>1. Linear independence of distinct eigenspaces:
    *Proof:*
    <2>1. Let $\lambda_1, \dots, \lambda_k \in K$ be distinct eigenvalues of $T$, and let $E_{\lambda_i} = \ker(T - \lambda_i I)$.
    <2>2. **Claim:** The sum $E_{\lambda_1} + E_{\lambda_2} + \cdots + E_{\lambda_k}$ is always a **direct sum**:
        $$E_{\lambda_1} + \cdots + E_{\lambda_k} = \bigoplus_{i=1}^k E_{\lambda_i}.$$
    <2>3. *Proof of Claim:* Suppose $v_1 + v_2 + \cdots + v_k = 0$ with $v_i \in E_{\lambda_i}$.
        - We apply the operator $(T - \lambda_2 I)(T - \lambda_3 I)\cdots(T - \lambda_k I)$ to this sum.
        - For any $j \ge 2$, $(T - \lambda_j I) v_j = (\lambda_j - \lambda_j) v_j = 0$.
        - Thus all terms for $j \ge 2$ vanish, leaving:
            $$\prod_{j=2}^k (\lambda_1 - \lambda_j) v_1 = 0.$$
        - Since $\lambda_1 \ne \lambda_j$ for all $j \ge 2$, the scalar $\prod_{j=2}^k (\lambda_1 - \lambda_j) \ne 0$, which forces $v_1 = 0$.
        - Repeating the argument for each index $i$ shows $v_i = 0$ for all $i \in \{1, \dots, k\}$.
    <2>4. Thus the eigenspaces are linearly independent and form an internal direct sum $W = \bigoplus_{i=1}^k E_{\lambda_i} \subseteq V$.

<1>2. Direction $(\implies)$: $T$ is diagonalizable $\implies V = \bigoplus_{i=1}^k E_{\lambda_i}$:
    *Proof:*
    <2>1. If $T$ is diagonalizable, there exists an eigenbasis $\mathcal{B} = \{v_1, \dots, v_n\}$ for $V$.
    <2>2. Every basis vector $v_j$ belongs to some eigenspace $E_{\lambda_i}$.
    <2>3. Therefore, the span of all eigenspaces contains $\mathcal{B}$:
        $$V = \operatorname{span}(\mathcal{B}) \subseteq \sum_{i=1}^k E_{\lambda_i} \subseteq V.$$
    <2>4. Combined with linear independence of eigenspaces from Step <1>1:
        $$V = \bigoplus_{i=1}^k E_{\lambda_i}.$$

<1>3. Direction $(\impliedby)$: $V = \bigoplus_{i=1}^k E_{\lambda_i} \implies T$ is diagonalizable:
    *Proof:*
    <2>1. For each $i \in \{1, \dots, k\}$, choose a basis $\mathcal{B}_i = \{v_{i, 1}, v_{i, 2}, \dots, v_{i, d_i}\}$ of $E_{\lambda_i}$, where $d_i = \dim_K(E_{\lambda_i})$.
    <2>2. Since $V = \bigoplus_{i=1}^k E_{\lambda_i}$, the union $\mathcal{B} = \bigcup_{i=1}^k \mathcal{B}_i$ is a basis for $V$.
    <2>3. Every vector in $\mathcal{B}$ is an eigenvector of $T$.
    <2>4. The matrix of $T$ relative to the basis $\mathcal{B}$ is diagonal:
        $$[T]_\mathcal{B} = \operatorname{diag}(\underbrace{\lambda_1, \dots, \lambda_1}_{d_1 \text{ times}}, \dots, \underbrace{\lambda_k, \dots, \lambda_k}_{d_k \text{ times}}).$$
    <2>5. Thus $T$ is diagonalizable.

<1>4. Dimension criterion:
    *Proof:*
    <2>1. As a corollary, $T$ is diagonalizable $\iff \sum_{i=1}^k \dim_K(E_{\lambda_i}) = \dim_K(V)$.

<1>5. Conclusion:
    $T$ is diagonalizable if and only if $V = \bigoplus_{i=1}^k \ker(T - \lambda_i I)$. Q.E.D.
:::
