---
schema: qual/card@1
id: P-ARTALG-SU05-2
kind: problem
title: 'Structure theorem and abelian groups of order $360$'
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts and the exhaustive pairwise-nonisomorphic list requirement with Summer 2005 problem 2 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked every partition of the 2-primary and 3-primary exponents, all six orders, and the pairwise distinct group exponents."
---

::: {.problem}
(a) State the structure theorem for finite Abelian groups.

(b) Up to isomorphism, what are the Abelian groups of order 360?
:::

::: {.solution}
Write $C_m=\mathbb Z/m\mathbb Z$ as an additive group.

<1>1. Every finite abelian group has a decomposition
$$
A\cong\bigoplus_{p\ \mathrm{prime}}
\bigoplus_{j=1}^{s_p}C_{p^{e_{p,j}}},
$$
where only finitely many $s_p$ are nonzero and
$1\leq e_{p,1}\leq\cdots\leq e_{p,s_p}$.
For each prime $p$, the ordered list of exponents is uniquely
determined by $A$. Conversely, any such finite direct sum is a
finite abelian group. Empty lists are allowed, including the
empty sum for the trivial group. This is the elementary-divisor
form of the structure theorem [@DF04].

<1>2. Exactly six isomorphism classes have order $360$.

| Group | Exponent |
| --- | --- |
| $C_8\oplus C_9\oplus C_5$ | $360$ |
| $C_8\oplus C_3\oplus C_3\oplus C_5$ | $120$ |
| $C_4\oplus C_2\oplus C_9\oplus C_5$ | $180$ |
| $C_4\oplus C_2\oplus C_3\oplus C_3\oplus C_5$ | $60$ |
| $C_2\oplus C_2\oplus C_2\oplus C_9\oplus C_5$ | $90$ |
| $C_2\oplus C_2\oplus C_2\oplus C_3\oplus C_3\oplus C_5$ | $30$ |

::: {.proof}
Factor $360=2^3\cdot3^2\cdot5$. In step <1>1, the exponents
for a prime $p$ sum to the exponent of $p$ in the group order.
For $p=2$ the sum must be $3$. The only partitions of $3$ into
positive integers are $(3)$, $(1,2)$, and $(1,1,1)$, giving
$$
C_8,\qquad C_2\oplus C_4,\qquad C_2\oplus C_2\oplus C_2.
$$
For $p=3$ the only partitions of $2$ are $(2)$ and $(1,1)$,
giving $C_9$ or $C_3\oplus C_3$. The $5$-part is $C_5$, and
no other prime occurs. These three choices for the $2$-part and
two choices for the $3$-part produce precisely the six rows.
Each row has order $8\cdot9\cdot5=360$, so every listed
possibility is realized.
:::

<1>3. The six listed groups are pairwise nonisomorphic.

::: {.proof}
The exponent of a finite additive group is the least positive
integer that annihilates every element, and is invariant under
isomorphism. In a direct sum of cyclic groups, an integer kills
every element exactly when it is divisible by the order of each
cyclic summand. Thus the exponent is the least common multiple
of those orders.

The least common multiples for the six rows are, respectively,
$360,120,180,60,90,30$. They are pairwise distinct, so no two
rows are isomorphic. Combined with step <1>2, this proves both
exhaustiveness and absence of repetitions.
:::
:::
