---
schema: qual/card@1
id: P-RAF09B
kind: problem
title: "Dominated convergence implies convergence in measure"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2009 real-analysis qualifying exam.
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Assume that $f_n$ is a sequence of measurable functions on $(X, \mathcal{M}, \mu)$.
Assume that there exists an integrable function $F$ such that $|f_n| \leq F$ $\mu$-a.e., and $f_n \to f$ $\mu$-a.e. Show that $f_n \to f$ in measure.
:::

::: solution
<1>1. The limit is also dominated by $F$.
::: proof
Since $f_n\to f$ almost everywhere and $|f_n|\le F$ almost everywhere for every $n$, passage to the pointwise limit gives
\[
|f|\le F
\]
almost everywhere. Consequently
\[
|f_n-f|\le |f_n|+|f|\le 2F
\]
almost everywhere.
:::

<1>2. Apply dominated convergence in $L^1$.
::: proof
We have $|f_n-f|\to0$ almost everywhere and
\[
|f_n-f|\le2F\in L^1(\mu).
\]
Therefore the Dominated Convergence Theorem yields
\[
\int_X |f_n-f|\,d\mu\longrightarrow0.
\]
Thus $f_n\to f$ in $L^1$.
:::

<1>3. Deduce convergence in measure.
::: proof
Fix $\varepsilon>0$. By Chebyshev's inequality,
\[
\mu\bigl(\{|f_n-f|>\varepsilon\}\bigr)
\le \frac1\varepsilon\int_X|f_n-f|\,d\mu.
\]
The right-hand side tends to $0$ by Step 2. Hence
\[
\boxed{f_n\to f\text{ in measure}.}
\]
:::
:::
