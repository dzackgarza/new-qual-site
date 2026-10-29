---
schema: qual/card@1
id: P-WNOA2
kind: problem
title: Cauchy estimates for a holomorphic function of polynomial growth on a strip
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Suppose that $f$ is holomorphic on the strip $S = \{x+iy \mid x\in \RR,~ -1<y<1\}$ with $\abs{f(z)} \leq A (1 + \abs{z})^\nu$ for $\nu \ge 0$ a fixed real number.
Show that for each integer $n\geq 0$ there exists an $A_n \geq 0$ such that $\abs{f^{(n)}(x)} \leq A_n (1 + \abs{x})^\nu$ for all $x\in \RR$.
:::

::: {.solution}
Fix $n\ge0$ and $x \in \RR$. The closed disc $\overline{D(x,1/2)}$ lies in $S$.

::: pf

::: {.pf-step #circle}

$\abs{f(\zeta)} \le A\qty(\frac32)^\nu(1+\abs{x})^\nu$ for $\abs{\zeta-x}=\frac12$.

::: pf-proof

For such $\zeta$, $1+\abs{\zeta}\le 1+\abs{x}+\frac12 \le \frac32(1+\abs{x})$, and $t \mapsto t^\nu$ is nondecreasing on $[0, \infty)$ since $\nu \geq 0$.

:::

:::

::: pf-step

$\abs{f^{(n)}(x)} \le A_n(1+\abs{x})^\nu$ with $\boxed{A_n=A\,n!\,2^n\qty(\frac32)^\nu}$.

::: pf-proof

Cauchy's estimate on the circle $\abs{\zeta-x}=\frac12$ gives $\abs{f^{(n)}(x)} \le n!\,2^n \max_{\abs{\zeta-x}=1/2}\abs{f(\zeta)}$; apply step [](#circle){.pf-ref}. The constant does not depend on $x$.

:::

:::

:::

:::
