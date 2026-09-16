---
schema: qual/card@1
id: E-SS6.EX-6
kind: problem
title: "SS 6.6: Odd harmonic partial sums approach gamma/2 + log 2"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
6. Show that

$$
1 + \frac {1}{3} + \frac {1}{5} + \dots + \frac {1}{2 n - 1} - \frac {1}{2} \log n \rightarrow \frac {\gamma}{2} + \log 2,
$$

where $\gamma$ is Euler’s constant.
:::

::: solution
Let
\[
H_n=1+\frac12+\cdots+\frac1n.
\]
The odd terms up to $2n-1$ satisfy
\[
1+\frac13+\cdots+\frac1{2n-1}
=H_{2n}-\frac12H_n.
\]
Hence
\[
1+\frac13+\cdots+\frac1{2n-1}-\frac12\log n
=H_{2n}-\frac12H_n-\frac12\log n.
\]
Using
\[
H_m=\log m+\gamma+o(1),
\]
we obtain
\[
\log(2n)+\gamma-\frac12(\log n+\gamma)-\frac12\log n+o(1)
=\log2+\frac\gamma2+o(1).
\]
Therefore
\[
\boxed{1+\frac13+\cdots+\frac1{2n-1}-\frac12\log n
\longrightarrow \frac\gamma2+\log2}.
\]
:::
