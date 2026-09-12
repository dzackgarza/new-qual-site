---
schema: qual/card@1
id: P-RASP13B
kind: problem
title: "Tail measure of an L^1 function vanishes: t times mu{|f| >= t} tends to zero"
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

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space and $f \in L^1(\mu)$.
Prove that
$$
\lim_{t \to \infty} t \, \mu\{x \in X : |f(x)| \geq t\} = 0.
$$
:::

::: solution
::: proof
Let
\[
E_t:=\{x\in X:|f(x)|\ge t\}.
\]
On $E_t$ one has $t\le |f|$, so
\[
t\,\mu(E_t)
\le \int_{E_t}|f|\,d\mu.
\]

As $t\to\infty$, the indicators $\mathbf1_{E_t}$ decrease pointwise to $0$ at every point where $|f(x)|<\infty$. Since $f\in L^1$, $|f|<\infty$ almost everywhere, and
\[
|f|\mathbf1_{E_t}\le |f|\in L^1.
\]
Therefore the dominated convergence theorem gives
\[
\int_{E_t}|f|\,d\mu
=\int_X |f|\mathbf1_{E_t}\,d\mu
\longrightarrow0.
\]
Hence
\[
0\le t\,\mu\{|f|\ge t\}
\le \int_{\{|f|\ge t\}}|f|\,d\mu
\longrightarrow0,
\]
and so
\[
\boxed{\lim_{t\to\infty}t\,\mu\{|f|\ge t\}=0.}
\]
:::
:::
