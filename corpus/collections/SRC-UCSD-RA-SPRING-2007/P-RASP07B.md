---
schema: qual/card@1
id: P-RASP07B
kind: problem
title: "Convergence of integrals under a.e. convergence and integral convergence of dominator"
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
  note: Checked against Problem 2 of the official UCSD Spring 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Prove that if $f_n, g_n, f, g \in L^1(X, \mu)$ with $f_n \to f$ a.e., $g_n \to g$ a.e., $|f_n| \leq g_n$ and $\int g_n \to \int g$, then $\int f_n \to \int f$.

Hint: The proof is similar to that of the Dominated Convergence Theorem.
Be sure to justify all your steps.
:::

::: solution
<1>1. Pass the domination to the limit.
::: proof
Outside a null set,
\[
f_n(x)\to f(x),
\qquad
g_n(x)\to g(x),
\qquad
|f_n(x)|\le g_n(x).
\]
Hence
\[
|f(x)|\le g(x)
\]
almost everywhere. In particular, $g_n\ge0$ and $g\ge0$ almost everywhere.
:::

<1>2. Apply Fatou to a nonnegative remainder.
::: proof
Define
\[
h_n:=g_n+g-|f_n-f|.
\]
By the triangle inequality and Step 1,
\[
|f_n-f|
\le |f_n|+|f|
\le g_n+g,
\]
so $h_n\ge0$. Moreover,
\[
h_n(x)\to2g(x)
\]
almost everywhere.

Fatou's lemma yields
\[
2\int_X g\,d\mu
\le
\liminf_n
\left(
\int_X g_n\,d\mu+
\int_X g\,d\mu-
\int_X|f_n-f|\,d\mu
\right).
\]
Using the hypothesis
\[
\int_Xg_n\,d\mu\to\int_Xg\,d\mu,
\]
we obtain
\[
\limsup_n\|f_n-f\|_1\le0.
\]
Therefore
\[
\|f_n-f\|_1\to0.
\]
:::

<1>3. Conclude convergence of the integrals.
::: proof
Finally,
\[
\left|\int_Xf_n\,d\mu-\int_Xf\,d\mu\right|
\le\|f_n-f\|_1\longrightarrow0.
\]
Thus
\[
\boxed{\int_X f_n\,d\mu\longrightarrow\int_X f\,d\mu.}
\]
:::
:::
