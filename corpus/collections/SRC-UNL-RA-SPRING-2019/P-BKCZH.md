---
schema: qual/card@1
id: P-BKCZH
kind: problem
title: $\abs{f'}\le k\abs{f}$ and $f(0)=0$ imply $f\equiv 0$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the preserved UNL January 23, 2019 qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Suppose that $f:[0,1]\to\RR$ is differentiable, $f(0)=0$, and there is $k>0$ such that
$$
\abs{f'(x)}\le k\abs{f(x)}
\qquad(x\in[0,1]).
$$
Prove that $f(x)=0$ for all $x\in[0,1]$.
:::

::: {.solution}

Let $M \coloneqq \max_{[0,1]}\abs{f}$, which is finite because $f$ is continuous on $[0,1]$.

::: pf

::: {.pf-step #integral}

$\abs{f(x)} \le k\int_0^x \abs{f(t)}\,dt$ for $0 \le x \le 1$.

::: pf-proof

The derivative bound gives $\abs{f'} \le kM$, so $f$ is Lipschitz and hence absolutely continuous. By the fundamental theorem of calculus and $f(0)=0$, $\abs{f(x)} = \abs{\int_0^x f'(t)\,dt} \le k\int_0^x \abs{f(t)}\,dt$.

:::

:::

::: {.pf-step #iterate}

$\abs{f(x)} \le M\frac{(kx)^n}{n!}$ for every integer $n \ge 1$ and $0 \le x \le 1$.

::: pf-proof

We induct on $n$. For $n = 1$, step [](#integral){.pf-ref} and $\abs{f} \le M$ give $\abs{f(x)} \le kMx$. If the bound holds for $n$, then step [](#integral){.pf-ref} gives $\abs{f(x)} \le k\int_0^x M\frac{(kt)^n}{n!}\,dt = M\frac{(kx)^{n+1}}{(n+1)!}$.

:::

:::

::: pf-step

$\boxed{f \equiv 0 \text{ on } [0,1]}$.

::: pf-proof

For fixed $x \in [0,1]$, step [](#iterate){.pf-ref} gives $0 \le \abs{f(x)} \le M\frac{(kx)^n}{n!}$, and the right side tends to $0$ as $n \to \infty$.

:::

:::

:::

:::
