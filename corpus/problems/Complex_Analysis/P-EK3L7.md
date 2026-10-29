---
schema: qual/card@1
id: P-EK3L7
kind: problem
title: $\frac1z\sum_{k=1}^\infty z^k/k$ converges on $S^1\setminus\{1\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Show that $\frac{1}{z}\sum_{k=1}^\infty \frac{z^k}{k}$ converges for all $z \in S^1 \setminus \{1\}$ using summation by parts (Dirichlet's test).
:::

::: {.solution}

Fix $z\in S^1\setminus\{1\}$ and let $A_n\coloneqq\sum_{k=1}^nz^k$.

::: pf

::: {.pf-step #bounded}
$\abs{A_n}\le\frac2{\abs{1-z}}$ for every $n$.

::: pf-proof
$A_n=z\frac{1-z^n}{1-z}$ and $\abs{z}=1$, so $\abs{1-z^n}\le2$.
:::

:::

::: {.pf-step #abel}
$\sum_{k=1}^N\frac{z^k}{k}=\frac{A_N}{N}+\sum_{k=1}^{N-1}A_k\left(\frac1k-\frac1{k+1}\right)$.

::: pf-proof
This is summation by parts with $z^k=A_k-A_{k-1}$, $A_0=0$.
:::

:::

::: pf-step
$\frac1z\sum_{k=1}^\infty\frac{z^k}{k}$ converges.

::: pf-proof
By step [](#bounded){.pf-ref}, $A_N/N\to0$ and $\sum_{k\ge1}\abs{A_k}\left(\frac1k-\frac1{k+1}\right)\le\frac2{\abs{1-z}}\sum_{k\ge1}\frac1{k(k+1)}<\infty$, so the right side of step [](#abel){.pf-ref} converges as $N\to\infty$.
Multiplying by $1/z$, which is defined because $z\ne0$, preserves convergence.
:::

:::

:::

:::
