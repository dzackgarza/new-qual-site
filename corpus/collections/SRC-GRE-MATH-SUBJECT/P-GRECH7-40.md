---
schema: qual/card@1
id: P-GRECH7-40
kind: problem
title: Order of a permutation of six letters
classification:
  areas: [prelim]
  topics:
  - Permutations
  - Symmetric Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 40 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
What is the order of the permutation
$$
\sigma=\begin{pmatrix}1&2&3&4&5&6\\5&6&2&3&1&4\end{pmatrix}
$$
on the set $S=\{1,2,3,4,5,6\}$?

(A) $1$
(B) $2$
(C) $3$
(D) $4$
(E) $6$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In disjoint-cycle notation,
$$
\sigma=(1\ 5)(2\ 6\ 4\ 3).
$$


::: pf-proof

From the two-line notation,
$$
1\mapsto5\mapsto1,
$$
which gives the cycle $(1\ 5)$. Starting at $2$ gives
$$
2\mapsto6\mapsto4\mapsto3\mapsto2,
$$
which gives $(2\ 6\ 4\ 3)$. These cycles contain all six elements and are disjoint.

:::

:::

::: {.pf-step #s1-2}

The order of $\sigma$ is
$$
\operatorname{lcm}(2,4)=4.
$$


::: pf-proof

For a permutation written as a product of disjoint cycles, a positive power is the identity exactly when its exponent is divisible by every cycle length. Thus the least positive exponent giving the identity is the least common multiple of the cycle lengths from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\operatorname{ord}(\sigma)=4},
$$
so the answer is (D).


::: pf-proof

This is the value computed in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested order.

:::

:::

:::
