---
schema: qual/card@1
id: E-SMI-8000E-SY3
kind: problem
title: No group of order 182 is simple
classification:
  areas:
  - algebra
  topics:
  - Sylow Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Smith 8000e Sylow problem 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Applied the Sylow congruence and divisibility conditions to the Sylow 7-subgroups, forcing uniqueness and hence a proper nontrivial normal subgroup."
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed problem, Smith 8000e.pdf page 7, Sylow problem 3:
    "Prove no group of order 182 is simple." Correct: 182 = 2·7·13, n_7 divides 26
    and is ≡ 1 mod 7, and 1, 2, 6, 5 are the four residues, so n_7 = 1 and the
    Sylow 7-subgroup is a proper nontrivial normal subgroup. No defect.
---
---

::: {.exercise}
Prove no group of order 182 is simple.
:::

::: {.solution}
Let $G$ be a group of order
$$
182=2\cdot7\cdot13.
$$

::: pf

::: pf-step

The Sylow $7$-subgroup is unique.

::: pf-proof

Let $n_7$ be the number of Sylow $7$-subgroups. Sylow's theorem gives
$$
n_7\mid \frac{182}{7}=26
$$
and
$$
n_7\equiv1\pmod7.
$$
The positive divisors of $26$ are
$$
1,2,13,26.
$$
Modulo $7$ these are respectively
$$
1,2,6,5.
$$
Hence the only possibility is
$$
n_7=1.
$$

:::

:::

::: pf-step

Conclude that $G$ is not simple.

::: pf-proof

The unique Sylow $7$-subgroup $P$ has order $7$, so it is nontrivial and
proper in $G$. Uniqueness makes it invariant under conjugation, hence normal:
$$
P\trianglelefteq G.
$$
Thus $G$ has a nontrivial proper normal subgroup and therefore is not simple.
Hence
$$
\boxed{\text{no group of order }182\text{ is simple}.}
$$

:::

:::

:::

:::
