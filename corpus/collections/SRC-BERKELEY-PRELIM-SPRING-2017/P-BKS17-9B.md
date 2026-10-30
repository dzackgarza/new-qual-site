---
schema: qual/card@1
id: P-BKS17-9B
kind: problem
title: Elements of order 20 and 18 in $S_9$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 20 problem 9B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 cycle-decomposition argument. Both parts are correct.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the order-$20$ example using disjoint cycle lengths and the impossibility of cycle lengths with least common multiple $18$ on only nine letters.
---

::: {.problem}
Let $S_9$ denote the group of permutations of $9$ objects.

(a) Exhibit an element of $S_9$ of order $20$.

(b) Prove that no element of $S_9$ has order $18$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (a), the permutation
$$
\boxed{\sigma=(1\ 2\ 3\ 4)(5\ 6\ 7\ 8\ 9)}
$$
has order $20$.


::: pf-proof

The two displayed cycles are disjoint and have lengths $4$ and $5$. The order of a permutation written as a product of disjoint cycles is the least common multiple of their lengths. Therefore
$$
\operatorname{ord}(\sigma)=\operatorname{lcm}(4,5)=20.
$$

:::

:::

::: {.pf-step #s1-2}

No element of $S_9$ has order $18$.


::: pf-proof

Suppose, for contradiction, that $\tau\in S_9$ has order $18$. Let
$$
n_1,\ldots,n_r>1
$$
be the lengths of the nontrivial cycles in its disjoint cycle decomposition. Then
$$
\operatorname{lcm}(n_1,\ldots,n_r)=18
$$
and
$$
n_1+\cdots+n_r\leq9.
$$
Since $9$ divides the least common multiple, at least one $n_i$ must be divisible by $9$: otherwise every $n_i$ would have $3$-adic valuation at most $1$, and so would their least common multiple. Because every cycle length is at most $9$, this forces $n_i=9$. That single cycle already uses all nine letters, so there can be no other nontrivial cycle. The order of $\tau$ would then be $9$, contradicting the assumption that its order is $18$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and step [](#s1-2){.pf-ref} proves part (b).

:::

:::

:::
