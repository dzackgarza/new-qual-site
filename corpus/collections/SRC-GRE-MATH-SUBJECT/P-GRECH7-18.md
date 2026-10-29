---
schema: qual/card@1
id: P-GRECH7-18
kind: problem
title: Contrapositive of $A\vee B\to\neg C\vee D$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 18 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If the formula $A \vee B \rightarrow \neg C \vee D$ is true, which of the following statements is its contrapositive?

(A) $\neg C \wedge D \rightarrow A \wedge B$
(B) $C \wedge \neg D \rightarrow \neg A \wedge \neg B$
(C) $\neg C \wedge \neg D \rightarrow \neg A \wedge \neg B$
(D) $C \vee \neg D \rightarrow \neg A \vee \neg B$
(E) $A \vee B \rightarrow C \vee \neg D$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The contrapositive of an implication $P\to Q$ is $\neg Q\to\neg P$.


::: pf-proof

The formulas $P\to Q$ and $\neg Q\to\neg P$ have the same truth table: both are false exactly when $P$ is true and $Q$ is false.

:::

:::

::: {.pf-step #s1-2}

For
$$
P=A\vee B,
\qquad
Q=\neg C\vee D,
$$
the negations are
$$
\neg P=\neg A\wedge\neg B
$$
and
$$
\neg Q=C\wedge\neg D.
$$


::: pf-proof

De Morgan's laws give
$$
\neg(A\vee B)=\neg A\wedge\neg B
$$
and
$$
\neg(\neg C\vee D)=\neg\neg C\wedge\neg D=C\wedge\neg D.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the contrapositive is
$$
\boxed{C\wedge\neg D\rightarrow\neg A\wedge\neg B},
$$
so the answer is (B).


::: pf-proof

Substitute the expressions from step [](#s1-2){.pf-ref} into the contrapositive form in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required formula.

:::

:::

:::
