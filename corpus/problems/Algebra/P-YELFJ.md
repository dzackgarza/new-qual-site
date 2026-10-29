---
schema: qual/card@1
id: P-YELFJ
kind: problem
title: An ideal maximal among annihilators of nonzero elements of an $R$-module is
  prime
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source states maximality as "if Ann(nu) strictly contains I for some nu != 0, no such nu exists"; the statement now says there is no nonzero nu with Ann(nu) strictly containing I.'
---

::: {.problem}
Let $R$ be a commutative ring and let $M$ be an $R$-module.
Recall that for $\mu \in M$, the *annihilator* of $\mu$ is the set
$$\Ann(\mu) = \{ r \in R \mid r \mu = 0 \}.$$

Suppose that $I$ is an ideal in $R$ which is maximal among the set of annihilators of non-zero elements of $M$: $I = \Ann(\mu)$ for some $\mu \in M \setminus \{0\}$, and there is no $\nu \in M\setminus\{0\}$ with $\Ann(\nu) \supsetneq I$.

Prove that $I$ is a **prime** ideal in $R$.
:::

::: {.solution}
Let $I=\Ann(\mu)$ with $\mu\ne0$ as in the statement.

::: pf

::: {.pf-step #proper}
$I\ne R$.

::: pf-proof
$1\cdot\mu=\mu\ne0$, so $1\notin I$.
:::

:::

::: pf-step
If $ab\in I$ and $b\notin I$, then $a\in I$.

::: pf-proof
Since $b\notin I$, $b\mu\ne0$.
For $r\in I$, $r(b\mu)=b(r\mu)=0$, so $I\subseteq\Ann(b\mu)$, and maximality gives $I=\Ann(b\mu)$.
Now $a(b\mu)=(ab)\mu=0$, so $a\in\Ann(b\mu)=I$.
:::

:::

::: pf-qed
With step [](#proper){.pf-ref}, $I$ is a prime ideal.
:::

:::

:::
