---
schema: qual/card@1
id: P-UCLAB09S-12
kind: problem
title: Local divergence identity from flux over all balls
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Problem 12. Let $F:\mathbb R^3\to\mathbb R^3$ and $\rho:\mathbb R^3\to\mathbb R$ be smooth.
Prove that
\[
\operatorname{div}F=\rho
\]
at every point if and only if
\[
\iint_{\partial\Omega}F\cdot dS
=
\iiint_\Omega \rho\,dx\,dy\,dz
\]
for every ball $\Omega$ of every positive radius and center.
You may use the standard theorems of vector calculus without proof.
:::
