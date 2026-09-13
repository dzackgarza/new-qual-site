---
schema: qual/card@1
id: P-BKS10-5A
kind: problem
title: Monotonicity for a nonlinear differential equation
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution. The packet prints y=y(t) once but then uses x consistently; this card normalizes that evident variable typo to y=y(x).
---

::: {.problem}
Let \(I=(a,b)\) be an interval containing \(1\), and let \(y=y(x)\) be a \(C^\infty\) function on \(I\) satisfying
\[
y'=2^y-\frac1x.
\]
Prove rigorously that:

(a) if \(y(1)>0\), then \(y\) is strictly increasing on \([1,b)\);

(b) the same conclusion holds if \(y(1)=0\).

The source packet prints \(y=y(t)\) in its introductory sentence but uses \(x\) throughout the differential equation and both conclusions; the statement above resolves that typographical variable mismatch.
:::
