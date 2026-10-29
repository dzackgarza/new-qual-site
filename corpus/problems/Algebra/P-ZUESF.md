---
schema: qual/card@1
id: P-ZUESF
kind: problem
title: $n_p=1$ when $n_p\mid q<p$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The statement read "Suppose that $n_p$ divides an integer $q < p$." This is false for $q=0$, which every $n_p$ divides; the statement now requires $q$ to be a positive integer.'
---

::: {.problem}
Let $G$ be a finite group of order $\abs{G} = p^k m$, where $p$ is a prime. Let $n_p$ denote the number of Sylow $p$-subgroups of $G$.
Suppose that $n_p$ divides a positive integer $q < p$.
Prove that $n_p = 1$, and consequently every Sylow $p$-subgroup is normal in $G$.
:::

::: {.solution}

::: pf

::: pf-step

$\boxed{n_p=1}$.

::: pf-proof

By the Sylow theorems, $n_p\equiv1\pmod p$. Since $n_p\mid q$ and $q>0$, $1\le n_p\le q<p$, and the only integer in $[1,p)$ congruent to $1$ modulo $p$ is $1$.

:::

:::

::: pf-step

Every Sylow $p$-subgroup is normal in $G$.

::: pf-proof

Conjugates of a Sylow $p$-subgroup are Sylow $p$-subgroups, and there is only one.

:::

:::

:::

:::
