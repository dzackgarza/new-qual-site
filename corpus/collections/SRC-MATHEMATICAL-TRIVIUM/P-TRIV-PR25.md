---
schema: qual/card@1
id: P-TRIV-PR25
kind: problem
title: Monte Carlo integration and its sample size
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 25, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost minus sign in the interval from -1 to 1 and removed stray digits against Probability Problem 25 on pages 30-31 of the source PDF.
---

::: problem
"Monte-Carlo method" Consider the function $f(x_1, \ldots, x_n)$ defined in $V = \{-1 \leqslant x_i \leqslant 1,\ i = 1, \ldots, n\}$ and bounded from below and above, $|f(x_1, \ldots, x_n)| \leqslant C$.
Define a random variable $\eta = f(\xi_1, \ldots, \xi_n)$, where $\xi_i$ are distributed uniformly between $-1$ and $1$.

(a) Show that $\mathbf{E}\eta = I$, where $I = \int_V f(x_1, \ldots, x_n)\, d^n x$.
Hence the random variables can be used to compute the high-dimensional integrals with a given precision.

(b) Consider the series of $N$ random variables $\eta_i = f(\xi_{i1}, \ldots \xi_{in})$, $i = 1, \ldots, N$ where all $\xi_{ij}$ are distributed uniformly in $[-1, 1]$.
Then the quantity $\tilde{I} = \frac{1}{N}(\eta_1 + \ldots + \eta_N)$ for large $N$ approaches $I$ with high enough probability.
Estimate how large $N$ should be to ensure that
$$
P(|\tilde{I} - I| < \Delta) \geqslant 1 - \alpha,
\tag{53}
$$
where $\Delta$ and $\alpha$ are given small numbers.
:::
