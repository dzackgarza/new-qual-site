---
schema: qual/card@1
id: P-CASP09D
kind: problem
title: "Derivative estimate for an analytic function at the origin"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Suppose $f(z)$ is analytic at $z = 0$.
Prove that there is an integer $n > 0$ such that $|f^{(n)}(0)| \leq n^n \cdot n!$.
:::

::: {.solution}
**Goal.** Show there is $n > 0$ with $|f^{(n)}(0)| \le n^n n!$.

::: pf

::: pf-step
$f$ is analytic at $0$, so it has a power series $f(z) = \sum_{k=0}^\infty a_k z^k$ with positive radius of convergence $R > 0$.

::: pf-proof
analyticity at $0$.
:::

:::

::: {.pf-step #s2}
By Cauchy's estimate, $|a_k| = \frac{|f^{(k)}(0)|}{k!} \le \frac{M(r)}{r^k}$ for $0 < r < R$, where $M(r) = \max_{|z|=r} |f(z)|$.

::: pf-proof
Cauchy's inequality for the Taylor coefficients.
:::

:::

::: {.pf-step #s3}
Choose $n$ large enough that $M(r) \le n^n r^n$ for some $r$.

::: pf-proof

::: {.pf-step #s3-1}
Since $M(r)$ is finite for $r < R$, and $n^n r^n \to \infty$ as $n \to \infty$ (for $r > 1/e$), there is $n$ with $M(r) \le n^n r^n$.

::: pf-proof
pick $r$ with $r > 1/e$ (possible since $R > 0$); then $n^n r^n \to \infty$, so for large $n$, $n^n r^n \ge M(r)$.
:::

:::

::: {.pf-step #s3-2}
Hence $|f^{(n)}(0)| = n! |a_n| \le n! \frac{M(r)}{r^n} \le n! \frac{n^n r^n}{r^n} = n^n n!$.

::: pf-proof
combine step [](#s2){.pf-ref} and step [](#s3-1){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
step [](#s3-2){.pf-ref} gives $|f^{(n)}(0)| \le n^n n!$ for some $n > 0$.
:::

:::
:::
