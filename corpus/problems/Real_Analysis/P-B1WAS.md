---
schema: qual/card@1
id: P-B1WAS
kind: problem
title: 'Uniform convergence of $x/(1+x)^{n+1}$ and of its series on $[0,\infty)$ and $[a,\infty)$'
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-30
  note: 'Split from P-4FH62, where it was part (j).'
---

::: {.problem}
Let $h_n(x) = \dfrac{x}{(1+x)^{n+1}}$.

1. Prove that $h_n$ converges uniformly to $0$ on $[0,\infty)$.

2. Verify that
    $$
    \sum_{n=0}^\infty h_n(x) = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{if } x = 0. \end{cases}
    $$
    Does $\sum_{n=0}^\infty h_n$ converge uniformly on $[0,\infty)$?

3. Prove that $\sum_{n=0}^\infty h_n$ converges uniformly on $[a,\infty)$ for any $a > 0$.
:::

::: {.solution}

::: pf

::: pf-step

$h_n\to0$ uniformly on $[0,\infty)$; $\sum_{n\ge0}h_n$ equals $1$ for $x > 0$ and $0$ at $x = 0$; it converges uniformly on each $[a,\infty)$ with $a>0$ but $\boxed{\text{not}}$ on $[0,\infty)$.

::: pf-proof

For $n\ge1$, $h_n'(x) = (1-nx)(1+x)^{-n-2}$, so the maximum on $[0,\infty)$ is at $x=1/n$, with
$$
\norm{h_n}_\infty=\frac{n^n}{(n+1)^{n+1}}\le\frac1{n+1}\to0.
$$
For $x>0$,
$$
\sum_{n=0}^\infty h_n(x)
=\frac{x}{1+x}\sum_{n=0}^\infty(1+x)^{-n}=1,
$$
while at $x=0$ every term is $0$. The uniform limit of continuous functions is continuous and this sum is not, so the convergence is not uniform on $[0,\infty)$. For $x > 0$ the tail $\sum_{n \geq N} h_n(x)$ equals $(1+x)^{-N}$, whose supremum on $[a,\infty)$ is $(1+a)^{-N}\to0$.

:::

:::

:::

:::
