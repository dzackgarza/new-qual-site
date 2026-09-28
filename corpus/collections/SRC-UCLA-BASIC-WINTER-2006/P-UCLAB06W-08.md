---
schema: qual/card@1
id: P-UCLAB06W-08
kind: problem
title: Existence and uniqueness of the adjoint of a linear map
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Qual Winter 2006 PDF.
---

::: {.problem}
Let $T:V\to W$ be a linear transformation of finite-dimensional real inner product spaces.
Show that there exists a unique linear transformation $T^t:W\to V$ such that
\[
\langle T(v),w\rangle_W=\langle v,T^t(w)\rangle_V
\]
for all $v\in V$ and $w\in W$, where $\langle\ ,\ \rangle_X$ denotes the inner product on $X=V$ or $W$.
:::
