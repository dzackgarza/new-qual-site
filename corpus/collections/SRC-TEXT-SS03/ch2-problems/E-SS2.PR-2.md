---
schema: qual/card@1
id: E-SS2.PR-2
kind: problem
title: Growth of $\sum d(n)z^n$ along rational rays
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
2. $^\ast$ Let

$$
F (z) = \sum_ {n = 1} ^ {\infty} d (n) z ^ {n} \quad \mathrm{for} | z | <   1
$$

where $d ( n )$ denotes the number of divisors of $n .$ Observe that the radius of convergence of this series is 1. Verify the identity

$$
\sum_ {n = 1} ^ {\infty} d (n) z ^ {n} = \sum_ {n = 1} ^ {\infty} \frac {z ^ {n}}{1 - z ^ {n}}.
$$

Using this identity, show that if $z = r$ with $0 < r < 1$ , then

$$
| F (r) | \geq c \frac {1}{1 - r} \log (1 / (1 - r))
$$

as $r \to 1$ . Similarly, if $\theta = 2 \pi p / q$ where $p$ and $q$ are positive integers and $z = r e ^ { i \theta }$ then

$$
| F (r e ^ {i \theta}) | \geq c _ {p / q} \frac {1}{1 - r} \log (1 / (1 - r))
$$
:::

::: {.solution}
<1>1. $\sum_{n\ge1} d(n) z^n = \sum_{n\ge1} \frac{z^n}{1 - z^n}$ for $\abs z<1$.

::: {.proof}
By the geometric series, $\frac{z^n}{1 - z^n} = \sum_{k\ge1} z^{kn}$. The double series converges absolutely, and the coefficient of $z^m$ in $\sum_n\sum_k z^{kn}$ is the number of pairs $(n,k)$ with $kn = m$, which is $d(m)$.
:::

<1>2. $F(r) \ge c \frac{1}{1-r}\log\frac{1}{1-r}$ as $r \to 1^-$.

::: {.proof}
All terms of $F(r) = \sum_{n} \frac{r^n}{1-r^n}$ are positive. Using $1 - r^n \le n(1-r)$ and keeping the terms with $n \le N$, where $N$ is the integer part of $\frac{1}{1-r}$, gives $F(r)\ge\frac{r^N}{1-r}\sum_{n\le N}\frac1n$. Since $r^N$ is bounded below by a positive constant as $r\to1^-$ and $\sum_{n\le N}\frac1n\ge\log N$, this is at least $c \frac{1}{1-r}\log\frac{1}{1-r}$.
:::

<1>3. For $\theta = 2\pi p/q$, $\abs{F(re^{i\theta})} \ge c_{p/q}\frac{1}{1-r}\log\frac{1}{1-r}$ as $r\to1^-$.

::: {.proof}
Assume $p/q$ is in lowest terms and put $z=re^{i\theta}$. For $q\mid n$, $z^n = r^n$, and the terms with $n=qj$ contribute $\sum_j\frac{r^{qj}}{1-r^{qj}}=F(r^q)$, which by step <1>2 is at least $c\frac{1}{1-r^q}\log\frac{1}{1-r^q}\ge \frac cq\frac{1}{1-r}\log\frac{1}{q(1-r)}$ since $1-r^q\le q(1-r)$. For $q\nmid n$, $e^{in\theta}$ is a $q$th root of unity different from $1$, so $\abs{1-z^n}\ge\delta_q>0$ for $r$ near $1$, and these terms contribute at most $\sum_n r^n/\delta_q=O\bigl(\frac1{1-r}\bigr)$. The logarithmic factor dominates, which gives the bound with a smaller constant $c_{p/q}$.
:::
:::
