---
schema: qual/card@1
id: P-GRECH7-45
kind: problem
title: Circular seatings of four people
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 45 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
In how many different ways can four people sit around a restaurant table (not including rotations)?

(A) $24$
(B) $18$
(C) $6$
(D) $48$
(E) $16$
:::

::: pf

::: pf-step

Fix one of the four people in a reference seat.


::: pf-proof

Two seatings that differ only by a rotation are to be identified. Every rotational equivalence class has a unique representative in which a chosen person, say $A$, occupies a fixed reference seat.

:::

:::

::: pf-step

The remaining three people can be arranged in
$$
3!=6
$$
ways around the remaining seats.


::: pf-proof

After fixing $A$ as in step <1>1, the three distinct people $B,C,D$ may be assigned arbitrarily to the three remaining seats, giving $3!$ permutations.

:::

:::

::: pf-step

Therefore the number of circular seatings, modulo rotations, is
$$
\boxed{6},
$$
so the answer is (C).


::: pf-proof

By step <1>1, each rotational equivalence class is counted exactly once by the arrangements enumerated in step <1>2.

:::

:::

::: pf-qed

Step <1>3 gives the requested count.

:::

:::
