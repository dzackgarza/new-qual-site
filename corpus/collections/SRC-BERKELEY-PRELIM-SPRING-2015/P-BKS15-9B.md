---
schema: qual/card@1
id: P-BKS15-9B
kind: problem
title: Legendre's formula and the base-$p$ digit sum of $n$
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
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
---

::: {.problem}
Let $p$ be a prime.
Let $p^{a(n)}$ be the largest power of $p$ dividing $n!$, and let $b(n)$ be the sum of the digits of $n$ in base $p$.

(a) Show that
\[
a(n)=\left\lfloor\frac np\right\rfloor+\left\lfloor\frac n{p^2}\right\rfloor+\left\lfloor\frac n{p^3}\right\rfloor+\cdots.
\]

(b) Express $a(n)$ in terms of the digits $d_k$ in the base-$p$ expansion
\[
n=\sum_k d_kp^k,
\qquad 0\le d_k<p.
\]

(c) Find a nontrivial linear relation between $n$, $a(n)$, and $b(n)$, with coefficients allowed to depend on $p$ but not on $n$.
:::
