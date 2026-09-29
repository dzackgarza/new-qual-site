---
schema: qual/card@1
id: P-UCLAB08S-12
kind: problem
title: Spectral theorem from the maximum Rayleigh quotient
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $A=(a_{ij})$ be a real symmetric $n\times n$ matrix and let
\[
S=\{x\in\mathbb R^n:\|x\|=1\}.
\]
Choose $x\in S$ such that
\[
(Ax,x)=\sup_{y\in S}(Ay,y),
\]
which exists by compactness.

(a) Prove that $(x,y)=0$ implies $(Ax,y)=0$.
Hint: expand $(A(x+\varepsilon y),x+\varepsilon y)$.

(b) Use part (a) to prove that $x$ is an eigenvector of $A$.

(c) Use induction to prove that $\mathbb R^n$ has an orthonormal basis of eigenvectors for $A$.
If you use part (c) in proving an earlier part, give a proof of part (c) that does not depend on those earlier parts.
:::
