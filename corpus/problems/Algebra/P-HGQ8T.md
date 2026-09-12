---
schema: qual/card@1
id: P-HGQ8T
kind: problem
title: For symmetric $A,B$, the product $AB$ is symmetric iff $AB=BA$; $BB^t$ and
  $B+B^t$ are symmetric
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Bilinear Forms
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

::: problem
Let $A, B \in M_n(R)$ be $n \times n$ matrices over a commutative ring $R$.
(1) Prove that if $A$ and $B$ are symmetric matrices ($A^t = A, B^t = B$), then the product $AB$ is symmetric if and only if $A$ and $B$ commute ($AB = BA$). (2) For an arbitrary matrix $B \in M_n(R)$, prove that $B B^t$ and $B + B^t$ are symmetric, and $B - B^t$ is skew-symmetric.
:::

::: solution
Assume first that $A^t=A$ and $B^t=B$. Then
\[
(AB)^t=B^tA^t=BA.
\]
Therefore
\[
AB\text{ is symmetric}
\iff (AB)^t=AB
\iff BA=AB.
\]
This proves part (1).

For arbitrary $B$,
\[
(BB^t)^t=(B^t)^tB^t=BB^t,
\]
so $BB^t$ is symmetric. Also
\[
(B+B^t)^t=B^t+B=B+B^t,
\]
while
\[
(B-B^t)^t=B^t-B=-(B-B^t).
\]
Thus $B+B^t$ is symmetric and $B-B^t$ is skew-symmetric.
:::
