---
schema: qual/card@1
id: P-APAS11B
kind: problem
title: Twisting irreducible characters by linear characters, and conjugate-partition signs
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Symmetric Functions
relations: []
review: draft
---

::: problem
As on the exam: if $\lambda=(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_k)$ is a partition of $n$, let $A^\lambda$ denote the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$.

(d) Prove that if $\lambda(x)$ is a linear character of a finite group $G$, then for any irreducible character $\chi$ of $G$, the function $\chi^*$ defined by $\chi^*(\sigma)=\lambda(\sigma)\chi(\sigma)$ for all $\sigma\in G$ is also an irreducible character of $G$.

(b) Given a partition $\lambda$ of $n$, let $\ell(\lambda)$ denote the number of parts of $\lambda$ and $\lambda'$ denote its conjugate partition.
Let $\chi^\lambda_\mu$ denote the value of the character of the irreducible representation $A^\lambda$ of $S_n$ at the conjugacy class indexed by the partition $\mu$.
Show that
\[
\chi^{\lambda'}_\mu=(-1)^{n-\ell(\mu)}\chi^\lambda_\mu.
\]
:::

::: solution
For the first assertion, let $\rho:G\to \operatorname{GL}(V)$ be an irreducible representation with character $\chi$, and let $\lambda:G\to\mathbb C^\times$ be the one-dimensional representation corresponding to the linear character $\lambda$. Define
\[
\rho^*(g)=\lambda(g)\rho(g).
\]
Then $\rho^*$ is a representation and its character is
\[
\chi_{\rho^*}(g)=\lambda(g)\chi(g)=\chi^*(g).
\]
A subspace $W\subseteq V$ is $\rho^*$-stable if and only if it is $\rho$-stable, because multiplication by the nonzero scalar $\lambda(g)$ does not change the image subspace. Since $\rho$ is irreducible, $\rho^*$ is irreducible. Hence $\chi^*$ is irreducible.

For the second assertion, take the linear character to be the sign character $\operatorname{sgn}$ of $S_n$. It is standard that tensoring a Specht module with the sign representation conjugates the indexing partition:
\[
A^{\lambda'}\cong A^\lambda\otimes \operatorname{sgn}.
\]
For completeness, this follows under the Frobenius characteristic map from the involution $\omega$ on symmetric functions, characterized by
\[
\omega(s_\lambda)=s_{\lambda'},\qquad \omega(p_r)=(-1)^{r-1}p_r.
\]
Tensoring a character by $\operatorname{sgn}$ corresponds to applying $\omega$ to its Frobenius characteristic.

Now let $\sigma\in S_n$ have cycle type $\mu=(\mu_1,\ldots,\mu_{\ell(\mu)})$. A cycle of length $r$ has sign $(-1)^{r-1}$, so
\[
\operatorname{sgn}(\sigma)
 =\prod_{i=1}^{\ell(\mu)}(-1)^{\mu_i-1}
 =(-1)^{\sum_i\mu_i-\ell(\mu)}
 =(-1)^{n-\ell(\mu)}.
\]
Therefore
\[
\chi^{\lambda'}(\sigma)
 =\operatorname{sgn}(\sigma)\chi^\lambda(\sigma)
 =(-1)^{n-\ell(\mu)}\chi^\lambda(\sigma).
\]
Since character values are constant on conjugacy classes, this is exactly
\[
\chi^{\lambda'}_\mu=(-1)^{n-\ell(\mu)}\chi^\lambda_\mu.
\]
:::
