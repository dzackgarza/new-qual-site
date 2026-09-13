---
schema: qual/card@1
id: P-ALGPAN11-08
kind: problem
title: Consequence of the identity (ab)^2 = a^2 b^2
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
![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-08.png)
:::

::: {.solution}
The group must be abelian, so the answer is $\boxed{\text{(D)}}$.

<1>1. Cancel in the given identity.
::: {.proof}
For arbitrary $a,b\in G$,
\[
(ab)^2=a^2b^2
\]
means
\[
abab=aabb.
\]
Left-multiplying by $a^{-1}$ gives
\[
bab=abb,
\]
and right-multiplying by $b^{-1}$ gives
\[
ba=ab.
\]
Thus every pair of elements commutes and $G$ is abelian.
:::
:::
