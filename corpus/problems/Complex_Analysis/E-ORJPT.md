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
Show that $\prod_{n\in \ZZ} (1 + a_n) < \infty$ if $\ts{a_n} \in \ell_1(\ZZ)$.
:::

::: {.solution}
<1>1. Since $\{a_n\} \in \ell_1(\ZZ)$, we have $\sum_{n \in \ZZ} |a_n| < \infty$.
::: {.proof}
definition of $\ell_1$.
:::

<1>2. Hence $a_n \to 0$, so for all sufficiently large $|n|$ we have $|a_n| < 1/2$.
::: {.proof}
a convergent series has terms tending to $0$.
:::

<1>3. For $|a_n| < 1/2$, $|\log(1 + a_n)| \le 2|a_n|$.
::: {.proof}
$|\log(1+z)| \le 2|z|$ for $|z| \le 1/2$ (standard estimate).
:::

<1>4. Hence $\sum_{n} |\log(1 + a_n)| \le 2\sum_n |a_n| < \infty$.
::: {.proof}
<1>3 and <1>1.
:::

<1>5. Therefore $\sum_n \log(1 + a_n)$ converges absolutely, so the product $\prod_n (1 + a_n)$ converges to a finite nonzero value.
::: {.proof}
a product $\prod (1 + a_n)$ converges (absolutely) iff $\sum \log(1 + a_n)$ converges (absolutely).
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
