---
schema: qual/card@1
id: P-EMRA2
kind: problem
title: Fatou's lemma
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Real Analysis Problem 2 in the preserved Emory qualifying-problems compilation collected by Santiago Arango.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
State and prove Fatou's Lemma on a general measurable space.
:::

::: {.solution}
<1>1. State Fatou's lemma.
::: {.proof}
Let $(X,\mathcal M,\mu)$ be a measure space and let $f_n:X\to[0,\infty]$ be measurable for every $n$.
Then
\[
\int_X \liminf_{n\to\infty} f_n\,d\mu
\le
\liminf_{n\to\infty}\int_X f_n\,d\mu.
\]
Both sides are allowed to be $+\infty$.
:::

<1>2. Introduce the monotone tail infima.
::: {.proof}
For each $n$, define
\[
g_n(x):=\inf_{k\ge n}f_k(x).
\]
Each $g_n$ is measurable, $0\le g_n\le g_{n+1}$, and pointwise
\[
g_n(x)\uparrow \liminf_{k\to\infty}f_k(x).
\]
Therefore the Monotone Convergence Theorem gives
\[
\int_X\liminf_{k\to\infty}f_k\,d\mu
=
\lim_{n\to\infty}\int_X g_n\,d\mu.
\]
:::

<1>3. Compare each tail infimum with every member of its tail.
::: {.proof}
For every $k\ge n$ one has $g_n\le f_k$, hence
\[
\int_X g_n\,d\mu
\le
\int_X f_k\,d\mu.
\]
Taking the infimum over $k\ge n$ gives
\[
\int_X g_n\,d\mu
\le
\inf_{k\ge n}\int_X f_k\,d\mu.
\]
Now let $n\to\infty$:
\[
\int_X\liminf_{k\to\infty}f_k\,d\mu
\le
\lim_{n\to\infty}
\inf_{k\ge n}\int_X f_k\,d\mu
=
\liminf_{k\to\infty}\int_X f_k\,d\mu.
\]
This is Fatou's lemma.
:::
:::
