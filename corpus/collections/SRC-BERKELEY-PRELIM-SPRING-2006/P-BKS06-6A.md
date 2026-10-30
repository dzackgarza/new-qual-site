---
schema: qual/card@1
id: P-BKS06-6A
kind: problem
title: Bounded quadratic variation implies at most countably many discontinuities
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Let $u \colon \RR \to \RR$ be a function for which there exists $B > 0$ such that
$$
\sum_{k=1}^{N-1} \abs{u(x_{k+1}) - u(x_{k})}^{2} \leq B
$$
for all finite increasing sequences $x_{1} < x_{2} < \cdots < x_{N}$. Show that $u$ has at most countably many discontinuities.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $m\ge1$, let $D_m$ be the set of points $x$ such that every interval $(x-\delta,x+\delta)$ contains points $y<z$ with $\abs{u(z)-u(y)}>\frac1m$. Then the set of discontinuities of $u$ is contained in $\bigcup_{m\ge1}D_m$.

::: pf-proof

Let $u$ be discontinuous at $x$. Then there are $\varepsilon>0$ and points $x_n\to x$, $x_n\ne x$, with $\abs{u(x_n)-u(x)}>\varepsilon$. Choose $m$ with $\frac1m<\varepsilon$. Every interval around $x$ contains some $x_n$, and the pair $\{x,x_n\}$, put in increasing order, has the property that defines $D_m$. So $x\in D_m$.

:::

:::

::: {.pf-step #s2}

Each $D_m$ has at most $Bm^2$ points.

::: pf-proof

Let $x_1<\cdots<x_k$ be points of $D_m$. Choose disjoint open intervals $I_1,\ldots,I_k$ around them, with every point of $I_i$ less than every point of $I_{i+1}$. In each $I_i$ choose $y_i<z_i$ with $\abs{u(z_i)-u(y_i)}>\frac1m$. Then $y_1<z_1<y_2<z_2<\cdots<y_k<z_k$ is an increasing sequence, and by the hypothesis
$$
\frac{k}{m^2}<\sum_{i=1}^k\abs{u(z_i)-u(y_i)}^2\le B,
$$
because the sum on the left is part of the sum of squared increments along this sequence. So $k<Bm^2$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the discontinuities of $u$ lie in a countable union of finite sets, so they are at most countable.

:::

:::

:::
