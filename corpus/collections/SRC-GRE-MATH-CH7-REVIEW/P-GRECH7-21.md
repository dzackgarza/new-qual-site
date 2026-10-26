---
schema: qual/card@1
id: P-GRECH7-21
kind: problem
title: Which propositional formula is not a tautology
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 21 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Which of the following is NOT a tautology?

(A) $\neg(\neg A) \leftrightarrow A$
(B) $A \lor (\neg A)$
(C) $[(A \land B) \to C] \leftrightarrow [A \to (B \lor C)]$
(D) $\neg(C \land D) \leftrightarrow \neg C \lor \neg D$
(E) $A \lor (B \land C) \leftrightarrow (A \land B) \lor (A \land C)$
:::

::: pf

::: pf-step

Choices (A), (B), and (D) are tautologies.


::: pf-proof

Choice (A) is the law of double negation,
$$
\neg\neg A\leftrightarrow A.
$$
Choice (B) is the law of excluded middle,
$$
A\lor\neg A.
$$
Choice (D) is De Morgan's law,
$$
\neg(C\land D)\leftrightarrow\neg C\lor\neg D.
$$
Each identity holds for every assignment of truth values.

:::

:::

::: {.pf-step #s1-2}

Choice (C) is not a tautology.


::: pf-proof

Take $A$ true, $B$ false, and $C$ false. Then
$$
(A\land B)\to C
$$
is true because its antecedent is false, while
$$
A\to(B\lor C)
$$
is false because its antecedent is true and its consequent is false. Hence the biconditional in (C) is false for this assignment.

:::

:::

::: {.pf-step #s1-3}

Choice (E), as printed, is also not a tautology.


::: pf-proof

Take $A$ true, $B$ false, and $C$ false. Then
$$
A\lor(B\land C)
$$
is true, whereas
$$
(A\land B)\lor(A\land C)
$$
is false. Thus the biconditional in (E) is false for this assignment.

:::

:::

::: {.pf-step #s1-4}

The source's explanation identifies (E) as the distributive law, whose correct right-hand side is
$$
(A\lor B)\land(A\lor C).
$$


::: pf-proof

The valid distributive law for disjunction over conjunction is
$$
A\lor(B\land C)
\leftrightarrow
(A\lor B)\land(A\lor C).
$$
With this correction, (E) is a tautology, leaving (C) as the unique non-tautology and matching the source's stated answer.

:::

:::

::: {.pf-step #s1-5}

Therefore the problem as printed has two correct choices, (C) and (E); under the evident correction in step [](#s1-4){.pf-ref}, the intended answer is
$$
\boxed{\text{(C)}}.
$$


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} show that both (C) and the printed (E) are non-tautologies. Step [](#s1-4){.pf-ref} identifies the source's evident intended version of (E), under which only (C) remains non-tautological.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives both the literal status of the printed question and the intended answer.

:::

:::
