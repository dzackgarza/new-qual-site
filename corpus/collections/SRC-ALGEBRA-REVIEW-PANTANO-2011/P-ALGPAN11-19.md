---
schema: qual/card@1
id: P-ALGPAN11-19
kind: problem
title: Symmetry group of the regular pentagram
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
---

::: {.problem}
![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-19.png)
:::

::: {.solution}
The successive remainders are
\[
\boxed{53,4,1,0},
\]
so the answer is $\boxed{\text{(D)}}$.

<1>1. Execute the Euclidean algorithm.
::: {.proof}
\[
273=2\cdot110+53,
\]
so the first remainder is $53$.
Then
\[
110=2\cdot53+4,
\]
so the second is $4$.
Next
\[
53=13\cdot4+1,
\]
and finally
\[
4=4\cdot1+0.
\]
Thus the algorithm computes $r=53,4,1,0$ in order.
:::
:::
