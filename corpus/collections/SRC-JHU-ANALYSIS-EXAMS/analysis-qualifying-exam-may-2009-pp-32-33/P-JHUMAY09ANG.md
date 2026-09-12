---
schema: qual/card@1
id: P-JHUMAY09ANG
kind: problem
title: '$L^p$ convergence implies convergence in measure on the unit interval'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, May 2009, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $1\le p<\infty$ and suppose $f_n\to f$ in $L^p([0,1])$.

(a) Prove that $f_n\to f$ in measure.

(b) Prove that some subsequence converges to $f$ almost everywhere.
:::

::: {.solution}
<1>1. Convergence in measure.
::: {.proof}
Fix $\varepsilon>0$. By Chebyshev's inequality,
\[
\mu\{|f_n-f|\ge\varepsilon\}
\le \frac1{\varepsilon^p}\int_0^1|f_n-f|^p\,dx.
\]
The right-hand side tends to $0$ because $f_n\to f$ in $L^p$. Hence $f_n\to f$ in measure.
:::

<1>2. An almost-everywhere convergent subsequence.
::: {.proof}
Choose a subsequence $(f_{n_k})$ such that
\[
\|f_{n_k}-f\|_p^p\le2^{-k}.
\]
Then
\[
\int_0^1\sum_{k=1}^\infty |f_{n_k}(x)-f(x)|^p\,dx
=\sum_{k=1}^\infty\|f_{n_k}-f\|_p^p
\le1.
\]
By Tonelli's theorem,
\[
\sum_{k=1}^\infty |f_{n_k}(x)-f(x)|^p<\infty
\]
for almost every $x$. Therefore its terms tend to zero, so
\[
f_{n_k}(x)\longrightarrow f(x)
\]
for almost every $x\in[0,1]$.
:::
:::
