---
schema: qual/card@1
id: PR-5A2W4
kind: proposition
title: Computing the Jordan canonical form and a change of basis via Jordan chains
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and $A \in \Mat_{n\times n}(k)$, and suppose that the [[D-QFYAC|characteristic polynomial]] factors as $\chi_A(x) = \pm\prod_{i=1}^r (x-\lambda_i)^{m_i}$ with $\lambda_1, \ldots, \lambda_r \in k$ distinct.
For each $i$, put $N_i \coloneqq A - \lambda_i I$.
The following procedure produces $P \in \GL_n(k)$ such that $P\inv A P = \JCF(A)$ is a Jordan canonical form of $A$.

(1) Let $\ell_i$ be the least integer $\ell \geq 1$ with $\rank N_i^{\ell} = \rank N_i^{\ell+1}$. Then
$$
n = \rank N_i^0 > \rank N_i > \cdots > \rank N_i^{\ell_i} = \rank N_i^{\ell_i+1} = \rank N_i^{\ell_i+2} = \cdots,
$$
$\dim_k \ker N_i^{\ell_i} = m_i$, and $\ell_i$ is the size of the largest Jordan block with eigenvalue $\lambda_i$.

(2) The eigenspace $E_{\lambda_i} = \ker N_i$ has dimension $n - \rank N_i$, the number of Jordan blocks with eigenvalue $\lambda_i$.
For $0 \leq j \leq \ell_i$, put $K_{i,j} \coloneqq \ker N_i \cap \im N_i^{j}$, so that
$$
\ker N_i = K_{i,0} \supseteq K_{i,1} \supseteq \cdots \supseteq K_{i,\ell_i} = 0
\quad\text{and}\quad
\dim_k K_{i,j} = \rank N_i^{j} - \rank N_i^{j+1}.
$$

(3) Choose a basis of $K_{i,\ell_i - 1}$ and extend it successively to bases of $K_{i,\ell_i-2}, \ldots, K_{i,0}$.
Each basis vector $v$ chosen at the stage of $K_{i,s-1}$ is an eigenvector lying in $\im N_i^{s-1}$.

(4) For each such $v$, solve $N_i^{s-1} w = v$, for instance by row reducing the augmented matrix $[\,N_i^{s-1} \mid v\,]$; the system is consistent because $v \in \im N_i^{s-1}$.
The Jordan chain of $v$ is $N_i^{s-1}w = v,\ N_i^{s-2}w,\ \ldots,\ N_i w,\ w$.

(5) Let $P$ be the matrix whose columns are the Jordan chains of all the vectors chosen in step (3), for all $i$, each chain listed consecutively in the order of step (4).
A chain of length $s$ for $\lambda_i$ contributes a Jordan block of size $s$ with eigenvalue $\lambda_i$ to $P\inv A P$.
:::
