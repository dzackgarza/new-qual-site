---
schema: qual/card@1
id: P-UCLAB04F-08
kind: problem
title: A symmetric quadratic form and its minimum eigenvalue
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Exam Fall 2004 PDF. The source denotes the unit sphere in $\mathbb R^n$ by $S^n$; the set itself is unambiguous and is denoted simply by $S$ here.
---

::: {.problem}
Let $A=(a_{ij})$ be a real symmetric $n\times n$ matrix, and define the associated quadratic form
\[
Q(v)=v\mathbin{\cdot}Av,
\qquad v\in\mathbb R^n.
\]

(a) Show that
\[
\nabla Q(v)=2Av.
\]

(b) Let
\[
S=\{v\in\mathbb R^n:\|v\|=1\},
\]
let $M$ be the minimum value of $Q$ on $S$, and choose $u\in S$ with $Q(u)=M$.
Use Lagrange multipliers to prove that $u$ is an eigenvector of $A$ with eigenvalue $M$.
:::
