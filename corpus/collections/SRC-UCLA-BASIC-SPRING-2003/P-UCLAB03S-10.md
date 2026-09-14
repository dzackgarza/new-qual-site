---
schema: qual/card@1
id: P-UCLAB03S-10
kind: problem
title: A self-adjoint operator with trace-zero square vanishes
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the official UCLA Basic Examination, May 2003 PDF. The source calls $T$ hermitian on a real inner-product space and refers to a matrix in the "standard basis" although an arbitrary inner-product space has no distinguished standard basis; the invariant content is $\operatorname{tr}(T^2)=0$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Gives a basis-independent proof using an arbitrary orthonormal basis and self-adjointness.
---

::: {.problem}
Let $V$ be a finite-dimensional real inner-product space and let $T:V\to V$ be self-adjoint.
Suppose
\[
\operatorname{tr}(T^2)=0.
\]
Prove that $T$ is the zero operator.
:::

::: {.solution}
Let $e_1,\ldots,e_n$ be any orthonormal basis of $V$.
Since $T=T^*$,
\[
\operatorname{tr}(T^2)
=\sum_{i=1}^n\langle T^2e_i,e_i\rangle
=\sum_{i=1}^n\langle Te_i,Te_i\rangle
=\sum_{i=1}^n\|Te_i\|^2.
\]
Every summand is nonnegative.
If the trace is zero, then $Te_i=0$ for every $i$.
Hence $T=0$.
:::
