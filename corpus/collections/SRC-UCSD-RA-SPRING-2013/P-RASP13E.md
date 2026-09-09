---
schema: qual/card@1
id: P-RASP13E
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
  note: Checked against Problem 5 of the official UCSD Spring 2013 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space.
Assume that $f : X \to \mathbb{R}$ and $f_n : X \to \mathbb{R}$ ($n = 1, 2, \ldots$) are all $\mu$-measurable and that $f_n \to f$ in measure.
Let $p$ be a real number such that $1 \leq p < \infty$.
Assume there exists $g \in L^p(\mu)$ such that $|f_n| \leq g$ on $X$ for all $n \geq 1$.
Prove that all $f$ and $f_n$ ($n = 1, 2, \ldots$) are in $L^p(\mu)$ and that $f_n \to f$ in the $L^p(\mu)$-norm.
:::

::: solution
<1>1. Each $f_n$ belongs to $L^p$, and $f$ is dominated by $g$ almost everywhere.
::: proof
Since $|f_n|\le g$ and $g\in L^p$,
\[
\|f_n\|_p^p\le\|g\|_p^p<\infty,
\]
so every $f_n\in L^p$.

Because $f_n\to f$ in measure, there exists a subsequence $(f_{n_k})$ converging to $f$ almost everywhere. Passing to the pointwise limit in
\[
|f_{n_k}|\le g
\]
gives
\[
|f|\le g
\]
almost everywhere. Hence $f\in L^p$ as well.
:::

<1>2. Every subsequence has a further subsequence converging to $f$ in $L^p$.
::: proof
Let $(f_{n_k})$ be any subsequence. It still converges to $f$ in measure, so there is a further subsequence $(f_{n_{k_j}})$ with
\[
f_{n_{k_j}}(x)\to f(x)
\]
for almost every $x$.

Moreover,
\[
|f_{n_{k_j}}-f|^p
\le (|f_{n_{k_j}}|+|f|)^p
\le (2g)^p,
\]
and $(2g)^p\in L^1$. Dominated convergence therefore gives
\[
\|f_{n_{k_j}}-f\|_p^p
=\int_X|f_{n_{k_j}}-f|^p\,d\mu
\longrightarrow0.
\]
Thus every subsequence has a further subsequence converging to $f$ in $L^p$.
:::

<1>3. Conclude convergence of the full sequence.
::: proof
Suppose, toward a contradiction, that
\[
\|f_n-f\|_p\not\to0.
\]
Then there are $\varepsilon>0$ and a subsequence $(f_{n_k})$ such that
\[
\|f_{n_k}-f\|_p\ge\varepsilon
\]
for every $k$. By Step 2, this subsequence has a further subsequence converging to $f$ in $L^p$, contradicting the uniform lower bound $\varepsilon$.

Hence
\[
\boxed{\|f_n-f\|_p\to0.}
\]
:::
:::
