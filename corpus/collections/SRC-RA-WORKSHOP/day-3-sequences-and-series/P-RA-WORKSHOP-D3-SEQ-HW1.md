---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW1
kind: problem
title: Uniqueness of the limit of a real sequence
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
For a real sequence $\{x_n\}$, if $\lim_{n\to\infty}x_n=x$ and $\lim_{n\to\infty}x_n=y$ then $x=y$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $\varepsilon>0$, one has $|x-y|<\varepsilon$.

::: pf-proof

Fix $\varepsilon>0$. Convergence to $x$ supplies $N_1$ such that $|x_n-x|<\varepsilon/2$ whenever $n\geq N_1$. Convergence to $y$ supplies $N_2$ such that $|x_n-y|<\varepsilon/2$ whenever $n\geq N_2$. Taking $n\geq\max(N_1,N_2)$ and applying the triangle inequality gives
\[
|x-y|\leq |x-x_n|+|x_n-y|<\varepsilon.
\]

:::

:::

::: {.pf-step #s2}

The two limits coincide: $\boxed{x=y}$.

::: pf-proof

If $|x-y|>0$, step [](#s1){.pf-ref} with $\varepsilon=|x-y|$ would assert $|x-y|<|x-y|$, a contradiction. Thus $|x-y|=0$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves uniqueness of the limit.

:::

:::

:::
