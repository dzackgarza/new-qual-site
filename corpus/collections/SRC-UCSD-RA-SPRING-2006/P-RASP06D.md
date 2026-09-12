---
schema: qual/card@1
id: P-RASP06D
kind: problem
title: "Convergence of integrals via dominated convergence with variable dominator"
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
  note: Checked against Problem 4 of the official UCSD Spring 2006 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\{f_j\}$ be a sequence of real-valued functions in $L^1(X, \mu)$ such that $f_j \to f$ a.e. with $f \in L^1(X, \mu)$.
Suppose $\{g_j\}$ is a sequence of functions in $L^1(X, \mu)$ such that $|f_j| \leq g_j$, $g_j \to g$ a.e. for some $g \in L^1(X, \mu)$, and also $g_j \to g$ in $L^1$.
Prove that
$$
\int_X f\,d\mu = \lim_{j \to \infty} \int_X f_j\,d\mu.
$$
:::

::: solution
<1>1. Pass the pointwise domination to the limit.
::: proof
Outside a null set, we have simultaneously
\[
f_j(x)\to f(x),
\qquad
g_j(x)\to g(x),
\qquad
|f_j(x)|\le g_j(x).
\]
Taking limits gives
\[
|f(x)|\le g(x)
\]
almost everywhere. In particular $g\ge0$ almost everywhere.
:::

<1>2. Use Fatou's lemma to prove $L^1$ convergence.
::: proof
Define
\[
h_j:=g_j+g-|f_j-f|.
\]
By the triangle inequality and Step 1,
\[
|f_j-f|\le |f_j|+|f|\le g_j+g,
\]
so $h_j\ge0$. Moreover,
\[
h_j(x)\longrightarrow 2g(x)
\]
almost everywhere.

Fatou's lemma therefore gives
\[
2\int_X g\,d\mu
\le
\liminf_{j\to\infty}
\left(
\int_X g_j\,d\mu+
\int_X g\,d\mu-
\int_X|f_j-f|\,d\mu
\right).
\]
Since $g_j\to g$ in $L^1$,
\[
\int_X g_j\,d\mu\longrightarrow\int_X g\,d\mu.
\]
Hence
\[
2\int g
\le
2\int g-\limsup_j\|f_j-f\|_1.
\]
Thus
\[
\limsup_j\|f_j-f\|_1\le0,
\]
and consequently
\[
\boxed{\|f_j-f\|_1\to0.}
\]
:::

<1>3. Conclude convergence of the integrals.
::: proof
Finally,
\[
\left|\int_X f_j\,d\mu-\int_X f\,d\mu\right|
\le \|f_j-f\|_1\longrightarrow0.
\]
Therefore
\[
\boxed{\int_X f\,d\mu=\lim_{j\to\infty}\int_X f_j\,d\mu.}
\]
:::
:::
