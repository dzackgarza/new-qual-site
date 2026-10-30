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
Show that if $\{ a _ { n } \} _ { n = 0 } ^ { \infty }$ is a sequence of non-zero complex numbers such that

$$
\lim _ {n \to \infty} \frac {\abs{ a _ {n + 1} }}{\abs{ a _ {n} }} = L,
$$

then

$$
\lim _ {n \to \infty} \abs{ a _ {n} } ^ {1 / n} = L.
$$

In particular, this exercise shows that when applicable, the ratio test can be used to calculate the radius of convergence of a power series.
:::

::: {.solution}
Fix $\varepsilon>0$; if $L>0$, take also $\varepsilon<L$. When $L=0$, the lower bounds below are replaced by the trivial bound $0\le\abs{a_n}^{1/n}$, and the argument gives $\limsup\abs{a_n}^{1/n}\le\varepsilon$.

::: pf

::: {.pf-step #s1}

There is $N$ such that for all $n > N$,
$$\abs{a_N} (L - \varepsilon)^{n-N} < \abs{a_n} < \abs{a_N} (L + \varepsilon)^{n-N}.$$

::: pf-proof

By the hypothesis there is $N$ with $L - \varepsilon < \abs{a_{k+1}}/\abs{a_k} < L + \varepsilon$ for all $k \ge N$. For $n>N$ the telescoping product $\abs{a_n} = \abs{a_N} \prod_{k=N}^{n-1} \abs{a_{k+1}}/\abs{a_k}$ then gives the bounds.

:::

:::

::: {.pf-step #s2}

$L - \varepsilon \le \liminf \abs{a_n}^{1/n} \le \limsup \abs{a_n}^{1/n} \le L + \varepsilon$.

::: pf-proof

Taking $n$th roots in step [](#s1){.pf-ref}, which preserves order of positive quantities,
$$\abs{a_N}^{1/n} (L - \varepsilon)^{(n-N)/n} < \abs{a_n}^{1/n} < \abs{a_N}^{1/n} (L + \varepsilon)^{(n-N)/n}.$$
As $n \to \infty$, $\abs{a_N}^{1/n} \to 1$ because $\abs{a_N}$ is a fixed positive number, and $(n-N)/n \to 1$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} holds for every $\varepsilon > 0$, so $\lim \abs{a_n}^{1/n} = L$.

:::

:::

:::
