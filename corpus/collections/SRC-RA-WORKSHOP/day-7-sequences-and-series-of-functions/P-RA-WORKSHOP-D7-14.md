---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-14
kind: problem
title: Uniform convergence along a convergent sequence of points
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuity
  - Sequences of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(June 2009 #4a) Let $\{f_n\}$ be a sequence of real-valued continuous functions such that $f_n\to f$ uniformly on $[0,1]$, and let $\{x_n\}\subset[0,1]$ be a sequence which converges to $x$.
Show that $$\lim_{n\to\infty}f_n(x_n)=f(x).$$
:::

:::: {.solution}
**Goal:** Show $f_n(x_n) \to f(x)$ given $f_n \to f$ uniformly on $[0,1]$, $f_n$ continuous, $x_n \to x$ in $[0,1]$.

<1>1. $|f_n(x_n) - f(x)| \le |f_n(x_n) - f(x_n)| + |f(x_n) - f(x)|$.
Proof: triangle inequality.

<1>2. $|f_n(x_n) - f(x_n)| \le \|f_n - f\|_\infty \to 0$.
Proof: uniform convergence, and $x_n \in [0,1]$.

<1>3. $|f(x_n) - f(x)| \to 0$.
Proof: $f$ is continuous (uniform limit of continuous functions) and $x_n \to x$, so continuity of $f$ at $x$ gives $f(x_n) \to f(x)$.

<1>4. Q.E.D. Proof: <1>2 and <1>3 force the right side of <1>1 to $0$, so $f_n(x_n) \to f(x)$.
:::
