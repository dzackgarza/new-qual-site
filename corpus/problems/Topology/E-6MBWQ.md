---
schema: qual/card@1
id: E-6MBWQ
kind: problem
title: A metrizable space is compact if and only if it is sequentially compact
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Compactness
relations:
- kind: related-to
  target: E-2LZES
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Upstream printed "Show that if X is metrizable, then X is compact", false for R; the statement reads that a metrizable space is compact iff it is sequentially compact.'
---

::: {.exercise}
Show that a metrizable space is compact if and only if it is sequentially compact.
:::

::: {.solution}
Fix a metric $d$ inducing the topology of $X$.

::: pf

::: pf-step

If $X$ is compact, then $X$ is sequentially compact.

::: pf-proof

Let $(x_n)$ be a sequence in $X$ and $S=\{x_n:n\in\NN\}$. If $S$ is finite, some value is taken for infinitely many $n$, which gives a constant, hence convergent, subsequence. Suppose $S$ is infinite and $(x_n)$ has no convergent subsequence. Then no $x\in X$ is a limit point of $S$: otherwise every ball $B(x,1/k)$ would contain infinitely many points of $S$, and we could choose $n_1<n_2<\cdots$ with $d(x_{n_k},x)<1/k$. So each $x\in X$ has a ball $U_x$ meeting $S$ in finitely many points. Finitely many $U_x$ cover $X$, so $S$ is finite, a contradiction.

:::

:::

::: pf-step

If $X$ is sequentially compact, then $X$ is compact.

::: pf-proof

Let $\mathcal{U}$ be an open cover of $X$.

::: {.pf-step #s2-1}

There is $\delta>0$ such that every ball $B(y,\delta)$ lies in some member of $\mathcal{U}$.

::: pf-proof

Otherwise choose, for each $n$, a point $x_n$ such that $B(x_n,1/n)$ lies in no member of $\mathcal{U}$. A subsequence $x_{n_k}$ converges to some $x$. Choose $U\in\mathcal{U}$ and $r>0$ with $B(x,r)\subseteq U$, and $k$ with $d(x_{n_k},x)<r/2$ and $1/n_k<r/2$. Then $B(x_{n_k},1/n_k)\subseteq B(x,r)\subseteq U$ by the triangle inequality, a contradiction.

:::

:::

::: {.pf-step #s2-2}

For every $\delta>0$, finitely many balls of radius $\delta$ cover $X$.

::: pf-proof

Otherwise choose inductively $y_{n+1}\notin\bigcup_{i\le n}B(y_i,\delta)$. Then $d(y_i,y_j)\ge\delta$ for $i\ne j$, so $(y_n)$ has no Cauchy, hence no convergent, subsequence.

:::

:::

::: pf-qed

Take $\delta$ from step [](#s2-1){.pf-ref} and, by step [](#s2-2){.pf-ref}, balls $B(y_1,\delta),\ldots,B(y_N,\delta)$ covering $X$. Each $B(y_i,\delta)$ lies in some $U_i\in\mathcal{U}$, so $U_1,\ldots,U_N$ is a finite subcover.

:::

:::

:::

:::

:::

::: {.remark}
In Munkres, *Topology*, §28, Theorem 28.2 states this equivalence together with limit point compactness as a third equivalent condition.
:::
