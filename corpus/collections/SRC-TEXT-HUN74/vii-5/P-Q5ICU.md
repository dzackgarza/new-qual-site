---
schema: qual/card@1
id: P-Q5ICU
kind: problem
title: Hungerford 7.5.7
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
---

::: problem
(a) Let $\phi, \psi$ be commuting endomorphisms of a finite-dimensional vector space $E$ over a field $K$ (so $\phi \psi = \psi \phi$). Show that if both $\phi$ and $\psi$ are diagonalizable (i.e. $E$ has a basis of eigenvectors for $\psi$ and a basis of eigenvectors for $\phi$), then $E$ has a basis consisting of simultaneous eigenvectors for both $\psi$ and $\phi$.

(b) Interpret the previous statement in terms of matrices similar to a diagonal matrix.
:::

::: solution
**Goal:** Prove that commuting diagonalizable endomorphisms admit a simultaneous eigenbasis in (a), and express this as simultaneous diagonalizability of commuting matrices in (b).

<1>1. Part (a): Invariance of eigenspaces of $\psi$ under $\phi$.
    *Proof:*
    <2>1. Since $\psi$ is diagonalizable, $E$ decomposes as a direct sum of its distinct eigenspaces:
    $$E = \bigoplus_{i=1}^k E_{\lambda_i}(\psi), \qquad \text{where } E_{\lambda_i}(\psi) = \{v \in E : \psi(v) = \lambda_i v\},$$
    and $\lambda_1, \dots, \lambda_k \in K$ are the distinct eigenvalues of $\psi$.
    <2>2. Let $v \in E_{\lambda_i}(\psi)$. Apply $\psi$ to $\phi(v)$ using commutativity $\psi \phi = \phi \psi$:
    $$\psi(\phi(v)) = (\psi \phi)(v) = (\phi \psi)(v) = \phi(\psi(v)) = \phi(\lambda_i v) = \lambda_i \phi(v).$$
    <2>3. Thus $\phi(v) \in E_{\lambda_i}(\psi)$, which proves that each eigenspace $E_{\lambda_i}(\psi)$ is a $\phi$-invariant subspace:
    $$\phi(E_{\lambda_i}(\psi)) \subseteq E_{\lambda_i}(\psi) \quad \text{for each } i \in \{1, \dots, k\}.$$

<1>2. Part (a): Diagonalizability of the restriction $\phi|_{E_{\lambda_i}(\psi)}$.
    *Proof:*
    <2>1. An endomorphism on a finite-dimensional vector space is diagonalizable if and only if its minimal polynomial splits into distinct linear factors (is square-free).
    <2>2. Since $\phi$ is diagonalizable on $E$, its minimal polynomial $m_\phi(x) \in K[x]$ is a product of distinct linear factors.
    <2>3. For each $i \in \{1, \dots, k\}$, the minimal polynomial of the restricted endomorphism $\phi|_{E_{\lambda_i}(\psi)}$ divides $m_\phi(x)$.
    <2>4. Since any divisor of a square-free polynomial that splits into linear factors is also square-free and splits into linear factors, the restricted endomorphism $\phi|_{E_{\lambda_i}(\psi)}$ is diagonalizable on $E_{\lambda_i}(\psi)$.
    <2>5. Therefore, each eigenspace $E_{\lambda_i}(\psi)$ has a basis $\mathcal{B}_i = \{v_{i, 1}, \dots, v_{i, d_i}\}$ consisting of eigenvectors of $\phi$.

<1>3. Part (a): Construction of the simultaneous eigenbasis.
    *Proof:*
    <2>1. Every vector $v_{i, j} \in \mathcal{B}_i$ satisfies:
    $$\psi(v_{i, j}) = \lambda_i v_{i, j} \quad \text{and} \quad \phi(v_{i, j}) = \mu_{i, j} v_{i, j}$$
    for some eigenvalue $\mu_{i, j} \in K$ of $\phi$.
    <2>2. Thus every $v_{i, j}$ is a simultaneous eigenvector for both $\psi$ and $\phi$.
    <2>3. Since $E = \bigoplus_{i=1}^k E_{\lambda_i}(\psi)$, the union
    $$\mathcal{B} = \bigcup_{i=1}^k \mathcal{B}_i = \{v_{i, j} : 1 \le i \le k, \, 1 \le j \le d_i\}$$
    is a basis for the entire vector space $E$.
    <2>4. Hence $\mathcal{B}$ is a simultaneous eigenbasis for $\psi$ and $\phi$.

<1>4. Part (b): Matrix interpretation (Simultaneous Diagonalization).
    *Proof:*
    <2>1. Let $A, B \in M_n(K)$ be two matrices that are each similar to a diagonal matrix (i.e. diagonalizable) and commute ($A B = B A$).
    <2>2. By Part (a) applied to the endomorphisms defined by multiplication by $A$ and $B$ on $K^n$, there exists a basis $\mathcal{B} = \{v_1, \dots, v_n\}$ of $K^n$ consisting of vectors that are simultaneous eigenvectors of both $A$ and $B$.
    <2>3. Form the invertible transition matrix $P \in \operatorname{GL}_n(K)$ whose columns are the basis vectors $v_1, \dots, v_n$.
    <2>4. Then both $P^{-1} A P$ and $P^{-1} B P$ are diagonal matrices:
    $$P^{-1} A P = \operatorname{diag}(\mu_1, \dots, \mu_n), \qquad P^{-1} B P = \operatorname{diag}(\lambda_1, \dots, \lambda_n).$$
    <2>5. Thus two commuting diagonalizable matrices are simultaneously diagonalizable by the same change-of-basis matrix $P$.

<1>5. Conclusion:
    *Proof:*
    Commuting diagonalizable endomorphisms share a common eigenbasis, and commuting diagonalizable matrices are simultaneously diagonalizable.
:::
