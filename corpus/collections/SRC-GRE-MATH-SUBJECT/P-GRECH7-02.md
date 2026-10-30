---
schema: qual/card@1
id: P-GRECH7-02
kind: problem
title: Negation of the disjunction $S\lor T$
classification:
  areas: [prelim]
  topics:
  - Logic
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 2 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Which of the following is the negation of the sentence $(S \lor T)$?

(A) $\neg S \land \neg T$
(B) $\neg S \land T$
(C) $S \land \neg T$
(D) $\neg S \lor \neg T$
(E) $S \land T$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The proposition $\neg(S\lor T)$ is true exactly when both $S$ and $T$ are false.


::: pf-proof

The disjunction $S\lor T$ is false exactly in the single case in which $S$ is false and $T$ is false. Negating the disjunction reverses its truth value, so $\neg(S\lor T)$ is true exactly in that case.

:::

:::

::: {.pf-step #s1-2}

The proposition $\neg S\land\neg T$ is true exactly when both $S$ and $T$ are false.


::: pf-proof

A conjunction is true exactly when both conjuncts are true. Thus $\neg S\land\neg T$ is true exactly when $\neg S$ and $\neg T$ are both true, equivalently when $S$ and $T$ are both false.

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\neg(S\lor T)\equiv\boxed{\neg S\land\neg T},
$$
so the answer is (A).


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that the two propositions have identical truth values for every assignment of truth values to $S$ and $T$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required negation.

:::

:::

:::
