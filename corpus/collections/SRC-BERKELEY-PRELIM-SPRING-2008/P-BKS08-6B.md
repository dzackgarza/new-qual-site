---
schema: qual/card@1
id: P-BKS08-6B
kind: problem
title: An orthogonality condition forced by a decaying ODE solution
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
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
---

::: {.problem}
Let \(y:[0,\infty)\to\mathbb R\) be smooth and satisfy
\[
y''-y=f(x)\qquad(x>0),
\]
with
\[
y(0)=y'(0)=0,
\]
and suppose \(y(x)\to0\) and \(y'(x)\to0\) as \(x\to\infty\). Here \(f\) is continuous on \([0,\infty)\) and vanishes for \(x>1\).

Find a nonzero function \(g\), independent of \(y\) and \(f\), such that
\[
\int_0^1 f(x)g(x)\,dx=0.
\]
:::
