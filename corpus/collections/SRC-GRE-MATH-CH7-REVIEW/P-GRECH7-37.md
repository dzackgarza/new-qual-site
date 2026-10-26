---
schema: qual/card@1
id: P-GRECH7-37
kind: problem
title: Consequences of membership in $(A\cup B)\cap C$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 37 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $x$ is an element of the set $(A \cup B) \cap C$, which of the following must be true?

- I. $x \in (A \cap B) \cup C$
- II. $x \in (A \cup B)$
- III. $x \in (A \cap B) \cap C$

(A) I only
(B) II only
(C) III only
(D) I and II only
(E) II and III only
:::

::: pf

::: pf-step

The hypothesis implies
$$
x\in C
$$
and
$$
x\in A\cup B.
$$


::: pf-proof

Membership in an intersection means membership in both factors. Thus
$$
x\in(A\cup B)\cap C
$$
is equivalent to the two displayed statements.

:::

:::

::: pf-step

Statement I must be true.


::: pf-proof

By step <1>1, $x\in C$. Since
$$
C\subseteq(A\cap B)\cup C,
$$
it follows that $x\in(A\cap B)\cup C$.

:::

:::

::: pf-step

Statement II must be true.


::: pf-proof

This is exactly the second membership assertion in step <1>1.

:::

:::

::: pf-step

Statement III need not be true.


::: pf-proof

Take, for example,
$$
A=\{x\},\qquad B=\varnothing,\qquad C=\{x\}.
$$
Then $x\in(A\cup B)\cap C$, but $A\cap B=\varnothing$, so
$$
x\notin(A\cap B)\cap C.
$$

:::

:::

::: pf-step

Therefore the statements that must be true are
$$
\boxed{\text{I and II only}},
$$
so the answer is (D).


::: pf-proof

Steps <1>2 and <1>3 prove I and II, while step <1>4 gives a counterexample to III.

:::

:::

::: pf-qed

Step <1>5 gives the required choice.

:::

:::
