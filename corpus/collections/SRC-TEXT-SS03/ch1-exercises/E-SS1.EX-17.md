---
schema: qual/card@1
id: E-SS1.EX-17
kind: problem
title: The ratio test computes the radius of convergence
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
17. Show that if $\{ a _ { n } \} _ { n = 0 } ^ { \infty }$ is a sequence of non-zero complex numbers such that

$$
\lim _ {n \to \infty} \frac {| a _ {n + 1} |}{| a _ {n} |} = L,
$$

then

$$
\lim _ {n \to \infty} | a _ {n} | ^ {1 / n} = L.
$$

In particular, this exercise shows that when applicable, the ratio test can be used to calculate the radius of convergence of a power series.
:::

::: {.solution}
Fix $\varepsilon>0$.

<1>1. There is $N$ such that for all $n > N$,
$$|a_N| (L - \varepsilon)^{n-N} < |a_n| < |a_N| (L + \varepsilon)^{n-N}.$$

::: {.proof}
By the hypothesis there is $N$ with $L - \varepsilon < |a_{k+1}|/|a_k| < L + \varepsilon$ for all $k \ge N$. For $n>N$ the telescoping product $|a_n| = |a_N| \prod_{k=N}^{n-1} |a_{k+1}|/|a_k|$ then gives the bounds.
:::

<1>2. $L - \varepsilon \le \liminf |a_n|^{1/n} \le \limsup |a_n|^{1/n} \le L + \varepsilon$.

::: {.proof}
Taking $n$th roots in step <1>1, which preserves order of positive quantities,
$$|a_N|^{1/n} (L - \varepsilon)^{(n-N)/n} < |a_n|^{1/n} < |a_N|^{1/n} (L + \varepsilon)^{(n-N)/n}.$$
As $n \to \infty$, $|a_N|^{1/n} \to 1$ because $|a_N|$ is a fixed positive number, and $(n-N)/n \to 1$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 holds for every $\varepsilon > 0$, so $\lim |a_n|^{1/n} = L$.
:::
:::
