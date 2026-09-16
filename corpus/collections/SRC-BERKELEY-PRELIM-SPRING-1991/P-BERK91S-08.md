---
schema: qual/card@1
id: P-BERK91S-08
kind: problem
title: Rank and simple spectrum of an irreducible symmetric tridiagonal matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $T$ be a real symmetric tridiagonal $n\times n$ matrix with diagonal entries $a_1,\dots,a_n$ and nonzero off-diagonal entries $b_1,\dots,b_{n-1}$:
\[
T=\begin{pmatrix}
a_1&b_1&&&0\\
b_1&a_2&b_2&&\\
&b_2&a_3&\ddots&\\
&&\ddots&\ddots&b_{n-1}\\
0&&&b_{n-1}&a_n
\end{pmatrix}.
\]
Prove that

1. $\operatorname{rank}T\ge n-1$;
2. $T$ has $n$ distinct eigenvalues.
:::
