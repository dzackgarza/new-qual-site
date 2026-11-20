---
schema: qual/card@1
id: T-HAMS1
kind: theorem
title: Ham sandwich theorem
slogan: 'One hyperplane bisects $n$ compact sets in $\RR^n$ at once.'
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
  - Fixed Points
relations: []
review: draft
---

::: {.theorem}
Let $A_1,\ldots,A_n\subseteq\RR^n$ be compact.
Then there is an affine hyperplane $P$ that divides each $A_i$ into two pieces of equal $n$-dimensional measure.
:::

::: {.proof}
Identify $\RR^n$ with the affine hyperplane $\RR^n\cross\theset{1}\subseteq\RR^{n+1}$, and write $\inner{\lambda}{(x,1)}\coloneqq\lambda_1x_1+\cdots+\lambda_nx_n+\lambda_{n+1}$ for $\lambda\in\RR^{n+1}$ and $x\in\RR^n$.
For $\lambda\in S^n$ put
$$
V_\lambda \coloneqq \theset{x\in\RR^n \st \inner{\lambda}{(x,1)}\geq 0}, \qquad
H_\lambda \coloneqq \theset{x\in\RR^n \st \inner{\lambda}{(x,1)}=0}.
$$
Then $V_\lambda\union V_{-\lambda}=\RR^n$ and $V_\lambda\intersect V_{-\lambda}=H_\lambda$.
If $\lambda_1,\ldots,\lambda_n$ are not all zero, then $H_\lambda$ is an affine hyperplane; if $\lambda=\pm e_{n+1}$, then $H_\lambda$ is empty.

For compact $A\subseteq\RR^n$ the function $\varphi_A\colon S^n\to\RR$, $\varphi_A(\lambda)\coloneqq\vol(A\intersect V_\lambda)$, is continuous.
Indeed, for a sequence $\mu_k\to\lambda$ the functions $\mathbf{1}_{V_{\mu_k}}$ converge to $\mathbf{1}_{V_\lambda}$ at every $x\notin H_\lambda$, a set of measure zero, and at every $x\in A$ when $\lambda=\pm e_{n+1}$; since $\abs{\mathbf{1}_{V_{\mu_k}}}\leq\mathbf{1}_A$ and $A$ is compact, [[T-IJQQG|dominated convergence]] gives $\varphi_A(\mu_k)\to\varphi_A(\lambda)$.

The map $g\coloneqq(\varphi_{A_1},\ldots,\varphi_{A_n})\colon S^n\to\RR^n$ is continuous, so by [[T-WNOWY|Borsuk--Ulam]] in the form [@Hat02, Corollary 2B.7] there is $\lambda\in S^n$ with $\varphi_{A_i}(\lambda)=\varphi_{A_i}(-\lambda)$ for every $i$.
Since $A_i\intersect H_\lambda$ has measure zero,
$$
\vol(A_i)=\vol(A_i\intersect V_\lambda)+\vol(A_i\intersect V_{-\lambda})=2\vol(A_i\intersect V_\lambda).
$$
If $\lambda_1,\ldots,\lambda_n$ are not all zero, then $H_\lambda$ is an affine hyperplane dividing each $A_i$ into two pieces of equal measure.
If $\lambda=\pm e_{n+1}$, then $\vol(A_i)=0$ for every $i$, and every affine hyperplane divides each $A_i$ into two pieces of equal measure.
:::
