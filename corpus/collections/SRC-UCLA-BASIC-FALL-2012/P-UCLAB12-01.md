---
schema: qual/card@1
id: P-UCLAB12-01
kind: problem
title: Dirichlet test for series
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\{b_n\}_{n=1}^\infty$ be a sequence of real numbers with bounded partial sums, i.e., there is $M < \infty$ such that for all $N$, $\abs{\sum_{n=1}^N b_n} \leq M$, and let $\{a_n\}_{n=1}^\infty$ be a sequence of positive numbers decreasing to $0$. Prove the series $\sum a_n b_n$ converges.
:::

::: {.solution}

Let
$$
B_n=\sum_{j=1}^n b_j,
\qquad
B_0=0.
$$
Then
$$
|B_n|\le M
$$
for every $n$.

::: pf

::: {.pf-step #s1-1}

For integers $m\le N$,
$$
\sum_{n=m}^N a_nb_n
=
a_NB_N-a_mB_{m-1}
+
\sum_{n=m}^{N-1}B_n(a_n-a_{n+1}).
$$


::: pf-proof

Since
$$
b_n=B_n-B_{n-1},
$$
one has
$$
\sum_{n=m}^Na_nb_n
=
\sum_{n=m}^Na_n(B_n-B_{n-1}).
$$
Reindexing the second sum gives
$$
\sum_{n=m}^Na_nB_n
-
\sum_{n=m-1}^{N-1}a_{n+1}B_n,
$$
which rearranges to the displayed identity.

:::

:::

::: {.pf-step #s1-2}

For integers $m\le N$,
$$
\left|
\sum_{n=m}^N a_nb_n
\right|
\le
2Ma_m.
$$


::: pf-proof

By step [](#s1-1){.pf-ref} and $|B_n|\le M$,
$$
\left|
\sum_{n=m}^N a_nb_n
\right|
\le
Ma_N+Ma_m
+
M\sum_{n=m}^{N-1}(a_n-a_{n+1}).
$$
Because $(a_n)$ is decreasing,
$$
a_n-a_{n+1}\ge0,
$$
and the sum telescopes:
$$
\sum_{n=m}^{N-1}(a_n-a_{n+1})
=
a_m-a_N.
$$
Hence
$$
\left|
\sum_{n=m}^N a_nb_n
\right|
\le
Ma_N+Ma_m+M(a_m-a_N)
=
2Ma_m.
$$

:::

:::

::: {.pf-step #s1-3}

The series
$$
\sum_{n=1}^{\infty}a_nb_n
$$
satisfies the Cauchy criterion.


::: pf-proof

Let $\varepsilon>0$. Since
$$
a_m\to0,
$$
choose $m_0$ such that
$$
2Ma_m<\varepsilon
$$
for every $m\ge m_0$.
Then for every $N\ge m\ge m_0$, step [](#s1-2){.pf-ref} gives
$$
\left|
\sum_{n=m}^N a_nb_n
\right|
<
\varepsilon.
$$
Thus the tails satisfy the Cauchy criterion.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\sum_{n=1}^{\infty}a_nb_n\text{ converges}.}
$$


::: pf-proof

The real numbers are complete, so the Cauchy criterion in step [](#s1-3){.pf-ref} implies convergence of the series.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
