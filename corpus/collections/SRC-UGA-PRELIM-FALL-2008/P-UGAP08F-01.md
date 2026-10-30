---
schema: qual/card@1
id: P-UGAP08F-01
kind: problem
title: Determine the truth of four quantified parity statements
classification:
  areas: [prelim]
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Discuss the truth of each statement.

(a) For each integer $x$, there is an integer $y$ such that $x+y$ is odd.

(b) There is an integer $x$ such that $x+y$ is odd for every integer $y$.

(c) For each integer $x$, there is an integer $y$ such that $xy$ is odd.

(d) There is an integer $x$ such that $xy$ is even for every integer $y$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement (a) is $\boxed{\text{true}}$.


::: pf-proof

Let $x\in\ZZ$ be arbitrary and choose
$$
y\coloneqq 1-x.
$$
Then $y\in\ZZ$ and
$$
x+y=1,
$$
which is odd. Thus the required integer $y$ exists for every integer $x$.

:::

:::

::: {.pf-step #s1-2}

Statement (b) is $\boxed{\text{false}}$.


::: pf-proof

Let $x\in\ZZ$ be arbitrary. Taking $y=-x$ gives
$$
x+y=0,
$$
which is even. Hence no single integer $x$ can make $x+y$ odd for every integer $y$.

:::

:::

::: {.pf-step #s1-3}

Statement (c) is $\boxed{\text{false}}$.


::: pf-proof

Take $x=2$. For every integer $y$,
$$
xy=2y
$$
is even, so there is no integer $y$ for which $xy$ is odd. Therefore the universal assertion over $x$ fails.

:::

:::

::: {.pf-step #s1-4}

Statement (d) is $\boxed{\text{true}}$.


::: pf-proof

Choose $x=0$. Then for every integer $y$,
$$
xy=0,
$$
which is even. Thus such an integer $x$ exists.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} determine the truth of all four statements.

:::

:::

:::
