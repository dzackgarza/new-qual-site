---
schema: qual/card@1
id: P-TRIV-LA04
kind: problem
title: Determinant under a row interchange
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let A be a non-degenerate matrix, and B is obtained from A by interchange two of its lines.
How are det A and det B related?
:::

::: {.solution}
<1>1. Let $P$ be the permutation matrix that interchanges the same two rows.
Then
$$
B=PA.
$$

::: {.proof}
Left multiplication by a permutation matrix permutes the rows of a matrix in
exactly the same way as the corresponding permutation.
:::

<1>2. The determinant of $P$ is
$$
\det P=-1.
$$

::: {.proof}
The row permutation is a single transposition, and a transposition has sign
$-1$. The determinant of its permutation matrix equals that sign.
:::

<1>3. Therefore
$$
\boxed{\det B=-\det A}.
$$

::: {.proof}
By multiplicativity of the determinant and steps <1>1--<1>2,
$$
\det B
=
\det(PA)
=
(\det P)(\det A)
=
-\det A.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required relation.
:::
:::
