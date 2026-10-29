---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-15
kind: problem
title: A series that is uniformly convergent away from zero but not near zero
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
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove that the series $$x^2+\frac{x^2}{1+x^2}+\frac{x^2}{(1+x^2)^2}+\frac{x^2}{(1+x^2)^3}+\cdots$$ converges uniformly on $[a,\infty)$ for every $a>0$; but not uniformly on $[0,b]$ for any $b>0$.
:::

::: {.solution}

Write the series as $\sum_{k=0}^\infty x^2(1+x^2)^{-k}$, a geometric series with ratio $1/(1+x^2)$, and let $R_N(x)\coloneqq\sum_{k=N+1}^\infty x^2(1+x^2)^{-k}$ be its $N$-th tail.

::: pf

::: {.pf-step #tail}

$R_N(x) = (1+x^2)^{-N}$ for $x \neq 0$, and $R_N(0) = 0$.

::: pf-proof

For $x\neq0$ the ratio $1/(1+x^2)$ lies in $(0,1)$, and the geometric tail formula gives
$$
R_N(x)=\frac{x^2}{(1+x^2)^{N+1}} \cdot \frac{1}{1 - 1/(1+x^2)} = \frac{x^2}{(1+x^2)^{N+1}} \cdot \frac{1+x^2}{x^2} = \frac{1}{(1+x^2)^N}.
$$
At $x = 0$ every term is $0$.

:::

:::

::: pf-step

For $a>0$, $\sup_{x \ge a} \abs{R_N(x)} \le (1+a^2)^{-N} \to 0$, so the series converges uniformly on $[a,\infty)$.

::: pf-proof

For $x \ge a$, $1 + x^2 \ge 1 + a^2$, so step [](#tail){.pf-ref} gives $R_N(x) = (1+x^2)^{-N} \le (1+a^2)^{-N}$. Since $1 + a^2 > 1$, $(1+a^2)^{-N} \to 0$.

:::

:::

::: pf-step

For $b>0$, $\sup_{x \in [0,b]} \abs{R_N(x)} = 1$ for every $N$, so the series does not converge uniformly on $[0,b]$.

::: pf-proof

By step [](#tail){.pf-ref}, $R_N(x) = (1+x^2)^{-N} \to 1$ as $x \to 0^+$, and $R_N\le1$ on $[0,b]$. So the suprema of the tails do not tend to $0$, which is the negation of uniform convergence.

:::

:::

:::

:::

::: {.remark}
Equivalently, the pointwise sum is $1+x^2$ for $x\neq0$ and $0$ at $x=0$. It is discontinuous at $0$, while the partial sums are continuous, so the convergence cannot be uniform on any interval containing $0$.
:::
