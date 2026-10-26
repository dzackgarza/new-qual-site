---
schema: qual/card@1
id: P-GRECH7-41
kind: problem
title: Implications derivable from four conditionals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 41 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $A$, $B$, $C$, and $D$ be well-formed sentences. Suppose $A\to C$, $B\to D$, $\neg C\to\neg D$, and $\neg A\to\neg C$. Which of the following statements must be true?

I. $A\to D$

II. $A$ and $C$ are logically equivalent.

III. $\neg A\to\neg B$

(A) I only
(B) II only
(C) III only
(D) I and II only
(E) II and III only
:::

::: pf

::: pf-step

The hypotheses imply
$$
C\to A
$$
and
$$
D\to C.
$$


::: pf-proof

The contrapositive of $\neg A\to\neg C$ is $C\to A$. The contrapositive of $\neg C\to\neg D$ is $D\to C$.

:::

:::

::: pf-step

Statement II must be true.


::: pf-proof

One hypothesis is $A\to C$, while step <1>1 gives $C\to A$. Thus
$$
A\leftrightarrow C,
$$
so $A$ and $C$ are logically equivalent.

:::

:::

::: pf-step

Statement III must be true.


::: pf-proof

Using the hypothesis $B\to D$ and step <1>1 gives the implication chain
$$
B\to D\to C\to A.
$$
Hence $B\to A$. Taking its contrapositive yields
$$
\neg A\to\neg B,
$$
which is statement III.

:::

:::

::: pf-step

Statement I need not be true.


::: pf-proof

Assign the truth values
$$
A=C=\text{true},
\qquad
B=D=\text{false}.
$$
Then all four hypotheses hold: $A\to C$ is true; $B\to D$ is true because $B$ is false; and both $\neg C\to\neg D$ and $\neg A\to\neg C$ are true because their antecedents are false. But $A\to D$ is false. Thus statement I is not forced.

:::

:::

::: pf-step

Therefore the statements that must be true are
$$
\boxed{\text{II and III only}},
$$
so the answer is (E).


::: pf-proof

Steps <1>2 and <1>3 prove II and III, while step <1>4 gives a counterexample to I.

:::

:::

::: pf-qed

Step <1>5 gives the required choice.

:::

:::
