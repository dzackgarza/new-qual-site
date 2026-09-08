---
schema: qual/card@1
id: P-RASP09C
kind: problem
title: "Measure convergence with L^p domination implies L^p convergence"
classification:
  areas:
  - real-analysis
  topics:
  - Convergence in Measure
  - Lp Spaces
  - Dominated Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Spring 2009 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Assume that $1 \leq p < \infty$ and $(X, \mathcal{M}, \mu)$ is a measure space.
If $f_n \to f$ in measure and $|f_n| \leq g \in L^p(X, d\mu)$ for all $n$, then $f_n \to f$ in $L^p$-norm.
:::


::: solution
<1>1. Show that the limit is also dominated by $g$.
::: proof
Since $f_n\to f$ in measure, there is a subsequence $(f_{n_k})$ such that
\[
f_{n_k}(x)\to f(x)
\]
for almost every $x$. Since $|f_{n_k}|\le g$ for every $k$, passage to the pointwise limit gives
\[
|f(x)|\le g(x)
\]
for almost every $x$. Therefore $f\in L^p(X,\mu)$.
:::

<1>2. Every subsequence has an $L^p$-convergent further subsequence.
::: proof
Let $(f_{n_k})$ be any subsequence. It still converges to $f$ in measure, so it has a further subsequence $(f_{n_{k_j}})$ converging to $f$ almost everywhere.

For this further subsequence,
\[
|f_{n_{k_j}}-f|^p
\le (|f_{n_{k_j}}|+|f|)^p
\le (2g)^p.
\]
Because $g\in L^p$, the function $(2g)^p$ is integrable. Hence the Dominated Convergence Theorem yields
\[
\int_X|f_{n_{k_j}}-f|^p\,d\mu\longrightarrow0,
\]
that is,
\[
\|f_{n_{k_j}}-f\|_p\longrightarrow0.
\]
:::

<1>3. Deduce convergence of the full sequence.
::: proof
Suppose, toward a contradiction, that $f_n$ does not converge to $f$ in $L^p$. Then there are $\varepsilon>0$ and a subsequence $(f_{n_k})$ such that
\[
\|f_{n_k}-f\|_p\ge\varepsilon
\]
for every $k$.

By Step 2, this subsequence has a further subsequence converging to $f$ in $L^p$, contradicting the displayed lower bound. Therefore
\[
\boxed{\|f_n-f\|_p\longrightarrow0.}
\]
:::
:::
