---
schema: qual/card@1
id: P-RASP22E
kind: problem
title: "L^q subset of L^p implies finite measure"
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
  date: 2026-09-09
  note: Checked against Problem 5 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $X \subseteq \mathbb{R}$ be a Borel set, let $\mu$ be the restriction of Lebesgue measure to $X$, and let $1 \leq p < q < \infty$.
Assume that $L^q(X, \mu) \subseteq L^p(X, \mu)$ and let $T : L^q(X, \mu) \to L^p(X, \mu)$ be the inclusion map.
Prove that $T$ is bounded and that $\mu(X) < \infty$.
:::


::: solution
<1>1. Prove that the inclusion map has closed graph.
::: proof
Let $f_n\in L^q(X)$ satisfy
\[
f_n\to f\quad\text{in }L^q(X)
\]
and
\[
Tf_n=f_n\to g\quad\text{in }L^p(X).
\]
From the $L^q$ convergence, choose a subsequence $f_{n_k}$ converging to $f$ almost everywhere. From that subsequence, choose a further subsequence converging to $g$ almost everywhere by the $L^p$ convergence. Hence $f=g$ almost everywhere. Thus the graph of
\[
T:L^q(X)\to L^p(X)
\]
is closed.

Both spaces are Banach, so the Closed Graph Theorem gives a constant $C<\infty$ such that
\[
\boxed{\|f\|_p\le C\|f\|_q\qquad(f\in L^q(X)).}
\]
Thus $T$ is bounded.
:::

<1>2. Apply the bound to characteristic functions.
::: proof
Let $E\subseteq X$ be measurable with $0<\mu(E)<\infty$. Then $\mathbf1_E\in L^q(X)$, so
\[
\mu(E)^{1/p}
=\|\mathbf1_E\|_p
\le C\|\mathbf1_E\|_q
=C\mu(E)^{1/q}.
\]
Therefore
\[
\mu(E)^{1/p-1/q}\le C.
\]
Since
\[
\frac1p-\frac1q=\frac{q-p}{pq}>0,
\]
we obtain the uniform bound
\[
\mu(E)\le C^{pq/(q-p)}.
\]
:::

<1>3. Exhaust $X$ by finite-measure sets.
::: proof
Set
\[
E_n:=X\cap[-n,n].
\]
Each $E_n$ has finite Lebesgue measure, and $E_n\uparrow X$. By Step 2,
\[
\mu(E_n)\le C^{pq/(q-p)}
\]
for every $n$. Continuity from below gives
\[
\mu(X)
=\lim_{n\to\infty}\mu(E_n)
\le C^{pq/(q-p)}<\infty.
\]
Hence
\[
\boxed{\mu(X)<\infty.}
\]
:::
:::
