---
schema: qual/card@1
id: P-WESTOP13-I4
kind: problem
title: Urysohn metrization and a metrizable counterexample to its hypotheses
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. State the Urysohn Metrization Theorem and illustrate it with two examples.
2. Describe in detail a metric space that does not satisfy the hypotheses of the Urysohn Metrization Theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

**Urysohn Metrization Theorem.** Every regular second-countable space is metrizable.


::: pf-proof

Here regular includes the $T_1$ separation axiom: points and disjoint closed sets can be separated by disjoint open neighborhoods. The theorem asserts that under regularity and a countable basis there exists a metric whose induced topology is the given topology.

:::

:::

::: {.pf-step #s1-2}

The Euclidean space $\RR^n$ illustrates the theorem.


::: pf-proof

The space $\RR^n$ is regular because it is a metric space. It is second countable: the collection of open balls with rational centers and positive rational radii is a countable basis. Hence the Urysohn Metrization Theorem applies. In this case the resulting metrizability is already realized by the Euclidean metric.

:::

:::

::: {.pf-step #s1-3}

The countable product
$$
X=[0,1]^{\NN}
$$
with the product topology also illustrates the theorem.


::: pf-proof

Each factor $[0,1]$ is regular. A product of regular Hausdorff spaces is regular. The product is second countable: if $\mathcal B$ is a countable basis of $[0,1]$, then the basic product sets in which only finitely many coordinates are restricted to members of $\mathcal B$ form a countable basis, because the set of finite subsets of $\NN$ and all finite tuples from a countable set are countable.

Thus Urysohn's theorem gives a metric inducing the product topology. One explicit such metric is
$$
d(x,y)=\sum_{n=1}^{\infty}2^{-n}|x_n-y_n|.
$$

:::

:::

::: {.pf-step #s1-4}

Let $X$ be any uncountable set and give it the discrete metric
$$
d(x,y)=
\begin{cases}
0,&x=y,\\
1,&x\ne y.
\end{cases}
$$
Then $X$ is metrizable but is not second countable.


::: pf-proof

The displayed function is a metric. Its open ball of radius $1/2$ about $x$ is the singleton $\{x\}$, so the induced topology is the discrete topology.

Suppose $\mathcal C$ were a basis for this topology. For each $x\in X$, since $\{x\}$ is open, there must be some $C_x\in\mathcal C$ such that
$$
x\in C_x\subseteq\{x\}.
$$
Thus $C_x=\{x\}$. Hence every singleton belongs to every basis, so
$$
|\mathcal C|\ge |X|.
$$
Because $X$ is uncountable, no basis can be countable. Therefore $X$ is not second countable.

:::

:::

::: {.pf-step #s1-5}

The example in step [](#s1-4){.pf-ref} does satisfy the regularity hypothesis, but fails the second-countability hypothesis; nevertheless it is metrizable.


::: pf-proof

Every discrete space is regular: a point and a closed set not containing it are separated by the disjoint open sets consisting of the point and the complement of that point. Step [](#s1-4){.pf-ref} proves failure of second countability, while the discrete metric already supplies metrizability. Thus Urysohn's hypotheses are sufficient but not necessary.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} states the theorem, steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} give two illustrations, and steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} give the requested metrizable space that fails one of the hypotheses.

:::

:::

:::
