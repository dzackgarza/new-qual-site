---
schema: qual/card@1
id: P-GRECH7-47
kind: problem
title: Set identities implied by $A\subseteq B$
classification:
  areas: [prelim]
  topics:
  - Set Theory
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 47 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $A \subseteq B$, which of the following conditions must be true?

I. $A \cup B = B$

II. $A - B = \emptyset$

III. $C - B \subseteq C - A$

(A) I only
(B) I and II only
(C) I and III only
(D) II and III only
(E) I, II, and III
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement I is true:
$$
A\cup B=B.
$$


::: pf-proof

Because $A\subseteq B$, every element of $A$ is already in $B$. Thus adjoining $A$ to $B$ adds no elements, so their union is $B$.

:::

:::

::: {.pf-step #s1-2}

Statement II is true:
$$
A-B=\varnothing.
$$


::: pf-proof

An element of $A-B$ would have to belong to $A$ but not to $B$. This is impossible because $A\subseteq B$.

:::

:::

::: {.pf-step #s1-3}

Statement III is true:
$$
C-B\subseteq C-A.
$$


::: pf-proof

Let $x\in C-B$. Then $x\in C$ and $x\notin B$. Since $A\subseteq B$, membership $x\in A$ would imply $x\in B$. Therefore $x\notin A$, so $x\in C-A$. Hence every element of $C-B$ belongs to $C-A$.

:::

:::

::: {.pf-step #s1-4}

Therefore all three statements must be true:
$$
\boxed{\text{I, II, and III}},
$$
so the answer is (E).


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} establish I, II, and III respectively.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
