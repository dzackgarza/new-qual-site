---
schema: qual/card@1
id: P-CALCPT3-29
kind: problem
title: "Limit of $\\sum_{k=1}^n(1/k-1/2^k)$"
classification:
  areas: [prelim]
  topics: [Series of Numbers]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 29 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
---

::: {.problem}
$$\lim_{n\to\infty}\sum_{k=1}^{n}\left(\frac1k-\frac1{2^k}\right)=$$

(A) $0$
(B) $1$
(C) $2$
(D) $4$
(E) $+\infty$
:::

::: {.solution}
Let $H_n\coloneqq\sum_{k=1}^n\frac1k$ and $G_n\coloneqq\sum_{k=1}^n\frac1{2^k}$, so the partial sum is $H_n-G_n$.

::: pf

::: {.pf-step #geometric}
$G_n=1-2^{-n}\le 1$ for every $n$.

::: pf-proof
This is the finite geometric sum with ratio $\frac12$.
:::

:::

::: {.pf-step #harmonic}
$H_n\to+\infty$.

::: pf-proof
For $m\ge1$, the block $\sum_{k=2^{m-1}+1}^{2^m}\frac1k$ has $2^{m-1}$ terms, each at least $2^{-m}$, so it is at least $\frac12$. Hence $H_{2^m}\ge 1+\frac m2$, and $H_n$ is increasing.
:::

:::

::: pf-step
The limit is $\boxed{+\infty}$, choice (E); choices (A) through (D) are finite and so are wrong.

::: pf-proof
By steps [](#geometric){.pf-ref} and [](#harmonic){.pf-ref}, $H_n-G_n\ge H_n-1\to+\infty$.
:::

:::

:::

:::
