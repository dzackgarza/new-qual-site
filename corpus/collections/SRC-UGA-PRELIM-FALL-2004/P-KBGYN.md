---
schema: qual/card@1
id: P-KBGYN
kind: problem
title: $\sum_{k=0}^{n-1}a^k=(a^n-1)/(a-1)$
classification:
  areas:
  - prelim
  topics:
  - Induction
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's induction into numbered steps; the base case, the algebraic step and the
    appeal to induction are unchanged. Checked: the base case at n = 1 with a != 1, and the
    algebra of the inductive step. Not checked against a printed source: the UGA preliminary
    examinations are not retained in tmp/sources, the card records no page, and the statement is
    the card's transcription.
---

::: {.problem}
Let $a$ be a real number other than 1. Use induction to show that for each positive integer $n$, $$\sum_{k=0}^{n-1} a^k = (a^n-1)/(a-1).$$
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $a\in\RR$, $a\neq1$, and the assertion is the geometric-sum formula for every positive integer $n$; the empty sum for $n=0$ is not needed.

::: pf

::: {.pf-step #base}

The formula holds for $n=1$.

::: pf-proof

$\sum_{k=0}^{0}a^{k}=a^{0}=1$ and $(a^{1}-1)/(a-1)=1$, the division being legitimate because $a\neq1$.

:::

:::

::: {.pf-step #step}

If it holds for $n$ then it holds for $n+1$.

::: pf-proof

Assume $\sum_{k=0}^{n-1}a^{k}=(a^{n}-1)/(a-1)$. Then $\sum_{k=0}^{n}a^{k}=\frac{a^{n}-1}{a-1}+a^{n}=\frac{a^{n}-1+a^{n}(a-1)}{a-1}=\frac{a^{n+1}-1}{a-1}$.

:::

:::

::: {.pf-step #done}

The formula holds for every positive integer $n$.

::: pf-proof

The principle of induction, from steps [](#base){.pf-ref} and [](#step){.pf-ref}.

:::

:::

:::

:::
