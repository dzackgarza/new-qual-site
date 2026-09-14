---
schema: qual/card@1
id: P-BERK83SU-09
kind: problem
title: Argument principle and a boundary integral locating a simple zero
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $\Omega\subset\mathbb C$ be a bounded domain whose boundary is a smooth Jordan curve $\gamma$. Let $f$ be holomorphic on a neighborhood of $\overline\Omega$, assume $f\ne0$ on $\gamma$, and let $z_1,\ldots,z_k$ be the zeros of $f$ in $\Omega$ with multiplicities $n_1,\ldots,n_k$.

1. Using Cauchy's integral formula, prove
\[
\frac1{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}\,dz
=\sum_{j=1}^k n_j.
\]
2. If $f$ has exactly one zero $z_1$ in $\Omega$, and it is simple, find a boundary integral involving $f$ whose value is $z_1$.
:::
