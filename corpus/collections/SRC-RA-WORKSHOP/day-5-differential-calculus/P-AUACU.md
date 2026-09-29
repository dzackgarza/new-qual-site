---
schema: qual/card@1
id: P-AUACU
kind: problem
title: A bounded derivative on $(a,b]$ implies $\lim_{x\to a^+}f(x)$ exists
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Limits
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove that if $f'$ exists and is bounded on $(a,b]$, then $\lim_{x\to a^+}f(x)$ exists.
:::
::: {.solution}

::: pf

::: pf-step

$f$ is continuous on $(a, b]$ and differentiable on $(a, b)$.

::: pf-proof

differentiability on $(a,b]$ implies continuity at every point of $(a,b]$, including $b$.

:::

:::

::: {.pf-step #s2}

$f$ is Lipschitz on $(a, b]$ with constant $M = \sup_{(a,b]}|f'| < \infty$: for $a < x < y \le b$, $|f(x) - f(y)| \le M|x - y|$.

::: pf-proof

the Mean Value Theorem applied to $f$ on $[x, y] \subset (a, b]$ gives $f(x) - f(y) = f'(\xi)(x - y)$ for some $\xi \in (x, y)$, and $|f'(\xi)| \le M$.

:::

:::

::: {.pf-step #s3}

$f$ satisfies the Cauchy criterion at $a^+$: for every $\eps > 0$ there is $\delta > 0$ such that $a < x, y < a + \delta$ implies $|f(x) - f(y)| < \eps$.

::: pf-proof

by step [](#s2){.pf-ref}, $|f(x) - f(y)| \le M|x - y| < M\delta$; choose $\delta = \eps/M$.

:::

:::

::: pf-step

$\lim_{x \to a^+} f(x)$ exists.

::: pf-proof

the Cauchy criterion step [](#s3){.pf-ref} is equivalent to the existence of the limit (pick a sequence $x_n \to a^+$; step [](#s3){.pf-ref} makes $(f(x_n))$ Cauchy in the complete space $\RR$, so it converges, and the limit is independent of the sequence by step [](#s3){.pf-ref} again).

:::

:::

:::

:::
