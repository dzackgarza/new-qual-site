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
Every field automorphism of $\QQ$ is the identity, so the answer is $\boxed{\text{(B)}\ 1}$.

::: pf

::: {.pf-step #s1}

Any automorphism fixes every rational number.

::: pf-proof

Let $\varphi:\QQ\to\QQ$ be a field automorphism.
Since $\varphi(1)=1$, additivity gives $\varphi(n)=n$ for every $n\in\ZZ$.
For $m/n\in\QQ$ with $n\ne0$,
\[
\varphi(m/n)=\varphi(m)\varphi(n)^{-1}=m/n.
\]
Thus $\varphi=\operatorname{id}_{\QQ}$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves that the identity is the only field automorphism of $\QQ$, so choice (B) is correct.

:::

:::

:::
