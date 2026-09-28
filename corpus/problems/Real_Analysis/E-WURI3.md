---
schema: qual/card@1
id: E-WURI3
kind: problem
title: The Fourier transform of an $L^1$ function is bounded and uniformly continuous
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Uniform Continuity
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that if $f\in L^1$ then $\hat f$ is bounded and uniformly continuous.
:::

::: {.solution}
Use $\hat f(\xi) = \int f(x)e^{-ix\xi}\,dx$.

<1>1. $|\hat f(\xi)| \le \|f\|_1$ for every $\xi$.

::: {.proof}
$|\hat f(\xi)| = \left|\int f(x)e^{-ix\xi}\,dx\right| \le \int |f(x)|\,dx$.
:::

<1>2. $\sup_\xi|\hat f(\xi + h) - \hat f(\xi)| \le \int |f(x)|\,|e^{-ihx} - 1|\,dx$.

::: {.proof}
$\hat f(\xi+h) - \hat f(\xi) = \int f(x)e^{-ix\xi}(e^{-ihx} - 1)\,dx$, and $|e^{-ix\xi}| = 1$.
:::

<1>3. $\int |f(x)|\,|e^{-ihx} - 1|\,dx \to 0$ as $h \to 0$.

::: {.proof}
The integrand tends to $0$ pointwise and is bounded by $2|f| \in L^1$, so the dominated convergence theorem applies along every sequence $h_k \to 0$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 is boundedness, and steps <1>2 and <1>3 give $\sup_\xi|\hat f(\xi + h) - \hat f(\xi)| \to 0$ as $h \to 0$, which is uniform continuity.
:::
:::
