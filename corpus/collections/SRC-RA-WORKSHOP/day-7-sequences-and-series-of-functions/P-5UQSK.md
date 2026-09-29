---
schema: qual/card@1
id: P-5UQSK
kind: problem
title: Equicontinuity on $[a,b]$ of differentiable functions with $|f(a)|\le M$ and
  $|f'|\le M$
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $M<\infty$ and $\mathcal{F} \subseteq C[a,b]$.
Assume that each $f \in \mathcal{F}$ is differentiable on $(a,b)$ and satisfies $|f(a)| \leq M$ and $|f'(x)| \leq M$ for all $x \in (a,b)$.
Prove that $\mathcal{F}$ is equicontinuous on $[a,b]$.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
Every $f \in \mathcal F$ is Lipschitz with constant $M$: $|f(x) - f(y)| \le M|x - y|$ for all $x, y \in [a,b]$.

::: pf-proof
mean value theorem — for $x \ne y$, $f(x) - f(y) = f'(c)(x - y)$ for some $c$ between $x$ and $y$, and $|f'(c)| \le M$.
:::

:::

::: pf-step
$\mathcal F$ is equicontinuous on $[a,b]$.

::: pf-proof

::: {.pf-step #s2-1}
Given $\eps > 0$, set $\delta = \eps/M$.

::: pf-proof
$M < \infty$ by hypothesis.
:::

:::

::: {.pf-step #s2-2}
For $|x - y| < \delta$: $|f(x) - f(y)| \le M|x - y| < \eps$ for every $f \in \mathcal F$.

::: pf-proof
Steps [](#s1){.pf-ref} and [](#s2-1){.pf-ref}.
:::

:::

::: pf-qed
Step [](#s2-2){.pf-ref} is exactly the definition of equicontinuity ($\delta$ independent of $x, y$, and $f$).
:::

:::

:::

::: pf-step
(Remark) each $f \in \mathcal F$ is also uniformly bounded: $|f(x)| \le M + M(b - a)$.

::: pf-proof
$|f(x)| \le |f(a)| + |f(x) - f(a)| \le M + M|x - a| \le M + M(b - a)$ by step [](#s1){.pf-ref}.
:::

:::

:::
:::
