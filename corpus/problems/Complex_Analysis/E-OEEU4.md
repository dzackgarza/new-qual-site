---
schema: qual/card@1
id: E-OEEU4
kind: problem
title: Entire functions of polynomial growth are polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
---

::: {.exercise}
Let $f$ be entire and suppose that for $\abs{z} \geq M$,
$$
\abs{f} \leq A + B\abs{z}^k
$$
for some constants $A, B$ and $k$.
Show that $f$ is a polynomial of degree at most $k$.
:::

::: {.solution}

Write $f(z) = \sum_{n\geq0} c_n z^n$, the Taylor series of $f$ at $0$, which converges on $\CC$.

::: pf

::: {.pf-step #cauchy}
For every $n\geq0$ and $R\geq M$, $\abs{c_n}\leq \frac{A+BR^k}{R^n}$.

::: pf-proof
By the Cauchy estimate on the circle $\abs{z}=R$, $\abs{c_n} = \frac{\abs{f^{(n)}(0)}}{n!}\leq R^{-n}\max_{\abs{z}=R}\abs{f(z)}\leq R^{-n}(A+BR^k)$.
:::

:::

::: pf-step
$c_n=0$ for every $n>k$, so $f$ is a polynomial of degree at most $k$.

::: pf-proof
For $n>k$, the bound in step [](#cauchy){.pf-ref} is $AR^{-n}+BR^{k-n}$, which tends to $0$ as $R\to\infty$.
:::

:::

:::

:::
