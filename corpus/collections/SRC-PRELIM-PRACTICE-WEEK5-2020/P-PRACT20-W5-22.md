---
schema: qual/card@1
id: P-PRACT20-W5-22
kind: problem
title: Computing $(1+i)^{10}$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 22).
---

::: {.problem}
Put $(1 + i)^{10}$ in the form $a + bi$ for $a, b \in \RR$.
:::

::: pf

::: pf-step

One has
\[
(1+i)^2=2i.
\]


::: pf-proof

Expanding gives
\[
(1+i)^2
=1+2i+i^2
=2i.
\]

:::

:::

::: pf-step

Therefore
\[
(1+i)^{10}=32i.
\]


::: pf-proof

Using step <1>1,
\[
(1+i)^{10}
=\bigl((1+i)^2\bigr)^5
=(2i)^5
=2^5i^5.
\]
Since
\[
i^5=i,
\]
the value is $32i$.

:::

:::

::: pf-step

In the requested form,
\[
\boxed{(1+i)^{10}=0+32i}.
\]


::: pf-proof

Step <1>2 gives real part $0$ and imaginary coefficient $32$.

:::

:::

::: pf-qed

Step <1>3 is the requested expression.

:::

:::
