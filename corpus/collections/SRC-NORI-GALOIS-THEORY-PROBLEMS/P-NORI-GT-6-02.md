---
schema: qual/card@1
id: P-NORI-GT-6-02
kind: problem
title: The splitting algebra of a monic polynomial is free with monomial basis
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 6.2 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rejoined the split quotient formula and removed the section note that belongs to the following problems, against Problem 6.2 on p. 5 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $f(T) = T^n - a_1 T^{n-1} + \cdots + (-1)^n a_n \in A[T]$.
Let $B = A[X_1, X_2, \ldots, X_n]/(s_1 - a_1, s_2 - a_2, \ldots, s_n - a_n)$, where $s_1, s_2, \ldots, s_n$ are the elementary symmetric polynomials in $X_1, X_2, \ldots, X_n$.
Prove that $B$ is a free $A$-module with basis (as the image in $B$) of the monomials $X_1^{m_1} X_2^{m_2} \cdots X_n^{m_n}$ where all the $m_i$ are non-negative integers such that $m_i + i \leq n$ for all $i = 1, 2, \ldots, n$.

Prove this for $n = 3$.
:::
