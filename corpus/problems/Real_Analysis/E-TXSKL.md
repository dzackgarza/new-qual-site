---
schema: qual/card@1
id: E-TXSKL
kind: problem
title: $\lim_{n\to\infty}\sum_{k\ge 1}k^{-2}\sin^n(k)$ and $\lim_{n\to\infty}\sum_{k\ge
  1}k^{-1}e^{-k/n}$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Series of Numbers
  - Fatou
relations: []
review: draft
---

::: {.exercise}
Compute the following limits:

- $\lim_{n\to\infty} \sum_{k\geq 1} {1\over k^2} \sin^n(k)$
- $\lim_{n\to\infty} \sum_{k\geq 1} {1\over k} e^{-k/n}$
:::

::: {.solution}
Both sums are integrals against counting measure on $\theset{1, 2, \ldots}$.

<1>1. $\lim_{n\to\infty} \sum_{k\geq 1} \frac{\sin^n(k)}{k^2} = \boxed{0}$.

<2>1. $\abs{\sin k} < 1$ for every integer $k \geq 1$.

::: {.proof}
$\abs{\sin k} = 1$ would force $k = \pi/2 + m\pi$ for some $m \in \ZZ$, so $\pi = 2k/(2m+1)$ would be rational.
:::

<2>2. $\sin^n(k)/k^2 \to 0$ for each $k$, and $\abs{\sin^n(k)/k^2} \leq 1/k^2$.

::: {.proof}
The limit follows from step <2>1, and the bound from $\abs{\sin k} \leq 1$.
:::

<2>3. Q.E.D.

::: {.proof}
$\sum_k 1/k^2 < \infty$, so by step <2>2 the dominated convergence theorem gives $\lim_n \sum_k \sin^n(k)/k^2 = \sum_k 0 = 0$.
:::

<1>2. $\lim_{n\to\infty} \sum_{k\geq 1} \frac{e^{-k/n}}{k} = \boxed{\infty}$.

::: {.proof}
The terms are nonnegative and $e^{-k/n}/k \to 1/k$ for each $k$. By Fatou's lemma,
$$
\liminf_{n\to\infty} \sum_{k\geq 1} \frac{e^{-k/n}}{k}
\geq \sum_{k\geq 1} \liminf_{n\to\infty} \frac{e^{-k/n}}{k}
= \sum_{k\geq 1} \frac{1}{k}
= \infty.
$$
:::
:::
