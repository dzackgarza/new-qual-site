---
schema: qual/card@1
id: P-CHAVAN-CA-1-2
kind: problem
title: Maximum modulus for polynomials from circular mean squares
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1.2 in the deterministic extraction; f/p and z/z_0 inconsistencies are normalized to the polynomial and center defined by the problem.
---

::: {.problem}
Let $p(z)=a_0+a_1z+\cdots+a_nz^n$ and suppose $z_0\in\mathbb C$, $|z_0|<1$, is such that
\[
|p(z)|\le |p(z_0)|\qquad(|z|\le1).
\]
Write
\[
p(z)=b_0+b_1(z-z_0)+\cdots+b_n(z-z_0)^n.
\]
For $0<r<1-|z_0|$, verify
\[
\frac1{2\pi}\int_{-\pi}^{\pi}|p(z_0+re^{i\theta})|^2\,d\theta
=|b_0|^2+|b_1|^2r^2+\cdots+|b_n|^2r^{2n},
\]
and
\[
\frac1{2\pi}\int_{-\pi}^{\pi}|p(z_0+re^{i\theta})|^2\,d\theta\le |b_0|^2.
\]
Conclude that a nonconstant polynomial cannot attain its maximum modulus in the open unit disk, and hence
\[
\max_{|z|\le1}|p(z)|=\max_{|z|=1}|p(z)|.
\]
:::
