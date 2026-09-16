---
schema: qual/card@1
id: P-BERK91S-17
kind: problem
title: An $L^2$ growth bound on circles truncates the negative Laurent tail
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f$ be analytic on the punctured disk
\[
0<|z|<r_0
\]
with Laurent expansion
\[
f(z)=\sum_{n=-\infty}^{\infty}c_nz^n.
\]
Suppose there is $M>0$ such that
\[
r^4\int_0^{2\pi}|f(re^{i\theta})|^2\,d\theta<M
\qquad(0<r<r_0).
\]
Prove that
\[
c_n=0
\qquad(n<-2).
\]
:::
