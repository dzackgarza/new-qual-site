---
schema: qual/card@1
id: P-GRECH7-29
kind: problem
title: Counting batting orders with the pitcher batting last
classification:
  areas: [prelim]
  topics:
  - Counting
  - Permutations
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 29 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Cracking_the_GRE_Mathematics_Subject.pdf`: the statement is question 29 of the Chapter 7
    Review Questions, printed on PDF p. 335, and its printed words are the card's. The chapter,
    the question number and the page are now named in the solution's opening sentence. Not checked
    in this pass: the argument, which the edit does not touch.
---

::: {.problem}
A baseball team consists of 20 players, 5 of whom are pitchers and 15 of whom are position players. If the batting order consists of 8 different position players and 1 pitcher, and if the pitcher always bats last in the order, then which of the following expressions gives the number of possible different batting orders for this baseball team?

(A) $\frac{15!(5)}{8!}$
(B) $\frac{15!(5)}{7!}$
(C) $\frac{15!(5!)}{7!}$
(D) $15!(5)$
(E) $20!$
:::

::: {.solution}
This is question 29 of the Chapter 7 Review Questions of *Cracking the GRE Mathematics Subject Test*, retained in this repository as `assets/attachments/Cracking_the_GRE_Mathematics_Subject.pdf`, on PDF p. 335; the statement below is its wording.

::: pf

::: {.pf-step #s1-1}

There are
$$
\frac{15!}{7!}
$$
ways to choose and order the eight position players in the first eight batting slots.


::: pf-proof

The eight position players must be distinct and their order matters. Thus the number of ordered selections is
$$
15\cdot14\cdots8
=\frac{15!}{(15-8)!}
=\frac{15!}{7!}.
$$

:::

:::

::: {.pf-step #s1-2}

There are $5$ independent choices for the pitcher in the ninth slot.


::: pf-proof

The pitcher is required to bat last, so after the first eight positions are filled, the only remaining choice is which one of the five pitchers occupies the ninth position.

:::

:::

::: {.pf-step #s1-3}

Therefore the number of batting orders is
$$
\boxed{\frac{15!(5)}{7!}},
$$
so the answer is (B).


::: pf-proof

By the multiplication principle, multiply the count in step [](#s1-1){.pf-ref} by the $5$ pitcher choices from step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested expression.

:::

:::

:::
