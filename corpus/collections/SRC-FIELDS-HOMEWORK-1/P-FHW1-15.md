---
schema: qual/card@1
id: P-FHW1-15
kind: problem
title: The algebraic closure of $\FF_p$ and its proper infinite subfields
classification:
  areas: [algebra]
  topics: [Finite Fields, Field Extensions]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
(a) Show that the algebraic closure of $\FF_p$ is the union of its finite subfields: $\overline{\FF}_p=\bigcup_{n=1}^\infty\FF_{p^n}$.

(b) Show that $\overline{\FF}_p$ contains proper infinite subfields.
:::

::: {.solution}
The algebraic closure $\closure{\FF}_p$ contains, for each $n\ge1$, exactly one subfield with $p^n$ elements, namely the set of roots of $x^{p^n}-x$; it is written $\FF_{p^n}$, and $\FF_{p^a}\subseteq\FF_{p^b}$ exactly when $a$ divides $b$.

::: pf

::: {.pf-step #part-a}
(a) $\closure{\FF}_p=\bigcup_{n\ge1}\FF_{p^n}$.

::: pf-proof
Every $\FF_{p^n}$ consists of elements algebraic over $\FF_p$, so the union lies in the algebraic closure.
Conversely let $\alpha\in\closure{\FF}_p$ and let $d$ be the degree of its minimal polynomial over $\FF_p$.
Then $\FF_p(\alpha)$ is a finite field with $p^d$ elements, hence equals $\FF_{p^d}$, and $\alpha\in\FF_{p^d}$ lies in the union.
:::

:::

::: {.pf-step #part-b}
(b) $\closure{\FF}_p$ has proper infinite subfields.

::: pf-proof
The fields $\FF_{p^{2^n}}$ form an increasing chain, because $2^n$ divides $2^{n+1}$, so their union $U$ is a subfield of $\closure{\FF}_p$.
It is infinite, since it contains $\FF_{p^{2^n}}$ for every $n$.
It is proper: an element of $\FF_{p^3}\setminus\FF_p$ lies in $\FF_{p^m}$ only if $3$ divides $m$, and no $m=2^n$ is divisible by $3$, so that element lies outside $U$.
:::

:::

:::

:::
