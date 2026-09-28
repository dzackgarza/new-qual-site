---
schema: qual/card@1
id: P-UCLAB01F-05
kind: problem
title: Equality of mixed partial derivatives under continuity hypotheses
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Suppose $f:\mathbb R^2\to\mathbb R$ is continuous, the first partial derivatives
\[
\frac{\partial f}{\partial x},\qquad \frac{\partial f}{\partial y}
\]
exist everywhere and are continuous everywhere, and the mixed partials
\[
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right),
\qquad
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)
\]
also exist everywhere and are continuous everywhere.
Prove that
\[
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)
=
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)
\]
at every point of $\mathbb R^2$.
:::
