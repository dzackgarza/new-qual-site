---
schema: qual/card@1
id: E-ORJPT
kind: problem
title: Convergence of $\prod_{n\in\mathbb{Z}}(1+a_n)$ when $\{a_n\}\in\ell_1(\mathbb{Z})$
classification:
  areas:
  - complex-analysis
  topics:
  - Weierstrass Factorization
  - Convergence Tests
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Show that $\prod_{n\in \ZZ} (1 + a_n) < \infty$ if $\theset{a_n} \in \ell_1(\ZZ)$.
:::

::: {.solution}
::: pf

::: {.pf-step #l1-sum-finite}
Since $\{a_n\} \in \ell_1(\ZZ)$, we have $\sum_{n \in \ZZ} |a_n| < \infty$.

::: pf-proof
definition of $\ell_1$.
:::

:::

::: pf-step
Hence $a_n \to 0$, so for all sufficiently large $|n|$ we have $|a_n| < 1/2$.

::: pf-proof
a convergent series has terms tending to $0$.
:::

:::

::: {.pf-step #log-bound}
For $|a_n| < 1/2$, $|\log(1 + a_n)| \le 2|a_n|$.

::: pf-proof
$|\log(1+z)| \le 2|z|$ for $|z| \le 1/2$ (standard estimate).
:::

:::

::: pf-step
Hence $\sum_{n} |\log(1 + a_n)| \le 2\sum_n |a_n| < \infty$.

::: pf-proof
Steps [](#log-bound){.pf-ref} and [](#l1-sum-finite){.pf-ref}.
:::

:::

::: {.pf-step #product-converges}
Therefore $\sum_n \log(1 + a_n)$ converges absolutely, so the product $\prod_n (1 + a_n)$ converges to a finite nonzero value.

::: pf-proof
a product $\prod (1 + a_n)$ converges (absolutely) iff $\sum \log(1 + a_n)$ converges (absolutely).
:::

:::

::: pf-qed
Step [](#product-converges){.pf-ref}.
:::

:::

:::
