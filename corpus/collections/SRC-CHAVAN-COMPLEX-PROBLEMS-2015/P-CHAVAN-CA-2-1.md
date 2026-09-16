---
schema: qual/card@1
id: P-CHAVAN-CA-2-1
kind: problem
title: Fundamental theorem of algebra from a minimum-modulus estimate
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $f:\mathbb C\to\mathbb C$ be entire and nowhere zero.
For $r>0$:

1. Show that, with the circle $|z|=r$ traversed counterclockwise,
   \[
   \int_{|z|=r}\frac{dz}{zf(z)}=\frac{2\pi i}{f(0)}.
   \]

2. Show that
   \[
   \left|\int_{|z|=r}\frac{dz}{zf(z)}\right|
   \le \frac{2\pi}{\min_{|z|=r}|f(z)|},
   \]
   and hence
   \[
   \min_{|z|=r}|f(z)|\le |f(0)|.
   \]

Deduce the fundamental theorem of algebra by applying this to a monic polynomial and verifying
\[
|a_0+a_1z+\cdots+a_{n-1}z^{n-1}+z^n|
\ge |z|^n\left(1-\frac{|a_{n-1}|}{|z|}-\cdots-\frac{|a_0|}{|z|^n}\right).
\]
:::
