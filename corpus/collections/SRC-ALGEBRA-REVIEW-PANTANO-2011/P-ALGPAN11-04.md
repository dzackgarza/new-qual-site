---
schema: qual/card@1
id: P-ALGPAN11-04
kind: problem
title: Prime expressions selected by an arithmetic property
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
![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-04.png)
:::

::: {.solution}
Every field automorphism of $\mathbb Q$ is the identity, so the answer is $\boxed{\text{(B)}\ 1}$.

<1>1. Any automorphism fixes every rational number.
::: {.proof}
Let $\varphi:\mathbb Q\to\mathbb Q$ be a field automorphism.
Since $\varphi(1)=1$, additivity gives $\varphi(n)=n$ for every $n\in\mathbb Z$.
For $m/n\in\mathbb Q$ with $n\ne0$,
\[
\varphi(m/n)=\varphi(m)\varphi(n)^{-1}=m/n.
\]
Thus $\varphi=\operatorname{id}_{\mathbb Q}$.
:::
:::
