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

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let $(y_n)$ be a sequence in $p(Z)$ converging to some $y\in Y$. For each $n$ there is $x_n\in X$ such that
$$
(x_n,y_n)\in Z.
$$


::: pf-proof

The condition $y_n\in p(Z)$ means exactly that some point of $Z$ has second coordinate $y_n$. Choose one such first coordinate and call it $x_n$.

:::

:::

::: {.pf-step #s1-2}

There is a subsequence $(x_{n_k})$ converging to some $x\in X$.


::: pf-proof

The space $X$ is compact and metric, hence sequentially compact. Apply sequential compactness to the sequence $(x_n)$.

:::

:::

::: {.pf-step #s1-3}

The corresponding subsequence in the product satisfies
$$
(x_{n_k},y_{n_k})\longrightarrow(x,y)
$$
in $X\times Y$.


::: pf-proof

By step [](#s1-2){.pf-ref},
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

::: {.pf-step #s1-4}

The limit point $(x,y)$ belongs to $Z$.


::: pf-proof

Every point $(x_{n_k},y_{n_k})$ lies in $Z$ by step [](#s1-1){.pf-ref}. Since $Z$ is closed in the metric space $X\times Y$, it contains the limit of every convergent sequence of its points. Apply step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The limit $y$ belongs to $p(Z)$.


::: pf-proof

Step [](#s1-4){.pf-ref} gives $(x,y)\in Z$. Applying the projection gives
$$
p(x,y)=y\in p(Z).
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{p(Z)\ \text{is closed in }Y}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} show that every convergent sequence in $p(Z)$ has its limit in $p(Z)$. Since $Y$ is metric, sequentially closed subsets are closed.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the desired conclusion.

:::

:::

:::
