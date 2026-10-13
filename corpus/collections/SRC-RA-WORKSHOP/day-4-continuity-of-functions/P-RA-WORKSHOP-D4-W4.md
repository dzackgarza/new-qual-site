---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W4
kind: problem
title: A limit at negative infinity
classification:
  areas:
  - real-analysis
  topics:
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(June 2013 #1b) Prove that $$\lim_{x\to-\infty}\frac{x-1}{x}=1.$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $x\ne0$,
\[
\left|\frac{x-1}{x}-1\right|=\frac1{|x|}.
\]

::: pf-proof

Subtracting the fractions gives $(x-1)/x-1=-1/x$. Taking absolute values yields the identity.

:::

:::

::: {.pf-step #s2}

The limit is $\boxed{\lim_{x\to-\infty}(x-1)/x=1}$.

::: pf-proof

Given $\varepsilon>0$, choose $M=1/\varepsilon$. If $x<-M$, then $|x|=-x>M$, and by step [](#s1){.pf-ref},
\[
\left|\frac{x-1}{x}-1\right|=\frac1{|x|}<\frac1M=\varepsilon.
\]
This is the definition of convergence to $1$ as $x\to-\infty$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the requested limit.

:::

:::

:::
