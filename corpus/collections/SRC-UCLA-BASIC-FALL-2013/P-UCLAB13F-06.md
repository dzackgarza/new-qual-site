---
schema: qual/card@1
id: P-UCLAB13F-06
kind: problem
title: A subsequence criterion for convergence in a compact metric space
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Let $X$ be a compact metric space, let $(x_n)$ be a sequence in $X$, and let $x\in X$. Assume that every subsequence $(y_n)$ of $(x_n)$ has a subsequence $(z_n)$ converging to $x$. Prove that $x_n\to x$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that
$$
x_n\not\to x.
$$


::: pf-proof

This is the negation of the desired conclusion.

:::

:::

::: {.pf-step #s1-2}

There exists $\varepsilon>0$ such that for every $N$ there is some $n\ge N$ with
$$
d(x_n,x)\ge\varepsilon.
$$


::: pf-proof

This is exactly the negation of convergence in a metric space.

:::

:::

::: {.pf-step #s1-3}

One can choose a subsequence
$$
y_k=x_{n_k}
$$
such that
$$
d(y_k,x)\ge\varepsilon
$$
for every $k$.


::: pf-proof

Choose $n_1$ using step [](#s1-2){.pf-ref} with $N=1$.
After choosing $n_k$, use step [](#s1-2){.pf-ref} with
$$
N=n_k+1
$$
to choose
$$
n_{k+1}>n_k
$$
with
$$
d(x_{n_{k+1}},x)\ge\varepsilon.
$$
This inductively defines the required subsequence.

:::

:::

::: {.pf-step #s1-4}

No subsequence of $(y_k)$ can converge to $x$.


::: pf-proof

Every term of every subsequence of $(y_k)$ remains at distance at least $\varepsilon$ from $x$.
But any sequence converging to $x$ must eventually lie in the open ball
$$
B(x,\varepsilon).
$$
Thus no subsequence of $(y_k)$ can converge to $x$.

:::

:::

::: {.pf-step #s1-5}

Step [](#s1-4){.pf-ref} contradicts the hypothesis of the problem.


::: pf-proof

The sequence $(y_k)$ constructed in step [](#s1-3){.pf-ref} is itself a subsequence of $(x_n)$.
By hypothesis, every subsequence of $(x_n)$ must have a further subsequence converging to $x$.
Step [](#s1-4){.pf-ref} says this particular subsequence has no such further subsequence.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{x_n\to x}.
$$


::: pf-proof

The assumption in step [](#s1-1){.pf-ref} leads to the contradiction in step [](#s1-5){.pf-ref}.
Hence the assumption is false, and the sequence converges to $x$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
