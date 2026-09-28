---
schema: qual/card@1
id: P-APAF20G
kind: problem
title: Eigenvalues of a compact-group representation have modulus one
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $R\colon G\to\mathrm{GL}(H)$ be a linear representation of a compact group $G$ on a finite-dimensional Hilbert space $H$.
Prove that, for all $g\in G$, the eigenvalues of $R(g)$ have modulus $1$.
:::

::: {.solution}
Assume, as usual for representations of compact topological groups, that $R$ is continuous.

<1>1. There is a constant $M>0$ such that
\[
\|R(h)\|_{\mathrm{op}}\le M
\qquad\text{for every }h\in G.
\]
::: {.proof}
Because $G$ is compact and $R:G\to\mathrm{GL}(H)$ is continuous, the image $R(G)$ is compact. The operator norm is continuous on the finite-dimensional space $\operatorname{End}(H)$, so it attains a finite maximum on $R(G)$.
:::

<1>2. If $R(g)v=\lambda v$ with $v\ne0$, then $|\lambda|\le1$.
::: {.proof}
For every positive integer $n$,
\[
R(g^n)v=R(g)^nv=\lambda^n v.
\]
Hence, by <1>1,
\[
|\lambda|^n\|v\|
=\|R(g^n)v\|
\le \|R(g^n)\|_{\mathrm{op}}\|v\|
\le M\|v\|.
\]
Since $v\ne0$,
\[
|\lambda|^n\le M
\]
for every $n$. If $|\lambda|>1$, the left side tends to infinity, a contradiction. Thus $|\lambda|\le1$.
:::

<1>3. In fact $|\lambda|\ge1$.
::: {.proof}
Since $R(g)$ is invertible,
\[
R(g^{-1})v=R(g)^{-1}v=\lambda^{-1}v.
\]
Applying <1>2 to the group element $g^{-1}$ and its eigenvalue $\lambda^{-1}$ gives
\[
|\lambda^{-1}|\le1,
\]
so $|\lambda|\ge1$.
:::

<1>4. Therefore every eigenvalue of every $R(g)$ has modulus $1$.
::: {.proof}
Combine <1>2 and <1>3:
\[
1\le|\lambda|\le1.
\]
Hence
\[
\boxed{|\lambda|=1}.
\]
:::
:::
