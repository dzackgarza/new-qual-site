---
schema: qual/card@1
id: P-BKS12-4B
kind: problem
title: Conjugacy classes of nilpotent $5\times 5$ complex matrices
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with pages 4--5 of the retained Spring 2012 solution PDF and independently reviewed the Jordan-form classification.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the bijection between nilpotent Jordan types and partitions of 5 and enumerated all seven partitions.
---

::: {.problem}
How many conjugacy classes of nilpotent 5 by 5 complex matrices are there (up to conjugacy by invertible matrices)?
:::

::: {.solution}
<1>1. Every nilpotent complex matrix is conjugate to a direct sum of
nilpotent Jordan blocks
$$
J_{r_1}(0)\oplus\cdots\oplus J_{r_k}(0)
$$
with
$$
r_1+\cdots+r_k=5.
$$

::: {.proof}
By the Jordan canonical form theorem, every complex matrix is similar to a
direct sum of Jordan blocks. A nilpotent matrix has only the eigenvalue
$0$, so every block has eigenvalue $0$. The block sizes are positive
integers whose sum is the dimension, here $5$.
:::

<1>2. Two nilpotent $5\times5$ complex matrices are conjugate exactly
when they have the same multiset of Jordan-block sizes.

::: {.proof}
Jordan canonical form is unique up to permutation of its blocks. Thus
conjugacy forgets only the order in which the blocks are displayed, not
their sizes.
:::

<1>3. The possible multisets of block sizes are the seven partitions
$$
\begin{aligned}
5&=5,\\
 &=4+1,\\
 &=3+2,\\
 &=3+1+1,\\
 &=2+2+1,\\
 &=2+1+1+1,\\
 &=1+1+1+1+1.
\end{aligned}
$$

::: {.proof}
List the partitions by largest part. If the largest part is $5$, $4$, or
$3$, the displayed possibilities are forced. If the largest part is $2$,
the remaining sum is partitioned using parts at most $2$, giving
$2+2+1$ and $2+1+1+1$. If the largest part is $1$, only the final
partition occurs. This exhausts all partitions of $5$.
:::

<1>4. The number of conjugacy classes is
$$
\boxed{7}.
$$

::: {.proof}
By steps <1>1 and <1>2, conjugacy classes are in bijection with partitions
of $5$. Step <1>3 lists exactly seven partitions.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested count.
:::
:::
