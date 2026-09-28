---
schema: qual/card@1
id: P-MMAQ-TCJZEHD655
kind: problem
title: If $\limsup a_n\le l$, then $\limsup\frac1n\sum_{i=1}^n a_i\le l$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
If $\limsup_{n\rightarrow \infty} a_n\leq l$, show that $\limsup_{n\rightarrow \infty}\sum_{i=1}^n{a_i/n}\leq l$.
:::

::: {.solution}
Write $\sigma_n = \frac{1}{n}\sum_{i=1}^n a_i$.

<1>1. If $K \in \RR$ and $a_n < K$ for all $n \geq N$, then $\limsup_n \sigma_n \leq K$.

::: {.proof}
With $C = \sum_{i=1}^{N-1} a_i$, for $n \geq N$
$$\sigma_n = \frac{C}{n} + \frac{1}{n}\sum_{i=N}^{n} a_i \leq \frac{C}{n} + \frac{n - N + 1}{n} K.$$
The right side converges to $K$ because $C/n \to 0$ and $(n - N + 1)/n \to 1$, and $x_n \leq y_n$ implies $\limsup x_n \leq \limsup y_n$.
:::

<1>2. If $l \in \RR$, then $\limsup_n \sigma_n \leq l$.

::: {.proof}
For $\eps > 0$, $\limsup_n a_n \leq l < l + \eps$, so $a_n < l + \eps$ for all large $n$. Step <1>1 with $K = l + \eps$ gives $\limsup_n \sigma_n \leq l + \eps$ for every $\eps > 0$.
:::

<1>3. If $l = -\infty$, then $\limsup_n \sigma_n = -\infty$.

::: {.proof}
For every $K \in \RR$, $\limsup_n a_n = -\infty < K$, so $a_n < K$ for all large $n$, and step <1>1 gives $\limsup_n \sigma_n \leq K$.
:::

<1>4. Q.E.D.

::: {.proof}
For $l = +\infty$ the inequality $\limsup_n \sigma_n \leq +\infty$ holds for every real sequence. Steps <1>2 and <1>3 cover the remaining cases.
:::
