---
schema: qual/card@1
id: E-TZFC7
kind: exercise
title: Uniform limits preserve boundedness and continuity
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuity
relations: []
review: draft
---

::: exercise
- Show that a uniform limit of bounded functions is bounded.

- Show that a uniform limit of continuous function is continuous.

  - I.e. if $f_n\to f$ uniformly with each $f_n$ continuous then $f$ is continuous.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. A uniform limit of bounded functions is bounded.
<2>1. Choose $N$ with $\|f - f_N\|_\infty \le 1$.
Proof: definition of uniform convergence with $\eps = 1$.
<2>2. $|f(x)| \le |f_N(x)| + 1 \le \|f_N\|_\infty + 1$ for every $x$.
Proof: triangle inequality, and boundedness of $f_N$.
<2>3. Q.E.D. Proof: <2>2 bounds $|f|$ uniformly by $\|f_N\|_\infty + 1$.

<1>2. A uniform limit of continuous functions is continuous.
<2>1. Fix $x_0$ and $\eps > 0$; choose $n$ with $\|f - f_n\|_\infty < \eps/3$.
Proof: uniform convergence.
<2>2. Choose $\delta > 0$ such that $|f_n(x) - f_n(x_0)| < \eps/3$ whenever $|x - x_0| < \delta$.
Proof: continuity of $f_n$ at $x_0$.
<2>3. For $|x - x_0| < \delta$: $|f(x) - f(x_0)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)| < \eps$.
Proof: triangle inequality; the first and third terms are $< \eps/3$ by uniform convergence (<2>1), the middle by <2>2. <2>4. Q.E.D. Proof: <2>3 shows $f$ is continuous at the arbitrary point $x_0$.
:::
