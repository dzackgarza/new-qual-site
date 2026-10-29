---
schema: qual/card@1
id: P-AMD-ZIGVO4GJ
kind: problem
title: $R/\nilrad{R}$ is reduced
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
  - Rings
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
Let $R$ be a commutative ring and let $\operatorname{nil}(R) = \sqrt{(0)}$ be its nilradical (the ideal of all nilpotent elements in $R$).
Prove that the quotient ring $R / \operatorname{nil}(R)$ is reduced (i.e. has no non-zero nilpotent elements).
:::

::: {.solution}
Let $N=\operatorname{nil}(R)$.

::: pf

::: {.pf-step #nilpotent-class}

If $x+N$ is nilpotent in $R/N$, then $x\in N$.

::: pf-proof

Suppose $(x+N)^m=N$ for some $m\ge1$. Then $x^m\in N$, so $(x^m)^k=0$ for some $k\ge1$. Hence $x^{mk}=0$, so $x$ is nilpotent and $x\in N$.

:::

:::

::: pf-step

$R/N$ is reduced.

::: pf-proof

By step [](#nilpotent-class){.pf-ref}, every nilpotent element $x+N$ of $R/N$ satisfies $x\in N$, that is, $x+N=0$.

:::

:::

:::

:::
