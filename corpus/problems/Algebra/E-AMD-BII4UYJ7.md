---
schema: qual/card@1
id: E-AMD-BII4UYJ7
kind: problem
title: Prime ideals are primary
classification:
  areas:
  - algebra
  topics:
  - Primary Decomposition
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard implication, no repair needed), and the existing prose solution against
    a fresh re-derivation: a prime ideal is proper by definition, and if ab lies in
    p then primality gives a in p or b in p, which is the primary condition with
    n = 1; so p is primary. Correct. The prose's "in the second case b^1" is now a
    stated instance, and the two halves of the definition (properness and the
    condition on products) are separate steps, since a proof that an ideal is
    primary has to establish both. No source solution is retained for this card, so
    no source comparison was made. What was not checked: any printed source.
---

::: {.exercise}
Show that every prime ideal is primary.
:::

::: {.solution}
Let $R$ be a commutative ring with $1$. An ideal $I\trianglelefteq R$ is primary when $I\neq R$ and, for all $a,b\in R$, $ab\in I$ implies $a\in I$ or $b^n\in I$ for some $n\geq1$; it is prime when $I\neq R$ and $ab\in I$ implies $a\in I$ or $b\in I$. Let $\mathfrak p$ be a prime ideal.

::: pf

::: {.pf-step #proper}
$\mathfrak p\neq R$.

::: pf-proof
Primality is defined only for proper ideals, so the hypothesis that $\mathfrak p$ is prime already includes $\mathfrak p\neq R$. It is recorded as a step because the definition of a primary ideal also requires the ideal to be proper, and this is the half of that requirement which has to be checked here.
:::

:::

::: {.pf-step #condition}
For all $a,b\in R$ with $ab\in\mathfrak p$, either $a\in\mathfrak p$ or $b^n\in\mathfrak p$ for some $n\geq1$.

::: pf-proof
Let $ab\in\mathfrak p$. Since $\mathfrak p$ is prime, $a\in\mathfrak p$ or $b\in\mathfrak p$. In the first case the first alternative holds; in the second, $b^1=b\in\mathfrak p$, so the second alternative holds with $n=1$.
:::

:::

::: {.pf-step}
$\mathfrak p$ is primary.

::: pf-proof
Step [](#proper){.pf-ref} gives $\mathfrak p\neq R$, and step [](#condition){.pf-ref} gives the primary condition. Those two are exactly the definition of a primary ideal, so every prime ideal is primary.
:::

:::

:::
:::
