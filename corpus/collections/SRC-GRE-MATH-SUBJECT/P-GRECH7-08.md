---
schema: qual/card@1
id: P-GRECH7-08
kind: problem
title: Counting safe combinations with arithmetic constraints
classification:
  areas: [prelim]
  topics:
  - Counting
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 8 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
A man forgot the combination to his safe. The combination consists of a sequence of four numbers, each from 1 to 60. The man only remembers the following pieces of information:

All the numbers are different.

The second number is twice the third number.

The third number is prime.

How many possible combinations must the man try to unlock his safe?

(A) 1377
(B) 33,060
(C) 34,220
(D) 35,400
(E) 11,703,240
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The third number has exactly $10$ possible values.


::: pf-proof

If the third number is the prime $p$, then the second number is $2p$ and must be at most $60$. Hence $p\le30$. The primes at most $30$ are
$$
2,3,5,7,11,13,17,19,23,29,
$$
so there are exactly $10$ choices for the third number. Each choice determines the second number uniquely.

:::

:::

::: {.pf-step #s1-2}

Once the second and third numbers are fixed, there are $58$ choices for the first number and then $57$ choices for the fourth number.


::: pf-proof

The second and third numbers are distinct because $2p\ne p$ for every positive prime $p$. The first number may therefore be any of the remaining $60-2=58$ numbers. After it is chosen, the fourth number may be any of the remaining $60-3=57$ numbers.

:::

:::

::: {.pf-step #s1-3}

The number of possible combinations is
$$
10\cdot58\cdot57=\boxed{33{,}060},
$$
so the answer is (B).


::: pf-proof

By step [](#s1-1){.pf-ref} there are $10$ choices for the constrained second-third pair, and by step [](#s1-2){.pf-ref} each such pair admits $58\cdot57$ ordered choices for the first and fourth positions. The multiplication principle gives
$$
10\cdot58\cdot57=33{,}060.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested number of possible combinations.

:::

:::

:::
