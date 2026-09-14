---
schema: qual/card@1
id: P-UCLAB03F-05
kind: problem
title: A second-order Taylor polynomial with cubic remainder in two variables
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
Let $f:\mathbb R^2\to\mathbb R$ have continuous partial derivatives of order $3$.
Write down explicitly, in terms of partial derivatives of $f$, a quadratic polynomial $P(x,y)$ such that
\[
|f(x,y)-P(x,y)|
\leq C(x^2+y^2)^{3/2}
\]
for all $(x,y)$ in some sufficiently small neighborhood of $(0,0)$, where $C$ may depend on $f$ but not on $x$ or $y$.
Then prove this estimate.
:::
