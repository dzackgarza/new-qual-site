---
schema: qual/card@1
id: P-BKF82-5
kind: problem
title: Moment convergence implies convergence against continuous functions
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let $\varphi_n\ge0$ be continuous on $[0,1]$ and suppose
\[
\lim_{n\to\infty}\int_0^1x^k\varphi_n(x)\,dx
\]
exists for every $k\ge0$. Show that
\[
\lim_{n\to\infty}\int_0^1f(x)\varphi_n(x)\,dx
\]
exists for every continuous $f$ on $[0,1]$.
:::
