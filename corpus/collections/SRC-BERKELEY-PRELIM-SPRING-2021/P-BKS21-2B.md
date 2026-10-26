---
schema: qual/card@1
id: P-BKS21-2B
kind: problem
title: Projection of a closed set from a compact factor is closed
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $X$ be compact metric, $Y$ metric, and $p:X\times Y\to Y$ the projection. Show that if $Z\subseteq X\times Y$ is closed, then $p(Z)$ is closed in $Y$.
:::

::: pf

::: pf-step

Let $(y_n)$ be a sequence in $p(Z)$ converging to some $y\in Y$. For each $n$ there is $x_n\in X$ such that
$$
(x_n,y_n)\in Z.
$$


::: pf-proof

The condition $y_n\in p(Z)$ means exactly that some point of $Z$ has second coordinate $y_n$. Choose one such first coordinate and call it $x_n$.

:::

:::

::: pf-step

There is a subsequence $(x_{n_k})$ converging to some $x\in X$.


::: pf-proof

The space $X$ is compact and metric, hence sequentially compact. Apply sequential compactness to the sequence $(x_n)$.

:::

:::

::: pf-step

The corresponding subsequence in the product satisfies
$$
(x_{n_k},y_{n_k})\longrightarrow(x,y)
$$
in $X\times Y$.


::: pf-proof

By step <1>2,
$$
x_{n_k}\to x.
$$
Since the original sequence $y_n$ converges to $y$, every subsequence does also:
$$
y_{n_k}\to y.
$$
Convergence in a product of metric spaces is coordinatewise, so the displayed product convergence follows.

:::

:::

::: pf-step

The limit point $(x,y)$ belongs to $Z$.


::: pf-proof

Every point $(x_{n_k},y_{n_k})$ lies in $Z$ by step <1>1. Since $Z$ is closed in the metric space $X\times Y$, it contains the limit of every convergent sequence of its points. Apply step <1>3.

:::

:::

::: pf-step

The limit $y$ belongs to $p(Z)$.


::: pf-proof

Step <1>4 gives $(x,y)\in Z$. Applying the projection gives
$$
p(x,y)=y\in p(Z).
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{p(Z)\ \text{is closed in }Y}.
$$


::: pf-proof

Steps <1>1--<1>5 show that every convergent sequence in $p(Z)$ has its limit in $p(Z)$. Since $Y$ is metric, sequentially closed subsets are closed.

:::

:::

::: pf-qed

Step <1>6 is the desired conclusion.

:::

:::
