---
schema: qual/card@1
id: P-BERK78S-11
kind: problem
title: Multiplying power-series coefficients by a polynomial factor preserves the radius of convergence
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
  note: The source indexes both series from n=0 and then prints |b_n|<n^2|a_n| "for all n". At n=0 that strict inequality is impossible, so the mathematically coherent intended condition is stated for n>=1, with b_0 unrestricted.
---

::: {.problem}
Suppose
\[
\sum_{n=0}^\infty a_nz^n
\]
converges for $|z|<R$, where $z,a_n\in\mathbb C$. Let $b_n\in\mathbb C$ satisfy
\[
|b_n|<n^2|a_n|
\qquad(n\ge1).
\]
Prove that
\[
\sum_{n=0}^\infty b_nz^n
\]
also converges for $|z|<R$.
:::
