---
schema: qual/card@1
id: P-RAF21F
kind: problem
title: "A sum of point masses $\\sum_j c_j\\delta_{x_j}$ is Radon iff the weights along every convergent subsequence are summable"
classification:
  areas:
  - real-analysis
  topics:
  - Radon Measures
  - Dirac Measures
  - Borel Measures
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
Let $\delta_x$ denote the Dirac delta mass at $x \in \mathbb{R}^n$.
Let $\{x_j\}_{j=1}^\infty$ be a sequence in $\mathbb{R}^n$, $\{c_j\}_{j=1}^\infty$ a sequence of positive numbers, and $\mu$ the Borel measure on $\mathbb{R}^n$ corresponding to the series $\sum_{j=1}^\infty c_j \delta_{x_j}$.
Prove that $\mu$ is Radon if and only if for all convergent subsequences $\{x_{j_k}\}_{k=1}^\infty$ it holds that $\sum_{k=1}^\infty c_{j_k} < \infty$.
:::

::: {.solution}
On $\mathbb R^n$, a Borel measure is Radon if and only if it is finite on compact sets.

::: pf

::: {.pf-step #s1}

If $\mu$ is Radon, then $\sum_k c_{j_k}<\infty$ for every convergent subsequence $\{x_{j_k}\}$.

::: pf-proof

Let $x_{j_k}\to x$. The set $K\coloneqq\{x\}\cup\{x_{j_k}:k\ge1\}$ is compact, so $\mu(K)<\infty$. The indices $j_k$ are distinct and each $x_{j_k}$ lies in $K$, so
$$
\sum_{k=1}^\infty c_{j_k}\le\sum_{j:\,x_j\in K}c_j=\mu(K)<\infty.
$$

:::

:::

::: {.pf-step #s2}

If $\sum_k c_{j_k}<\infty$ for every convergent subsequence, then $\mu(C)<\infty$ for every compact $C\subseteq\mathbb R^n$.

::: pf-proof

::: {.pf-step #s2-1}

Suppose, for a contradiction, that $C$ is compact and $\mu(C)=\infty$. Then some $x\in C$ satisfies $\mu(C\cap B(x,r))=\infty$ for every $r>0$.

::: pf-proof

Otherwise every $y\in C$ has a radius $r_y>0$ with $\mu(C\cap B(y,r_y))<\infty$.
Finitely many of the balls $B(y,r_y)$ cover the compact set $C$, so $\mu(C)<\infty$.

:::

:::

::: pf-step

There are finite sets of indices $I_1,I_2,\ldots$ with $\max I_{m-1}<\min I_m$, $x_j\in B(x,1/m)$ for $j\in I_m$, and $\sum_{j\in I_m}c_j>1$.

::: pf-proof

Suppose $I_1,\ldots,I_{m-1}$ are chosen and let $N=\max I_{m-1}$ (with $N=0$ when $m=1$).
Since each $c_j$ is finite and $\sum_{j:\,x_j\in B(x,1/m)}c_j=\infty$ by step [](#s2-1){.pf-ref}, the sum over the indices $j>N$ with $x_j\in B(x,1/m)$ is also infinite, so a finite set of such indices has sum greater than $1$.

:::

:::

::: pf-qed

Listing the indices of $I_1,I_2,\ldots$ in increasing order gives a subsequence $\{x_{j_k}\}$ that converges to $x$, because every index in $I_m$ has $|x_j-x|<1/m$.
Its weights satisfy
$$
\sum_{k=1}^\infty c_{j_k}=\sum_{m=1}^\infty\sum_{j\in I_m}c_j=\infty,
$$
which contradicts the hypothesis.

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the forward implication. Step [](#s2){.pf-ref} shows that $\mu$ is finite on compact sets, hence Radon on $\mathbb R^n$.

:::

:::

:::
