---
schema: qual/card@1
id: P-GRECH7-40
kind: problem
title: Order of a permutation of six letters
classification:
  areas: [prelim]
  topics: []
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
\[
\sigma=\begin{pmatrix}1&2&3&4&5&6\\5&6&2&3&1&4\end{pmatrix}
\]
on the set $S=\{1,2,3,4,5,6\}$?

(A) $1$
(B) $2$
(C) $3$
(D) $4$
(E) $6$
:::

::: {.solution}
<1>1. In disjoint-cycle notation,
$$
\sigma=(1\ 5)(2\ 6\ 4\ 3).
$$

::: {.proof}
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

<1>2. The order of $\sigma$ is
$$
\operatorname{lcm}(2,4)=4.
$$

::: {.proof}
For a permutation written as a product of disjoint cycles, a positive power is the identity exactly when its exponent is divisible by every cycle length. Thus the least positive exponent giving the identity is the least common multiple of the cycle lengths from step <1>1.
:::

<1>3. Therefore
$$
\boxed{\operatorname{ord}(\sigma)=4},
$$
so the answer is (D).

::: {.proof}
This is the value computed in step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested order.
:::
:::
