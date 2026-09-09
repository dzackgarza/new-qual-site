---
schema: qual/card@1
id: P-HCAO50
kind: problem
title: An Artinian ring has finitely many maximal ideals
classification:
  areas:
  - algebra
  topics:
  - Artinian Rings
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Show that an Artinian ring has only finitely many maximal ideals.
:::

::: solution
Suppose, for contradiction, that $R$ has infinitely many distinct maximal
ideals $\mathfrak m_1,\mathfrak m_2,\ldots$.

For $n\ge1$, set
\[
I_n=\mathfrak m_1\mathfrak m_2\cdots\mathfrak m_n.
\]
Then
\[
I_1\supseteq I_2\supseteq I_3\supseteq\cdots.
\]

<1>1. Every containment $I_n\supsetneq I_{n+1}$ is strict.
::: proof
Distinct maximal ideals are comaximal. By the Chinese remainder theorem,
\[
R/I_{n+1}\cong\prod_{i=1}^{n+1}R/\mathfrak m_i.
\]
Under this isomorphism, $I_n/I_{n+1}$ corresponds to
\[
0\times\cdots\times0\times R/\mathfrak m_{n+1},
\]
which is nonzero. Hence $I_n\ne I_{n+1}$.
:::

<1>2. This contradicts the Artinian condition.
::: proof
An Artinian ring satisfies the descending chain condition on ideals, whereas
<1>1 gives an infinite strictly descending chain.
:::

Therefore $R$ has only finitely many maximal ideals.
:::
