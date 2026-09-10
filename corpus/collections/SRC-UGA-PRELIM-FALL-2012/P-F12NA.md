---
schema: qual/card@1
id: P-F12NA
kind: problem
title: $N(A^t A)=N(A)$
classification:
  areas:
  - prelim
  topics:
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $A$ be an $m \times n$ real matrix.
Write $A^t$ for the transpose of $A$, and $N(A)$ for the nullspace of $A$.
Prove that $N(A^t A) = N(A)$.
:::

::: solution
If $x\in N(A)$, then $Ax=0$, so $A^tAx=0$ and hence $x\in N(A^tA)$. Thus
\[
N(A)\subseteq N(A^tA).
\]
Conversely, if $A^tAx=0$, then
\[
0=x^tA^tAx=(Ax)^t(Ax)=\|Ax\|^2.
\]
Therefore $Ax=0$, so $x\in N(A)$. Hence
\[
N(A^tA)=N(A).
\]
:::
