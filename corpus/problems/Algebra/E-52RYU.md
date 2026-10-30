---
schema: qual/card@1
id: E-52RYU
kind: problem
title: Irreducible with a root in a splitting field splits completely
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Field Extensions
  - Irreducibility Criteria
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
Let $F$ be the splitting field of $f \in K[x]$ over $K$.
Prove that if $g \in K[x]$ is irreducible and has a root in $F$, then $g$ splits into linear factors over $F$.
:::

::: {.solution}
Let $\alpha\in F$ be a root of $g$, let $\overline F$ be an algebraic closure of $F$, and let $\beta\in\overline F$ be any root of $g$. Let $r_1,\ldots,r_n\in F$ be the roots of $f$, so that $F=K(r_1,\ldots,r_n)$.

::: pf

::: {.pf-step #extend}
There is an isomorphism $\sigma\colon F\to F(\beta)$ with $\sigma(\alpha)=\beta$ and $\sigma\restrict_K=\operatorname{id}$.

::: pf-proof
Since $g$ is irreducible, there is a $K$-isomorphism $K(\alpha)\to K(\beta)$ with $\alpha\mapsto\beta$. The field $F=K(\alpha)(r_1,\ldots,r_n)$ is a splitting field of $f$ over $K(\alpha)$, and $F(\beta)=K(\beta)(r_1,\ldots,r_n)$ is a splitting field of $f$ over $K(\beta)$. The isomorphism extension theorem for splitting fields extends $K(\alpha)\to K(\beta)$ to $\sigma$.
:::

:::

::: {.pf-step #beta-in-F}
$\beta\in F$.

::: pf-proof
By step [](#extend){.pf-ref}, $[F(\beta):K]=[F:K]$. Since $F\subseteq F(\beta)$ and both are finite over $K$, $F(\beta)=F$.
:::

:::

::: pf-step
$\boxed{g\text{ splits into linear factors in }F[x].}$

::: pf-proof
By step [](#beta-in-F){.pf-ref}, every root of $g$ in $\overline F$ lies in $F$, and $g$ splits over $\overline F$.
:::

:::

:::

:::
