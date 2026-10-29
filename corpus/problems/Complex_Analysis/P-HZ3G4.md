---
schema: qual/card@1
id: P-HZ3G4
kind: problem
title: Uniform convergence of $\sum\sin(nz)/2^n$ on closed substrips of $\{|\Im z|<\ln 2\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Convergence Tests
  - Series of Functions
  - Trigonometry
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source asked for uniform convergence on {Im z < ln 2}, which is false since the terms do not tend to zero at z = -iy with y > ln 2; the statement now asks for uniform convergence on each closed substrip {|Im z| <= a} with 0 <= a < ln 2.'
---

::: {.problem}
Prove that the following series converges uniformly on each set $\theset{z \suchthat \abs{\Im(z)} \le a}$ with $0 \le a < \ln 2$:
\[
\sum_{n=1}^\infty {\sin(nz) \over 2^n}
.\]
:::

::: {.solution}

::: pf

::: {.pf-step #term-bound}

If $\abs{\Im z} \le a$, then $\abs{\sin(nz)} \le e^{na}$ for every $n \ge 1$.

::: pf-proof

Write $z = x + iy$. Then $\sin(nz) = \frac{e^{inz} - e^{-inz}}{2i}$, with $\abs{e^{inz}} = e^{-ny}$ and $\abs{e^{-inz}} = e^{ny}$, so $\abs{\sin(nz)} \le \frac12\left(e^{-ny} + e^{ny}\right) \le e^{n\abs y} \le e^{na}$.

:::

:::

::: pf-qed

By step [](#term-bound){.pf-ref}, on $\theset{\abs{\Im z} \le a}$ the $n$-th term is bounded by $M_n = (e^a/2)^n$. Since $e^a < 2$, $\sum_n M_n$ is a convergent geometric series, and the Weierstrass $M$-test gives uniform convergence on $\theset{\abs{\Im z} \le a}$.

:::

:::

:::
