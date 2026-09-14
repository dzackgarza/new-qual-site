---
schema: qual/card@1
id: P-UCLAB05S-LA2
kind: problem
title: Annihilators, spans, and the dual of a quotient
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra Problem 2 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
Let $V$ be a finite-dimensional vector space, and let $V^*$ be its dual, the space of linear maps $\phi:V\to\mathbb C$.
For $W\subset V$, define
\[
W^\perp=\{\phi\in V^*: \phi(w)=0\text{ for every }w\in W\}.
\]
For $U\subset V^*$, define
\[
{}^\perp U=\{v\in V: \phi(v)=0\text{ for every }\phi\in U\}.
\]

(a) Show that for every subset $W\subset V$,
\[
{}^\perp(W^\perp)=\operatorname{span}(W).
\]

(b) Let $W\subset V$ be a linear subspace.
Give an explicit isomorphism between $(V/W)^*$ and $W^\perp$, and prove that it is an isomorphism.
:::
