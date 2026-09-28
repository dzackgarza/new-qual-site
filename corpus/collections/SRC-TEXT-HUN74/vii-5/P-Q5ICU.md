---
schema: qual/card@1
id: P-Q5ICU
kind: problem
title: Commuting diagonalizable endomorphisms are simultaneously diagonalizable
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

::: {.problem}
(a) Let $\phi, \psi$ be commuting endomorphisms of a finite-dimensional vector space $E$ over a field $K$ (so $\phi \psi = \psi \phi$). Show that if both $\phi$ and $\psi$ are diagonalizable (i.e. $E$ has a basis of eigenvectors for $\psi$ and a basis of eigenvectors for $\phi$), then $E$ has a basis consisting of simultaneous eigenvectors for both $\psi$ and $\phi$.

(b) Interpret the previous statement in terms of matrices similar to a diagonal matrix.
:::

::: {.solution}
Let $\lambda_1, \ldots, \lambda_k \in K$ be the distinct eigenvalues of $\psi$ and $E_{\lambda_i}(\psi) = \{v \in E : \psi(v) = \lambda_i v\}$. Since $\psi$ is diagonalizable, $E = \bigoplus_{i=1}^k E_{\lambda_i}(\psi)$.

<1>1. (a) $E$ has a basis of simultaneous eigenvectors of $\phi$ and $\psi$.

<2>1. Each $E_{\lambda_i}(\psi)$ is $\phi$-invariant.

::: {.proof}
For $v \in E_{\lambda_i}(\psi)$, $\psi(\phi(v)) = \phi(\psi(v)) = \lambda_i \phi(v)$.
:::

<2>2. The restriction $\phi_i=\phi|_{E_{\lambda_i}(\psi)}$ is diagonalizable.

::: {.proof}
An endomorphism of a finite-dimensional space is diagonalizable if and only if its minimal polynomial is a product of distinct linear factors. The minimal polynomial of $\phi$ has this form, and the minimal polynomial of $\phi_i$ divides it, so it has this form as well.
:::

<2>3. Q.E.D.

::: {.proof}
By step <2>2, each $E_{\lambda_i}(\psi)$ has a basis $\mathcal{B}_i$ of eigenvectors of $\phi$; each vector of $\mathcal B_i$ is also a $\lambda_i$-eigenvector of $\psi$. Since $E = \bigoplus_i E_{\lambda_i}(\psi)$, the union $\bigcup_i \mathcal{B}_i$ is a basis of $E$ consisting of simultaneous eigenvectors.
:::

<1>2. (b) If $A, B \in M_n(K)$ commute and are each similar to a diagonal matrix, then there is $P \in \operatorname{GL}_n(K)$ with $P^{-1} A P$ and $P^{-1} B P$ both diagonal.

::: {.proof}
Apply step <1>1 to the endomorphisms $x\mapsto Ax$ and $x\mapsto Bx$ of $K^n$ to obtain a basis $v_1, \ldots, v_n$ of simultaneous eigenvectors, $Av_j=\mu_jv_j$ and $Bv_j=\lambda_jv_j$. The matrix $P$ with columns $v_1, \ldots, v_n$ is invertible, and $P^{-1} A P = \operatorname{diag}(\mu_1, \ldots, \mu_n)$, $P^{-1} B P = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$.
:::
:::
