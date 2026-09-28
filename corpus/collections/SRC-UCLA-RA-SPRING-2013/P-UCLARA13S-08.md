---
schema: qual/card@1
id: P-UCLARA13S-08
kind: problem
title: Three-lines interpolation for positive definite matrices
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $A$ and $B$ be positive-definite real symmetric $n\times n$ matrices such that
\[
\|BA^{-1}x\|\le \|x\|\qquad\text{for every }x\in\mathbb R^n.
\]

(a) For $x,y\in\mathbb R^n$, show that
\[
z\longmapsto \langle y,B^zA^{-z}x\rangle
\]
admits an analytic continuation from $0<z<1$ to the whole complex plane.

(b) Show that
\[
\|B^\theta A^{-\theta}x\|\le \|x\|
\]
for every $0\le\theta\le1$ and every $x\in\mathbb R^n$.
:::
