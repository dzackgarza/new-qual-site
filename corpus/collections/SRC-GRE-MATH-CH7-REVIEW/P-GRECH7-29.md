---
schema: qual/card@1
id: P-GRECH7-29
kind: problem
title: Counting batting orders with the pitcher batting last
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 29 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
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
<1>1. There are
$$
\frac{15!}{7!}
$$
ways to choose and order the eight position players in the first eight batting slots.

::: {.proof}
The eight position players must be distinct and their order matters. Thus the number of ordered selections is
$$
15\cdot14\cdots8
=\frac{15!}{(15-8)!}
=\frac{15!}{7!}.
$$
:::

<1>2. There are $5$ independent choices for the pitcher in the ninth slot.

::: {.proof}
The pitcher is required to bat last, so after the first eight positions are filled, the only remaining choice is which one of the five pitchers occupies the ninth position.
:::

<1>3. Therefore the number of batting orders is
$$
\boxed{\frac{15!(5)}{7!}},
$$
so the answer is (B).

::: {.proof}
By the multiplication principle, multiply the count in step <1>1 by the $5$ pitcher choices from step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested expression.
:::
:::
