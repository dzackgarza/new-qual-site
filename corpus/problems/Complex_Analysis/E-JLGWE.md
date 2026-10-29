---
schema: qual/card@1
id: E-JLGWE
kind: problem
title: Extended Liouville theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source prints "polynomal"; the statement reads "polynomial".
---

::: {.exercise}
Let $f$ be an entire function. Assume that for some $k \in \NN$, and sufficiently large $\abs{z}$, we have that $\abs{f(z)} \leq A+B\abs{z}^{k}$. Prove that $f$ is a polynomial of degree at most $k$.

:::

::: {.solution}
We induct on $k\ge0$, for all constants $A,B\ge0$ at once.

::: pf

::: pf-step
If $k=0$, then $f$ is constant.

::: pf-proof
There is $R>0$ with $\abs{f}\le A+B$ for $\abs z\ge R$, and $f$ is bounded on the compact disk $\abs z\le R$ by continuity. So $f$ is a bounded entire function, and it is constant by Liouville's theorem.
:::

:::

::: {.pf-step #g-bound}
Let $k\ge1$ and $\abs{f(z)}\le A+B\abs z^k$ for $\abs z\ge R$. The function $g$ defined by $g(z)\coloneqq\frac{f(z)-f(0)}{z}$ for $z\neq0$ and $g(0)\coloneqq f'(0)$ is entire and satisfies $\abs{g(z)}\le\qty{A+\abs{f(0)}}+B\abs z^{k-1}$ for $\abs z\ge\max(R,1)$.

::: pf-proof
The singularity of $\frac{f(z)-f(0)}{z}$ at $0$ is removable with value $f'(0)$, so $g$ is entire. For $\abs z\ge\max(R,1)$,
$$
\abs{g(z)}\le\frac{A+\abs{f(0)}+B\abs z^k}{\abs z}\le\qty{A+\abs{f(0)}}+B\abs z^{k-1}.
$$
:::

:::

::: pf-step
If $k\ge1$, then $f$ is a polynomial of degree at most $k$.

::: pf-proof
By step [](#g-bound){.pf-ref} and the induction hypothesis for $k-1$, $g$ is a polynomial of degree at most $k-1$, so $f(z)=f(0)+zg(z)$ is a polynomial of degree at most $k$.
:::

:::

:::

:::
