---
schema: qual/card@1
id: P-RASP13B
kind: problem
title: '$t\,\mu\{\abs{f}\geq t\}\to0$ for $f\in L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Distribution Functions
  - Chebyshev Inequality
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Spring 2013 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a measure space and $f \in L^1(\mu)$.
Prove that
$$
\lim_{t \to \infty} t \, \mu\{x \in X : \abs{f(x)} \geq t\} = 0.
$$
:::

::: {.solution}
::: {.proof}
Let
$$
E_t:=\{x\in X:\abs{f(x)}\ge t\}.
$$
On $E_t$ one has $t\le \abs{f}$, so
$$
t\,\mu(E_t)
\le \int_{E_t}\abs{f}\,d\mu.
$$

As $t\to\infty$, the indicators $\mathbf1_{E_t}$ decrease pointwise to $0$ at every point where $\abs{f(x)}<\infty$. Since $f\in L^1$, $\abs{f}<\infty$ almost everywhere, and
$$
\abs{f}\mathbf1_{E_t}\le \abs{f}\in L^1.
$$
Therefore the dominated convergence theorem gives
$$
\int_{E_t}\abs{f}\,d\mu
=\int_X \abs{f}\mathbf1_{E_t}\,d\mu
\longrightarrow0.
$$
Hence
$$
0\le t\,\mu\{\abs{f}\ge t\}
\le \int_{\{\abs{f}\ge t\}}\abs{f}\,d\mu
\longrightarrow0,
$$
and so
$$
\boxed{\lim_{t\to\infty}t\,\mu\{\abs{f}\ge t\}=0.}
$$
:::
:::
