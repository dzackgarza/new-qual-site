---
schema: qual/card@1
id: P-JTRQ2
kind: problem
title: Injective module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homological Algebra
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
What is an injective module over a ring $R$?
State Baer's Criterion and the characterization of injective modules over PIDs (divisible modules).
:::

::: {.solution}
A left $R$-module $Q$ is injective if for every injective $R$-linear map $A\hookrightarrow B$ and every $R$-linear $f:A\to Q$ there is an $R$-linear $g:B\to Q$ with $g|_A=f$. Equivalently, the contravariant functor $\Hom_R(-,Q)$ is exact.

Baer's criterion: a left $R$-module $Q$ is injective if and only if every $R$-linear map $f:I\to Q$ from a left ideal $I\subseteq R$ extends to an $R$-linear map $R\to Q$.

Over a PID $R$, a module $Q$ is divisible if for every $0\ne r\in R$ and $q\in Q$ there is $y\in Q$ with $ry=q$.

::: pf

::: pf-step

Over a PID $R$, an $R$-module $Q$ is injective if and only if it is divisible.

::: pf-proof

Every ideal is $(r)$ for some $r\in R$, and the zero ideal imposes no condition in Baer's criterion. For $r\ne0$, the map $r\mapsto q$ defines an $R$-linear $f:(r)\to Q$ for each $q\in Q$, since $R$ is a domain, and every $f$ arises this way with $q=f(r)$. An extension $g:R\to Q$ of $f$ is determined by $y=g(1)$, and it extends $f$ exactly when $ry=q$. So Baer's criterion for $Q$ is the divisibility condition.

:::

:::

:::

:::

::: {.remark}
Over $\ZZ$, the injective modules are the divisible abelian groups, such as $\QQ$, $\QQ/\ZZ$, and the Prüfer $p$-groups. Over any PID $R$, the field $\Frac(R)$ is divisible and hence injective as an $R$-module.
:::
