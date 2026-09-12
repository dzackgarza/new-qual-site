---
schema: qual/card@1
id: P-ALGREV1-01
kind: problem
title: Multiplicative groups of rationals and reals
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, open-ended question 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Distinguished the groups by cardinality: Q* is countable while R* is uncountable."
---

::: {.problem}
Prove or disprove that $\mathbb{Q}^*$ under multiplication is isomorphic to $\mathbb{R}^*$ under multiplication.
:::

::: solution
The two groups are not isomorphic.

<1>1. The multiplicative group $\mathbb Q^*$ is countable.
::: proof
$\mathbb Q$ is countable, and removing the single element $0$ preserves
countability. Hence $\mathbb Q^*=\mathbb Q\setminus\{0\}$ is countable.
:::

<1>2. The multiplicative group $\mathbb R^*$ is uncountable.
::: proof
$\mathbb R$ is uncountable. If $\mathbb R^*=\mathbb R\setminus\{0\}$ were
countable, then adjoining the one-element set $\{0\}$ would make $\mathbb R$
countable, a contradiction. Thus $\mathbb R^*$ is uncountable.
:::

<1>3. Therefore no group isomorphism can exist.
::: proof
A group isomorphism is, in particular, a bijection of the underlying sets.
Steps <1>1 and <1>2 show that the two underlying sets have different
cardinalities. Hence
$$
\boxed{\mathbb Q^*\not\cong\mathbb R^*.}
$$
:::
:::
