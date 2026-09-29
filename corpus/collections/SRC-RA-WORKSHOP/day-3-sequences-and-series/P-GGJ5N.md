---
schema: qual/card@1
id: P-GGJ5N
kind: problem
title: $\sum\frac{a_n}{\beta+a_n}$ diverges whenever $\sum a_n$ diverges, for $a_n>0$
  and $\beta>0$
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Assume $\beta >0$, $a_n>0$, $n=1,2,\ldots$, and the series $\sum a_n$ is divergent.
Show that $\displaystyle \sum \frac{a_n}{\beta + a_n}$ is also divergent.
:::
::: {.solution}

::: pf

::: pf-step

Claim: $\sum \frac{a_n}{\beta + a_n}$ diverges.

::: pf-proof

we show its partial sums are unbounded, using the divergence of $\sum a_n$.

:::

:::

::: {.pf-step #s2}

Two-case bound: if $a_n \le \beta$ then $\frac{a_n}{\beta + a_n} \ge \frac{a_n}{2\beta}$; if $a_n > \beta$ then $\frac{a_n}{\beta + a_n} > \frac{1}{2}$.

::: pf-proof

$a_n \le \beta \Rightarrow \beta + a_n \le 2\beta$; $a_n > \beta \Rightarrow \beta + a_n < 2a_n \Rightarrow \frac{a_n}{\beta + a_n} > \frac{1}{2}$.

:::

:::

::: {.pf-step #s3}

Hence $\frac{a_n}{\beta + a_n} \ge \frac{1}{2}\min\left\{\frac{a_n}{\beta}, 1\right\}$ for every $n$.

::: pf-proof

Step [](#s2){.pf-ref} covers both cases uniformly: for $a_n \le \beta$ the min is $a_n/\beta$ and the RHS is $a_n/(2\beta)$; for $a_n > \beta$ the min is $1$ and the RHS is $1/2$.

:::

:::

::: {.pf-step #s4}

$\sum \min\left\{\frac{a_n}{\beta}, 1\right\}$ diverges.

::: pf-proof

let $I = \{n : a_n \ge \beta\}$.

If $\sum_{n \in I} 1 = \infty$ we are done.
Otherwise $I$ is finite, so for all but finitely many $n$, $\min\{a_n/\beta, 1\} = a_n/\beta$, and $\sum a_n/\beta = \infty$ (as $\sum a_n$ diverges).
Either way the sum diverges.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give $\sum \frac{a_n}{\beta + a_n} \ge \frac12 \sum \min\{a_n/\beta, 1\} = \infty$.

:::

:::

:::
