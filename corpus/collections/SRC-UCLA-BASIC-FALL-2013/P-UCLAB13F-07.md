---
schema: qual/card@1
id: P-UCLAB13F-07
kind: problem
title: Hermite interpolation with prescribed derivatives
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained PDF defines z_j and m_j only for 1 <= j <= n but prints N+1=sum_{j=0}^n(1+m_j). This card corrects the forced indexing typo to j=1,...,n.
---

::: {.problem}
Let $z_1,\ldots,z_n$ be distinct complex numbers and let $m_j\ge0$ be integers. Write
\[
N+1=\sum_{j=1}^n(1+m_j).
\]
Prove that, given any $N+1$ complex numbers
\[
c_{j,k},\qquad 1\le j\le n,\quad 0\le k\le m_j,
\]
there is a unique polynomial $P(z)$ of degree at most $N$ such that
\[
P^{(k)}(z_j)=c_{j,k}
\]
for all $j,k$.
:::
