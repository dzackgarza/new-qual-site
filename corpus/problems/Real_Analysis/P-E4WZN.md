---
schema: qual/card@1
id: P-E4WZN
kind: problem
title: Radius of convergence of $\sum (a_n+b_n)x^n$
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

::: {.problem}
If $R_1 \neq R_2$, prove that the radius of convergence, $R$, of the power series $\sum_{n=0}^\infty (a_n+b_n)x^n$ is $\min\{R_1, R_2\}$.
What can be said about $R$ when $R_1 = R_2$?
:::
::: {.solution}
Here $R_1$ and $R_2$ are the radii of convergence of $\sum a_n x^n$ and $\sum b_n x^n$.

<1>1. $R \ge \min\{R_1, R_2\}$.

::: {.proof}
For $|x| < \min\{R_1, R_2\}$ both $\sum a_n x^n$ and $\sum b_n x^n$ converge absolutely, and $|(a_n + b_n)x^n| \le |a_nx^n| + |b_nx^n|$.
:::

<1>2. If $R_1 < R_2$, then $R \le R_1$.

::: {.proof}
Let $R_1 < |x| < R_2$. Then $\sum a_n x^n$ diverges and $\sum b_n x^n$ converges. If $\sum (a_n + b_n)x^n$ converged, then $\sum a_n x^n$ would converge as the difference of two convergent series. So $\sum (a_n + b_n)x^n$ diverges at points with $|x| > R_1$ arbitrarily close to $R_1$, and $R \le R_1$.
:::

<1>3. If $R_1 = R_2$, then $R \ge R_1$, and both $R = R_1$ and $R > R_1$ occur.

::: {.proof}
The inequality is step <1>1. With $b_n = a_n$, the coefficients $2a_n$ give $R = R_1$. With $b_n = -a_n$, the series is $0$ and $R = \infty$, which exceeds $R_1$ whenever $R_1 < \infty$.
:::

<1>4. Q.E.D.

::: {.proof}
If $R_1 \neq R_2$, steps <1>1 and <1>2, with the roles of the series exchanged if $R_2 < R_1$, give $R = \min\{R_1, R_2\}$. Step <1>3 is the case $R_1 = R_2$.
:::
:::
