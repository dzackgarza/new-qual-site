---
schema: qual/card@1
id: P-GRECH7-43
kind: problem
title: Pigeonhole statements for $61$ flowers on four tables
classification:
  areas: [prelim]
  topics:
  - Pigeonhole Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 43 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
A florist is arranging flowers in centerpieces at each of four tables at an event. If he has $61$ flowers total, which of the following statements are true?

I. One table has no more than $13$ flowers.

II. One table has at least $16$ flowers.

III. Two of the tables have at least $31$ flowers combined.

(A) II only
(B) I and II only
(C) I and III only
(D) II and III only
(E) I, II, and III
:::

::: {.solution}

Let the four table counts be nonnegative integers $a,b,c,d$ with
$$
a+b+c+d=61.
$$

::: pf

::: {.pf-step #s1-1}

Statement I need not be true.


::: pf-proof

The distribution
$$
(a,b,c,d)=(16,15,15,15)
$$
uses all $61$ flowers, but every table has at least $15$ flowers. Thus no table has $13$ or fewer.

:::

:::

::: {.pf-step #s1-2}

Statement II must be true.


::: pf-proof

If every table had at most $15$ flowers, then
$$
a+b+c+d\le4\cdot15=60,
$$
contradicting the total of $61$. Hence some table has at least $16$ flowers.

:::

:::

::: {.pf-step #s1-3}

Statement III must be true.


::: pf-proof

Reorder the four counts so that
$$
a\ge b\ge c\ge d.
$$
If no pair of tables had at least $31$ flowers, then in particular
$$
a+b\le30.
$$
Since $a\ge c$ and $b\ge d$, one also has
$$
c+d\le a+b\le30.
$$
Therefore
$$
a+b+c+d\le60,
$$
again contradicting the total $61$. Thus some two tables contain at least $31$ flowers combined.

:::

:::

::: {.pf-step #s1-4}

Therefore the statements that must be true are
$$
\boxed{\text{II and III only}},
$$
so the answer is (D).


::: pf-proof

Step [](#s1-1){.pf-ref} gives a counterexample to I, while steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} prove II and III.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
