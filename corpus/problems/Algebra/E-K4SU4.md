---
schema: qual/card@1
id: E-K4SU4
kind: problem
title: $R_p$ is a local ring for $p\in\Spec R$
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Local Rings
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the characterization of the unique maximal ideal as the set of nonunits.
---

::: {.exercise}
Show that if $\mathfrak p\in\Spec(R)$, then $R_\mathfrak p$ is local with unique maximal ideal $\mathfrak pR_\mathfrak p$.
:::

::: {.solution}
Let $S=R\setminus\mathfrak p$, so $R_\mathfrak p=S^{-1}R$, and let $\mathfrak m=\mathfrak pR_\mathfrak p$.

::: pf

::: {.pf-step #m-proper}
$\mathfrak m$ is a proper ideal of $R_\mathfrak p$.

::: pf-proof
Every element of $\mathfrak m$ has the form $a/s$ with $a\in\mathfrak p$ and $s\in S$. If $a/s=1$, then $u(a-s)=0$ for some $u\in S$, so $us=ua\in\mathfrak p$; since $\mathfrak p$ is prime and $u,s\notin\mathfrak p$, this is impossible. Hence $1\notin\mathfrak m$.
:::

:::

::: {.pf-step #outside-m-units}
Every element of $R_\mathfrak p$ outside $\mathfrak m$ is a unit.

::: pf-proof
Let $r/s\notin\mathfrak m$. If $r\in\mathfrak p$, then $r/s\in\mathfrak m$, so $r\notin\mathfrak p$, that is, $r\in S$. Then $s/r\in R_\mathfrak p$ and $\frac rs\cdot\frac sr=1$.
:::

:::

::: pf-step
$R_\mathfrak p$ is local with unique maximal ideal $\mathfrak m$.

::: pf-proof
A proper ideal contains no unit, so by step [](#outside-m-units){.pf-ref} every proper ideal of $R_\mathfrak p$ lies in $\mathfrak m$. By step [](#m-proper){.pf-ref}, $\mathfrak m$ is itself proper, so it is the unique maximal ideal.
:::

:::

:::

:::
