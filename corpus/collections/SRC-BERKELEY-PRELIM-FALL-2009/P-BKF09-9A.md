---
schema: qual/card@1
id: P-BKF09-9A
kind: problem
title: Locally uniform convergence of $(1+z/n)^n$ to $e^z$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow under the limit and separated the display from the prose against f09solutions.pdf page 4 problem 9A.
---

::: {.problem}
Show that

$$
\lim_{n \to \infty} \left( 1 + \frac{z}{n} \right)^n = e^z
$$

uniformly on compact subsets of $\mathbb{C}$.
:::

::: {.solution}
Since $\log(1+u)$ is holomorphic for $\abs{u}<1$ and has Taylor expansion at $0$ $\sum_{k\ge1}(-1)^{k+1}u^k/k$, we infer for $\abs{u}\le1/2$ that
$$
\abs{\log(1+u)-u}\le C\abs{u}^2
$$
for some constant $C$. If $n>2N$ and $\abs{z}\le N$ this gives $\left\lvert\log\left(1+\frac{z}{n}\right)-\frac{z}{n}\right\rvert\le CN^2n^{-2}$ and $\left\lvert\log\left(1+\frac{z}{n}\right)^n-z\right\rvert\le CN^2n^{-1}$.
On the other hand, since $\abs{\sum_{k>0}a^k/k!}\le\sum_{k>0}\abs{a}^k/k!$, we have $\abs{e^a-1}\le e^{\abs{a}}-1$.
Hence if $n>2N$ and $\abs{z}\le N$ we find
$$
\left\lvert\left(1+\frac{z}{n}\right)^n-e^z\right\rvert=\abs{e^z}\cdot\left\lvert e^{\log\left(1+\frac{z}{n}\right)^n-z}-1\right\rvert\le e^N\cdot\left(e^{CN^2n^{-1}}-1\right),
$$
so that $\lim_{n\to\infty}\left\lvert\left(1+\frac{z}{n}\right)^n-e^z\right\rvert=0$ uniformly for $\abs{z}\le N$.
:::
