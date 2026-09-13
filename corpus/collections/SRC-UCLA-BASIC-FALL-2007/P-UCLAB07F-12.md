---
schema: qual/card@1
id: P-UCLAB07F-12
kind: problem
title: Evaluation functionals and interpolatory quadrature
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Let $x_0<x_1<\cdots<x_n$ be points in $[a,b]$, and let $\mathbb P^n$ be the vector space of polynomials of degree at most $n$. Define $l_j:\mathbb P^n\to\mathbb R$ by $l_j(p)=p(x_j)$.

(a) Show that $\{l_j\}_{j=0}^n$ is linearly independent.

(b) Show that there are unique coefficients $c_j$ such that
\[\int_a^b p(x)\,dx=\sum_{j=0}^n c_jl_j(p)\]
for every $p\in\mathbb P^n$.
:::
