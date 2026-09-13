---
schema: qual/card@1
id: P-BKS08-1B
kind: problem
title: Represent a linear functional by an L2 polynomial pairing
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
For \(n\ge1\), let \(P_n\) be the real vector space of polynomials of degree at most \(n\). Show that there exists \(q\in P_n\) such that for every \(p\in P_n\),
\[
\int_0^1 p(x)q(x)\,dx
=
\int_0^1 \frac{p(x)}{x^2+1}\,dx.
\]
:::
