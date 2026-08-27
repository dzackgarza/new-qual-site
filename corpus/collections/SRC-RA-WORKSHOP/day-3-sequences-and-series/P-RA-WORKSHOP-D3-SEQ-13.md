---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-13
kind: problem
title: Prove the ratio test from the root test
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Convergence Tests
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Assume that Theorem 2.4 (the root test) is true and prove the ratio test (Theorem 2.5).
:::

:::: {.solution}
<1>1. Recall the root test (Theorem 2.4). Proof: if $\limsup_{n\to\infty}|a_n|^{1/n} < 1$ then $\sum a_n$ converges absolutely; if $\limsup |a_n|^{1/n} > 1$ then $\sum a_n$ diverges.
<1>2. Relate the root-test quantity to the ratio-test quantity.
Proof: for a sequence of positive numbers $c_n$, \[\liminf_{n\to\infty}\frac{c_{n+1}}{c_n} \le \liminf_{n\to\infty} c_n^{1/n} \le \limsup_{n\to\infty} c_n^{1/n} \le \limsup_{n\to\infty}\frac{c_{n+1}}{c_n}.\] The upper bound: write $q = \limsup c_{n+1}/c_n$; for $\epsilon > 0$ there is $N$ with $c_{n+1} \le (q+\epsilon)c_n$ for $n \ge N$, hence $c_n \le C(q+\epsilon)^n$, so $c_n^{1/n} \le C^{1/n}(q+\epsilon) \to q+\epsilon$.
The lower bound is analogous (or apply the upper bound to $1/c_n$). <1>3. Apply to $c_n = |a_n|$ and invoke the root test.
Proof: if $\limsup |a_{n+1}|/|a_n| = r < 1$, then by <1>2, $\limsup |a_n|^{1/n} \le r < 1$, so the root test gives absolute convergence.
If $\liminf |a_{n+1}|/|a_n| > 1$ (the ratio test's divergence hypothesis), then $\liminf |a_n|^{1/n} > 1$, so in particular $\limsup |a_n|^{1/n} > 1$ and the root test gives divergence.
<1>4. Q.E.D.
:::
