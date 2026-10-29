---
schema: qual/card@1
id: P-D6ZX6
kind: problem
title: Maximal implies prime
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Maximal $\implies$ prime, but generally not the converse." with no ring and no request; the statement declares a commutative ring with identity and asks for the proof and a counterexample to the converse.'
---

::: {.problem}
Let $R$ be a commutative ring with identity. Show that every maximal ideal of $R$ is prime, but that a prime ideal need not be maximal.
:::

::: {.solution}

::: pf

::: pf-step

Every maximal ideal $\mm$ of $R$ is prime.

::: pf-proof

The ideal $\mm$ is proper by definition.
Suppose $ab\in\mm$ and $b\notin\mm$.
Then $\mm\subsetneq\mm+(b)$, so maximality gives $\mm+(b)=R$, and $1=m+rb$ for some $m\in\mm$ and $r\in R$.
Hence $a=am+r(ab)$, and both $am$ and $r(ab)$ lie in $\mm$, so $a\in\mm$.

:::

:::

::: pf-step

The ideal $(0)\subset\ZZ$ is prime but not maximal.

::: pf-proof

It is prime because $\ZZ$ is an integral domain, and it is not maximal because $(0)\subsetneq(2)\subsetneq\ZZ$.

:::

:::

:::

:::
