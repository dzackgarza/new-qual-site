---
schema: qual/card@1
id: E-7NCMJ
kind: exercise
title: "Compute the following limits:"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Compute the following limits:

- $\lim_{n\to\infty} \sum_{k\geq 1} {1\over k^2} \sin^n(k)$
- $\lim_{n\to\infty} \sum_{k\geq 1} {1\over k} e^{-k/n}$
:::

:::{.solution}
For the first, use that
\[
\abs{ \sum_{k\geq 1} {1\over k^2} \sin^n(k) }
\leq
\sum_{k\geq 1} \abs{ {1\over k^2} \sin^n(k) }
\sum_{k\geq 1} \abs{ {1\over k^2}} < \infty
,\]
since $\abs{\sin(x)} \leq 1$ and $x^n < x$ for $\abs{x}\leq 1$.
By the dominated convergence theorem, we can pass the limit inside.
Using the same fact as above, $\lim_{n\to\infty}\sin^n(x) = 0$,

For the second, the claim is that it diverges (very slowly).
Note that $\lim_{n\to\infty} e^{-k/n} = 1$ for any $k$.
By Fatou, we have
\[
\liminf_{n\to\infty} \sum_{k\geq 1} {e^{-k/n} \over k}
\geq \sum_{k\geq 1} \liminf_{n\to\infty} {e^{-k/n} \over k} 
= \sum_{k\geq 1} {1 \over k} 
= \infty
.\]
:::

