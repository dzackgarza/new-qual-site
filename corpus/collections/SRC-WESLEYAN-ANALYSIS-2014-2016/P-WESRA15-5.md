---
schema: qual/card@1
id: P-WESRA15-5
kind: problem
title: 'Scheffé-type $L^1$ convergence from convergence of norms'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $(X,\mathcal A,\mu)$ be a measure space and let $f_n,f$ be integrable real-valued functions.
Prove that if $f_n\to f$ almost everywhere and
$$
\int_X|f_n|\,d\mu\to\int_X|f|\,d\mu,
$$
then
$$
\int_X|f_n-f|\,d\mu\to0.
$$
:::

::: {.solution}

Define
$$
g_n=|f_n|+|f|-|f_n-f|.
$$

::: pf

::: {.pf-step #s1-1}

Each $g_n$ is measurable, integrable, and nonnegative.


::: pf-proof

Measurability follows from measurability of $f_n$ and $f$. By the triangle inequality,
$$
|f_n-f|\le |f_n|+|f|,
$$
so $g_n\ge0$. Also
$$
0\le g_n\le |f_n|+|f|,
$$
and the right-hand side is integrable because both $f_n$ and $f$ are integrable. Hence $g_n$ is integrable.

:::

:::

::: {.pf-step #s1-2}

One has
$$
g_n\longrightarrow 2|f|
$$
almost everywhere.


::: pf-proof

At every point where $f_n\to f$,
$$
|f_n|\to|f|
$$
and
$$
|f_n-f|\to0.
$$
Therefore
$$
g_n=|f_n|+|f|-|f_n-f|\to2|f|.
$$
The assumed convergence holds almost everywhere.

:::

:::

::: pf-step

Fatou's lemma gives
$$
2\int_X|f|\,d\mu
\le
\liminf_{n\to\infty}\int_X g_n\,d\mu.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the functions $g_n$ are nonnegative. By step [](#s1-2){.pf-ref},
$$
\liminf_{n\to\infty}g_n=2|f|
$$
almost everywhere. Fatou's lemma therefore yields
$$
\int_X2|f|\,d\mu
\le
\liminf_{n\to\infty}\int_Xg_n\,d\mu.
$$

:::

:::

::: {.pf-step #s1-4}

Suppose, for contradiction, that
$$
\int_X|f_n-f|\,d\mu
$$
does not tend to $0$. Then there are $\varepsilon>0$ and a subsequence $(n_k)$ such that
$$
\int_X|f_{n_k}-f|\,d\mu\ge\varepsilon
$$
for every $k$.


::: pf-proof

The integrals are nonnegative. Failure to converge to $0$ therefore yields a positive $\varepsilon$ and infinitely many indices for which the integral is at least $\varepsilon$; enumerate those indices increasingly.

:::

:::

::: {.pf-step #s1-5}

Along the subsequence from step [](#s1-4){.pf-ref},
$$
\limsup_{k\to\infty}\int_Xg_{n_k}\,d\mu
\le
2\int_X|f|\,d\mu-\varepsilon.
$$


::: pf-proof

By the definition of $g_n$,
$$
\int_Xg_{n_k}\,d\mu
=
\int_X|f_{n_k}|\,d\mu
+
\int_X|f|\,d\mu
-
\int_X|f_{n_k}-f|\,d\mu.
$$
Using step [](#s1-4){.pf-ref},
$$
\int_Xg_{n_k}\,d\mu
\le
\int_X|f_{n_k}|\,d\mu
+
\int_X|f|\,d\mu
-\varepsilon.
$$
The hypothesis
$$
\int_X|f_n|\,d\mu\to\int_X|f|\,d\mu
$$
then gives the asserted limit-superior bound.

:::

:::

::: {.pf-step #s1-6}

Step [](#s1-5){.pf-ref} contradicts Fatou's lemma applied to the subsequence $(g_{n_k})$.


::: pf-proof

The subsequence still satisfies
$$
g_{n_k}\to2|f|
$$
almost everywhere and remains nonnegative. Therefore Fatou's lemma gives
$$
2\int_X|f|\,d\mu
\le
\liminf_{k\to\infty}\int_Xg_{n_k}\,d\mu.
$$
But step [](#s1-5){.pf-ref} gives
$$
\liminf_{k\to\infty}\int_Xg_{n_k}\,d\mu
\le
\limsup_{k\to\infty}\int_Xg_{n_k}\,d\mu
\le
2\int_X|f|\,d\mu-\varepsilon,
$$
a contradiction.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\int_X|f_n-f|\,d\mu\longrightarrow0
}.
$$


::: pf-proof

The contradiction in step [](#s1-6){.pf-ref} shows that the negation assumed in step [](#s1-4){.pf-ref} is impossible. Since the integrals are nonnegative, they must converge to $0$.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is exactly the required $L^1$ convergence.

:::

:::

:::
