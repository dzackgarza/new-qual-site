---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W3
kind: problem
title: Uniform limits of continuous functions are continuous
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuity
  - Convergence of Functions
relations:
- kind: uses
  target: T-RA-WORKSHOP-D7-6-1
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Assume that $\{f_n\}$ is a sequence of continuous functions $f_n:E\subset\mathbb R\to\mathbb R$ which converges uniformly to $f$.
Prove the results of Theorem 6.1 directly.
:::

::: {.solution}
<1>1. For every $x_0\in E$ and $\varepsilon>0$, there exists $N\geq1$ such that
\[
|f_N(x)-f(x)|<\varepsilon/3\qquad(x\in E).
\]

::: {.proof}
This is the definition of uniform convergence applied with tolerance $\varepsilon/3$. If $E$ is empty, the continuity assertion is vacuous.
:::

<1>2. For $x_0,\varepsilon,N$ as in step <1>1, there exists $\delta>0$ such that
\[
|f_N(x)-f_N(x_0)|<\varepsilon/3
\quad\text{whenever }x\in E,\ |x-x_0|<\delta.
\]

::: {.proof}
The function $f_N$ is continuous at $x_0$ by hypothesis. Apply its epsilon-delta condition with tolerance $\varepsilon/3$.
:::

<1>3. The function $f$ is continuous at every $x_0\in E$.

::: {.proof}
Fix $x_0\in E$ and $\varepsilon>0$, and choose $N$ and $\delta$ by steps <1>1 and <1>2. Whenever $x\in E$ and $|x-x_0|<\delta$, the triangle inequality gives
\[
\begin{aligned}
|f(x)-f(x_0)|
&\leq |f(x)-f_N(x)|+|f_N(x)-f_N(x_0)|\\
&\quad+|f_N(x_0)-f(x_0)|
<\varepsilon.
\end{aligned}
\]
Thus the epsilon-delta condition holds at every $x_0\in E$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves continuity of the uniform limit on $E$.
:::
:::
