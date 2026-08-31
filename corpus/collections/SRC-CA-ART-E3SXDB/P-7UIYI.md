---
schema: qual/card@1
id: P-7UIYI
kind: problem
title: $\lim|a_{n+1}/a_n|=L$ implies $\lim|a_n|^{1/n}=L$, and the ratio test for the
  radius of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
  - Sequences of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

:::{.problem}
Let $a_n\neq 0$ and show that
\[
\lim_{n\to \infty} {\abs{a_{n+1}} \over \abs{a_n}} = L \implies \lim_{n\to\infty} \abs{a_n}^{1\over n} = L
.\]
In particular, this shows that when applicable, the ratio test can be used to calculate the radius of convergence of a power series.
:::

::: {.solution}
<1>1. Let $r_n = \frac{|a_{n+1}|}{|a_n|}$, so $r_n \to L$.
::: {.proof}
definition.
:::

<1>2. For any $\epsilon > 0$, there is $N$ such that $L - \epsilon < r_n < L + \epsilon$ for all $n \ge N$.
::: {.proof}
convergence of $r_n$.
:::

<1>3. Hence for $n > N$, $|a_n| = |a_N| \prod_{k=N}^{n-1} r_k$, so
$$|a_N|(L - \epsilon)^{n-N} < |a_n| < |a_N|(L + \epsilon)^{n-N}.$$
::: {.proof}
telescope the product.
:::

<1>4. Taking $n$-th roots and letting $n \to \infty$ gives
$$L - \epsilon \le \liminf |a_n|^{1/n} \le \limsup |a_n|^{1/n} \le L + \epsilon.$$
::: {.proof}
$|a_N|^{1/n} \to 1$ and $(L \pm \epsilon)^{(n-N)/n} \to L \pm \epsilon$.
:::

<1>5. Since $\epsilon > 0$ is arbitrary, $\lim |a_n|^{1/n} = L$.
::: {.proof}
<1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::

