---
schema: qual/card@1
id: P-UCLARA11F-06
kind: problem
title: Upper semicontinuity of measure under weak-star convergence
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
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $(X,d)$ be a compact metric space.
Let $(\mu_n)$ be positive Borel measures on $X$ converging weak-* to a finite positive Borel measure $\mu$, meaning
\[
\int_X f\,d\mu_n\to\int_X f\,d\mu
\qquad\text{for every }f\in C(X).
\]
Show that
\[
\mu(K)\ge \limsup_{n\to\infty}\mu_n(K)
\]
for every compact set $K\subseteq X$.
:::
