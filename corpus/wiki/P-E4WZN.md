---
schema: qual/card@1
id: P-E4WZN
kind: problem
title: If $R_1 \neq R_2$, prove that the radius of convergence, $R$, of
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
If $R_1 \neq R_2$, prove that the radius of convergence, $R$, of the power series $\sum_{n=0}^\infty (a_n+b_n)x^n$ is $\min\{R_1, R_2\}$.
What can be said about $R$ when $R_1 = R_2$?
:::
::: {.solution}
<1>1. $R \ge \min\{R_1, R_2\}$: $\sum (a_n + b_n)x^n$ converges absolutely for $|x| < \min\{R_1, R_2\}$.
Proof: for such $x$, both $\sum a_n x^n$ and $\sum b_n x^n$ converge absolutely, so their sum does (triangle inequality).

<1>2. If $R_1 \neq R_2$, say $R_1 < R_2$, then $R = R_1 = \min\{R_1, R_2\}$.
<2>1. For $R_1 < |x| < R_2$: $\sum a_n x^n$ diverges while $\sum b_n x^n$ converges absolutely.
Proof: $|x| > R_1$ forces divergence of $\sum a_n x^n$; $|x| < R_2$ forces absolute convergence of $\sum b_n x^n$.
<2>2. At such $x$, the sum $\sum (a_n + b_n)x^n$ diverges.
Proof: if it converged, then $\sum a_n x^n = \sum (a_n + b_n)x^n - \sum b_n x^n$ would converge as the difference of two convergent series, contradicting <2>1. <2>3. Hence $R \le R_1$.
Proof: <2>2 shows divergence somewhere in $(R_1, R_2)$, so the radius cannot exceed $R_1$.
<2>4. Q.E.D. Proof: <1>1 and <2>3 give $R = R_1$.

<1>3. If $R_1 = R_2$, nothing general can be said beyond $R \ge R_1$: $R$ may be larger or equal.
<2>1. Example with cancellation: $b_n = -a_n$ gives $(a_n + b_n) = 0$, so $R = \infty > R_1 = R_2$.
Proof: the sum is the zero series.
<2>2. Example with no cancellation: $b_n = a_n$ gives $(a_n + b_n) = 2a_n$, so $R = R_1 = R_2$.
Proof: multiplying coefficients by $2$ does not change the radius.
<2>3. Q.E.D. Proof: <2>1 and <2>2 show both extremes occur.

<1>4. Q.E.D. Proof: <1>1, <1>2, <1>3 settle the claim and the equal-radii discussion.
:::
