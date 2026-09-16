---
schema: qual/card@1
id: FF-IAUQG
kind: fact
title: Weierstrass $M$-test for uniform convergence
prompts:
- What is the $M{\hbox{-}}$test?
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
---

::: {.fact}
Let $A$ be a set and let $f_n\colon A\to\CC$ for $n\geq 0$.
Put $\norm{f_n}_{\infty, A}\coloneqq\sup_{x\in A}\abs{f_n(x)}$.
If $\sum_{n\geq 0}\norm{f_n}_{\infty, A} < \infty$, then for every $x\in A$ the series $\sum_{n\geq 0} f_n(x)$ converges absolutely, and its partial sums [[D-YZC3C|converge uniformly]] on $A$ to $\sum_{n\geq 0} f_n$.

Equivalently, the conclusion holds whenever there are real numbers $M_n$ with $\abs{f_n(x)} \leq M_n$ for all $x\in A$ and $n\geq 0$ and $\sum_{n\geq 0} M_n < \infty$.
:::

::: {.proof}
For each $x$, $\sum_n\abs{f_n(x)}\leq\sum_n M_n<\infty$, so $S(x)\coloneqq\sum_{n\geq 0}f_n(x)$ exists.
For $x\in A$ and $N\geq 0$, $\abs{S(x) - \sum_{n=0}^{N}f_n(x)}\leq\sum_{n>N}M_n$, which tends to $0$ as $N\to\infty$ independently of $x$.
The first form is the case $M_n = \norm{f_n}_{\infty,A}$, and conversely $\norm{f_n}_{\infty,A}\leq M_n$.
:::
