---
schema: qual/card@1
id: P-GRECH7-21
kind: problem
title: Which propositional formula is not a tautology
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
  note: Checked against Question 21 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints (E) as $A\lor(B\land C)\leftrightarrow(A\land B)\lor(A\land C)$, which is also not a tautology; its solution calls (E) the distributive law. Choice (E) now reads $A\lor(B\land C)\leftrightarrow(A\lor B)\land(A\lor C)$, so (C) is the unique answer.
---

::: {.problem}
Which of the following is NOT a tautology?

(A) $\neg(\neg A) \leftrightarrow A$
(B) $A \lor (\neg A)$
(C) $[(A \land B) \to C] \leftrightarrow [A \to (B \lor C)]$
(D) $\neg(C \land D) \leftrightarrow \neg C \lor \neg D$
(E) $A \lor (B \land C) \leftrightarrow (A \lor B) \land (A \lor C)$
:::

::: {.solution}

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

::: pf-step

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

::: pf-step

Choice (E) is a tautology.


::: pf-proof

Choice (E) is the distributive law of disjunction over conjunction. If $A$ is true, both sides are true. If $A$ is false, both sides reduce to $B\land C$.

:::

:::

::: pf-step

Choice (C) is the only formula that is not a tautology, so the answer is
$$
\boxed{\text{(C)}}.
$$


::: pf-proof

Combine the three preceding steps.

:::

:::

:::

:::
