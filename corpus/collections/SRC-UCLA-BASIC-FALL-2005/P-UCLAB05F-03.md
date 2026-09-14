---
schema: qual/card@1
id: P-UCLAB05F-03
kind: problem
title: Uniform convergence and convergence of square integrals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
(a) Let $f_j:[0,1]\to\mathbb R$ be continuous functions converging uniformly on $[0,1]$ to a continuous function $F:[0,1]\to\mathbb R$.
Prove that
\[
\int_0^1F(x)^2\,dx
=
\lim_{j\to\infty}\int_0^1f_j(x)^2\,dx.
\]

(b) Give a sequence of continuous functions $f_j:[0,1]\to\mathbb R$ converging pointwise to a continuous function $F:[0,1]\to\mathbb R$ such that
\[
\lim_{j\to\infty}\int_0^1f_j(x)^2\,dx
\]
exists but is not equal to
\[
\int_0^1F(x)^2\,dx.
\]
:::
