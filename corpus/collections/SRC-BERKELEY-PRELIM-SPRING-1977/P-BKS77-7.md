---
schema: qual/card@1
id: P-BKS77-7
kind: problem
title: Vandermonde invertibility and polynomial interpolation
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Let
\[
V=\begin{pmatrix}
1&a_0&a_0^2&\cdots&a_0^n\\
1&a_1&a_1^2&\cdots&a_1^n\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&a_n&a_n^2&\cdots&a_n^n
\end{pmatrix}.
\]

1. Prove that $V$ is invertible if $a_0,\ldots,a_n$ are distinct.
2. If the $a_i$ are distinct and $b_0,\ldots,b_n\in\mathbb C$, prove that there is a unique complex polynomial $f$ of degree at most $n$ satisfying $f(a_i)=b_i$ for all $i$.
:::
