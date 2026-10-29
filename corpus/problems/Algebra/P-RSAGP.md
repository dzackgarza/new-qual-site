---
schema: qual/card@1
id: P-RSAGP
kind: problem
title: Bilinear forms and orthogonal matrices
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Matrix Groups
  - Quadratic Forms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(a) What is a bilinear form on a vector space $V$ over a field $K$?

(b) When are two bilinear forms equivalent (congruent)?

(c) What is an orthogonal matrix $Q \in \operatorname{O}(n)$, and what are its special geometric and algebraic properties?
:::

::: {.solution}

Let $V$ have basis $e_1,\ldots,e_n$, and write vectors of $V$ as coordinate columns.

::: pf

::: pf-step

(a) A bilinear form on $V$ is a map $B\colon V\times V\to K$ that is linear in each argument. With Gram matrix $M=(B(e_i,e_j))_{i,j}$, it is $B(x,y)=x^TMy$.

::: pf-proof

Expanding $x=\sum_i x_ie_i$ and $y=\sum_j y_je_j$ by bilinearity gives $B(x,y)=\sum_{i,j}x_iB(e_i,e_j)y_j=x^TMy$.

:::

:::

::: pf-step

(b) Bilinear forms $B_1,B_2$ with Gram matrices $M_1,M_2$ are equivalent when $B_2(x,y)=B_1(Px,Py)$ for some $P\in\operatorname{GL}_n(K)$, that is, when $M_2=P^TM_1P$.

::: pf-proof

By step (a), $B_1(Px,Py)=x^TP^TM_1Py$, and two forms agree exactly when their Gram matrices agree. Thus equivalence of forms is congruence of their Gram matrices, not similarity.

:::

:::

::: pf-qed

(c) A real matrix $Q$ is orthogonal when $Q^TQ=I$, equivalently $Q^{-1}=Q^T$. For $x,y\in\RR^n$,
$$
\inner{Qx}{Qy}=x^TQ^TQy=\inner{x}{y},
$$
so $Q$ preserves lengths, distances, and angles, and its columns (and, since $QQ^T=I$, its rows) are orthonormal. From $(\det Q)^2=\det(Q^TQ)=1$ we get $\det Q=\pm1$. If $Qv=\lambda v$ with $v\in\CC^n$ nonzero, then $\norm{v}=\norm{Qv}=\abs{\lambda}\norm{v}$ for the Hermitian norm, since $Q$ is real with $Q^TQ=I$; hence $\abs{\lambda}=1$. Finally, for orthogonal $Q$ the congruence $Q^TAQ$ equals the similarity $Q^{-1}AQ$, which is why orthogonal diagonalization of real symmetric matrices serves both bilinear forms and linear maps.

:::

:::

:::
