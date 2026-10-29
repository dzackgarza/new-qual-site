---
schema: qual/card@1
id: P-WB56B
kind: problem
title: An uncountable $E\subset[0,1]$ meets both $(-\infty,t)$ and $(t,\infty)$ in
  uncountable sets
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Counterexamples
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
Show that if $E \subset [0, 1]$ is uncountable, then there exists some $t \in (0, 1)$ such that both $E \cap (-\infty, t)$ and $E \cap (t, \infty)$ are uncountable.
:::

::: {.solution}
For $t\in[0,1]$, put $L_t=E\cap[0,t)$ and $R_t=E\cap(t,1]$. Suppose, for a contradiction, that for every $t\in(0,1)$ at least one of $L_t$ and $R_t$ is countable. Put
$$
a=\sup\{t\in[0,1]:L_t\text{ is countable}\},
$$
which exists because $L_0=\varnothing$.

::: pf

::: {.pf-step #left}

$E\cap[0,a)$ is countable.

::: pf-proof

For each rational $q<a$ there is $t > q$ with $L_t$ countable, so $L_q \subseteq L_t$ is countable. Hence $E\cap[0,a)=\bigcup_{q\in\QQ,\,q<a}L_q$ is a countable union of countable sets.

:::

:::

::: {.pf-step #right}

$E\cap(a,1]$ is countable.

::: pf-proof

Let $q$ be rational with $q>a$. If $q \geq 1$, then $R_q = \varnothing$. If $q < 1$, then $q \in (0, 1)$ and $L_q$ is uncountable by the definition of $a$, so $R_q$ is countable by the assumption. Hence $E\cap(a,1]=\bigcup_{q\in\QQ,\,q>a}R_q$ is countable.

:::

:::

::: pf-step

Some $t\in(0,1)$ makes both $E\cap(-\infty,t)$ and $E\cap(t,\infty)$ uncountable.

::: pf-proof

By steps [](#left){.pf-ref} and [](#right){.pf-ref}, $E=(E\cap[0,a))\cup(E\cap\{a\})\cup(E\cap(a,1])$ is countable, which contradicts the hypothesis. So the assumption fails, and since $E \subset [0, 1]$, $E\cap(-\infty,t) = L_t$ and $E\cap(t,\infty) = R_t$.

:::

:::

:::

:::
