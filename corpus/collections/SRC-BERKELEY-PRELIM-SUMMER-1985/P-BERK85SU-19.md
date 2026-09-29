---
schema: qual/card@1
id: P-BERK85SU-19
kind: problem
title: Limit of the $n$th root of a finite sum of $n$th powers
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Since 0<=A_j<=A_1, the sum of nth powers lies between A_1^n and
    k A_1^n. Taking nth roots and using k^{1/n}->1 squeezes the limit
    to A_1.
---

::: {.problem}
Let
\[
A_1\ge A_2\ge\cdots\ge A_k\ge0.
\]
Evaluate
\[
\lim_{n\to\infty}\left(A_1^n+A_2^n+\cdots+A_k^n\right)^{1/n}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every positive integer $n$,
$$
A_1
\le
\left(A_1^n+A_2^n+\cdots+A_k^n\right)^{1/n}
\le
k^{1/n}A_1.
$$

::: pf-proof

Since all $A_j$ are nonnegative, the sum contains the term $A_1^n$,
so
$$
A_1^n
\le
A_1^n+A_2^n+\cdots+A_k^n.
$$
Also $A_j\le A_1$ for every $j$, hence
$$
A_1^n+A_2^n+\cdots+A_k^n
\le
kA_1^n.
$$
Taking nonnegative $n$th roots gives the displayed inequalities.

:::

:::

::: {.pf-step #s2}

The required limit is
$$
\boxed{A_1}.
$$

::: pf-proof

Since
$$
\lim_{n\to\infty}k^{1/n}=1,
$$
step [](#s1){.pf-ref} and the squeeze theorem give
$$
\lim_{n\to\infty}
\left(A_1^n+A_2^n+\cdots+A_k^n\right)^{1/n}
=
A_1.
$$
This also covers $A_1=0$, in which case every $A_j$ is $0$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} gives the requested value.

:::

:::

:::
