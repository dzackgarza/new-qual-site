---
schema: qual/card@1
id: P-WESRA07-II5
kind: problem
title: A dominated-convergence limit with powers of $1+x^2$
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, item 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Compute
\[
\lim_{n\to\infty}\int_0^1\frac{1+n x^2}{(1+x^2)^n}\,dx.
\]
:::

::: solution
For $x\in[0,1]$, Bernoulli's inequality gives
\[
(1+x^2)^n\ge 1+n x^2.
\]
Hence
\[
0\le \frac{1+n x^2}{(1+x^2)^n}\le1
\]
for every $n$ and every $x\in[0,1]$.

For each fixed $x>0$, the denominator grows exponentially in $n$, while the numerator grows only linearly.
More explicitly,
\[
\frac{1+n x^2}{(1+x^2)^n}\longrightarrow0.
\]
At $x=0$ the integrand equals $1$, but this single point is irrelevant for Lebesgue integration.
Thus the integrands converge almost everywhere to $0$ and are dominated by the integrable function $1$.

By the Dominated Convergence Theorem,
\[
\boxed{
\lim_{n\to\infty}\int_0^1\frac{1+n x^2}{(1+x^2)^n}\,dx=0.}
\]
:::
