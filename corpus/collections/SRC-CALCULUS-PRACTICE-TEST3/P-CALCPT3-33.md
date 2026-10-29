---
schema: qual/card@1
id: P-CALCPT3-33
kind: problem
title: "Probability that a random arrangement of $n$ weights is increasing"
classification:
  areas: [prelim]
  topics: [Probability, Permutations]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 33 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree where the extraction is legible."
---

::: {.problem}
If $n$ apples, no two of the same weight, are lined up at random on a table, what is the probability that they are lined up in order of increasing weight from left to right?

(A) $\frac12$
(B) $\frac1n$
(C) $\frac1{n!}$
(D) $\frac1{2^n}$
(E) $\left(\frac1n\right)^n$
:::

::: {.solution}
"At random" means each of the $n!$ left-to-right orders of the apples is equally likely.

::: pf

::: {.pf-step #unique}
Exactly one order is increasing in weight.

::: pf-proof
The weights are distinct, so sorting them gives one and only one increasing sequence.
:::

:::

::: pf-step
The probability is $\boxed{\frac1{n!}}$, choice (C).

::: pf-proof
By step [](#unique){.pf-ref}, one of $n!$ equally likely outcomes is favorable. For $n=3$, $\frac1{3!}=\frac16$, while (A), (B), (D), (E) give $\frac12$, $\frac13$, $\frac18$, $\frac1{27}$, so each other choice is wrong.
:::

:::

:::

:::
