---
schema: qual/card@1
id: E-AMD-RRYNGX7L
kind: problem
title: The cokernel of $A\in M_n(\ZZ)$ is finite of order $\abs{\det A}$ iff $\det A\neq
  0$
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Determinants
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used Smith normal form to identify both finiteness and the cokernel order.
---

::: {.exercise}
Prove that for $A\in M_n(\ZZ)$, viewed as $A:\ZZ^n\to\ZZ^n$, the cokernel is finite if and only if $\det A\ne0$, and in that case
$$
\abs{\coker A}=\abs{\det A}.
$$
:::

::: {.solution}
By Smith normal form there are $P,Q\in\GL_n(\ZZ)$ such that
$$
PAQ=\diag(d_1,\ldots,d_r,0,\ldots,0),
\qquad d_1\mid\cdots\mid d_r,
$$
with each $d_i>0$. Since $P$ and $Q$ are automorphisms of $\ZZ^n$, they do not change the cokernel up to isomorphism. Therefore
$$
\coker A
\cong
\bigoplus_{i=1}^r\ZZ/d_i\ZZ\oplus\ZZ^{\,n-r}.
$$

This group is finite exactly when $r=n$, equivalently when $A$ has full rank over $\QQ$, equivalently when $\det A\ne0$.

In the full-rank case,
$$
\abs{\coker A}=\prod_{i=1}^n d_i.
$$
Also
$$
\abs{\det A}=\abs{\det(PAQ)}=\prod_{i=1}^n d_i,
$$
because $P,Q$ are unimodular. Hence
$$
\abs{\coker A}=\abs{\det A}.
$$
:::
