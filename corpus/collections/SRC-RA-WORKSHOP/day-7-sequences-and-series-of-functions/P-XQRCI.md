---
schema: qual/card@1
id: P-XQRCI
kind: problem
title: Equicontinuity of $\bigl\{\frac{x}{1+nx^2}\bigr\}_{n\ge 1}$ on compact intervals
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Convergence of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $f_n(x) = \frac{x}{1+nx^2}$ for $n \in \NN$.
Let $\mathcal{F} \coloneqq \{f_n \, \colon \, n = 1, 2, 3, \ldots\}$ and $[a,b]$ be any compact subset of $\RR$.
Is $\mathcal{F}$ equicontinuous?
Justify your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #derivative}

$f_n'(x) = \dfrac{1 - nx^2}{(1+nx^2)^2}$.

::: pf-proof

By the quotient rule,
$$
f_n'(x) = \frac{(1+nx^2) - 2nx^2}{(1+nx^2)^2} = \frac{1 - nx^2}{(1+nx^2)^2}.
$$

:::

:::

::: {.pf-step #s2}

$\abs{f_n'(x)} \le 1$ for all $n$ and all $x$.

::: pf-proof

Let $u = nx^2 \ge 0$. By step [](#derivative){.pf-ref}, $\abs{f_n'(x)} = \abs{1-u}/(1+u)^2$.
For $0 \le u \le 1$: $\frac{1-u}{(1+u)^2} \le \frac{1}{(1+u)^2} \le 1$.
For $u > 1$: $\frac{u-1}{(1+u)^2} \le \frac{u}{(1+u)^2} \le 1$, because $u \le (1+u)^2$.

:::

:::

::: pf-step

$\boxed{\text{Yes}}$: $\mathcal{F}$ is equicontinuous on $\RR$, hence on every compact $[a,b]$.

::: pf-proof

By the mean value theorem and step [](#s2){.pf-ref}, for all $n$ and all $x, y$,
$$
\abs{f_n(x) - f_n(y)} \le \sup \abs{f_n'} \cdot \abs{x - y} \le \abs{x - y}.
$$
So the family is uniformly $1$-Lipschitz: given $\varepsilon > 0$, the choice $\delta = \varepsilon$ works independently of $n$ and $x$.

:::

:::

:::

:::
