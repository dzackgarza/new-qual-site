---
schema: qual/card@1
id: P-ALGPAN11-03
kind: problem
title: Which direct product of cyclic groups is not cyclic
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
Let $G_n$ denote the cyclic group of order $n$.
Which of the listed direct products is not cyclic?

![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-03.png)
:::

::: {.solution}
A finite direct product of cyclic groups is cyclic exactly when the factor orders are pairwise coprime.

<1>1. Apply the criterion to the five choices.
::: {.proof}
The orders in (A), (B), (C), and (E) are pairwise coprime:
\[
\gcd(17,11)=1,
\quad \gcd(17,11)=\gcd(17,5)=\gcd(11,5)=1,
\]
\[
\gcd(17,33)=1,
\qquad \gcd(49,121)=1.
\]
Thus those products are cyclic.
In (D),
\[
\gcd(22,33)=11>1,
\]
so $G_{22}\times G_{33}$ is not cyclic.
:::

Hence the answer is $\boxed{\text{(D)}}$.
:::
